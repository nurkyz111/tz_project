from django.urls import path
from .views import UserRegisterAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='user_profile'),

]