# Generated by Django 3.1.2 on 2020-10-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='framework',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
