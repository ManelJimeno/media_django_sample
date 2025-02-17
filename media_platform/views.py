from rest_framework import viewsets
from .models import Content, Channel, Group
from .serializers import ContentSerializer, ChannelSerializer, GroupSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_queryset(self):
        # Allow filtering by group if the parameter is provided
        group_id = self.request.query_params.get('group', None)
        if group_id:
            return self.queryset.filter(groups__id=group_id)
        return self.queryset
