# Generated by Django 2.1.5 on 2021-07-27 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210727_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL),
        ),
    ]
