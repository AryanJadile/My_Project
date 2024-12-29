# Generated by Django 2.2.28 on 2024-12-27 12:01

import applications.chapter.models
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events_news', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('wall_picture', models.ImageField(blank=True, null=True, upload_to=applications.chapter.models.upload_photo)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(choices=[('President', 'President'), ('Hon. Secretary', 'Hon. Secretary'), ('Treasurer', 'Treasurer'), ('Other', 'Other')], max_length=50)),
                ('other_post', models.CharField(blank=True, max_length=100, null=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chapter.Chapters')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapter.Chapters')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_news.Event')),
            ],
            options={
                'unique_together': {('chapter', 'event')},
            },
        ),
        migrations.CreateModel(
            name='ChapterAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapter.Chapters')),
            ],
            options={
                'unique_together': {('chapter', 'album')},
            },
        ),
    ]
