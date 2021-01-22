from django.urls import path

from . import views

app_name = 'playground'
urlpatterns = [
    path(''                                    , views.index       , name='index'),
    path('run/'                               , views.run         , name='run'),
    path('<int:code_id>/'                      , views.index_edit  , name='index_edit'),
    path('<int:code_id>/run/'                  , views.run_code    , name='run_code'),
    path('question/<int:question_id>/'         , views.question    , name='question'),
    path('question/<int:question_id>/run/'     , views.run_question, name='run_question'),
    path('<int:code_id>/save/'                 , views.save        , name='save'),
]