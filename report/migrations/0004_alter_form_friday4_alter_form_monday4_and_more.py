# Generated by Django 4.2.3 on 2023-11-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_form_friday2_alter_form_monday2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='friday4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='monday4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='thursday4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='tuesday4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='wednessday4',
            field=models.IntegerField(),
        ),
    ]