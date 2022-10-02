from email import message
from urllib import request, response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .serializer import DummySerializer, ProfileSerializer
from shan.models import Profile


# Create your views here.

global data
data = ["test"]


class PersonView(APIView):
    def get(self, request, format=None):
        message = {
            'Response': 200,
            'Message': "Welcome to Django Rest API",
            'data': data
        }
        return Response(message)

    def post(self, request, format=None):
        datas = request.data
        name = datas.get('name', None)
        data.append(name)
        message = {
            'Response': 200,
            'Message': "Welcome to Django Rest API",
            'data': data
        }
        return Response(message)


class WeatherView(generics.CreateAPIView):
    serializer_class = DummySerializer

    def create(self, request, *args, **kwargs):
        try:

            zipp = request.data.get('zipp')
            city = request.data.get('city')
            name = request.data.get('name')
            age = request.data.get('age')
            return super.create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "Message": "Success!",
                "zipp": zipp,
                "city": city,
                "name": name,
                "age": age
            })


class ProfileView(APIView):
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume uploaded successfully', 'status': 'success', 'candidate': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None, *args, **kwargs):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)


class ProfileSecond(generics.CreateAPIView):
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        try:

            name = request.data.get('name')
            email = request.data.get('email')
            dob = request.data.get('dob')
            state = request.data.get('state')
            gender = request.data.get('gender')
            location = request.data.get('location')
            pimage = request.data.get('pimage')
            rdoc = request.data.get('rdoc')
            return super.create(request, *args, **kwargs)
        except Exception as e:
            return Response(e)


def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, "index.html")


def contact(request):
    myName = ''
    myAge = ''

    try:
        if request.method == 'POST':
            myName = request.POST['name']
            myAge = request.POST['age']
    except:
        pass
    return render(request, "contactForm.html", {"name": myName, "age": myAge})
