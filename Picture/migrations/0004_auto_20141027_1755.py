# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Picture', '0003_auto_20141027_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploaded',
            name='upFile',
            field=models.FileField(upload_to=b'sangeeta/uploads'),
            preserve_default=True,
        ),
    ]
