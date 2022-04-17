from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger import renderers

from presentation.models import Presentation
from presentation.serializers import PresentationSerializer
from rest_framework.schemas import SchemaGenerator


class PresentationCreateAndListAPIView(generics.ListCreateAPIView):

    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer

    def post(self, request, *args, **kwargs):
        serializer = PresentationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PresentationDetailAPIView(generics.RetrieveAPIView):
    queryset = Presentation
    serializer_class = PresentationSerializer
