from django.shortcuts import get_object_or_404
from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import User
from translators.models import Translator


@receiver(pre_save, sender=User)
def add_translator(sender, instance: User, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = get_object_or_404(User, id=instance.id)
        if previous.identity_verified != instance.identity_verified:
            if instance.identity_verified:
                obj = Translator.objects.create(user=instance)
                obj.save()