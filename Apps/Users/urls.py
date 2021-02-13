from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/update/', UpdateUserApi.as_view(), name="update_user"),
    path('auth/deactivate-account/', DeactivateUserApi.as_view(), name="user_status"),

]
