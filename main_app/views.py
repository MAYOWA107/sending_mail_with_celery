from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from mail.tasks import send_mail_func_new


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func_new.delay()
    return HttpResponse("Email has been sent. Check your gmail.")
