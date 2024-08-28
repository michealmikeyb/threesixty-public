import json
import csv
import uuid

from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import reverse
from django.utils import timezone
from django.conf import settings
from os import makedirs
from django.template.loader import get_template
from django.template import Context


from surveys.models import Question, Survey, Dimension, Choice, Group, Defaults, ParticipantKey, Session, EmailListing, EmailList
from surveys.forms import QuestionForm, DimensionForm
from surveys.utils import report_context, set_context
from userManagement.models import Settings


def delete_survey(request):
    if request.POST and request.POST.get('id'):
        survey = Survey.objects.filter(id=request.POST.get('id'))
        if survey.exists():
            survey.delete()
            return JsonResponse({'success': 'successfully deleted survey'})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def toggle_survey(request):
    if request.POST and request.POST.get('id'):
        survey = Survey.objects.filter(id=request.POST.get('id'))
        if survey.exists():
            survey = survey.first()
            survey.survey_open = not survey.survey_open
            survey.save()

            return JsonResponse({'success': 'successfully started survey'})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})


def toggle_session(request):
    if request.POST and request.POST.get('id'):
        survey = Survey.objects.filter(id=request.POST.get('id'))
        if survey.exists():
            survey = survey.first()
            if survey.current_session:
                cur = survey.current_session
                cur.current = False
                cur.date_ended = timezone.now()
                cur.save()
                set_context(cur)

                survey.survey_open = False
                survey.save()
            else:
                Session.objects.create(survey=survey, current=True, name=request.POST.get('name'))
                survey.survey_open = True
                survey.save()

                if survey.closed:
                    key = ParticipantKey.objects.create(group=None, admin=True)
                    survey_url = request.get_host()+reverse('start-survey', args=[survey.id,])+'?key='+str(key.key)
                    message =  Settings.objects.filter(name='closed_survey_start_email', category='email').first().content.replace('{survey_url}', survey_url).replace('{name}','')
                    html = get_template('surveys/open_survey_email.html')

                    context ={ 
                        'message': message,
                        'host': request.get_host()
                    }
                    html_content = html.render(context)
                    send_mail(
                        'Survey Invitation',
                        message,
                        'automated@schoolleader360.com',
                        [survey.admin_email],
                        fail_silently=False,
                        html_message=html_content
                    )
                    print(survey.admin_email)

                    for group in survey.group_set.all():
                        emails = group.emails.emaillisting_set.all()
                        for email in emails:
                            key = ParticipantKey.objects.create(group=group)
                            survey_url = request.get_host()+reverse('start-survey', args=[survey.id,])+'?key='+str(key.key)
                            message =  Settings.objects.filter(name='closed_survey_start_email', category='email').first().content.replace('{survey_url}', survey_url).replace('{name}', email.name)
                            html = get_template('surveys/open_survey_email.html')

                            context ={ 
                                'message': message,
                                'host': request.get_host()
                            }

                            html_content = html.render(context)
                            send_mail(
                                'Survey Invitation',
                                message,
                                'automated@schoolleader360.com',
                                [email.email],
                                fail_silently=False,
                                html_message=html_content
                            )

            return JsonResponse({'success': 'successfully started survey'})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'}) 

def duplicate_survey(request):
    if request.POST and request.POST.get('id'):
        id = request.POST.get('id')
        survey = Survey.objects.filter(id=id)
        if survey.exists():
            survey = survey.first()
            name = request.POST.get('name')
            survey.pk = None
            survey.name = name
            survey.template = False
            survey.save()
            new_survey = survey

            for group in Group.objects.filter(survey__id=id):
                group.pk = None
                group.survey = new_survey
                group.save()
            
            for dimension in Dimension.objects.filter(survey__id=id):
                dim_id = dimension.id
                dimension.pk = None
                dimension.survey = new_survey
                dimension.save()
                new_dimension = dimension

                for question in Question.objects.filter(dimension__id=dim_id):
                    question_id = question.id
                    question.pk = None
                    question.dimension = new_dimension
                    question.save()
                    new_question = question
                    
                    for choice in Choice.objects.filter(question__id=question_id):
                        choice.pk = None
                        choice.question = new_question
                        choice.save()

            return JsonResponse({'success': 'successfully duplicated survey', 'id': survey.id})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def delete_question(request):
    if request.POST and request.POST.get('id'):
        question = Question.objects.filter(id=request.POST.get('id'))
        if question.exists():
            question.first().choice_set.all().delete()
            question.first().delete()
            return JsonResponse({'success': 'successfully deleted question'})
        return JsonResponse({'error': 'question not found'})
    return JsonResponse({'error': 'malformed request'})
    

def delete_dimension(request):
    if request.POST and request.POST.get('id'):
        dimension = Dimension.objects.filter(id=request.POST.get('id'))
        if dimension.exists():
            dimension.delete()
            return JsonResponse({'success': 'successfully deleted dimension'})
        return JsonResponse({'error': 'dimension not found'})
    return JsonResponse({'error': 'malformed request'})

def add_group(request):
    if request.POST and request.POST.get('survey_id'):
        survey = Survey.objects.filter(id=request.POST.get('survey_id'))
        if survey.exists():
            if survey.first().closed:
                group = Group.objects.create(survey=survey.first(), name=request.POST.get('name'), emails=EmailList.objects.get(id=request.POST.get('emails')))
            else:
                group = Group.objects.create(survey=survey.first(), name=request.POST.get('name'))
            return JsonResponse({'success': 'Successfully added group', 'id': group.id})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def edit_group(request):
    if request.POST and request.POST.get('group_id'):
        group = Group.objects.filter(id=request.POST.get('group_id'))
        if group.exists():
            group = group.first()
            group.name=request.POST.get('name')
            group.emails=EmailList.objects.get(id=request.POST.get('emails'))
            group.save()
            return JsonResponse({'success': 'Successfully edited group'})
        return JsonResponse({'error': 'group not found'})
    return JsonResponse({'error': 'malformed request'})

def delete_group(request):
    if request.POST and request.POST.get('group_id'):
        group = Group.objects.filter(id=request.POST.get('group_id'))
        if group.exists():
            group.delete()
            return JsonResponse({'success': 'Successfully deleted group'})
        return JsonResponse({'error': 'group not found'})
    return JsonResponse({'error': 'malformed request'})

def add_default_groups(request):
    if request.POST and request.POST.get('survey_id'):
        survey = Survey.objects.filter(id=request.POST.get('survey_id'))
        if survey.exists():
            groups = []
            default_groups = json.loads(Defaults.objects.get(user=request.user).groups)
            for group in default_groups:
                group, created = Group.objects.update_or_create(survey=survey.first(), name=group)
                if created:
                    groups.append({'id': group.id, 'name': group.name})

            return JsonResponse({'success': 'Successfully added group', 'groups': groups})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def add_dimension(request):
    if request.POST and request.POST.get('survey_id'):
        survey = Survey.objects.filter(id=request.POST.get('survey_id'))
        if survey.exists():
            dimension = Dimension.objects.create(survey=survey.first(), name=request.POST.get('name'), description=request.POST.get('description'), color=request.POST.get('color'))
            
            if request.FILES:
                dimension.icon = request.FILES['icon']
            elif request.POST.get('icon') and request.POST.get('icon')!='undefined':
                dimension.icon = request.POST.get('icon').replace('/media', '')
            else:
                dimension.icon = '/icons/default_icons/icon-default.png'

            dimension.save()

            return JsonResponse({'success': 'Successfully added dimension', 'id': dimension.id, 'icon': dimension.icon.url})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def edit_dimension(request):
    if request.POST and request.POST.get('dimension_id'):
        dimension = Dimension.objects.filter(id=request.POST.get('dimension_id'))
        if dimension.exists():
            dimension = dimension.first()
            dimension.name=request.POST.get('name')
            dimension.description=request.POST.get('description')
            dimension.color=request.POST.get('color')


            if request.FILES:
                icon = request.FILES['icon']
                dimension.icon = icon
            dimension.save()
            return JsonResponse({'success': 'Successfully edited dimension', 'icon_url': dimension.icon.url})
        return JsonResponse({'error': 'group not found'})
    return JsonResponse({'error': 'malformed request'})

def delete_dimension(request):
    if request.POST and request.POST.get('dimension_id'):
        dimension = Dimension.objects.filter(id=request.POST.get('dimension_id'))
        if dimension.exists():
            dimension.delete()
            return JsonResponse({'success': 'Successfully deleted dimension'})
        return JsonResponse({'error': 'group not found'})
    return JsonResponse({'error': 'malformed request'})

def add_default_dimensions(request):
    if request.POST and request.POST.get('survey_id'):
        survey = Survey.objects.filter(id=request.POST.get('survey_id'))
        if survey.exists():
            dimensions = []
            default_dimensions = json.loads(Defaults.objects.get(user=request.user).dimensions)
            for dimension in default_dimensions:
                dimension, created = Dimension.objects.update_or_create(survey=survey.first(), name=dimension['name'], description=dimension['description'], color=dimension['color'], icon=dimension['icon'].replace('/media', ''))
                if created:
                    dimensions.append({'id': dimension.id, 'name': dimension.name, 'description': dimension.description, 'color': dimension.color, 'icon': dimension.icon.url})

            return JsonResponse({'success': 'Successfully added group', 'dimensions': dimensions})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def add_question(request):
    if request.POST and request.POST.get('survey_id'):
        survey = Survey.objects.filter(id=request.POST.get('survey_id'))
        if survey.exists():
            if (request.POST.get('choices[0][value]') and  request.POST.get('choices[0][text]')) or (request.POST.get('choices[1][value]') and  request.POST.get('choices[1][text]')):
                choices = [{'text': request.POST.get('choices['+key[8]+'][text]'), 'value': request.POST.get('choices['+key[8]+'][value]', None)} for key, value in request.POST.items() if 'choice' in key and 'value' in key]
            else:
                choices = [{'text': request.POST.get('choices['+key[8]+'][text]'), 'value': None} for key, value in request.POST.items() if 'choice' in key and 'value' in key]
            dimension = Dimension.objects.filter(id=request.POST.get('dimension')).first()
            calculating = request.POST.get('calculating') == 'true'
            question = Question.objects.create(text=request.POST.get('text'), question_type=request.POST.get('type'), calculating=calculating, dimension=dimension)

            if request.POST.get('type') == 'radio':
                for choice in choices:
                    if choice['value'] == '':
                        choice['value'] = None
                    Choice.objects.create(option=choice['text'], value=choice['value'], question=question)

            for group in request.POST.getlist('groups[]'):
                question.groups.add(Group.objects.get(id=group))

            return JsonResponse({'success': 'Successfully added Question', 'id': question.id})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def add_default_questions(request):
    if request.POST and request.POST.get('survey_id'):
        survey = Survey.objects.filter(id=request.POST.get('survey_id'))
        if survey.exists():
            survey = survey.first()
            default_questions = json.loads(Defaults.objects.filter(user=request.user).first().questions)
            default_questions = [d for d in default_questions if d['dimension'] == request.POST.get('name')]
            dimension = Dimension.objects.filter(survey=survey, name=request.POST.get('name')).first()
            questions = []

            for default in default_questions:
                question, created = Question.objects.get_or_create(dimension=dimension, text=default['text'], question_type=default['type'])

                if created:
                    for choice in default['choices']:
                        if choice[1] == '':
                            choice[1] = None
                        Choice.objects.create(option=choice[0], value=choice[1], question=question)

                    questions.append({
                        'choices': default['choices'],
                        'id': question.id,
                        'text': question.text,
                        'type': question.question_type
                    })

            return JsonResponse({'success': 'Successfully added Question', 'questions': questions})
        return JsonResponse({'error': 'survey not found'})
    return JsonResponse({'error': 'malformed request'})

def edit_question(request):
    if request.POST and request.POST.get('question_id'):
        question = Question.objects.filter(id=request.POST.get('question_id'))
        if question.exists():
            question = question.first()
            question.text = request.POST.get('text')
            question.question_type = request.POST.get('type')
            question.calculating = request.POST.get('calculating') == 'true'
            question.save()

            choices = [{'text': request.POST.get('choices['+key[8]+'][text]'), 'value': request.POST.get('choices['+key[8]+'][value]')} for key, value in request.POST.items() if 'choice' in key and 'value' in key]
            question.choice_set.all().delete()
            for choice in choices:
                if choice['value'] == '':
                    choice['value'] = None
                Choice.objects.create(option=choice['text'], value=choice['value'], question=question)

            question.groups.clear()
            for group in request.POST.getlist('groups[]'):
                question.groups.add(Group.objects.get(id=group))

            return JsonResponse({'success': 'Successfully edited question'})
        return JsonResponse({'error': 'question not found'})
    return JsonResponse({'error': 'malformed request'})

def edit_default_group(request):
    if request.POST.get('new_name'):
        defaults = Defaults.objects.filter(user=request.user).first()
        groups = json.loads(defaults.groups)

        if request.POST.get('old_name'):
            groups.remove(request.POST.get('old_name'))
        
        groups.append(request.POST.get('new_name'))
        defaults.groups = json.dumps(groups)
        defaults.save()
        return JsonResponse({'Success': 'Successfully edited group'})
    return JsonResponse({'error': 'malformed request'})

def delete_default_group(request):
    if request.POST.get('name'):
        defaults = Defaults.objects.filter(user=request.user).first()
        groups = json.loads(defaults.groups)

        groups.remove(request.POST.get('name'))
        defaults.groups = json.dumps(groups)
        defaults.save()
        return JsonResponse({'Success': 'Successfully deleted group'})
    return JsonResponse({'error': 'malformed request'})

def edit_default_dimension(request):
    if request.POST.get('new_name'):
        defaults = Defaults.objects.filter(user=request.user).first()
        dimensions = json.loads(defaults.dimensions)

        icon_url = ''
        if request.POST.get('old_name'):
            if [d for d in dimensions if d['name'] == request.POST.get('old_name')][0].get('icon', False):
                icon_url = [d for d in dimensions if d['name'] == request.POST.get('old_name')][0]['icon']
            dimensions = [d for d in dimensions if d['name'] != request.POST.get('old_name')]

        if request.FILES:
            icon = request.FILES['icon']
            icon_path = settings.MEDIA_ROOT+'/icons/'+str(request.user.id)
            makedirs(icon_path, exist_ok=True)
            icon_path = icon_path+'/'+icon.name

            with open(icon_path, 'wb+') as destination:
                for chunk in icon.chunks():
                    destination.write(chunk)
            icon_url = icon_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)

        elif icon_url=='':
            icon_url = '/media//icons/default_icons/icon-default.png'

        dimensions.append({
            'name': request.POST.get('new_name'), 
            'description': request.POST.get('description'), 
            'color': request.POST.get('color'),
            'icon': icon_url})
        defaults.dimensions = json.dumps(dimensions)
        defaults.save()
        return JsonResponse({'Success': 'Successfully edited dimension', 'icon_url': icon_url})
    return JsonResponse({'error': 'malformed request'})

def delete_default_dimension(request):
    if request.POST.get('name'):
        defaults = Defaults.objects.filter(user=request.user).first()
        dimensions = json.loads(defaults.dimensions)

        dimensions = [d for d in dimensions if d['name'] != request.POST.get('name')]
        
        defaults.dimensions = json.dumps(dimensions)
        defaults.save()
        return JsonResponse({'Success': 'Successfully deleted dimension'})
    return JsonResponse({'error': 'malformed request'})

def edit_default_question(request):
    if request.POST.get('new_text'):
        defaults = Defaults.objects.filter(user=request.user).first()
        questions = json.loads(defaults.questions)

        if request.POST.get('old_text'):
            questions = [q for q in questions if q['text'] != request.POST.get('old_text')]
        
        new_question = {
            'text': request.POST.get('new_text'),
            'dimension': request.POST.get('dimension'),
            'type': request.POST.get('type'),
        }
        new_question['choices'] = [(request.POST.get('choices['+key[8]+'][text]'), request.POST.get('choices['+key[8]+'][value]')) for key, value in request.POST.items() if 'choice' in key and 'value' in key]
        
        questions.append(new_question)
        defaults.questions = json.dumps(questions)
        defaults.save()
        return JsonResponse({'Success': 'Successfully edited question'})
    return JsonResponse({'error': 'malformed request'})

def delete_default_question(request):
    if request.POST.get('text'):
        defaults = Defaults.objects.filter(user=request.user).first()
        questions = json.loads(defaults.questions)

        questions = [q for q in questions if q['text'] != request.POST.get('text')]
        
        defaults.questions = json.dumps(questions)
        defaults.save()
        return JsonResponse({'Success': 'Successfully deleted question'})
    return JsonResponse({'error': 'malformed request'})

def survey_data(request):
    if request.GET.get('id'):
        survey = Survey.objects.filter(id=request.GET.get('id')).first()
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="'+str(survey)+'-data.csv"'

        writer = csv.writer(response)
        writer.writerow([survey.name])
        writer.writerow(['responding to a given item'])
        writer.writerow(['Date Created: '+timezone.now().strftime('%B %d, %Y')])
        writer.writerow([''])
        writer.writerow(['Respondents'])

        header = ['Date', 'Email Address', 'Group']
        for question in Question.objects.filter(dimension__survey=survey).order_by('text'):
            header.append(question.text)
            header.append('score')
        writer.writerow(header)

        for res in survey.response_set.all():
            row = [res.date_taken.strftime('%b %d, %Y'), res.email, res.group]
            answers = res.answer_set.all()
            for question in Question.objects.filter(dimension__survey=survey).order_by('text'):
                if answers.filter(question=question).exists():
                    answer = answers.filter(question=question).first()
                    row.append(answer.answer)
                    row.append(answer.value)
                else:
                    row.append('')
                    row.append('')
                
            writer.writerow(row)


        return response
    return JsonResponse({'error': 'malformed request'})


def delete_email(request):
    if request.POST and request.POST.get('email_id'):
        listing = EmailListing.objects.filter(id=request.POST.get('email_id'))
        if listing.exists:
            listing.delete()
            return JsonResponse({'success': 'Successfully deleted email listing'})
        return JsonResponse({'error': 'email not found'})
    return JsonResponse({'error': 'malformed request'})


def edit_email(request):
    if request.POST and request.POST.get('email_id'):
        listing = EmailListing.objects.filter(id=request.POST.get('email_id'))
        if listing.exists:
            listing = listing.first()
            listing.email = request.POST.get('email')
            listing.name = request.POST.get('name')
            listing.save()

            return JsonResponse({'success': 'Successfully edited email listing'})
        return JsonResponse({'error': 'email not found'})
    return JsonResponse({'error': 'malformed request'})


def add_email(request):
    if request.POST and request.POST.get('list_id'):
        email_list = EmailList.objects.filter(id=request.POST.get('list_id'))
        if email_list.exists:
            email_list = email_list.first()
            listing = EmailListing.objects.create(email=request.POST.get('email'), name=request.POST.get('name'), email_list=email_list)

            return JsonResponse({'success': 'Successfully added email listing', 'id': listing.id})
        return JsonResponse({'error': 'email list not found'})
    return JsonResponse({'error': 'malformed request'})


def get_email_list(request):
    if request.GET and request.GET.get('list_id'):
        email_list = EmailList.objects.filter(id=request.GET.get('list_id'))
        if email_list.exists:
            email_list = email_list.first()
            emails = [{'email': listing.email, 'name': listing.name, 'id': listing.id} for listing in email_list.emaillisting_set.all()]

            return JsonResponse({'success': 'Successfully added email listing', 'emails': emails, 'name': email_list.name})
        return JsonResponse({'error': 'email list not found'})
    return JsonResponse({'error': 'malformed request'})

def add_email_list(request):
    if request.POST and request.POST.get('name'):
        email_list = EmailList.objects.create(name=request.POST.get('name'), user=request.user)
        return JsonResponse({'success': 'Successfully added email list', 'id': email_list.id, 'name': email_list.name})
    return JsonResponse({'error': 'malformed request'})

def import_email_list(request):
    if request.POST and request.POST.get('emails') and request.POST.get('list_name'):
        email_list = EmailList.objects.create(name=request.POST.get('list_name'), user=request.user)
        zipped_emails = zip(request.POST.get('emails').split(',').remove(' '), request.POST.get('names').split(','))
        emails = []
        for email in zipped_emails:
            emails.append(EmailListing.objects.create(email=email[0], name=email[1], email_list=email_list))
        return JsonResponse({'success': 'Successfully imported email list', 'list_name': email_list.name, 'emails': [{'email': email.email, 'name': email.name, 'id': email.id} for email in emails]})
    return JsonResponse({'error': 'malformed request'})

    