# Generated by Django 3.0.5 on 2022-04-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_scope_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Tag name'),
        ),
    ]