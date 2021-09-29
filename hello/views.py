from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from hello.models import HelloWorld
from hello.serializer import HelloWorldSerializer

@api_view(['GET', 'POST'])
def hello_world(request, format=None):
    if request.method == 'GET':
        values = HelloWorld.objects.all()
        serializer = HelloWorldSerializer(values, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HelloWorldSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
