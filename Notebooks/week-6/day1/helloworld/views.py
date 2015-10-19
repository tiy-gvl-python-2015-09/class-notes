from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    context = {"name": "Joel Taddei", "age": 32}
    return render_to_response(template_name="hello.html", context=context)

