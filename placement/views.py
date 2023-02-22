from django.shortcuts import render,HttpResponse
# Create your views here.
def landing(request):
	return render(request, "landing.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")