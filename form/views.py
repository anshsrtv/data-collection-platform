from django.shortcuts import render
from django.http import HttpResponse
from celery import shared_task
from .models import FormResponse
from django.core.mail import EmailMessage
import csv
import datetime

def generate_csv(request):
    from_time = request.GET['from'] if 'from' in request.GET else None
    to_time = request.GET['to'] if 'to' in request.GET else None
 
    if 'email' in request.GET:
        email = request.GET['email']
    else:
        return HttpResponse("Email is required! Try adding `?email=<YOUR_EMAIL_ADDRESS>`")

    func = fetch_data.delay(from_time, to_time, email)
    
    return HttpResponse("A CSV file will be exported to your email id.`")


@shared_task
def fetch_data(from_time, to_time, email):
    
    if from_time!=None and to_time!=None:
        forms = FormResponse.objects.filter(
            timestamp__gte=from_time,
            timestamp__lte=to_time,
        )
    elif from_time!=None:
        forms = FormResponse.objects.filter(
            timestamp__gte=from_time
        )
    elif to_time!=None:
        forms = FormResponse.objects.filter(
            timestamp__lte=to_time
        )
    else:
        print("4")
        forms = FormResponse.objects.all()

    forms = forms.values_list('timestamp','user','name_of_respondent','gender_of_respondent','reading_books',
                            'listening_music','mobile_no','record_latitude','record_longitude')
    filename = "FormResponse_%s.csv" % fetch_data.request.id
    path = "/mnt/c/Users/ansh_/OneDrive/Documents/data-collection-platform/form/"

    # Creating CSV File in form/ directory.
    with open("%s%s" % (path, filename), "w+") as f:
        writer = csv.writer(f, dialect=csv.excel)
        fields = ['timestamp','user','name','gender_of_respondent','reading_books',
                'listening_music','mobile_no','record_latitude','record_longitude']
        writer.writerow(fields)
        for form in forms:
            writer.writerow(form)

    # Emailing the CSV file.
    email = EmailMessage(
        'Your data is ready!',
        'Hello! The report for your form has been generated. Please find it attached to this mail.',
        'no.reply.mail.for.work@gmail.com',
        [email,]
    )
    email.attach_file(path+filename)
    email.send()
    
    return filename


