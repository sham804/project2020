# Generated by Django 5.1.1 on 2024-09-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('marketing_module', models.JSONField(default=list)),
            ],
        ),
    ]
