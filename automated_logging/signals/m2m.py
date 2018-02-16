"""
    This file handles eveerything related to saving and deleting model objects.
"""
from .. import settings
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.contrib.contenttypes.models import ContentType

from ..models import ModelChangelog, ModelObject, Model, Application
from . import validate_instance, get_current_user


@receiver(m2m_changed, weak=False)
def m2m_callback(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    """" detect m2m changes and append to existing entry or create - also append to latest model change entry """
    if validate_instance(instance) and settings.AUTOMATED_LOGGING['to_database']:
        if action in ["post_add", 'post_remove']:
            modification = [model.objects.get(pk=x) for x in pk_set]

            if 'al_chl' in instance.__dict__.keys():
                changelog = instance.al_chl
            else:
                changelog = ModelChangelog()

                changelog.information = ModelObject()
                changelog.information.value = repr(instance)
                changelog.information.type = ContentType.objects.get_for_model(instance)
                changelog.information.save()
                changelog.save()

            for f in modification:
                obj = ModelObject()
                obj.value = repr(f)

                try:
                    obj.type = ContentType.objects.get_for_model(f)
                except Exception:
                    pass

                obj.save()
                if action == 'post_add':
                    changelog.inserted.add(obj)
                else:
                    changelog.removed.add(obj)

            changelog.save()

            if 'alevt' in instance.__dict__.keys():
                target = instance.al__evt
            else:
                target = Model()
                target.user = get_current_user()
                target.action = 1 if action == 'post_add' else 2
                target.save()

                target.application = Application.objects.get_or_create(name=ContentType.objects.get_for_model(instance).app_label)[0]

                target.information = ModelObject()
                target.information.value = repr(instance)
                target.information.type = ContentType.objects.get_for_model(instance)
                target.information.save()

            target.modification = changelog
            target.save()