# Generated by Django 3.2 on 2021-05-06 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
    ]
