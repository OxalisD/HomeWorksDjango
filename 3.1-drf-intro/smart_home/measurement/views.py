# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
# from .models import Sensor, Measurements
# from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
#
# class SensorView(ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
# class SensorUpdateView(RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

# class SensorOne(APIView):
#     def patch(self, request, pk):
#         print(pk)
#         sensor = Sensor.objects.get(id=pk)
#         sensor =
#         print(sensor)
#         serializer = SensorSerializer(sensor, many=False)
#         return Response(serializer.data)



# class MeasurementNew(ListAPIView):
#     queryset = Measurements.objects.all()
#     serializer_class = MeasurementSerializer




