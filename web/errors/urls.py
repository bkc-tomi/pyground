from django.urls import path

from . import views

app_name = 'errors'
urlpatterns = [
    path(''        , views.errors       , name='errors'),
]