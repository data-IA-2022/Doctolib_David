# Generated by Django 4.2.5 on 2023-11-15 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctolib', '0003_alter_generalformrecord_patient_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalformrecord',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 11, 15)),
        ),
        migrations.AlterField(
            model_name='stressformrecord',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 11, 15)),
        ),
    ]