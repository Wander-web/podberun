# Generated by Django 3.0.5 on 2022-04-30 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_scope'),
        ('user', '0006_auto_20220428_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subj',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='subj',
            name='prof_art',
        ),
        migrations.RemoveField(
            model_name='subj',
            name='prof_conventional',
        ),
        migrations.RemoveField(
            model_name='subj',
            name='prof_initiative',
        ),
        migrations.RemoveField(
            model_name='subj',
            name='prof_intellect',
        ),
        migrations.RemoveField(
            model_name='subj',
            name='prof_real',
        ),
        migrations.RemoveField(
            model_name='subj',
            name='prof_social',
        ),
        migrations.AddField(
            model_name='subj',
            name='main_sphere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_sphere', to='main.Scope'),
        ),
        migrations.AddField(
            model_name='subj',
            name='off_sphere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='off_sphere', to='main.Scope'),
        ),
    ]
