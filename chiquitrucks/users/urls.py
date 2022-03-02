from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
# I can refer as the app accounts on the left side of the template 
# tag in the html section
app_name = 'users'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('profile/', views.Profile, name='profile'),

]