from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings

from webapp.models import Service


def index(request):
    service = Service.objects.first()
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

    return render(request, 'webapp/index.html', {'success': success, 'service': service})


def company(request):
    return render(request, 'webapp/about_company.html')

def success(request):
    return render(request, 'webapp/success.html')


def robots_txt(request):
    content = """User-agent: *
Disallow:

Sitemap: https://phoenixpegasus81.pythonanywhere.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")
