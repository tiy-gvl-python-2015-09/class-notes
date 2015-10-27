from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, View
from tweet.models import Tweet, Favorite


class TweetListView(ListView):
    model = Tweet


class TweetDetailView(DetailView):
    model = Tweet


class TopTweetListView(ListView):
    model = Tweet
    template_name = "tweet/tweet_list.html"

    def get_queryset(self):
        return self.model.objects.top_tweets()


class TweetCreateView(CreateView):
    model = Tweet
    fields = ["body"]
    success_url = "/"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.author = self.request.user
        return super().form_valid(form)


class UserTweetListView(ListView):
    model = Tweet

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(author__id=user_id)


class FavoriteTweetView(View):

    def post(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        Favorite.objects.create(creator=request.user, tweet=tweet)
        return HttpResponseRedirect("/")


class UnFavoriteTweetView(View):

    # when a user "unfavorites" a tweet we boot them out of the app!
    def post(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        Favorite.objects.get(creator=request.user, tweet=tweet).delete()
        return HttpResponseRedirect("http://joel.io") # partially broken app to show how to redirect externally
