from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["username"],
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {"errors":"비밀번호가 일치하지 않습니다."})
    return render(request, 'signup.html')
