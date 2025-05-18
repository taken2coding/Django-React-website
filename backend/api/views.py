from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Book
from .serializers import UserSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import generics


class Home(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        return Response(data)


class UserProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()


def home(request):
    Response({
        "Welcome to our API"
    })

