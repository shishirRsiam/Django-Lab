from django.contrib import admin
from django.urls import path
from Authentication_App import views as Authentication_App_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Authentication_App_Views.home, name='home'),
    path('login/', Authentication_App_Views.login_view, name='login'),
    path('logout/', Authentication_App_Views.logout_view, name='logout'),
    path('signup/', Authentication_App_Views.signup_by_html, name='signup'),
    path('edit/profile/', Authentication_App_Views.edit_profile, name='editprofile'),
    path('edit/password/', Authentication_App_Views.change_password, name='changepassword'),
]
