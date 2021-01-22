from django.urls import path

from . import views

app_name = 'playground'
urlpatterns = [
    path('<int:code_id>'                       , views.index       , name='index'),
    path('<int:code_id>/run/'                  , views.run         , name='run'),
    path('<int:question_id>/<int:code_id>'     , views.question    , name='question'),
    path('<int:question_id>/<int:code_id>/run/', views.run_question, name='run_question'),
    path('<int:code_id>/save/'                 , views.save        , name='save'),
]