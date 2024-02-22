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

    def __str__(self):
        return self.title

    @property
    def rating_num(self):
        return self.ratings.all().count()

    @property
    def avg_rating(self):
        # get average of the ratings assigned to this content
        result = Content.objects.filter(id=self.id).annotate(
            average_rating=Avg('ratings__rating')).values_list('average_rating', flat=True)[0]

        # if there were at least one vote, the result is not empty
        if result:
            return result
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

        # handle only one rating per content-user combination constraint in db-level
        constraints = [
            UniqueConstraint(fields=['content', 'user'], name='unique_user_content')
        ]
