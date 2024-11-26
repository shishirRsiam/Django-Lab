from django.urls import path
from Authenticator_App import views as Authenticator_App_Views


urlpatterns = [
    path('profile/', Authenticator_App_Views.profile_page, name='profile'),
    path('edit/profile/', Authenticator_App_Views.edit_profile, name='edit_profile'),
    path('edit/password/', Authenticator_App_Views.change_password, name='change_password'),
    path('login/', Authenticator_App_Views.login_page, name='login'),
    path('logout/', Authenticator_App_Views.logout_page, name='logout'),
    path('signup/', Authenticator_App_Views.signup_page, name='signup'),
    path('help/', Authenticator_App_Views.signup_page, name='help'),
]
