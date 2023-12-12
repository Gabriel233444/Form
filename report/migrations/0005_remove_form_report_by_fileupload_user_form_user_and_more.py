# Generated by Django 4.0.4 on 2023-12-11 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0004_alter_form_friday4_alter_form_monday4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='report_by',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='files',
            field=models.FileField(upload_to='files/'),
        ),
    ]
