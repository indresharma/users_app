from django.urls import path
from django.contrib.auth import views as auth_views


from users import views as user_views


app_name = 'users'


urlpatterns = [
    path('register/', user_views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<int:pk>/', user_views.ProfileView.as_view(), name='profile'),
    path('profile-update/<int:pk>/', user_views.ProfileUpdate.as_view(), name='update-profile'),
]
