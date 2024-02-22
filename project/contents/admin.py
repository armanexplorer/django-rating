from django.contrib import admin
from .models import Content, Rating


# custom admin model
class ContentModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


class RatingModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'rating')


# register the models to see in django admin panel
admin.site.register(Content, ContentModelAdmin)
admin.site.register(Rating, RatingModelAdmin)
