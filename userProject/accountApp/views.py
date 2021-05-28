from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def main(request):
    return render(request, "main.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): #유효성 검사
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password=password)
            if user is not None :
                login(request, user)
            return redirect("main")
    else :
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form}) #Get방식

def logout_view(requset):
    logout(requset)
    return redirect("main")

def signup_view(request):
    if request.method == "POST": #요청방식이 POST
        form = UserCreationForm(request.POST)
        if form.is_valid(): #form 유효성 검사
            user = form.save()
            login(request, user)
        return redirect("main")
    else: #요청방식이 GET
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})