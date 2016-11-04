from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from golem_tournament.models import Golem
from golem_tournament.serializers import GolemSerializer

class GolemList(APIView):

    def get(self, request, format=None):
        golems = Golem.objects.all()
        serializer = GolemSerializer(golems, many=True)
        return Response(serializer.data)


class GolemDetail(APIView):

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        self.get_object(pk)
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

    def post(self, request):
        serializer = GolemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
