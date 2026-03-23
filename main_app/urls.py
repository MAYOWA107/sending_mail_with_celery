from django.urls import path
from .views import test, send_mail_to_all, schedule_task

urlpatterns = [
    path("", test, name="test"),
    path("mail", send_mail_to_all, name="mail"),
    path("task", schedule_task, name="task"),
]
