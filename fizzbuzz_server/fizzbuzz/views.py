from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from fizzbuzz.serializers import FizzBuzzSerializer
from fizzbuzz.models import FizzBuzzRequest

class FizzBuzzView(APIView):
    def post(self, request):
        serializer = FizzBuzzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class StatsView(APIView):
    def get(self, request):
        most_frequent = FizzBuzzRequest.objects.most_common(1)[0][0]
        return Response({
            'most_frequent_params': FizzBuzzSerializer(most_frequent).data,
            'hits': most_frequent.hits
        })
