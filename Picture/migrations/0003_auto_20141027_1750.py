# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Picture', '0002_auto_20141027_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploaded',
            name='upFile',
            field=models.FileField(upload_to=b'/minidjangoproject/sangeeta/uploads'),
            preserve_default=True,
        ),
    ]
