# Generated by Django 3.0.5 on 2022-05-01 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20220501_1938'),
        ('user', '0008_auto_20220501_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subj',
            name='main_sphere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_sphere', to='main.Scope'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='off_sphere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='off_sphere', to='main.Scope'),
        ),
    ]