import json
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from surveys.defaults import default_groups, default_dimensions, default_questions, default_survey

# Create your models here.


class EmailList(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    

    class Meta:
        verbose_name = _("EmailList")
        verbose_name_plural = _("EmailLists")

    def __str__(self):
        return self.name


class EmailListing(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    email_list = models.ForeignKey(EmailList, verbose_name=_("List"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("EmailListing")
        verbose_name_plural = _("EmailListings")

    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    closed = models.BooleanField(_("Closed"), default=False)
    admin_email = models.EmailField(_("Admin Email"),null=True,  max_length=254)
    admin_password = models.CharField(max_length=32, null=True, blank=True)
    participant_password = models.CharField(max_length=32, null=True, blank=True)
    welcome_message = models.TextField()
    group_message = models.TextField()
    closing_message = models.TextField()
    department = models.ForeignKey('userManagement.department', on_delete=models.CASCADE, null=True, blank=True)
    survey_open = models.BooleanField(_("Survey Open"), default=False)
    template = models.BooleanField(_("Template"), default=False)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    email_required = models.BooleanField(_("Email Required"), default=True)
    public_use = models.BooleanField(_("Public Use"), null=True, blank=True)
    admin_email = models.EmailField(_("Admin Email"),null=True,  max_length=254, blank=True)

    def __str__(self):
        return self.name

    @property
    def current_session(self):
        if self.session_set.filter(current=True).exists():
            return self.session_set.filter(current=True).first()
        else:
            return None


class Dimension(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(_("Description"))
    color = models.CharField(_("Color"), max_length=12, null=True)
    icon = models.ImageField(_("Icon"), null=True, upload_to='icons')

class Group(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    survey = models.ForeignKey(Survey, verbose_name=_("Survey"), on_delete=models.CASCADE)
    emails = models.ForeignKey(EmailList, verbose_name=_("Emails"), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Group_detail", kwargs={"pk": self.pk})

TYPE_CHOICES = [
    ('radio','Likert'),
    ('number', 'Number'),
    ('short_answer', 'Short Answer'),
    ('long_answer', 'Long Answer')
]


SHORT_ANSWER_MAX=256
LONG_ANSWER_MAX=2048
class Question(models.Model):
    text = models.CharField(max_length=256)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    groups = models.ManyToManyField(Group, verbose_name=_(""))
    calculating = models.BooleanField(_("Calculating"), default=True)

    def validate(self, input):
        if self.question_type == 'short_answer':
            return len(input)<SHORT_ANSWER_MAX
        elif self.question_type == 'long_answer':
            return len(input)<LONG_ANSWER_MAX
        elif self.question_type == 'number':
            try:
                int(input)
                return True
            except ValueError:
                return False
        elif self.question_type == 'radio' and self.calculating:
            if input=='None':
                return self.choice_set.filter(value=None).exists()
            return self.choice_set.filter(value=int(input)).exists()
        else:
            return True


class Choice(models.Model):
    option = models.CharField(max_length=128)
    value = models.IntegerField(default=0, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name=_("Group"), on_delete=models.CASCADE, null=True)
    admin_response = models.BooleanField(default=False)
    email= models.EmailField(_("Email"), max_length=254)
    date_taken = models.DateTimeField(_("Taken"), auto_now_add=True)
    session = models.ForeignKey("surveys.Session", verbose_name=_("Session"), on_delete=models.CASCADE)


class ParticipantKey(models.Model):

    group = models.ForeignKey(Group, verbose_name=_("Group"), on_delete=models.CASCADE, null=True)
    key = models.UUIDField(_("key"), default=uuid4, editable=False, unique=True)
    response = models.ForeignKey(Response, verbose_name=_("Response"), on_delete=models.CASCADE, null=True)
    admin = models.BooleanField(_("Admin"), default=False)

    class Meta:
        verbose_name = _("ParticipantKey")
        verbose_name_plural = _("ParticipantKeys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ParticipantKey_detail", kwargs={"pk": self.pk})


class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(null=True)
    value = models.IntegerField(null=True)

class Defaults(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    groups = models.TextField(_("Groups"), default=json.dumps(default_groups))
    dimensions = models.TextField(_("Dimensions"), default=json.dumps(default_dimensions))
    questions = models.TextField(_("Questions"), default=json.dumps(default_questions))
    survey = models.TextField(_("Survey"), default=json.dumps(default_survey))
    

    class Meta:
        verbose_name = _("Defaults")
        verbose_name_plural = _("Defaults")


class Session(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    survey = models.ForeignKey(Survey, verbose_name=_("Survey"), on_delete=models.CASCADE)
    report_context = models.TextField(_("Report Context"))
    current = models.BooleanField(_("Current"), default=True)
    date_started = models.DateTimeField(_("Date Started"), auto_now_add=True)
    date_ended = models.DateTimeField(_("Date Ended"), null=True)

    class Meta:
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")

    def __str__(self):
        return self.name


