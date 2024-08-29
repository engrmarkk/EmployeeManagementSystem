from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from rest_framework.exceptions import ValidationError
from .helper import get_tokens_for_user


# Create your views here.
class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        raise ValidationError(serializer.errors)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # token, created = Token.objects.get_or_create(user=user)
            token = get_tokens_for_user(user)
            return Response({
                "message": "Login successful",
                "token": token,
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)
