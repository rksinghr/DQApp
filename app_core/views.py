from django.shortcuts import render

def view_home(request):
    msg = "Welcome to DQ Home Page"
    return render(request, 'app_core/home.html', {'msg': msg})