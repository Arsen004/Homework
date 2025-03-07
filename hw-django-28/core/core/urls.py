from django.urls import path
from django.contrib.auth import views as auth_views
from app.views import user_info

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('user-info/', user_info, name='user_info'),
]
