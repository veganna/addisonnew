# Generated by Django 3.2.3 on 2021-05-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='file',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.FileField(default=1, upload_to='', verbose_name='Images'),
            preserve_default=False,
        ),
    ]
