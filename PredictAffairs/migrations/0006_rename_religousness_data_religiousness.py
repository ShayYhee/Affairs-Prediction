# Generated by Django 4.2.1 on 2023-05-14 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PredictAffairs', '0005_remove_data_occupation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='religousness',
            new_name='religiousness',
        ),
    ]
