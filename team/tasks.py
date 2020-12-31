from .models import Team
from celery import shared_task

@shared_task
def import_job(my_list):
    
    for my_dict in my_list:
        Team.objects.create(
            name=my_dict['name'],
            description=my_dict['description'],
            manager=my_dict['manager'],
            members=my_dict['members']
        )