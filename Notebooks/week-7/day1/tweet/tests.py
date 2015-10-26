from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

# Create your tests here.
from tweet.models import Tweet, Favorite


class TweetModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="asdf")
        self.user_two = User.objects.create(username="qwerty")
        self.user_three = User.objects.create(username="zxcvv")
        self.user_four = User.objects.create(username="023947qwl")
        self.user_five = User.objects.create(username="laksjda")
        self.tweet = Tweet.objects.create(author=self.user, body="Some random text")

    def test_favorites_property_returns_count_of_favorites(self):
        Favorite.objects.create(creator=self.user, tweet=self.tweet)
        Favorite.objects.create(creator=self.user_two, tweet=self.tweet)
        Favorite.objects.create(creator=self.user_three, tweet=self.tweet)
        self.assertEqual(self.tweet.favorites, 3)

    def test_favorites_users_property_returns_users_who_favorited_tweet_unordered(self):
        Favorite.objects.create(creator=self.user, tweet=self.tweet)
        Favorite.objects.create(creator=self.user_two, tweet=self.tweet)
        Favorite.objects.create(creator=self.user_three, tweet=self.tweet)
        self.assertCountEqual(self.tweet.favorites_users, [self.user_two, self.user, self.user_three])

    def test_favorites_users_property_returns_users_who_favorited_tweet_ordered(self):
        Favorite.objects.create(creator=self.user_three, tweet=self.tweet)
        Favorite.objects.create(creator=self.user, tweet=self.tweet)
        Favorite.objects.create(creator=self.user_two, tweet=self.tweet)
        self.assertEqual(self.tweet.favorites_users, [self.user_two, self.user, self.user_three])

    def test_integrity_error_raised_when_more_than_one_favorite_per_user_per_tweet(self):
        Favorite.objects.create(creator=self.user, tweet=self.tweet)
        with self.assertRaises(IntegrityError):
            Favorite.objects.create(creator=self.user, tweet=self.tweet)

    def test_top_tweet_manager_returns_top_3_tweets_by_favorite_sum(self):
        tweet = Tweet.objects.create(author=self.user_two, body="aslkdjasd")
        tweet_two = Tweet.objects.create(author=self.user_two, body="32094ukd")
        tweet_three = Tweet.objects.create(author=self.user_three, body="23094wl")
        tweet_four = Tweet.objects.create(author=self.user_three, body="xdlkjdwfkldj")

        # tweet_two has 2 favorites
        Favorite.objects.create(tweet=tweet_two, creator=self.user_two)
        Favorite.objects.create(tweet=tweet_two, creator=self.user_three)

        # tweet three has 3 favorites
        Favorite.objects.create(tweet=tweet_three, creator=self.user_two)
        Favorite.objects.create(tweet=tweet_three, creator=self.user_three)
        Favorite.objects.create(tweet=tweet_three, creator=self.user_four)

        Favorite.objects.create(tweet=tweet_four, creator=self.user_two)

        self.assertEqual(Tweet.objects.top_tweets(), [tweet_three, tweet_two, tweet_four])
