from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('register/'                    , views.register         , name='register'),
    path('register/complete/'           , views.register_complete, name='register_complete'),
    path('run/register/'                , views.run_register     , name='run_register'),
    path('login/'                       , views.login            , name='login'),
    path('<int:user_id>/run/login/'     , views.run_login        , name='run_login'),
    path('<int:user_id>/run/logout/'    , views.run_logout       , name='run_logout'),
    path('<int:user_id>/withdrawal/'    , views.withdrawal       , name='withdrawal'),
    path('<int:user_id>/run/withdrawal/', views.run_withdrawal   , name='run_withdrawal'),
    path('<int:user_id>/detail/'        , views.detail           , name='detail'),
    path('create/'                      , views.create           , name='create'),
    path('run/create/'                  , views.run_create       , name='run_create'),
    path('<int:user_id>/edit/'          , views.edit             , name='edit'),
    path('<int:user_id>/run/edit/'      , views.run_edit         , name='run_edit'),
    path(''                             , views.index            , name='index'),
]