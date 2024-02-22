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
            return rating.rating  # Replace with the actual field name


class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('content', 'rating')

    def create(self, validated_data):
        content = validated_data['content']
        user = validated_data['user']

        # check if there is this combination of user and content already, so we should only update
        try:
            rating_obj = Rating.objects.get(content=content, user=user)
            rating_obj.rating = validated_data['rating']
            rating_obj.save()
            return rating_obj
        except Rating.DoesNotExist:
            return Rating.objects.create(**validated_data)
