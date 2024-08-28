from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from user_app.models import OrganizationUsers
from .serializers import UserSerializer
from .exceptions import custom_exception_handler


# Create your views here.
class AuthAppViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUsers.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Create a serializer instance with the provided data
        serializer = self.get_serializer(data=request.data)
        # Validate the data; raise an exception if invalid
        serializer.is_valid(raise_exception=True)
        # Save the new user instance to the database
        self.perform_create(serializer)
        # Get the HTTP headers for the response
        headers = self.get_success_headers(serializer.data)
        # Return the response with the created instance data
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


