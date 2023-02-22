from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import landing,signup,signin

urlpatterns = [
	path('', landing, name="landingpage" ),
	path('signup/', signup, name="signuppage" ),
    path('signin/', signin, name="signinpage"),
]
