# Generated by Django 2.2 on 2021-05-09 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetails', '0002_auto_20210507_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=500)),
                ('coursename', models.CharField(max_length=500)),
            ],
        ),
    ]
