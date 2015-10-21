from django.shortcuts import render, render_to_response
import datetime
from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView, View
from helloworld.models import Person


def index_view(request):
    if request.POST:
        return HttpResponse("Hey cool post bro")

    eye_color = request.GET.get('eye_color')
    if eye_color:
        people = Person.objects.filter(eye_color=eye_color)
    else:
        people = Person.objects.all()

    context = {
        "name": "Joel Taddei",
        "age": 32,
        "panels": people
    }
    return render_to_response(template_name="hello.html", context=context)


def football_view(request):
    context = {
        "teams": [
            {"title": "Chicago Bears", "body": "Da Bears"},
            {"title": "Seattle Seahawks", "body": "Da seahawks"},
            {"title": "San Francisco", "body": "Da niners"},
        ]
    }
    return render_to_response(template_name="football.html", context=context)


class FootballView(TemplateView):
    template_name = "football.html"

    def get_context_data(self, **kwargs):
        context = {
            "teams": [
                {"title": "Chicago Bears", "body": "Da Bears"},
                {"title": "Seattle Seahawks", "body": "Da seahawks"},
                {"title": "San Francisco", "body": "Da niners"},
            ]
        }
        return context


def dow_view(request, dow):
    english_day_of_week = datetime.datetime.strptime(dow, "%Y-%m-%d").strftime("%A")
    context = {
        "dow": english_day_of_week,
    }
    return render_to_response(template_name="hello.html", context=context)

def name_view(request):
    context = {}
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")
    prefix = request.GET.get("prefix")
    if request.GET:
        context["name"] = "{} {} {}".format(prefix, first_name, last_name)
    return render_to_response(template_name="name.html", context=context)


class StupidView(View):

    def get(self, request):
        return HttpResponse("This is stupid!")

    def post(self, request):
        return HttpResponse("This is a stupid post request!")
