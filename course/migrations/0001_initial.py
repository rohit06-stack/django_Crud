# Generated by Django 4.2.7 on 2023-12-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=50, unique=True)),
                ('courseFee', models.IntegerField()),
                ('courseDuration', models.CharField(max_length=50)),
            ],
        ),
    ]
