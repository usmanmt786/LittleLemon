from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

booking_router = routers.DefaultRouter()
booking_router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuListView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuView.as_view(), name='menu-item'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('booking/', include(booking_router.urls)),
    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
