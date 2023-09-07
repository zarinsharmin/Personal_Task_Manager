from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("hello")
    data = {"title": "Personal Task Manager"}
    return render(request, "index.html", data)


# Dynamic path
# def course(request, courseid):
# return HttpResponse(courseid)
