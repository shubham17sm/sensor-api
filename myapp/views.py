from django.shortcuts import render
from .models import Sensor
from .serializers import SensorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SensorView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sensor_qs = Sensor.objects.all()
        serializer = SensorSerializer(sensor_qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorDetail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get_object(self, pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        sensor_qs = self.get_object(pk)
        serializer = SensorSerializer(sensor_qs)
        return Response(serializer.data)


    def put(self, request, pk):
        sensor_qs = self.get_object(pk)
        serializer = SensorSerializer(sensor_qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        sensor_qs = self.get_object(pk)
        sensor_qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    