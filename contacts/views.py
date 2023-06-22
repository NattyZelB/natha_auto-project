from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
def inquiry(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            car_id = request.POST['car_id']
            car_title = request.POST['car_title']
            user_id = request.POST['user_id']
            first_name = request.POST['first_name']
            lase_name = request.POST['last_name']
            customer_need = request.POST['customer_need']
            plaatsnaam = request.POST['plaatsnaam']
            land = request.POST['land']
            email = request.POST['email']
            phone = request.POST['phone']
            GSM = request.POST['GSM']
            message =request.POST['message']

        #user_id = request.user_id
        has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
        if has_contacted:
            messages.error(request, 'U heeft al een vraag over deze auto, wacht tot we contact met u opnemen.')
            return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name, last_name=lase_name, customer_need=customer_need,
                          plaatsnaam=plaatsnaam, land=land, email=email, phone=phone,
                          GSM=GSM, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        #search Sending email django
        send_mail(
            "Aanvraag nieuwe auto",
            'U heeft een nieuwe aanvraag voor de auto ' + car_title + '. Log in op uw beheerderspaneel voor meer informatie.',
            "developer.nattananphermsin@gmail.com",
            [email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Uw aanvraag is ingediend.We nemen spoedig contact met u op.')
        return redirect('/cars/' + car_id)
    else:
        messages.error(request, 'Gelieve in te loggen voordat het bericht wordt verzonden')
        return redirect('/login/')
