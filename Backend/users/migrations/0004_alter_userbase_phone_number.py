# Generated by Django 3.2.3 on 2021-11-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userbase_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
