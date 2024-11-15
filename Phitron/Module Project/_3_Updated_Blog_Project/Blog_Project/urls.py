from django.contrib import admin
from django.urls import path

from Post_App import views as PostAppViews
from Authenticator_App import views as AuthenticatorAppViews
from Categories_App import views as CategoriesAppViews

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', PostAppViews.home, name='home'),
    path('add/post', PostAppViews.add_post, name='addpost'),
    path('edit/profile', PostAppViews.home, name='editprofile'),
    path('post/<slug:url>/', PostAppViews.view_post, name='viewpost'),

    path('add/category', CategoriesAppViews.add_categories, name='addcategory'),

    path('login', AuthenticatorAppViews.login_page, name='login'),
    path('signup', AuthenticatorAppViews.signup_page, name='signup'),
    path('profile', AuthenticatorAppViews.profile, name='profile'), 
    path('logout', AuthenticatorAppViews.logout_page, name='logout'), 
]
