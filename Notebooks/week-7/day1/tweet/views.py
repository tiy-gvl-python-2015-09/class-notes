from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from tweet.models import Tweet


class TweetListView(ListView):
    model = Tweet


class TweetDetailView(DetailView):
    model = Tweet


class TopTweetListView(ListView):
    model = Tweet
    template_name = "tweet/tweet_list.html"

    def get_queryset(self):
        return Tweet.objects.top_tweets()


class TweetCreateView(CreateView):
    model = Tweet
    fields = ["author", "body"]
    success_url = "/"
