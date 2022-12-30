from django.http import HttpResponse
from django.shortcuts import render

from main.tasks import task_check

# Create your views here.

def main_worker(request):
    task_check.delay("vikas")
    return HttpResponse("Tested")