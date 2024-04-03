# Generated by Django 5.0.3 on 2024-04-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('protocol', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('uptime', models.CharField(max_length=100)),
            ],
        ),
    ]
