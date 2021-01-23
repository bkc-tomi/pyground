from django.urls import path

from . import views

app_name = 'playground'
urlpatterns = [
    path(''                                    , views.index       , name='index'),
    path('run/'                                , views.run         , name='run'),
    path('<int:code_id>/'                      , views.edit        , name='edit'),
    path('<int:code_id>/run/'                  , views.run_edit    , name='run_edit'),
    path('question/<int:question_id>/'         , views.question    , name='question'),
    path('question/<int:question_id>/run/'     , views.run_question, name='run_question'),
    path('save/'                               , views.save        , name='save'),
    path('<int:code_id>/upate/'                , views.update      , name='update'),
]