import json

import requests
from rest_framework import generics
from rest_framework.response import Response
from Apps.Compradores.models import Compradores
from Apps.Compradores.serializer import CompradoresSerializer
from Prueba.settings import API_URL


class CreateBuyerApi(generics.CreateAPIView):
    serializer_class = CompradoresSerializer

    def post(self, request, *args, **kwargs):
        status = 400
        try:
            nombre = request.data["nombre"]
            apellido = request.data["apellido"]
            direccion = request.data["direccion"]
            ciudad = request.data["ciudad"]

            if nombre and apellido and direccion and ciudad:
                buyer = Compradores.objects.create(nombre=nombre[:20],
                                                   apellido=apellido[:20],
                                                   direccion=direccion[:100],
                                                   ciudad=ciudad[:20])
                response = {
                    "detail": "Buyer created successfully",
                    "id": buyer.pk
                }
                status = 200
            else:
                response = {
                    "detail": "You have to fill the nombre, apellido, direccion and ciudad fields."
                }
        except:
            response = {
                "detail": "You must to send the data with the correct format."
            }

        return Response(response, status=status)


class BuyersListApi(generics.ListAPIView):
    serializer_class = CompradoresSerializer
    queryset = Compradores.objects.all()


class DetailBuyerApi(generics.RetrieveAPIView):
    serializer_class = CompradoresSerializer

    def get_object(self):
        return Compradores.objects.get(pk=self.request.GET["id"])


class DeleteBuyerApi(generics.DestroyAPIView):
    serializer_class = CompradoresSerializer
    model = Compradores

    def delete(self, request, *args, **kwargs):
        try:
            Compradores.objects.get(pk=kwargs["pk"]).delete()
            return Response({"detail": "Buyer deleted"}, status=203)
        except:
            return Response({"detail": "Buyer not found"}, status=404)


def format_address(address, city):
    address_formatted = address.replace("#", ",")
    city_formatted = city.replace("#", ",")
    return address_formatted + "," + city_formatted


def retrieve_geo_localization_data(address):
    resp = requests.get(API_URL+address)
    return json.loads(resp.text)


def get_lon_lat_info(api_data):
    try:
        location = api_data["results"][0]["geometry"]["location"]
        longitud = location["lng"]
        latitud = location["lat"]
        return longitud, latitud
    except:
        return 0, 0


class GeoCodifyBaseApi(generics.RetrieveAPIView):
    serializer_class = CompradoresSerializer
    buyers = Compradores.objects.filter(estado_geo=False)
    queryset = Compradores.objects.filter(estado_geo=False)
    def get(self, request, *args, **kwargs):
        response = []
        for buyer_data in self.buyers:
            api_data = retrieve_geo_localization_data(format_address(buyer_data.direccion, buyer_data.ciudad))
            lon, lat = get_lon_lat_info(api_data)
            self.save_geo_info(lon=lon, lat=lat, buyer=buyer_data)
            response.append(buyer_data.serializer())
        return Response(response)

    def save_geo_info(self, lon, lat,  buyer):
        if lon and lat:
            buyer.longitud = lon
            buyer.latitud = lat
            buyer.estado_geo = True
        else:
            buyer.longitud = 0
            buyer.latitud = 0
        buyer.save()