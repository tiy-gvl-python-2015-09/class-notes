from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View, ListView
from shorty.models import UrlRecord, UrlCounter

class UrlListView(ListView):
    model = UrlRecord




class UrlRedirectView(View):

    def get(self, request, short_url):
        url = UrlRecord.objects.get(short_url=short_url)
        UrlCounter.objects.create(record=url)
        return HttpResponseRedirect(url.long_url)
