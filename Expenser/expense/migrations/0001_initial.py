# Generated by Django 4.0.4 on 2022-04-19 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
