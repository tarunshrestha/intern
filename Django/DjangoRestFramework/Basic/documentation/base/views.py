from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *

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
        



# --------------------------------------------- Class Based ------------------------------------------------------------------------------------------
class TodoView(APIView):

    def get(self, request):
        id = request.GET.get('id')
        if id != None:
            todo = Todo.objects.get(url_id = id)
            serializer = TodoSerializer(todo)
        else:
            todo = Todo.objects.all()
            serializer = TodoSerializer(todo, many=True)
        return Response({
            'status':True,
            'message':'All Todos.',
            'data': serializer.data
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