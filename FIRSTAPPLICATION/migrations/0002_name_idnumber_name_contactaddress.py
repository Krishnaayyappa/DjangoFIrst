# Generated by Django 4.1.5 on 2023-01-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='Idnumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='contactaddress',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
