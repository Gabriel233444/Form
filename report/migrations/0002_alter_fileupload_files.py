# Generated by Django 4.2.3 on 2023-11-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='files',
            field=models.FileField(default='file.pdf', upload_to='files/'),
        ),
    ]
