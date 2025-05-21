from django.urls import path
from .views import login_user, register_user,logout_user,user_profile_view,edit_profile
# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login", login_user, name="login"),
    path("register", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("my-profile", user_profile_view, name="my_profile"),
    path("edit-my-profile", edit_profile, name="edit_profile"),

]
