from rest_framework import serializers

from .models import Content, Rating


class ContentListSerializer(serializers.ModelSerializer):
    user_rating = serializers.SerializerMethodField('get_user_rating')

    class Meta:
        model = Content
        fields = ('id', 'title', 'text', 'rating_num', 'avg_rating', 'user_rating')

    def get_user_rating(self, obj):
        # Access the user id from the context of the request
        user = self.context['request'].user

        try:
            rating = user.ratings.get(content=obj.id)
        except Rating.DoesNotExist:
            return None
        else:
            return rating  # Replace with the actual field name
