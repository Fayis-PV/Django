# Generated by Django 4.0.4 on 2022-06-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0013_alter_contact_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_time',
            field=models.TimeField(),
        ),
    ]