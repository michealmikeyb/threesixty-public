from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    name = models.CharField(max_length=64)
    admin = models.ForeignKey(User, related_name='admin' , on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class HeaderSettings(models.Model):

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    logo = models.ImageField(_("Logo"), upload_to='logos/', default='default_logo.png')
    size = models.IntegerField(_("Font Size"), default=32)
    color = models.CharField(_("Text Color"), max_length=8, default='#C2EFF0')
    background = models.CharField(_("Background Color"), max_length=8, default='#000000')

    class Meta:
        verbose_name = _("HeaderSettings")
        verbose_name_plural = _("HeaderSettingss")

    def __str__(self):
        return str(self.user)



class RegistrationRequest(models.Model):
    rid = models.UUIDField(_("rid"), default=uuid4, editable=False, unique=True)
    

    class Meta:
        verbose_name = _("RegistrationRequest")
        verbose_name_plural = _("RegistrationRequests")


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    rid = models.UUIDField(_("rid"), default=uuid4, editable=False, unique=True)
    

    class Meta:
        verbose_name = _("RegistrationRequest")
        verbose_name_plural = _("RegistrationRequests")


SETTINGS_CATEGORIES = (
    ('report', 'Report'),
    ('email', 'Email')
)
class Settings(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    category = models.CharField(_("Category"), choices=SETTINGS_CATEGORIES ,max_length=50)
    content = models.TextField(_("Content"))
    list_setting = models.BooleanField(_("List Setting"), default=False)
    

    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settingss")

    def __str__(self):
        return self.name

