# Generated by Django 3.0.4 on 2020-03-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
