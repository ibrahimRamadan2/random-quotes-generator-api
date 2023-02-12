from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, exceptions
from .models import Quote
import random
from django.db.models import Max
from .serializer import qoute_serializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission


def get_random():
    max_id = Quote.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        quote = Quote.objects.filter(pk=pk).first()

        if quote:
            return quote


class QuoteAuthenticationPermission(BasePermission):
    message = 'You are not authorized to use this API!'

    def has_permission(self, request, view):
        print("i am heres ")
        return bool(request.user and request.user.is_authenticated)


class CustomNotAuthenticated(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {"message": "You are not authorized to use this API!"}
    default_code = 'not_authenticated'


class QouteView(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def permission_denied(self, request, message=None, code=None):
        """
        If request is not permitted, determine what kind of exception to raise.
        """
        print("i am here")
        if request.authenticators and not request.successful_authenticator:
            raise CustomNotAuthenticated()
        raise exceptions.PermissionDenied(detail=message, code=code)

    def get(slef, request):
        quote = get_random()
        quote_serializer = qoute_serializer(quote)
        return Response(quote_serializer.data, status.HTTP_200_OK)
