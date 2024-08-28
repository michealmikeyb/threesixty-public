from django.forms import ModelForm, HiddenInput
from surveys.models import Survey, Dimension, Question, Choice
from userManagement.models import Department

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        exclude=('survey_open', 'template', 'department', 'public_use')
        widgets = {
            'user': HiddenInput
        }
        
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.fields['department'].queryset = Department.objects.filter(users=user)
    

class DimensionForm(ModelForm):
    class Meta:
        model = Dimension
        fields = '__all__'


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'