# Generated by Django 4.2.1 on 2023-06-15 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eid_light', '0009_alter_light_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='light',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eid_light.light'),
        ),
    ]