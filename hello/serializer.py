from hello.models import HelloWorld
from rest_framework import serializers

class HelloWorldSerializer(serializers.ModelSerializer):

    class Meta:
        model = HelloWorld
        fields = '__all__'
        # fields = ('status', 'value', 'active', 'created')