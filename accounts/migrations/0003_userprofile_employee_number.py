# Generated by Django 3.0.5 on 2020-04-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='employee_number',
            field=models.IntegerField(default=500259),
            preserve_default=False,
        ),
    ]