from django.urls import path
from .views import *

# Just authenticated users can access these endpoints
urlpatterns = [
    path('crear/', CreateBuyerApi.as_view(), name="create_buyer"),
    path('lista/', BuyersListApi.as_view(), name="buyer_list"),
    path('usuario/', DetailBuyerApi.as_view(), name="buyer_detail"),
    path('eliminar/<int:pk>/', DeleteBuyerApi.as_view(), name="delete_buyer"),
    path('geocodificar_base/', GeoCodifyBaseApi.as_view(), name="geo_base_buyer"),
]
