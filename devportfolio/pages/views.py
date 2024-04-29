from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def work(request):
    return render(request, 'pages/work.html')

def contact(request):
    return render(request, 'pages/contact.html')

def act2(request):
    return render(request, 'work/act2.png')

def act3(request):
    return render(request, 'work/act3.png')