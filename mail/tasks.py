from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


@shared_task(bind=True)
def send_mail_func_new(self):
    print("new task is running.")
    users = User.objects.all()

    for u in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you are enjoying my code, please follow me for more."
        to_mail = u.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently=True,
        )
    return "Done"
