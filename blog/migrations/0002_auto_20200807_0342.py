# Generated by Django 3.1 on 2020-08-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='summary',
            new_name='body',
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
