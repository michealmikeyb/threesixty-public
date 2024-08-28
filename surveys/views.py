import json
from weasyprint import HTML, CSS
from django_weasyprint.utils import django_url_fetcher
import os

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db.models import Avg, Q
from django.core.paginator import Paginator
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.conf import settings

from surveys.forms import SurveyForm
from surveys.models import Survey, Dimension, Question, Choice, TYPE_CHOICES, Response, Answer, Group, Defaults, ParticipantKey, Session, EmailList
from surveys.utils import report_context, set_context, get_context
import threesixty
from userManagement.models import Settings


def landing(request):
    if request.user.is_staff:
        surveys = Survey.objects.filter(template=False).all()
    else:
        surveys = Survey.objects.filter(user=request.user, template=False)
    
    context = {
        'surveys': surveys
    }

    return render(request, 'surveys/landing.html', context)

def templates(request):
    if request.user.is_staff:
        surveys = Survey.objects.filter(template=True).all()
    else:
        surveys = Survey.objects.filter(Q(user=request.user, template=True)|Q(public_use=True, template=True))

    context = {
        'surveys': surveys
    }

    return render(request, 'surveys/templates.html', context)

def view_survey(request, id):
    survey = Survey.objects.filter(id=id).first()

    return render(request, 'surveys/view_survey.html', {'survey': survey})


def add_survey(request, template='False'):
    if request.POST:
        survey_form = SurveyForm(data=request.POST, user=request.user, initial={'user': request.user})

        if survey_form.is_valid():
            survey = survey_form.save()
            survey.template = template == 'True'
            if survey.template:
                survey.public_use = request.POST.get('public-use') == 'on'
            survey.save()

            return redirect('survey-confirm', survey.id)
        
    defaults = Defaults.objects.filter(user=request.user).first()
    default_survey = json.loads(defaults.survey)

    initial = {
        'description': default_survey['description'],
        'welcome_message': default_survey['welcome'],
        'closing_message': default_survey['closing'],
        'group_message': default_survey['group'],
        'user': request.user,
    }
    survey_form = SurveyForm(user=request.user, initial=initial)
    context = {
        'survey_form': survey_form,
        'default': default_survey,
        'template': template=='True',
    }

    return render(request, 'surveys/add_survey.html', context)

def survey_confirm(request, id):
    survey = Survey.objects.filter(id=id).first()
    num_email_lists = EmailList.objects.filter(user=request.user).all().count()

    return render(request, 'surveys/survey_confirm.html', {'survey': survey, 'num_email_lists': num_email_lists})

def add_groups(request, id):
    survey = Survey.objects.filter(id=id).first()
    default_groups = json.loads(Defaults.objects.get(user=request.user).groups)
    email_lists = EmailList.objects.filter(user=request.user)

    context = {
        'survey': survey, 
        'defaults': default_groups,
        'email_lists': email_lists
    }

    return render(request, 'surveys/add_groups.html', context)

def add_dimensions(request, id):
    survey = Survey.objects.filter(id=id).first()
    default_dimensions = json.loads(Defaults.objects.get(user=request.user).dimensions)
    default_names = [d['name'] for d in default_dimensions]

    context = {
        'survey': survey, 
        'defaults': default_dimensions,
        'default_names': default_names
    }

    return render(request, 'surveys/add_dimensions.html', context)

def add_questions(request, id):
    survey = Survey.objects.filter(id=id).first()
    default_questions = json.loads(Defaults.objects.get(user=request.user).questions)

    default_texts=[d['text'] for d in default_questions]
    context = {
        'survey': survey, 
        'defaults': default_questions,
        'type_choices': TYPE_CHOICES,
        'default_texts': default_texts
    }

    return render(request, 'surveys/add_questions.html', context)

def edit_survey(request, id):
    survey = Survey.objects.filter(id=id).first()
    survey_form = SurveyForm(user=request.user, instance=survey)


    defaults = Defaults.objects.filter(user=request.user).first()
    default_survey = json.loads(defaults.survey)
    
    if request.POST:
        survey_form = SurveyForm(data=request.POST, user=request.user, instance=survey)

        if survey_form.is_valid():
            survey = survey_form.save()

    context = {
        'survey': survey,
        'survey_form': survey_form,
        'default': default_survey}

    return render(request, 'surveys/edit_survey.html', context)

def start_survey(request, id):
    survey = Survey.objects.filter(id=id).first()
    error = None

    if not survey.survey_open:
        return render(request, 'surveys/start_survey.html', {'survey': survey, 'error': 'survey closed'})

    if request.GET:
        key = request.GET.get('key', '')
        if ParticipantKey.objects.filter(key=key).exists():
            key = ParticipantKey.objects.filter(key=key).first()

            if key.response:
                response = key.response
                key.response.answer_set.all().delete()
            else:
                response = Response.objects.create(group=key.group, survey=survey, session=survey.current_session, admin_response=key.admin)

            return redirect(reverse('survey-welcome', args=[id, response.id]))
        else:
            error = 'Survey Taken Already'
            return render(request, 'surveys/start_survey.html', {'survey': survey, 'error': error})

    if request.POST:
        response = None
        if Response.objects.filter(survey=survey, email=request.POST.get('email', 'blank@blank.com'), session=survey.current_session).exists() and survey.email_required:
                error = 'Survey Taken Already'
                return render(request, 'surveys/start_survey.html', {'survey': survey, 'error': error})

        if request.POST.get('password') == survey.admin_password:
            if Response.objects.filter(survey=survey, admin_response=True, session=survey.current_session).exists():
                error = 'Survey Taken Already'
                return render(request, 'surveys/start_survey.html', {'survey': survey, 'error': error})
            else:
                response = Response.objects.create(survey=survey, admin_response=True, email=request.POST.get('email'), session=survey.current_session)
        elif request.POST.get('password') == survey.participant_password:
            response = Response.objects.create(survey=survey, email=request.POST.get('email', 'blank@blank.com'), session=survey.current_session)
        
        if response:
            return redirect(reverse('survey-welcome', args=[id, response.id]))
        else:
            error = 'Password not valid'
        
    
    return render(request, 'surveys/start_survey.html', {'survey': survey, 'error': error})

def survey_welcome(request, id, response_id):
    survey = Survey.objects.filter(id=id).first()
    response = Response.objects.filter(id=response_id).first()

    return render(request, 'surveys/survey_welcome.html', {'survey': survey, 'response': response})


def group_select(request, id, response_id):
    survey = Survey.objects.filter(id=id).first()
    response = Response.objects.filter(id=response_id).first()

    if request.POST:
        group = Group.objects.filter(id=request.POST.get('group')).first()
        response.group = group
        response.save()
        
        return redirect(reverse('take-survey', args=[id, response_id]))

    return render(request, 'surveys/group_select.html', {'survey': survey, 'response': response})


def take_survey(request, id, response_id):
    survey = Survey.objects.filter(id=id).first()
    response = Response.objects.filter(id=response_id).first()
    errors = []
    questions = []

    for choice in TYPE_CHOICES:
        if response.admin_response:
            dimensions = [list(dim.question_set.filter(question_type=choice[0], calculating=True))for dim in survey.dimension_set.all()]
        else:
            dimensions = [list(dim.question_set.filter(Q(groups=response.group)|Q(groups=None), question_type=choice[0], calculating=True))for dim in survey.dimension_set.all()]
        calculating_questions = []
        if response.admin_response:
            while len(calculating_questions) < Question.objects.filter(dimension__survey=survey, question_type=choice[0], calculating=True).count():
                for dim in dimensions:
                    if len(dim):
                        calculating_questions.append(dim.pop())
        else: 
            while len(calculating_questions) < Question.objects.filter(Q(groups=response.group)|Q(groups=None), dimension__survey=survey, question_type=choice[0], calculating=True).count():
                for dim in dimensions:
                    if len(dim):
                        calculating_questions.append(dim.pop())

        if response.admin_response:
            dimensions = [list(dim.question_set.filter(question_type=choice[0], calculating=False))for dim in survey.dimension_set.all()]
        else:
            dimensions = [list(dim.question_set.filter(Q(groups=response.group)|Q(groups=None), question_type=choice[0], calculating=False))for dim in survey.dimension_set.all()]
        non_calculating_questions = []
        if response.admin_response:
            while len(non_calculating_questions) < Question.objects.filter(dimension__survey=survey, question_type=choice[0], calculating=False).count():
                for dim in dimensions:
                    if len(dim):
                        non_calculating_questions.append(dim.pop())
        else:
            while len(non_calculating_questions) < Question.objects.filter(Q(groups=response.group)|Q(groups=None), dimension__survey=survey, question_type=choice[0], calculating=False).count():
                for dim in dimensions:
                    if len(dim):
                        non_calculating_questions.append(dim.pop())
        questions.extend(calculating_questions)
        questions.extend(non_calculating_questions)
        
    
    page_number = 1
    paginator = Paginator(questions, 10)


    if request.POST:
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken' and key != 'page_number' and key != 'response_id':
                question = Question.objects.filter(id=key).first()
                if not question.validate(value):
                    errors.append({question.text: 'invalid input'})
        if not len(errors):
            for key, value in request.POST.items():
                if value=='None':
                    value = None
                if key != 'csrfmiddlewaretoken' and key != 'page_number' and key != 'response_id':
                    question = Question.objects.filter(id=key).first()
                    answer = Answer.objects.create(response=response, question=question, answer=value)
                    if question.question_type == 'radio' or question.question_type == 'number':
                        if (question.question_type == 'radio' and question.calculating) or question.question_type == 'number':
                            if value is None:
                                answer.value=None
                            else:
                                answer.value = int(value)
                        if question.question_type == 'radio' and question.calculating:
                            answer.answer = question.choice_set.filter(value=value).first().option
                        else:
                            answer.answer = value
                        answer.save()

            page_number = int(request.POST.get('page_number', 1))+1
            if page_number > paginator.num_pages:
                return redirect(reverse('survey-close', args=[id, response_id]))
            

    questions = paginator.page(page_number)

    context = {
        'survey': survey,
        'questions': questions,
        'page_number': page_number,
        'response': response,
        'errors': errors}

    return render(request, 'surveys/take_survey.html', context)


def survey_close(request, id, response_id):
    survey = Survey.objects.filter(id=id).first()
    response = Response.objects.filter(id=response_id).first()

    return render(request, 'surveys/survey_close.html', {'survey': survey, 'response': response})

def survey_report(request, id): 
    survey = Survey.objects.filter(id=id).first()
    
    context = report_context(survey)
    report_settings = {setting.name: setting.content for setting in Settings.objects.filter(category='report')}

    list_settings = set([setting.name for setting in Settings.objects.filter(list_setting=True)])
    for setting in list_settings:
        report_settings[setting] = [setting.content for setting in Settings.objects.filter(name=setting)]

    context['report_settings'] = report_settings
    context['top_col_span'] = survey.group_set.all().count()*2+1
    
    return render(request, 'surveys/survey_report.html', context)

def edit_defaults(request):
    if not Defaults.objects.filter(user=request.user).exists():
        Defaults.objects.create(user=request.user)
    return render(request, 'surveys/edit_defaults.html')

def edit_group_defaults(request):
    default_groups = json.loads(Defaults.objects.get(user=request.user).groups)

    return render(request, 'surveys/edit_group_defaults.html', {'groups': default_groups})

def edit_dimension_defaults(request):
    default_dimensions = json.loads(Defaults.objects.get(user=request.user).dimensions)

    return render(request, 'surveys/edit_dimension_defaults.html', {'dimensions': default_dimensions})

def edit_survey_defaults(request):
    defaults = Defaults.objects.get(user=request.user)
    default_survey = json.loads(defaults.survey)

    if request.POST:
        default_survey ={
            'description': request.POST.get('description'),
            'welcome': request.POST.get('welcome'),
            'closing': request.POST.get('closing'),
            'closed_system': request.POST.get('closed_system'),
            'group': request.POST.get('group'),
        }
        survey_json = json.dumps(default_survey)
        defaults.survey = survey_json
        defaults.save()


    return render(request, 'surveys/edit_survey_defaults.html', {'default': default_survey})

def edit_question_defaults(request):
    defaults = Defaults.objects.get(user=request.user)
    default_questions = json.loads(defaults.questions)
    default_dimensions = json.loads(defaults.dimensions)

    context = {
        'questions': default_questions, 
        'dimensions': default_dimensions,
        'type_choices': TYPE_CHOICES
    }
    return render(request, 'surveys/edit_question_defaults.html', context)

def survey_report_pdf(request, id):
    survey = Survey.objects.filter(id=id).first()
    context = report_context(survey)

    report_settings = {setting.name: setting.content for setting in Settings.objects.filter(category='report')}

    list_settings = set([setting.name for setting in Settings.objects.filter(list_setting=True)])
    for setting in list_settings:
        report_settings[setting] = [setting.content for setting in Settings.objects.filter(name=setting)]
    context['report_settings'] = report_settings

    context['pdf'] = True
    context['path']= os.path.dirname(threesixty.__file__).replace('/threesixty', '')+'/threesixty'
    context['top_col_span'] = survey.group_set.all().count()*2+1
    html_template = render_to_string('surveys/survey_report.html', context)

    pdf_file = HTML(string=html_template, base_url=request.build_absolute_uri('/'), url_fetcher=django_url_fetcher).write_pdf(stylesheets=[
        CSS(settings.STATIC_ROOT +  '/surveys/css/report_pdf.css'),
        CSS(settings.STATIC_ROOT +  '/surveys/css/report.css'),
        CSS(settings.STATIC_ROOT +  '/css/base.css'),
        CSS(settings.STATIC_ROOT +  '/css/mdb.min.css'),])
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    return response

def comparison_report(request, id):
    survey = Survey.objects.filter(id=id).first()
    if request.GET:
        session_ids = [int(value) for key, value in request.GET.items() if key != 'csrfmiddlewaretoken' and key!='pdf']
        sessions = Session.objects.filter(survey=survey, id__in=session_ids).order_by('date_started')
        base_session = sessions.first()
        base_session = get_context(base_session)
        comparisons = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        report_settings = {setting.name: setting.content for setting in Settings.objects.filter(category='report')}

        list_settings = set([setting.name for setting in Settings.objects.filter(list_setting=True)])
        for setting in list_settings:
            report_settings[setting] = [setting.content for setting in Settings.objects.filter(name=setting)]

        for i, session in enumerate(sessions):
            session.letter = alphabet[i]
            if i < sessions.count()-1:
                first = session
                second = sessions[i+1]
                comparison = {
                    'first': alphabet[i],
                    'second': alphabet[i+1]
                }
                first_context = get_context(first)
                second_context = get_context(second)
                dimensions = [{'name': dim1['name'], 'color': dim1['color'], 'groups': zip(dim1['groups'], dim2['groups']), 'session1_average': dim1['dimension_average'], 'session2_average': dim2['dimension_average']} for dim1, dim2 in zip(first_context['dimension_responses'], second_context['dimension_responses'])]

                first_context['all_questions'].sort(reverse=True, key=lambda q: q['text'])
                second_context['all_questions'].sort(reverse=True, key=lambda q: q['text'])
                questions = [{'text': q1['text'], 'dimension': q1['dimension'], 'dimension_color': q1.get('dimension_color', None), 'first_average': q1['average'], 'second_average': q2['average']} for q1, q2 in zip(first_context['all_questions'], second_context['all_questions'])]
                
                comparison['dimensions'] = dimensions
                comparison['questions'] = questions
                comparisons.append(comparison)

        context = {
            'base_session': base_session,
            'sessions': sessions,
            'comparisons': comparisons,
            'survey': survey
        }
        context['top_table_header'] = survey.group_set.all().count()*2+1
        context['bot_table_header'] = survey.group_set.all().count()*3+1
        context['report_settings'] = report_settings
        if request.GET.get('pdf') == 'on':
            context['pdf'] = True
            context['path']= os.path.dirname(threesixty.__file__).replace('/threesixty', '')+'/threesixty'
            html_template = render_to_string('surveys/comparison_report.html', context)

            pdf_file = HTML(string=html_template, base_url=request.build_absolute_uri('/'), url_fetcher=django_url_fetcher).write_pdf(stylesheets=[
                CSS(settings.STATIC_ROOT +  '/surveys/css/report_pdf.css'),
                CSS(settings.STATIC_ROOT +  '/surveys/css/report.css'),
                CSS(settings.STATIC_ROOT +  '/css/base.css'),
                CSS(settings.STATIC_ROOT +  '/css/mdb.min.css'),])
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'filename="report.pdf"'
            return response
        return render(request, 'surveys/comparison_report.html', context)


def email_lists(request, survey_id=False):
    EmailList.objects.filter(user=request.user).delete()
    email_lists = EmailList.objects.filter(user=request.user)
    context = {
        'email_lists': email_lists,
        'survey_id': survey_id
    }

    return render(request, 'surveys/email_lists.html', context)



