# Generated by Django 4.2.2 on 2023-07-17 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 16, 18, 55, 46, 632569), verbose_name='дата истечения'),
        ),
    ]
