from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('sign-in/', views.sign_in, name="sign_in"),
    path('sign-out/', views.sign_out, name="sign_out"),
    path('sign-up/', views.sign_up, name="sign_up"),
    path('profile/', views.user_profile, name="user_profile"),
    path('createpost', views.post_create, name="post_create")
]