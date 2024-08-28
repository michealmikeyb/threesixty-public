import json

from django.db.models import Avg, Q

from surveys.models import Response, Survey, Question, Answer, Session

def report_context(survey, session=None):
    dimension_reponses = []
    all_questions = []

    if session is None:
        if survey.current_session is not None:
            session = survey.current_session
        else:
            session = Session.objects.filter(survey=survey).order_by('date_started').first()

    if Response.objects.filter(survey=survey, session=session).exists():
        for dimension in survey.dimension_set.all():
            questions = []

            question_total = 0
            admin_total = 0
            for question in dimension.question_set.filter(Q(question_type='radio')|Q(question_type='number'), calculating=True):
                participant_answers = Answer.objects.filter(question=question, value__isnull=False, response__admin_response=False, response__session=session)
                average = participant_answers.aggregate(Avg('value'))
                
                if Answer.objects.filter(question=question, value__isnull=False, response__admin_response=True, response__session=session).exists():
                    admin_response = Answer.objects.filter(question=question, value__isnull=False, response__admin_response=True, response__session=session).first().value
                else:
                    admin_response = 0

                if average['value__avg']:
                    question_total = question_total + average['value__avg']
                admin_total = admin_total+admin_response

                if admin_response is not None and average['value__avg'] is not None:
                    difference = admin_response - average['value__avg']
                else:
                    difference = 0

                if average['value__avg'] is not None:
                    average = average['value__avg']
                else:
                    average = 0

                questions.append({'text': question.text, 'dimension': dimension.name,'dimension_color': dimension.color,  'average': average, 'admin_response': admin_response, 'difference': difference})

            if Answer.objects.filter(question__dimension=dimension, response__admin_response=True, response__session=session).exists():
                admin_average = admin_total/Answer.objects.filter(question__dimension=dimension, response__admin_response=True, response__session=session).count()
            else:
                admin_average = 0

            answers = Answer.objects.filter(value__isnull=False, question__calculating=True, response__session=session)
            groups = [{'name': group.name, 'avg': answers.filter(response__group=group, question__dimension=dimension).aggregate(Avg('value'))['value__avg'], 'num_resp': Response.objects.filter(group=group, survey=survey, session=session).count()} for group in survey.group_set.all()]
            
            dimension_total = 0
            for group in groups:
                if group['avg']:
                    dimension_total+=group['avg']
            if len([group for group in groups if group['avg']]):
                dimension_average = dimension_total/len([group for group in groups if group['avg']])
            else:
                dimension_average = 0

            dimension_reponses.append({'name': dimension.name, 
                                        'color': dimension.color, 
                                        'dimension_average': dimension_average, 
                                        'admin_average': admin_average,
                                        'difference': dimension_average-admin_average,
                                        'groups': groups})
            all_questions.extend(questions)

    option_questions = []
    for question in Question.objects.filter(question_type='radio', calculating=False, dimension__survey=survey):
        options = []
        group_totals = {}
        total_answers = question.answer_set.filter(response__session=session).count()
        for group in survey.group_set.all().order_by('name'):
            group_total = Response.objects.filter(survey=survey, group=group, session=session).count()
            group_totals[group.name] = group_total

        for option in question.choice_set.all():
            groups = []
            for group in survey.group_set.all().order_by('name'):
                group_option_total = Answer.objects.filter(answer=option.option, response__group=group, question=question, response__session=session).count()
                if group_totals[group.name] is not None and group_totals[group.name]!=0:
                    percent = group_option_total/group_totals[group.name]*100
                else:
                    percent = 0

                groups.append({'name': group.name, 'percent': percent})

            option_total = Answer.objects.filter(answer=option.option, question=question, response__session=session).count()

            if total_answers is not None and total_answers != 0:
                percent = option_total/total_answers * 100
            else:
                percent = 0
            options.append({'groups': groups, 'percent': percent, 'name': option.option})

        option_questions.append({'text': question.text, 'options': options})

    all_questions.sort(reverse=True, key=lambda q: q['average'])
    text_questions = Question.objects.filter(Q(question_type='short_answer')|Q(question_type='long_answer'),  dimension__survey=survey)
    context = {
        'dimension_responses': dimension_reponses,
        'survey': survey,
        'num_responses': Response.objects.filter(survey=survey, session=session, admin_response=False).count(),
        'all_questions': all_questions,
        'text_questions': text_questions,
        'option_questions': option_questions
    }
    return context


def set_context(session):
    context = report_context(session.survey, session)

    context['survey'] = context['survey'].id
    context['text_questions'] = [q.id for q in context['text_questions']]

    context_json = json.dumps(context)
    session.report_context = context_json
    session.save()

def get_context(session):
    if session.report_context:
        context = json.loads(session.report_context)
        
        context['survey'] = Survey.objects.filter(id=context['survey']).first()
        context['text_questions'] = [Question.objects.get(id=q) for q in context['text_questions']]
    else:
        context = report_context(session.survey, session)

    return context
