# Generated by Django 3.2.11 on 2022-01-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custumer',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='custumer',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='custumer',
            name='phone',
            field=models.CharField(max_length=150, null=True),
        ),
    ]