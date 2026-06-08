from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import (
    ProfileForm,
    ProfessionalApplicationForm
)

from .models import (
    Profile,
    ProfessionalApplication,
    Contractor
)
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





@csrf_exempt
def find_pros(request):
    service = request.GET.get('service')
    zip_code = request.GET.get('zip')

    # Твоя логика поиска (Postgres query)
    pros = [
        {'name': 'John Painter', 'service': 'House Painting', 'zip': zip_code, 'rating': 4.8, 'reviews': 124},
        {'name': 'Sarah Plumber', 'service': service, 'zip': zip_code, 'rating': 4.9, 'reviews': 89},
    ]

    return JsonResponse({'pros': pros})


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

@login_required
def account(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    application = ProfessionalApplication.objects.filter(
        user=request.user
    ).first()

    contractor = Contractor.objects.filter(
        user=request.user
    ).first()

    # Если заявка уже одобрена и есть подрядчик,
    # статус заявки больше не показываем
    if (
        application
        and application.status == 'approved'
        and contractor
        and contractor.approved
    ):
        application = None

    context = {
        'profile': profile,
        'application': application,
        'contractor': contractor,
    }

    return render(
        request,
        'webapp/account/account.html',
        context
    )

@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Profile updated.'
            )

            return redirect('account')

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'webapp/account/edit_profile.html',
        {
            'form': form
        }
    )

@login_required
def become_professional(request):

    if ProfessionalApplication.objects.filter(
            user=request.user
    ).exists():

        messages.info(
            request,
            'Application already submitted.'
        )

        return redirect('account')

    if request.method == 'POST':

        form = ProfessionalApplicationForm(
            request.POST
        )

        if form.is_valid():

            application = form.save(
                commit=False
            )

            application.user = request.user

            application.save()

            messages.success(
                request,
                'Application submitted.'
            )

            return redirect('account')

    else:

        form = ProfessionalApplicationForm()

    return render(
        request,
        'webapp/account/become_professional.html',
        {
            'form': form
        }
    )


def company(request):
    return render(request, 'webapp/about_company.html')

def success(request):
    return render(request, 'webapp/success.html')


def favorites_view(request):
    return render(request, "webapp/favorite.html")

def robots_txt(request):
    content = """User-agent: *
Disallow:

Sitemap: https://phoenixpegasus81.pythonanywhere.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")
