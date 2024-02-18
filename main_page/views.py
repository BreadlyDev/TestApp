import time

from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import models as m, forms as f


def main_view(request):
    news = m.News.objects.all()
    courses = m.Course.objects.values('id', 'image', 'title', 'language')
    context = {
        'news': news,
        'courses': courses
    }
    return render(request, 'index.html', context)


def course_view(request, pk):
    course = m.Course.objects.get(pk=pk)
    videos = course.videos.model.objects.all()
    tests = course.tests.model.objects.all()
    context = {
        'videos': videos,
        'tests': tests,
        'course': course
    }
    return render(request, 'pages/course.html', context)


def test_view(request, pk):
    tests = m.Test.objects.get(pk=pk)
    return render(request, 'pages/tests.html', {'tests': tests})


@login_required(login_url='sign-in')
def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    pass


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['email']

        user = authenticate(email=email, password=password)

        print(user)

        if user:
            login(request, user)
            return redirect('course/1')
    else:
        return render(request, 'pages/login.html')





