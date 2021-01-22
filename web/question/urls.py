from django.urls import path

from . import views

app_name = 'question'
urlpatterns = [
    path('list/'                      , views.questions  , name='questions'),
    path('<int:user_id>/manage/'      , views.manage     , name='manage'),
    path('<int:question_id>/detail/'  , views.detail     , name='detail'),
    path('create/'                    , views.create     , name='create'),
    path('run/create/'                , views.run_create , name='run_create'),
    path('<int:question_id>/edit/'    , views.edit       , name='edit'),
    path('<int:question_id>/run/edit/', views.run_edit   , name='run_edit'),
]