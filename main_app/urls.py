from django.urls import path
from .views import test, send_mail_to_all

urlpatterns = [
    path("", test, name="test"),
    path("mail", send_mail_to_all, name="mail"),
]
