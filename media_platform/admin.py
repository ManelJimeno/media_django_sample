from django.contrib import admin
from .models import Content, Channel, Group

# Register the Content model
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')  # Columns to display in the admin list view
    search_fields = ('title',)  # Add a search bar for title
    list_filter = ('rating',)  # Add filters for rating

# Register the Group model
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the Channel model
class ContentInline(admin.TabularInline):
    model = Channel.contents.through  # Many-to-Many relationship
    extra = 1  # Number of empty rows to display for new content

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'parent_channel')  # Display these fields in admin
    search_fields = ('title', 'language')  # Add a search bar for title and language
    list_filter = ('language',)  # Add filters for language
    raw_id_fields = ('parent_channel',)  # Use a raw ID field for parent_channel
    inlines = [ContentInline]  # Add inline management for related contents
