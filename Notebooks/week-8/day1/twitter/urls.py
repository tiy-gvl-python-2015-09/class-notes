"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from tweet.views import TopTweetListView, TweetListView, TweetDetailView, TweetCreateView, UserTweetListView, \
    FavoriteTweetView, UnFavoriteTweetView
from tweet.api_views import api_tweet_list_create, api_tweet_detail

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', TweetListView.as_view(), name="tweet_list"),
    url(r'^top/$', TopTweetListView.as_view(), name="top_tweet_list"),
    url(r'^create/$', login_required(TweetCreateView.as_view()), name="tweet_create"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="tweet_detail"),
    url(r'^user/(?P<pk>\d+)/$', UserTweetListView.as_view(), name="user_tweet_list"),
    url(r'^favorite/(?P<tweet_id>\d+)/$', FavoriteTweetView.as_view(), name="favorite_tweet"),
    url(r'^unfavorite/(?P<tweet_id>\d+)/$', UnFavoriteTweetView.as_view(), name="unfavorite_tweet"),
    url(r'^api/tweets/$', api_tweet_list_create, name="api_tweet_list_create"),
    url(r'^api/tweets/(?P<pk>\d+)/$', api_tweet_detail, name="api_tweet_detail"),
    url(r'^admin/', include(admin.site.urls)),
]
