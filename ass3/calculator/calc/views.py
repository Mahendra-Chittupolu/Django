from django.shortcuts import render
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return render(requests,'calc/home.html')
def calc(requests):
    text = requests.GET['exp']
    x = eval(text)
    return render(requests,'calc/calc.html',{'ans':x,'text':text})
# Create your views here.
