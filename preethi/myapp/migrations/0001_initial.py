# Generated by Django 4.2.5 on 2023-10-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footballplayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Height', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('MobileNo', models.IntegerField()),
            ],
        ),
    ]
