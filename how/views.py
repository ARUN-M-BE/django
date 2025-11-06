from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import How

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))
def faq(request):
    template = loader.get_template('faq.html')
    context = {}
    return HttpResponse(template.render(context, request))
def how(request):
  User = How.objects.all().values()
  template = loader.get_template('how.html')
  context = {
    'User': User,
  }
  return HttpResponse(template.render(context, request))
def details(request, id):
  User = How.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'User': User,
  }
  return HttpResponse(template.render(context, request))