from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Case, When, Value, IntegerField
from django.shortcuts import redirect
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework import status, generics, mixins, viewsets
from django.contrib.auth import login

from .serializer import *
from .models import *


# Create your views here.

# -------------------------------------------- Class Based User --------------------------
class UserAPI(APIView):
    def get(self,request):
        id = request.user.id

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

    def get(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({
                'message': "User logged out successfully."
            }, status=status.HTTP_202_ACCEPTED)

        else:
            return Response({
                'message': "User is not logged in."
            }, status=status.HTTP_400_BAD_REQUEST)

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class LoginUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
            data= request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                # print('@' in serializer.data['username'])
                if '@' not in serializer.data['username']:
                    user = CustomUser.objects.get(username=serializer.data['username'])
                else:
                    user = CustomUser.objects.get(email=serializer.data['username'])
                tokens = RefreshToken.for_user(user)
                return Response({
                'message': "User Logged in.",
                'token': {'access': str(tokens.access_token), 'refresh': str(tokens)},
                'data': serializer.data
                }, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)

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

# ------------------------------------ Normal User ----------------------------------------------------------         
class UserTicketApi(viewsets.ModelViewSet):
    # queryset = Ticket.objects.all()
    queryset = Ticket.objects.annotate(
    severity_order=Case(
        When(severity='high', then=Value(1)),
        When(severity='medium', then=Value(2)),
        When(severity='low', then=Value(3)),
        output_field=IntegerField(),
    )).order_by('severity_order')[::-1]
    serializer_class = TicketSerializer
    lookup_field = 'pk'
    # pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    

    # def base_auth(self, request, pk=None):
    #     id = request.user.id
    #     user = CustomUser.objects.filter(id=id)
    #     if user.exists():
    #         if user.first().groups.first() != Group.objects.get(name = "NormalUser"): 
    #             return redirect('developer_ticket')
    #     return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data= request.data
        user_id = request.user.id
        if user_id:
            if CustomUser.objects.filter(id=user_id).exists():
                user = CustomUser.objects.get(id = user_id)
                serializer = self.get_serializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Ticket created", 'data':serializer.data}, status=status.HTTP_201_CREATED)
                return Response({"message":"Ticket validation error.", "error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message":"User id invalid."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        id = pk
        user_id = request.user.id
        user = CustomUser.objects.filter(id=user_id)
        if user.exists():
            if user.first().groups.first() != Group.objects.get(name = "NormalUser"): 
                return redirect('developer_ticket')
        else: return Response("User not found.", status=status.HTTP_404_NOT_FOUND)
        if id:
            if Ticket.objects.filter(id=id).exists():
               
                ticket = Ticket.objects.get(id = id)
                serializer = self.get_serializer(ticket)                
                return Response({'message':"Ticket details.",
                                 "data":serializer.data}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"meassage":"Ticket id invalid."}, status=status.HTTP_400_BAD_REQUEST)
                
        if user_id:
            user = CustomUser.objects.filter(id=user_id)
            serializer = self.get_serializer(Ticket.objects.filter(created_user = user_id), many=True)
            return Response({'message':"All User Tickets.",
                                 "data":serializer.data}, status=status.HTTP_202_ACCEPTED)
        else: return Response({'message':"Login first."}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=["PATCH"])
    def update(self, request, pk=None):
        data = request.data
        id = pk
        user_id = request.user.id
        user = CustomUser.objects.filter(id=user_id)
        if user.exists():
            if user.first().groups.first() != Group.objects.get(name = "NormalUser"): 
                return redirect('developer_ticket')
        else: return Response("User not found.", status=status.HTTP_404_NOT_FOUND)
        if id:
            if Ticket.objects.filter(id = id).exists():
                ticket = Ticket.objects.get(id = id)
                serializer = self.serializer_class(ticket, data=data, partial=True, context = {"request":request})
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'message':"Success data updated.",
                        'data':serializer.data
                            }, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({"message":"something went wrong.", "error":serializer.errors}, 
                                    status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':"Ticket id invalid.",}, status=status.HTTP_400_BAD_REQUEST)
                
        return Response({'message':"Ticket id required.",}, status=status.HTTP_400_BAD_REQUEST)
    

#     {
#     "status": "Forwarded"
# }


    def delete(self, request, pk=None):
        user_id = request.user.id
        user = CustomUser.objects.filter(id=user_id)
        if user.exists():
            if user.first().groups.first() != Group.objects.get(name = "NormalUser"): 
                return redirect('developer_ticket')
        else: return Response("User not found.", status=status.HTTP_404_NOT_FOUND)
        id = pk
        print(id)
        if not Ticket.objects.filter(id=id).exists():
            return Response({'message':"Ticket id invalid."}, status=status.HTTP_400_BAD_REQUEST)
        ticket = Ticket.objects.get(id = id)
        ticket.delete()
        return Response({
            'message': "Ticket deleted successfully."
        }, status=status.HTTP_202_ACCEPTED)
    
# ------------------------------------ Dev User ----------------------------------------------------------         

class DevUserApi(viewsets.ModelViewSet):
    # queryset = Ticket.objects.all()
    queryset= Ticket.objects.annotate(severity_order=Case(
        When(severity='high', then=Value(1)),
        When(severity='medium', then=Value(2)),
        When(severity='low', then=Value(3)),
        output_field=IntegerField(),
    )).order_by('severity_order')[::-1]
    serializer_class = TicketSerializer
    # pagination_class = PageNumberPagination
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        id = request.user.id
        ticket_id = pk
        user = CustomUser.objects.filter(id=id)
        if user.first().groups.first() == Group.objects.get(name = "NormalUser"):
                return redirect('user_ticket')
        if id:
            if Ticket.objects.filter(id=ticket_id).exists():
                ticket = Ticket.objects.get(id = ticket_id)
                if user.first().groups.first() != ticket.assigned_to:
                    return redirect('developer_ticket')
                serializer = self.get_serializer(ticket)                
                return Response({'message':"Ticket details.",
                                 "data":serializer.data}, status=status.HTTP_202_ACCEPTED)
        # print("-----------------------------------------------------------")
        # print( user.first().groups.first() == Group.objects.get(name = "NormalUser"))
        data = Ticket.objects.filter(assigned_to = user.first().groups.first())
        serializer = self.serializer_class(data, many=True)
        return Response({'message':"Assigned Tickets.", 
                            'data':serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    @action(detail=True, methods=["PATCH"])
    def update(self, request, pk=None):
        data = request.data # recent_user
        ticket_id = pk
        user_id = request.user.id
        user = CustomUser.objects.filter(id=user_id)
        if user.first().groups.first() == Group.objects.get(name = "NormalUser"):
            if not user.exists():
                return Response({"message":"Something went wrong."}, status=status.HTTP_404_NOT_FOUND)
            return redirect('user_ticket')
        tickets = Ticket.objects.filter(id=ticket_id)
        if not tickets.exists():
            return Response({"message":"Something went wrong."}, status=status.HTTP_404_NOT_FOUND)
        ticket = tickets.first()
        if user.first().groups.first() != ticket.assigned_to:
                    return redirect('developer_ticket')
        serializer = self.serializer_class(ticket, data=data, partial=True, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':"Ticket updated.",
                'data': serializer.data
            }, status=status.HTTP_202_ACCEPTED)
        return Response({"message":"Something went wrong.",
                            "error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

            
#----------------------------- CommentApi -------------------------------------------------
class CommentApi(generics.ListCreateAPIView, mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        data = request.data
        print(data)
        if data['ticket'] and data['user']:
            if Ticket.objects.filter(id=data['ticket']).exists() and CustomUser.objects.filter(id=data['user']).exists():
                serializer = self.serializer_class(data=data)
                if serializer.is_valid():
                    serializer.save()
                return Response({'message': 'Something went wrong.', 
                                 'data': serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'message': 'Ticket id invalid.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        id = request.GET.get('ticket')
        print(id)
        if not Ticket.objects.filter(id=id).exists():
            return Response({'message': 'Ticket id invalid.'}, status=status.HTTP_400_BAD_REQUEST)
        data = Comment.objects.filter(ticket = id)
        serializer = self.serializer_class(data, many=True)
        return Response({'message': 'Ticket comments.', 'data':serializer.data}, status=status.HTTP_202_ACCEPTED)

        


        
        