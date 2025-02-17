import csv
from django.core.management.base import BaseCommand
from media_platform.models import Channel

class Command(BaseCommand):
    help = 'Export channel ratings to a CSV file'

    def handle(self, *args, **kwargs):
        # Query all channels
        channels = Channel.objects.all()

        # Prepare CSV file
        with open('channel_ratings.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Channel Title', 'Average Rating'])

            for channel in channels:
                writer.writerow([channel.title, channel.calculate_rating() or 'Undefined'])

        self.stdout.write(self.style.SUCCESS('Channel ratings have been exported to channel_ratings.csv'))
