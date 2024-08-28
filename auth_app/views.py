from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response


# Create your views here.
class AuthAppViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
