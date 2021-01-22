from django.urls import path

from . import views

app_name = 'friend'
urlpatterns = [
    path('<int:user_id>/follow/'             , views.follow      , name='follow'),
    path('<int:user_id>/follow/release'      , views.release     , name='release'),
    path('<int:user_id>/follower/'           , views.follower    , name='follower'),
    path('<int:user_id>/follow/permit/'      , views.permit      , name='permit'),
    path('<int:user_id>/follow/run/permit/'  , views.run_permit  , name='run_permit'),
    path('<int:user_id>/follow/run/nopermit/', views.run_nopermit, name='run_nopermit'),
]