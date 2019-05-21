# Generated by Django 2.2.1 on 2019-05-21 14:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_survey.Group')),
            ],
        ),
        migrations.CreateModel(
            name='HappinessLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField(choices=[(1, 'Unhappy'), (2, 'Not Happy'), (3, 'Neutral'), (4, 'Happy'), (5, 'Very Happy')])),
                ('date', models.DateField(default=datetime.date(2019, 5, 21))),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_survey.UserProfile')),
            ],
        ),
    ]
