# Generated by Django 2.2.12 on 2020-07-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
