from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))
def faq(request):
    template = loader.get_template('faq.html')
    context = {}
    return HttpResponse(template.render(context, request))

def member(request):
  user = Member.objects.all().values()
  template = loader.get_template('member.html')
  context = {
    'user': user,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  user = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'user': user,
  }
  return HttpResponse(template.render(context, request))