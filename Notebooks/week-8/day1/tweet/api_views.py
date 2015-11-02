from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from tweet.models import Tweet


@csrf_exempt
def api_tweet_list_create(request):
    # IF POST TO LIST VIEW, CREATE A RECORD
    if request.POST:
        author = User.objects.get(username=request.POST.get("author"))
        body = request.POST.get("body")
        Tweet.objects.create(author=author, body=body)
        return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
    # ELSE JUST GIVE ME ALL TWEETS
    all_tweets = Tweet.objects.all()
    data = [{"id": tweet.id, "body": tweet.body, "author": tweet.author.username} for tweet in all_tweets]
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")


def api_tweet_detail(request, pk):
    tweet = Tweet.objects.get(id=pk)
    serialized_tweet = json.dumps({"id": tweet.id, "body": tweet.body, "author": tweet.author.username})
    return HttpResponse(serialized_tweet, content_type="application/json")