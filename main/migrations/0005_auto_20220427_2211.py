# Generated by Django 3.0.5 on 2022-04-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220427_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_art',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_conventional',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_initiative',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_intellect',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_real',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_social',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
