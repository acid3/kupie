# Generated by Django 4.0.2 on 2022-07-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privmsg', '0003_prvmsg_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='prvmsg',
            name='slug',
            field=models.SlugField(default='testslugmsg'),
            preserve_default=False,
        ),
    ]
