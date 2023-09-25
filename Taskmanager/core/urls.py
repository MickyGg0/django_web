from django.urls import path
from . import views


urlpatterns=[
    path("",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register_user,name="register"),
    path("home/",views.homepage,name="homepage"),
    path("create_task/",views.create_task,name="create-task"),
    path("delete_task/<str:pk>",views.delete_task,name="delete-task"),
    path("update_task/<str:pk>",views.update_task,name='update-task'),
    path("user_profile/",views.user_profile,name="user-profile"),
    path("complete_task/<str:pk>",views.complete_task,name="complete-task"),
    path("restore_task/<str:pk>",views.restore_task,name="restore-task"),
    path("update_profile",views.update_profile,name="profile-update")
   
] 


