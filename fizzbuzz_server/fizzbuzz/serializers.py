from rest_framework import serializers
from .models import FizzBuzzRequest

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzzRequest
        fields = ('int1', 'int2', 'limit', 'str1', 'str2', 'result')

    def create(self, validated_data):
        result = self.calculate_fizzbuzz(validated_data)
        instance = FizzBuzzRequest.objects.create(**validated_data, result=result)
        return instance

    def calculate_fizzbuzz(self, data):
        int1, int2, limit, str1, str2 = data.values()
        results = []
        for i in range(1, limit + 1):
            output = str(i)
            if i % int1 == 0:
                output = str1
            if i % int2 == 0:
                output = str2 if output == str(i) else str1 + str2
            results.append(output)
        return ','.join(results)
