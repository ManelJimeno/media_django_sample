from django.test import TestCase
from .models import Content, Channel


class ChannelRatingTestCase(TestCase):
    def setUp(self):
        # Create content with ratings
        content1 = Content.objects.create(title="Content 1", rating=8.0)
        content2 = Content.objects.create(title="Content 2", rating=6.0)

        # Create channels
        self.channel = Channel.objects.create(title="Main Channel")
        self.channel.contents.add(content1, content2)

    def test_channel_rating(self):
        # Test the average rating of the channel
        self.assertEqual(self.channel.calculate_rating(), 7.0)
