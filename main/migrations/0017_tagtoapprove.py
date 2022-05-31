# Generated by Django 3.0.5 on 2022-05-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20220506_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagToApprove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_app_name', models.CharField(blank=True, max_length=50, verbose_name='Tag name')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]