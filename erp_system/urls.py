from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "اسم المستخدم أو كلمة المرور غير صحيحة"})
    return render(request, "login.html")

from investors.models import InvestmentAccount, Transaction
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dashboard(request):
    account = InvestmentAccount.objects.get(user=request.user)
    transactions = Transaction.objects.filter(account=account).order_by('-date')[:10]
    return render(request, "dashboard.html", {
        "account": account,
        "transactions": transactions,
    })
from django.urls import path
from investors.views import dashboard



def logout_view(request):
    logout(request)
    return redirect("login")
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "register.html", {"error": "كلمتا المرور غير متطابقتين"})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "اسم المستخدم موجود بالفعل"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect("login")
    return render(request, "register.html")


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),

]
