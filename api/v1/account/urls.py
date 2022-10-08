from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
    

urlpatterns = [
path('accounts/',views.CustomUserListCreateAPIView.as_view(),name='user-list'),
path('accounts/<int:pk>/',views.CustomUserDetailAPIView.as_view(),name='user-detail'),

# path('api-auth/', include('rest_framework.urls')),

path('register/',views.RegisterAPIView.as_view(),name='register'),

path('login/', TokenObtainPairView.as_view(), name='login'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

path('logout/', views.LogOutAPIView.as_view(), name='logout')

]

