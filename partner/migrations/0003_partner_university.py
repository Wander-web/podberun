# Generated by Django 3.0.5 on 2022-05-16 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_tagtoapprove'),
        ('partner', '0002_auto_20220426_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vuz', to='main.University'),
        ),
    ]
