# Generated by Django 3.2 on 2021-05-04 08:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pyboard', '0006_auto_20210504_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]