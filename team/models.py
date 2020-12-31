from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=600)
    description = models.TextField()
    manager = models.CharField(max_length=20)
    members = models.TextField()

    def __str__(self):
        return self.name

class Registered_task(models.Model):
    task_id = models.UUIDField()
    start_time = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=500, null=True, blank=True)
    models_before = models.IntegerField()

    def __str__(self):
        return self.task_id

    