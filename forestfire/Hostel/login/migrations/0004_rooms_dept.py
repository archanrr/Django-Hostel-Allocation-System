# Generated by Django 2.1.1 on 2018-10-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181006_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='dept',
            field=models.CharField(default='IT', max_length=4),
        ),
    ]