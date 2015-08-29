# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import oauth2_provider.generators


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0002_08_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='token',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='client_id',
            field=models.CharField(default=oauth2_provider.generators.generate_client_id, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='client_secret',
            field=models.CharField(blank=True, default=oauth2_provider.generators.generate_client_secret, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='grant',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='token',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
