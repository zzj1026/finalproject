# Generated by Django 2.2 on 2021-05-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=500)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
