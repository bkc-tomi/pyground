from django.urls import path

from . import views

app_name = 'friend'
urlpatterns = [
    path('<int:user_id>/'                                    , views.follow      , name='follow'),
    path('<int:user_id>/<int:follow_user_id>/run/'           , views.run_follow  , name='run_follow'),
    path('<int:user_id>/<int:follow_id>/release/'            , views.release     , name='release'),
    path('<int:user_id>/follower/'                           , views.follower    , name='follower'),
    path('<int:user_id>/follow/permit/'                      , views.permit      , name='permit'),
    path('<int:user_id>/follow/run/permit/<int:follow_id>/'  , views.run_permit  , name='run_permit'),
    path('<int:user_id>/follow/run/nopermit/<int:follow_id>/', views.run_nopermit, name='run_nopermit'),
]