# Generated by Django 3.2.9 on 2021-11-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
