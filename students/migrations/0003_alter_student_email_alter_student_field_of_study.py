# Generated by Django 4.1.1 on 2022-09-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_student_rollno_student_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='field_of_study',
            field=models.CharField(max_length=100),
        ),
    ]
