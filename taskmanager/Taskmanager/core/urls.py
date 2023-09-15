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
    
    path("into_task/<str:pk>",views.into_task,name="into-task"),
    path("delete_task/<str:pk>",views.delete_task,name="delete-task"),
    path("update_task/<str:pk>",views.update_task,name='update-task'),
    path("user_profile/",views.user_profile,name="user-profile"),
    path("profile_update/",views.profile_update,name="profile-update"),
    path("edit/",views.edit_profile,name="edit-profile"),
    path("complete_task/<str:pk>",views.complete_task,name="complete-task"),
    path("restore_task/<str:pk>",views.restore_task,name="restore-task"),
   
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)