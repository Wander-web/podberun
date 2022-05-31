# Generated by Django 3.0.5 on 2022-05-02 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20220502_1018'),
        ('user', '0009_auto_20220501_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subj',
            name='main_sphere',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main_sphere', to='main.Scope'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='off_sphere',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='off_sphere', to='main.Scope'),
        ),
    ]