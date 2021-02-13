from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Apps.Users.serializer import UserSerializer, UserStateSerializer


class UpdateUserApi(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        try:
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            username = request.data["username"]
        except:
            response = {
                "Detail": "It lacks to add all info (first_name, last_name, username)"
            }
            return Response(response, status=400)

        user = request.user
        if first_name and last_name and username:
            try:
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.save()
                response = {
                    "Detail": "User info updated successfully",
                    "user": {
                        "id": user.pk,
                        "username": user.username,
                        "last_name": last_name,
                        "first_name": first_name,
                        "email": user.email,
                    }
                }
                return Response(response, status=200)
            except:
                response = {
                    "Detail": "Given username is duplicated. Please, change it."
                }
                return Response(response, status=409)
        else:
            response = {
                "Detail": "User info don't have to be empty"
            }
            return Response(response, status=400)


class DeactivateUserApi(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserStateSerializer

    def put(self, request, *args, **kwargs):
        user = request.user
        user.is_active = False
        user.save()
        response = {
            "Detail": "User account deactivated successfully",
            "status": user.is_active
        }
        return Response(response, status=200)


class ActivateUser(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):
        username = request.data["username"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]
