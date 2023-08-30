# from rest_framework import serializers
# from .models import Sensor, Measurements
#
# class SensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description']
#
# class MeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurements
#         fields = ['temperature', 'created_at']
# TODO: опишите необходимые сериализаторы

# class MeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = ['temperature', 'created_at']


# class SensorDetailSerializer(serializers.ModelSerializer):
#     measurements = MeasurementSerializer(read_only=True, many=True)
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description', 'measurements']