# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuploaded',
            name='ct',
            field=models.CharField(default='image/jpg', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fileuploaded',
            name='title',
            field=models.CharField(default='picture', max_length=50),
            preserve_default=False,
        ),
    ]
