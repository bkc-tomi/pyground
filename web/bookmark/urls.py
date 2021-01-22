from django.urls import path

from . import views

app_name = 'bookmark'
urlpatterns = [
    path('<int:user_id>/list/'        , views.index, name='index'),
    path('<int:user_id>/list/release/', views.release, name='release'),
]