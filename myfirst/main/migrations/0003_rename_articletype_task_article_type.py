# Generated by Django 3.2.16 on 2022-12-17 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_articletype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='ArticleType',
            new_name='article_type',
        ),
    ]
