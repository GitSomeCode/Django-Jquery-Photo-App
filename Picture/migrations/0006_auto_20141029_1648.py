# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Picture', '0005_auto_20141029_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploaded',
            name='upFile',
            field=models.FileField(upload_to=b'sangeeta/uploads'),
            preserve_default=True,
        ),
    ]
