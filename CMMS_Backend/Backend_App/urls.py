from django.urls import path
from .views import (
    SignupView,
    LoginView,
    LogoutView,
    ForgotPasswordView,
    ResetPasswordTemplateView,
    HallListView,
    UserProfileView,
    NotificationListView
)

urlpatterns = [
    path('halls/', HallListView.as_view(), name='halls'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordTemplateView.as_view(), name='reset-password'),
]
