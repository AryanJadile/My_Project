# Generated by Django 2.2.28 on 2024-12-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_template', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=250)),
                ('batch', models.CharField(max_length=250)),
                ('branch', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('total_recipients', models.IntegerField()),
                ('total_delivered', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=500)),
                ('body', models.TextField()),
            ],
        ),
    ]