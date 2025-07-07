from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

def index(request):
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
            ['Badminton500@inbox.lv'],  # сюда придёт письмо заменить на confide
            reply_to=[email]
        )

        if photo:
            mail.attach(photo.name, photo.read(), photo.content_type)

        mail.send()
        # success = True
        return redirect('success')

    return render(request, 'webapp/index.html', {'success': success})


def company(request):
    return render(request, 'webapp/about_company.html')

def success(request):
    return render(request, 'webapp/success.html')
