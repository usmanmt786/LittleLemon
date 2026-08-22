from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer

def sayHello(request):
	return HttpResponse('Hello World')


def index(request):
	return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
