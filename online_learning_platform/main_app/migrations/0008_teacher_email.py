# Generated by Django 5.0.4 on 2024-05-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_assignment_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]