from django.urls import path
from . import views

urlpatterns=[
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="register"),
    path("register/",views.register_user,name="register"),
    path("",views.homepage,name="homepage"),
    path("create_task/",views.create_task,name="create-task"),
    path("view_task/",views.view_task,name="view-task"),
    path("into_task/<str:pk>",views.into_task,name="into-task"),
    path("delete_task/<str:pk>",views.delete_task,name="delete-task"),
]