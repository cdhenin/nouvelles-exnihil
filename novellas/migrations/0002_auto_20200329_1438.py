# Generated by Django 3.0.4 on 2020-03-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novellas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novella',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='novella',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]