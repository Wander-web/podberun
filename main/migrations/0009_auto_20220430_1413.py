# Generated by Django 3.0.5 on 2022-04-30 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220430_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tag_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_1', to='main.Tag'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tag_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_2', to='main.Tag'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tag_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_3', to='main.Tag'),
        ),
    ]
