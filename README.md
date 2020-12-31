# Data Collection Platform

 A data collection platform that allows a series of long-running import/export tasks with an API endpoint to stop/terminate the task.

### API Endpoints
1. API to import teams into the database. The HTML page, that loads, asks for uploading a CSV file in specified format. Once uploaded properly, Celery is assigned the task. The task_id for which gets printed in the console.

        http://localhost:8000/import_teams/
2. To stop the task, the following API may be used. The TASK_ID here, is the ID assigned to the task.

        http://localhost:8000/stop_task/<TASK_ID>
3. To export data in CSV format for Form Responses, use the following API:

        http://localhost:8000/export_data/?email=<YOUR_EMAIL_ID>&from=2017-05-15%2000:00&to=2020-05-15%2000:00
4. To stop the export task, the procedure to stop task may be repeated:
        
        http://localhost:8000/stop_task/<TASK_ID>
    
### External Dependencies
*  MYSQL
*  RabbitMQ


### Installation

1. Install the dependencies [MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database) & [RabbitMQ](https://www.rabbitmq.com/install-debian.html)

2. Start both the services by the commands below:

        sudo service mysql start
        sudo service rabbitmq-server start       
 
3. First clone the repo using:

    `git clone https://github.com/anshsrtv/data-collection-platform`
  
2. Change the CWD to the project folder

    `cd data-collection-platform`
    

3. Make virtual Environment (Python version recommeded = v3.6)

    `virtualenv --python=/usr/bin/python3 myenv`

4. Activate the Virtual Environment

    `source myenv/bin/activate`

5. Install requirements.txt

    `pip install -r requirements.txt`
    
6. Setup Postgres Database with given credentials

    >DATABASE NAME : collect_db
    
    >USERNAME : admin
    
    >PASSWORD : admin@123

7. Make all the Migrations

    `python manage.py makemigrations`

8. Run Migration command
    
    `python manage.py migrate`

9. Make a superuser for admin panel

    `python manage.py createsuperuser`
    
10. Run the server
  
    `python manage.py runserver`

### Milestones to be Achieved

1. Concurrent tasks in celery
2. Package it in a docker image.

### Room for improvement
1. The import tasks in teams can be assigned in batches of 10-50 to allow easier rollbacks and data consistency.
2. To rollback the records post stop action of import task, an extra field in Team Model may be included to store the task id. When the task is stopped, the records corresponding to the task id shall be deleted.



