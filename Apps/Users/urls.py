from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', UserRegistrationApi.as_view(), name="user_registration"),
    path('update-account-info/', UpdateUserApi.as_view(), name="update_user"),
    path('deactivate-account/', DeactivateUserApi.as_view(), name="user_deactivate"),
    path('activate-account/', ActivateUser.as_view(), name="user_activate"),
    path('delete-account/', DeleteAccount.as_view(), name="user_delete"),
]
