# Generated by Django 3.2.9 on 2021-11-23 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ['-execution_date']},
        ),
    ]