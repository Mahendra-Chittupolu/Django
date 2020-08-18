from django.shortcuts import render
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1>This is First page</h1>')
def about(requests):
    return HttpResponse('<h1>About</h1><br><ul><li>Mahendra</li><li>1602-18-737-081</li></ul>')
def hobbies(requests):
    return HttpResponse('<h1>Hobbies</h1><br><ul><li>Watching movies</li><li>listening music</li></ul>')
    
# Create your views here.
