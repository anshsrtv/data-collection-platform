# Generated by Django 3.1.4 on 2020-12-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('user', models.CharField(max_length=500)),
                ('name_of_respondent', models.CharField(max_length=500)),
                ('gender_of_respondent', models.CharField(choices=[['Male', 'Male'], ['Female', 'Female'], ['Other', 'Other']], max_length=7)),
                ('reading_books', models.BooleanField()),
                ('listening_music', models.BooleanField()),
                ('mobile_no', models.CharField(max_length=15)),
                ('record_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('record_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
