# Generated by Django 4.1.1 on 2022-09-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rollno', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('field_of_study', models.EmailField(max_length=100)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
