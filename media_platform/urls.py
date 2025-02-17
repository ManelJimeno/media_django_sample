from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, ChannelViewSet, GroupViewSet

router = DefaultRouter()
router.register('contents', ContentViewSet, basename='content')
router.register('channels', ChannelViewSet, basename='channel')
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
