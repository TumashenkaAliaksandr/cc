from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from webapp.models import MoreServices, SliderService


def index(request):
    slider_services = SliderService.objects.all()
    more_services = MoreServices.objects.filter(
        is_active=True
    ).order_by('sort_order')
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        photo = request.FILES.get('photo')

        email_subject = 'New Plaster Drywall Repair Request'
        email_body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        mail = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ['Badminton500@inbox.lv', 'sreda@gmail.com'],  # сюда придёт письмо заменить на confide
            reply_to=[email]
        )

        if photo:
            mail.attach(photo.name, photo.read(), photo.content_type)

        mail.send()
        # success = True
        return redirect('success')

    return render(request, 'webapp/index.html', {'success': success, 'slider_services': slider_services, 'more_services': more_services})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, "webapp/auntifications/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("index")
    else:
        form = AuthenticationForm()

    return render(request, "webapp/auntifications/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")

def company(request):
    return render(request, 'webapp/about_company.html')

def success(request):
    return render(request, 'webapp/success.html')


def cart_view(request):
    return render(request, "webapp/cart.html")

def robots_txt(request):
    content = """User-agent: *
Disallow:

Sitemap: https://phoenixpegasus81.pythonanywhere.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")
