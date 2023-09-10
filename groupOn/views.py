import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Group, GroupMembers, Messages, Subject, User


# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("username: ", username)
        print("password: ", password)

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        print("user: ", user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")

    return render(request, 'groupOn/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request: HttpRequest) -> HttpResponse:
    allSubjects = Subject.objects.all()
    userId = request.GET.get('id')
    userCreatedGroups = Group.objects.filter(creator_id=userId)
    context = {'subjects': allSubjects, 'groups': userCreatedGroups}
    return render(request, 'groupOn/home.html', context)


def profile(request: HttpRequest) -> HttpResponse:
    userId = request.GET.get('userId')
    userDetails = User.objects.filter(id=userId)

    context = {'userDetails': userDetails}
    return render(request, 'groupOn/home.html', context)


def create_group(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        dict_data = json.loads(request.body)
        subjectName = dict_data['subjectName']
        groupName = dict_data['groupName']
        userId = dict_data['userId']

        Subject.objects.create(subjectName=subjectName)
        Group.objects.create(creator_id=userId, subject_id=subjectName)

        return redirect('home')

    return render(request, 'groupOn/home.html')

#  q: write a function to add two numbers?
#  a: def add(a, b):
#         return a + b

# test this whole file to find any bugs in the codebase
#  python manage.py test
#  python manage.py test groupOn.tests.test_views
#  python manage.py test groupOn.tests.test_views.test_home
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest.test_home_view
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest.test_home_view_with_no_groups
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest.test_home_view_with_groups
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest.test_home_view_with_groups_and_subjects
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest.test_home_view_with_groups_and_subjects_and_users
#  python manage.py test groupOn.tests.test_views.test_home.HomeViewTest.test_home_view_with_groups_and_subjects_and_users_and_messages

