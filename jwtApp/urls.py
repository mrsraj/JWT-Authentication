from django.urls import path
from .views import RegisterUser , LoginUser 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from . import views 

urlpatterns = [
    
    #two new
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('register/', RegisterUser .as_view(), name='register_user'),  # Corrected
    path('login/', LoginUser .as_view(), name='login_user'),  # Ensure this view exists
    
    
    path('profile/', views.ProfileData, name='profile-data'),
]