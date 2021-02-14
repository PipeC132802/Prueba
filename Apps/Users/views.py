from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from Apps.Users.serializer import *


class UserRegistrationApi(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        status = 400
        try:
            username = request.data["username"]
            email = request.data["email"]
            password1 = request.data["password1"]
            password2 = request.data["password2"]

            if username and email and password1 and password2:
                if password1 != password2:
                    response = {
                        "detail": "Passwords not match."
                    }
                else:
                    try:
                        user = User.objects.create(username=username, email=email)
                        user.set_password(password1)
                        user.save()
                        response = self.get_tokens_for_user(user)
                        status = 200
                    except:
                        response = {
                            "detail": "username is already taken. Please, change yours and try again."
                        }
            else:
                response = {
                    "detail": "You have to fill all the required info."
                }
        except:
            response = {
                "detail": "You must send the data with the correct format."
            }
        if status == 200:
            response_obj = Response(response, status=status)
            response_obj.set_cookie('token', response["access_token"])
            return response_obj
        else:
            return Response(response, status=status)

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }


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
                "detail": "You must send the data with the correct format."
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
                    "detail": "User info updated successfully",
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
                    "detail": "Given username is duplicated. Please, change it."
                }
                return Response(response, status=409)
        else:
            response = {
                "detail": "User info don't have to be empty"
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
            "detail": "User account deactivated successfully",
            "status": user.is_active
        }
        return Response(response, status=200)


class ActivateUser(generics.UpdateAPIView):
    serializer_class = UserActiveSerializer

    def put(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            password = request.data["password"]
            if username and password:
                try:
                    user = User.objects.get(username=username)
                    if check_password(password, user.password):
                        user.is_active = True
                        user.save()
                        response = {
                            "detail": "User account activated successfully"
                        }
                        status = 200
                    else:
                        response = {
                            "detail": "Password not match. Try again"
                        }
                        status = 400
                except:
                    response = {
                        "detail": "User not found"
                    }
                    status = 404
            else:
                response = {
                    "detail": "You have to fill all the required info."
                }
                status = 400
        except:
            response = {
                "detail": "You must send the data with the correct format."
            }
            status = 406
        return Response(response, status=status)


class DeleteAccount(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = request.user
        try:
            user.delete()
            response = {
                "detail": "User account deleted."
            }
            status = 200
        except:
            response = {
                "detail": "User does not exist"
            }
            status = 406
        return Response(response, status=status)
