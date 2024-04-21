from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView    # 追記
from django.contrib.auth.forms import UserCreationForm    # 追記
from .views import UserCreateAndLoginView
from .forms import CustomUserCreationForm
from . import views


urlpatterns = [
    path('signup/', UserCreateAndLoginView.as_view(
        template_name='account/signup.html',
        form_class=CustomUserCreationForm,
        success_url='/account/login',
    ), name='signup'),    # 追記
    path('login/', LoginView.as_view(
        #redirect_authenticated_user=True,
        template_name='account/login.html'
    ), name='login'),
    path('logout/', views.cerrarsesion, name='logout'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(),
        name='password_change_done'),
path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
]