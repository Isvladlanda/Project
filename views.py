from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from app.models import Users
from django.template.loader import render_to_string


@csrf_exempt
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = Users()
        user.name = name
        user.email = email
        user.password = password
        saved = user.save()
        return render(request, 'about.html')
    return render(request, 'index.html')


@csrf_exempt
def about(request):
    return render(request, 'about.html')
