# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import types

class UserProfileBase(models.Model):
    u"""
    User Profile to extend the User model
    """
    user = models.ForeignKey(User, unique=True, blank=False)
    adress = models.TextField(_('adress'), blank=False)
    town = models.CharField(_('town'), max_length=75, blank=False)
    zipcode = models.CharField(_('zipcode'), max_length=6, blank=False)
    phone_number = models.CharField(_('phone'), max_length=20, blank=False)
    mobile_number = models.CharField(_('mobile'), max_length=20, blank=True, null=True)
    
    def __unicode__(self):
        return u"{0}'s profile".format(self.user.username)
    
    class Meta:
        abstract = True
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

def append_profile_on_user_create(sender, instance, created, **kwargs):
    """
    Automatically add an empty profile on user create if it doesn't exist yet
    
    Need to be connected to model with something like that : ::
    
        from django.contrib.auth.models import User
        from django.db.models.signals import post_save as post_save_signal
        post_save_signal.connect(append_profile_on_user_create, sender=User)
        
    "extra_fields" can be passed in kwargs, it will contain extra fields (like these 
    appended by inherit the abstract model) with their default value. Also theses values 
    can be a lambda which receive the user instance and return a correct value.
    """
    if created:
        try:
            instance.get_profile()
        except ObjectDoesNotExist:
            extra_fields = kwargs.get('extra_fields', {})
            
            for k,v in extra_fields.items():
                if isinstance(v, types.FunctionType):
                    extra_fields[k] = v(instance)
            
            instance.userprofile_set.create(
                adress='placeholder',
                town='placeholder',
                zipcode='empty',
                phone_number='placeholder',
                **extra_fields
            )
