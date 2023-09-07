from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("hello")
    return render(request, "index.html")


# Dynamic path
# def course(request, courseid):
# return HttpResponse(courseid)
