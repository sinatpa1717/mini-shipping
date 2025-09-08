from django.shortcuts import render, redirect
from .models import My_mode
from .forms import My_form1, Img_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import poshtibani_mdoel

# Create your views here.


@login_required
def home_page_web(request):
    iteam = My_mode.objects.all()
    return render(request, "page1/home.html", {"iteam": iteam})


def login_page_web(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "ورود به حساب کاربری موفق بود")
            return redirect("home_page_web")
        else:
            messages.error(request, "ورود به حساب کاربری موفق نبود دوباره تلاش کنید")
            return render(request, "page1/login.html")
    else:
        return render(request, "page1/login.html")


def signup_page_web(request):
    if request.method == "POST":
        form = My_form1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ساخت اکانت موفق بود")
            return redirect("login_page_web")
        else:
            messages.error(request, "ساخت اکانت موفق نبود")
            return render(request, "page1/signup.html", {"form": form})
    else:
        form = My_form1()
        return render(request, "page1/signup.html", {"form": form})


@login_required
def logout_page_web(request):
    logout(request)
    messages.success(request, "خروج از حساب کاربری موفق بود")
    return redirect("login_page_web")


@login_required
def upload_iteam_page(request):
    if request.method == "POST":
        form = Img_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "محصول با موفقیت آپلود شد")
            return redirect("home_page_web")
        else:
            messages.error(request, "محصول آپلود نشد. لطفاً دوباره تلاش کنید.")
    else:
        form = Img_form()
        return render(request, "page1/upload.html", {"form": form})


def poshtibani_page_web(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        info = request.POST.get("info", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone_number", "").strip()

        if name and info and email and phone:
            poshtibani_mdoel.objects.create(
                name=name, info=info, email=email, phone_number=phone
            )
            messages.success(request, "پیام شما با موفقیت ارسال شد")
            return redirect("home_page_web")
        else:
            messages.error(request, "پیام شما ارسال نشد، لطفاً همه فیلدها را پر کنید")

    return render(request, "page1/poshtibani.html")
