from django.urls import path

from . import views

app_name = 'bookmark'
urlpatterns = [
    path('<int:user_id>/list/'        , views.index       , name='index'),
    path('<int:question_id>/run/'     , views.run_bookmark, name='run_bookmark'),
    path('<int:bookmark_id>/release/' , views.release     , name='release'),
]