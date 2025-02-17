from typing import Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Content(models.Model):
    """
    Model representing individual pieces of content.
    """
    title: models.CharField = models.CharField(max_length=255)
    description: models.TextField = models.TextField(blank=True, null=True)
    file_url: models.URLField = models.URLField(blank=True, null=True)  # URL for the associated file (video, PDF, etc.)
    rating: models.DecimalField = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )  # Rating between 0 and 10
    metadata: models.JSONField = models.JSONField(blank=True, null=True)  # Arbitrary metadata in JSON format

    def __str__(self) -> str:
        return self.title


class Group(models.Model):
    """
    Model representing groups that channels can belong to.
    """
    name: models.CharField = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Channel(models.Model):
    """
    Model representing a channel, which can contain subchannels or content.
    """
    title: models.CharField = models.CharField(max_length=255)
    language: models.CharField = models.CharField(max_length=10, blank=True, null=True)  # Language code (e.g., 'en', 'es')
    picture_url: models.URLField = models.URLField(blank=True, null=True)  # URL for the channel picture
    parent_channel: models.ForeignKey= models.ForeignKey(
        'self',
        related_name='subchannels',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )  # Parent channel for hierarchical structure
    groups: models.ManyToManyField = models.ManyToManyField(Group, blank=True)  # Groups associated with the channel
    contents: models.ManyToManyField = models.ManyToManyField(Content, blank=True)  # Content items associated with the channel

    def is_leaf_channel(self) -> bool:
        """
        Determines if the channel is a leaf (has no subchannels).
        """
        if hasattr(self, 'subchannels'):
            return not self.subchannels.exists() # type: ignore
        return True # If no subchannels exist, consider it a leaf

    def calculate_rating(self) -> Optional[float]:
        """
        Calculates the average rating of the channel.
        If the channel has no subchannels, the average is calculated based on its contents.
        If it has subchannels, the average is calculated based on their ratings.
        """
        if self.is_leaf_channel():
            # Average of ratings from the associated contents
            ratings = self.contents.aggregate(models.Avg('rating'))['rating__avg']
        else:
            # Average of ratings from the subchannels contents
            subchannel_contents = Content.objects.filter(channel__in=self.subchannels.all()) # type: ignore
            ratings = subchannel_contents.aggregate(models.Avg('rating'))['rating__avg']
        return ratings or None  # Returns None if there are no ratings

    def get_groups_from_subchannels(self):
        """
        Returns the set of all groups from subchannels if the channel is not a leaf.
        If the channel is a leaf, returns its own groups.
        """
        if self.is_leaf_channel():
            return self.groups.all()  # Return the groups directly associated with this channel
        else:
            # Collect groups from all subchannels
            group_set = set()
            for subchannel in self.subchannels.all():
                group_set.update(subchannel.get_groups_from_subchannels())
            return group_set

    def __str__(self) -> str:
        return self.title
