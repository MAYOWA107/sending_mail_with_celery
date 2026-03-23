from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from mail.tasks import send_mail_func_new
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func_new.delay()
    return HttpResponse("Email has been sent. Check your gmail.")


def schedule_task(request):
    schedule, created = CrontabSchedule.objects.get_or_create(minute="*/3")
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name="schedule_mail_task_" + "7",
        task="mail.tasks.send_mail_func_new",
    )
    return HttpResponse("Done")
