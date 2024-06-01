from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework import status
from django.contrib.auth import login

from .serializer import *
from .models import *


# Create your views here.

# -------------------------------------------- Class Based User --------------------------
class UserAPI(APIView):
    def get(self,request):
        id = request.GET.get('id')
        if CustomUser.objects.filter(id = id).exists():
            user = CustomUser.objects.get(id = id)
            serializer = UserSerializer(user)
            return Response({
                'message':"User Info",
                "data": serializer.data
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
            'message':'User id is incorrect.',
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        data = request.data
        id = data['user']
        if not CustomUser.objects.filter(id = id).exists():
            Response({'message: "User id invalid.'}, 
                     status=status.HTTP_404_NOT_FOUND)
        user = CustomUser.objects.get(id = id)
        serializer = UserSerializer(user, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':"User updated successfully",
                "data": serializer.data
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({
                'message': "User logged out successfully."
            }, status=status.HTTP_202_ACCEPTED)

        else:
            return Response({
                'message': "User is not logged in."
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data= request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                print(serializer.data)
                user = CustomUser.objects.get(email=serializer.data['email'])
                tokens = RefreshToken.for_user(user)
                # return Response({'access': str(tokens.access_token), 'refresh': str(tokens)})
                return Response({
                'message': "User Logged in.",
                'token': {'access': str(tokens.access_token), 'refresh': str(tokens)},
                'data': serializer.data
                }, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response({
            #     'status':400,
            #     'message':"Form is invalid.",
            #     'error': serializer.errors   
            #     })
        except Exception as e:
            print("------------------------------------------------------------------------")
            print(e)
            return Response({
                'message':"Something went wrong"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': "User Registered Successfully.",
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'message':"User Form Error.",
                'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        
        
        