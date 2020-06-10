# Generated by Django 3.0.5 on 2020-04-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ['name'],
            },
        ),
    ]
