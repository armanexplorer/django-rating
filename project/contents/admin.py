from django.contrib import admin
from .models import Content  # Import your model here


# Create an admin class for your model
class ContentModelAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin list view
    # list_display = ('field1', 'field2', 'field3')  # Replace with your actual field names
    pass


# Register your model with the admin site
admin.site.register(Content, ContentModelAdmin)
