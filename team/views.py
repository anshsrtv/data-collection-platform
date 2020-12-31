import csv, io
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Team, Registered_task
from data_app.celery import app
from .tasks import import_job

def import_teams(request):
    template = "team_import.html"
    context = {
        'order': 'Order of the CSV should be name, description, manager, members',
        }

    if request.method == "POST":
        csv_file = request.FILES['file']
        # Check if it's a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')


        data_set = csv_file.read().decode('UTF-8')
        dict_list=[]
        io_string = io.StringIO(data_set)

        # Skipping header row.
        next(io_string)

        # Creating a list of dictionaries from CSV
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            my_dict={
                'name': column[0],
                'description': column[1],
                'manager': column[2],
                'members': column[3]
            }
            dict_list.append(my_dict)
        
        # Assigning task to Celery 
        import_task = import_job.delay(dict_list)
        print(import_task.task_id)
    
        context = {}

    return render(request, template, context)


def show_tasks(request):        
    template = 'import_tasks.html'
    tasks = Registered_task.objects.all()
    return render(request, template, {'tasks': tasks})


def stop_task(request, task_id):
    print(task_id)
    app.control.revoke(task_id)
    print("revoked")
    return HttpResponse("Task {} flagged as revoked!".format(task_id))

