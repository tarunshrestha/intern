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
from .email import Email

email = Email()

# Create your views here.
@api_view(['GET', 'POST', "PATCH"])
def index(request):
    if request.method == 'GET':
        return Response({
        'status':200, 
        'message': "Yes! Its working.",
        "method_used": "GET"
        })
    elif request.method == 'POST':
        return Response({
        'status':200, 
        'message': "Yes! Its working.",
        "method_used": "POST"
        })
    elif request.method == 'PATCH':
        return Response({
        'status':200, 
        'message': "Yes! Its working.",
        "method_used": "PATCH"
        })
    else:
        return Response({
        'status':400, 
        'message': "No! Its not working.",
        "method_used": "Invalid"
        })


@api_view(["GET"])
def get_todo(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response({
        'status':True,
        'message':'Todo Fetch',
        'data': serializer.data
    })

@api_view()
def get_individual(request):
    id = request.GET.get('id')
    todo = Todo.objects.get(url_id = id)
    serializer = TodoSerializer(todo)
    return Response({
        'status':True,
        'message':'Todo Fetch',
        'data': serializer.data
    })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        print(data)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':"Success data",
                'data':serializer.data
                    })

        return Response({
        'status':False,
        'message':"invalid data",
        'data':serializer.errors
            })
    except Exception as e:
        print(e)
    return Response({
        'status':False,
        'message':"Something went wrong"    
        })


@api_view(["PATCH"])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('url_id'):
            return Response({
                'status':False,
                'message':"url_id is required.",
                'data':{}
                })
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':"Invalid url_id."    
            })
    else:
        obj = Todo.objects.get(url_id = data.get('url_id'))
        serializer = TodoSerializer(obj, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':"Success data",
                'data':serializer.data
                    })
        

# -------------------------------------------- Class Based User --------------------------
class UserAPI(APIView):
    def get(self,request):
        id = request.GET.get('id')
        if CustomUser.objects.filter(id = id).exists():
            user = CustomUser.objects.get(id = id)
            serializer = UserSerializer(user)
            return Response({
                'status': 200,
                'message':"User Info",
                "data": serializer.data
            })
        return Response({
            'status':400,
            'message':'User id is incorrect.',
        })

class UserLogout(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            Response({
                'status': 200,
                'message': "User logged out successfully."
            })

        else:
            Response({
                'status': 400,
                'message': "User is not logged in."
            })

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
                email.send_otp(serializer.data['email'])
                return Response({
                    'status':200,
                    'message': "User Registered Successfully.",
                    'data': serializer.data
                })
            return Response({
                'status':400,
                'message':"User Form Error.",
                'errors': serializer.errors
                })
        # except Exception as e:
        #     print(e)
        #     return Response({
        #         'status':400,
        #         'message':"Something went wrong"    
        #         })
        
class VerifyOTP(APIView):
    def post(self,request):
        try:
            data= request.data
            serializer = VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = CustomUser.objects.filter(email=email)
                if not user.exists() or user[0].otp != otp:
                    return Response({
                    'status':400,
                    'message': "User email or Otp not matched."
                        })
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({
                    'status':200,
                    'message': "User Verified Successfully.",
                    'data': serializer.data
                })

        except Exception as e:
            print(e)
            return Response({
                'status':400,
                'message':"Something went wrong"    
                })
        
            


# --------------------------------------------- Class Based Todo------------------------------------------------------------------------------------------
class TodoView(APIView):

    def get(self, request):
        # if request.user.is_authenticated:
        #     return Response({'detail': 'You need to registered or logged in.'})

        id = request.GET.get('id')
        todo_id = request.GET.get('tid') 
        if id:
            todo = CustomUser.objects.get(id=id).todo.all()
            serializer = TodoSerializer(todo, many=True)
            if todo_id:
                todo = Todo.objects.get(url_id = todo_id)
                serializer = TodoSerializer(todo)
                return Response({
                    'status':200,
                    'message':'Todo details got successfully.',
                    'data': serializer.data
                        })
            return Response({
                    'status':200,
                    'message':'All todo received.',
                    'data': serializer.data
                        })
        else:
            return Response({
                'status':False,
                'message':'Something went wrong.',
            })
    
    def post(self, request):
        try:
            data = request.data
            print(data)
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':"Successfull todo added.",
                    'data':serializer.data
                        })

            return Response({
            'status':False,
            'message':"Cannot add todo.",
            'data':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':"Something went wrong",    
                })
    
    def patch(self, request):
        try:
            id = request.GET.get('id')
            data = request.data
            if id == None:
                return Response({
                    'status':False,
                    'message':"url_id is required.",
                    'data':{}
                    })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':"Invalid url_id."    
                })
        else:
            obj = Todo.objects.get(url_id = id)
            serializer = TodoSerializer(obj, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':"Success data updated.",
                    'data':serializer.data
                        })

    def delete(self, request):
        try:
            id = request.GET.get('id')
            data = Todo.objects.get(url_id = id)
            if not data:
                return Response({
                    'status': False,
                    'message': "Id not found.",
                    'data': {}
                })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "Url invalid or something went wrong."
            })
        else:
            data.delete()
            return Response({
                'status': True,
                'message': "Todo deleted successfully."
            })