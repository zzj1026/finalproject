# Generated by Django 2.2 on 2021-05-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetails', '0003_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='studentid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
