# Generated by Django 4.2.3 on 2023-11-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_alter_fileupload_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='friday2',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='monday2',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='supervisor',
            field=models.CharField(default='The Chairman', max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='thursday2',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='tuesday2',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='wednessday2',
            field=models.TimeField(),
        ),
    ]
