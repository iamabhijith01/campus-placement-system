from django.shortcuts import render,HttpResponse
# Create your views here.
def landing(request):
	
	return render(request, "landing.html")
	# return HttpResponse("<h1>Hello</h1>")
def signup(request):
    return render(request, "signup.html")