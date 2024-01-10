from django.http import HttpResponse
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView, Response
from posts.models import Post

from .serializers import PostsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
class PostsViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by("title")
    serializer_class = PostsSerializer
    permission_classes = [permissions.AllowAny]


def return_response(content: list, success: bool, status: str):
    response = {}
    response['success'] = success
    response['status'] = status
    response['message'] = content
    return response


@api_view(['POST'])
def create_post(request):
    post = PostsSerializer(data=request.data)
    if post.is_valid():
        post.save()
        return Response(return_response(post.data, True, status.HTTP_201_CREATED))
    return Response(return_response(post.errors, False, status.HTTP_400_BAD_REQUEST))
    

@api_view(['PATCH'])
def update_post(request):
    try:
        instance = Post.objects.get(pk=request.data['id'])
        post = PostsSerializer(instance, data=request.data)
        if post.is_valid():
            post.save()
            return Response(return_response(post.data, True, status.HTTP_201_CREATED))
        return Response(return_response(post.errors, False, status.HTTP_400_BAD_REQUEST))
    except Exception as error:
        return Response(return_response(error, False, status.HTTP_404_NOT_FOUND))


@api_view(['GET'])
def get_post(request):
    try:
        id = request.GET.get("id")
        post = Post.objects.get(pk=id)
        serializer = PostsSerializer(post)
        return Response(return_response(serializer.data, True, status.HTTP_302_FOUND))
    except Exception as error:
        return Response(return_response(error, False, status.HTTP_404_NOT_FOUND))


@api_view(['DELETE'])
def delete_post(request):
    try:
        id = request.GET.get("id")
        post = Post.objects.get(pk=id)
        post.delete()
        return Response(return_response({}, True, status.HTTP_204_NO_CONTENT))
    except Exception as error:
        print("delete", error)
        return Response(return_response(error, False, status.HTTP_404_NOT_FOUND))


def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")