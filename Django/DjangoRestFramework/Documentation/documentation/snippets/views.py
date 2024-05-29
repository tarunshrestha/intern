from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from rest_framework import status
from rest_framework import mixins, generics
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .permissions import IsOwnerOrReadOnly

from .models import *
from .serializers import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def index(request):
    return HttpResponse("Home")

# ------------------------------ ViewSet-------------------------
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

# ----------------------------- End Point for api ---------------------------------------------
@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse('user-list', request = request, format = format),
        'snippets': reverse('snippet-list', request = request, format = format)
    })

# ----------------------------- End-point for Snippet Highlights ---------------------------------------------
class SnippetHighlight(generics.GenericAPIView):
    query = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


# ----------------------------- User Class ---------------------------------------------
class UserAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ------------------- Class based --------------------------------------------------------------------------

# class SnippetList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializers = SnippetSerializer(snippets, many=True)
#         return Response(data=serializers.data, status=status.HTTP_207_MULTI_STATUS)

#     def post(self, request, format=True):
#         serializer = SnippetSerializer(data=request.data)
#         if serializers.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)

# ------------------- Class based ( generic ) --------------------------------------------------------------------------

class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# ------------------- Class based ( mixins ) --------------------------------------------------------------------------

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    

# ------------------- Class based --------------------------------------------------------------------------
    
# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# ------------------- Function based --------------------------------------------------------------------------

# @api_view(['POST', "GET"])
# def snippet_list(request, format=None):
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response({'data' :serializer.data})
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data' :serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({'error' :serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
        
# @api_view(['POST', "GET"])
# def snippet_detail(request, pk, format=None):
#     if Snippet.objects.filter(pk=pk).exists():
#         snippet = Snippet.objects.get(pk=pk)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=="GET":
#         serializer = SnippetSerializer(snippet)
#         return Response(data = serializer.data)
#     elif request.method == "PUT":
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        


