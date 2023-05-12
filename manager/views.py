from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Link
from .serializers import LinkSerializer


class LinkAPI(APIView):
    http_method_names = ['get', 'post']
    serializer = LinkSerializer
    model = Link

    def get(self, request, short=None):
        if short:
            link = get_object_or_404(klass=self.model, short=short)
            return link.redirect()

        serializer = LinkSerializer(self.model.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *arg, **kwargs):
        data = JSONParser().parse(request)
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
