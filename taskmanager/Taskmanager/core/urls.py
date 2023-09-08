from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns=[
    path("",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register_user,name="register"),
    path("home/",views.homepage,name="homepage"),
    path("create_task/",views.create_task,name="create-task"),
    path("view_task/",views.view_task,name="view-task"),
    path("into_task/<str:pk>",views.into_task,name="into-task"),
    path("delete_task/<str:pk>",views.delete_task,name="delete-task"),
    path("update_task/<str:pk>",views.update_task,name='update-task'),
    path("user_profile/",views.user_profile,name="user-profile"),
    path("profile_update/",views.profile_update,name="profile-update")

   
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)