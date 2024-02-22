from django.db import models
from django.db.models import UniqueConstraint
from django.db.models import Avg


# Create your models here.
class Content(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, null=False)
    text = models.TextField(null=False)

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    @property
    def rating_num(self):
        return self.ratings.all().count()

    @property
    def avg_rating(self):
        # get average of the ratings assigned to this content
        result = self.ratings.annotate(average_rating=Avg('rating')).values_list('average_rating', flat=True)

        # if there were at least one vote, the result is not empty
        if result:
            return result[0]
        else:
            return 0.0


class Rating(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField()
    content = models.ForeignKey('contents.Content', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='ratings', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

        # handle one rating per content-user combination constraint in db-level
        constraints = [
            UniqueConstraint(fields=['content', 'user'], name='unique_user_content')
        ]
