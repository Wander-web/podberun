# Generated by Django 3.0.5 on 2022-04-27 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220426_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='prof_conv',
            new_name='prof_conventional',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='prof_entre',
            new_name='prof_initiative',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='prof_intell',
            new_name='prof_intellect',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='prof_soc',
            new_name='prof_social',
        ),
    ]