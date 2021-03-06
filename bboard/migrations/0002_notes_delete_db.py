# Generated by Django 4.0.4 on 2022-04-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Заметка')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание заметки')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Заметка создана')),
            ],
        ),
        migrations.DeleteModel(
            name='Db',
        ),
    ]
