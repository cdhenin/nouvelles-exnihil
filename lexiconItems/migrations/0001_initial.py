# Generated by Django 3.0.4 on 2020-03-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LexiconItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='creation date')),
            ],
        ),
    ]
