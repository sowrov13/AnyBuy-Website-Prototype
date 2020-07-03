# Generated by Django 3.0.7 on 2020-06-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]