# Generated by Django 3.2.23 on 2023-11-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=250)),
                ('PhoneNumber', models.IntegerField()),
                ('MailId', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
            ],
        ),
    ]