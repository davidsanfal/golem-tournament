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


class SignUp(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GolemCreator(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Golem.objects.all()
    serializer_class = GolemSerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GolemList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Golem.objects.all()
    serializer_class = GolemSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_by_name(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_by_name(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class GolemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Golem.objects.all()
    serializer_class = GolemSerializer
