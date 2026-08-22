from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Booking, Menu, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, MenuSerializer, UserSerializer

def sayHello(request):
	return HttpResponse('Hello World')


def index(request):
	return render(request, 'index.html', {})


class MenuListView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class MenuItemsView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def msg(request):
	return Response({'message': 'This view is protected'})
