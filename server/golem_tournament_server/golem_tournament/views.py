from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, generics
from django.http import Http404
from golem_tournament.models import Golem
from golem_tournament.serializers import GolemSerializer, UserSerializer
from golem_tournament.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreate
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


class SignUp(APIView):
    permission_classes = (IsAuthenticatedOrCreate,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        print(username)
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class GolemList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        golems = Golem.objects.all()
        serializer = GolemSerializer(golems, many=True)
        return Response(serializer.data)


class GolemDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            return Golem.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        golem = self.get_object(pk)
        serializer = GolemSerializer(golem)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        golem = self.get_object(pk)
        serializer = GolemSerializer(golem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        golem = self.get_object(pk)
        golem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GolemCreator(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        print(request.user.id)
        serializer = GolemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
