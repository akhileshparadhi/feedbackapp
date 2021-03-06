# Generated by Django 3.2 on 2021-04-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('lastName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='country')),
                ('feed', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
