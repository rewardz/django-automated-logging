from automated_logging.middleware import AutomatedLoggingMiddleware
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, weak=False)
@transaction.atomic
def post_save_signal(sender, instance, created, **kwargs) -> None:
    try:
        # check if sender has created_by and updated_by fields or not
        sender._meta.get_field("created_by")
        sender._meta.get_field("updated_by")

        user_id = AutomatedLoggingMiddleware.get_current_user()
        # update created_by and updated_by only if user is logged in
        if user_id:
            if created:
                instance.created_by = user_id
            instance.updated_by = user_id
            instance.save()
    except Exception:
        pass
