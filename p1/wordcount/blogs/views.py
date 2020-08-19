from django.shortcuts import render
from django.http import HttpResponse
import operator
def drinks(requests):
    return HttpResponse('<h2>drink water</h2>')
def foods(requests):
    return HttpResponse('<h2>Donot Eat Junk Food</h2>')
# Create your views here.
