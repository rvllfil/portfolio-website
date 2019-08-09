from django.urls import re_path
from .views import index, message_post
#url for app

app_name = 'profile'

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^add_message', message_post, name='add_message'),
]
