from rest_framework import serializers
from .models import Content, Channel, Group

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'file_url', 'rating', 'metadata']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class ChannelSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    subchannels = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Channel
        fields = ['id', 'title', 'language', 'picture_url', 'parent_channel', 'subchannels', 'contents', 'groups', 'rating']

    def get_subchannels(self, obj):
        # Ensure subchannels exists before querying
        if hasattr(obj, 'subchannels'):
            subchannels = obj.subchannels.all()
            return ChannelSerializer(subchannels, many=True).data
        return []

    def get_groups(self, obj):
        # Use combined_groups or get_groups_from_subchannels to include subchannel groups
        groups = obj.combined_groups if hasattr(obj, 'combined_groups') else obj.get_groups_from_subchannels()
        if isinstance(groups, set):  # Convert to a list of dictionaries if it's a set
            return [{'id': group.id, 'name': group.name} for group in groups]
        return GroupSerializer(groups, many=True).data

    def get_rating(self, obj):
        return obj.calculate_rating()
