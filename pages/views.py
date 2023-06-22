from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import send_mail
from django.contrib import messages
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    brand_search = Car.objects.values_list('car_title', flat=True).distinct()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    plaatsnaam_search = Car.objects.values_list('plaatsnaam', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'brand_search': brand_search,
        'model_search': model_search,
        'plaatsnaam_search': plaatsnaam_search,
        'year_search': year_search,
        'body_style_search': body_style_search,

    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,

    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'U heeft een nieuw bericht van de Carzone-website over.' + subject
        message_body = 'Naam: ' + name + '. E-mail:' + email +'. Telefoon nummer:' + phone + '. Bericht:' + message
        send_mail(
            email_subject,
            message_body,
            "developer.nattananphermsin@gmail.com",
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Bedankt dat u contact met ons opneemt. We komen spoedig bij u terug.')
        return redirect('contact')
    return render(request, 'pages/contact.html')
