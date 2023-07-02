
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from myapp.serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful.'})
    return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
# # @authentication_classes([SessionAuthentication])  # Add this line
@permission_classes([])  # Optionally, allow non-authenticated requests
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out.'})

