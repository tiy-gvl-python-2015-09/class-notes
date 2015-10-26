from django.contrib.auth.models import User
from django.db import models


class TweetManager(models.Manager):

    def filter_for_user(self, user):
        return self.filter(author=user)

    def top_tweets(self):
        return sorted(self.all(), key=lambda x: x.favorites, reverse=True)[:3]


class Tweet(models.Model):
    author = models.ForeignKey(User)
    body = models.CharField(max_length=140)

    objects = TweetManager()

    @property
    def favorites(self):
        return self.favorite_set.all().count()

    @property
    def favorites_users(self):
        return [favorite.creator for favorite in self.favorite_set.all()]

    def __str__(self):
        return self.body

    class Meta:
        ordering = ["-id"]


class Favorite(models.Model):
    tweet = models.ForeignKey(Tweet)
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        unique_together = ("tweet", "creator")