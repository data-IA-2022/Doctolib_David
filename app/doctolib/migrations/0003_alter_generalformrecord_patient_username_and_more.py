# Generated by Django 4.2.5 on 2023-11-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctolib', '0002_generalformrecord_quantite_eau_litre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalformrecord',
            name='patient_username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='generalformrecord',
            name='poids_kg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalformrecord',
            name='taille_cm',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stressformrecord',
            name='patient_username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]