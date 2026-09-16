from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello_world(request):
    return HttpResponse("hello World")


class HelloEthopia(View):
    def get(self, request):
        return HttpResponse("hello Ethopia")