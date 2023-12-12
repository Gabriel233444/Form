# Generated by Django 4.2.3 on 2023-11-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='Files')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_by', models.CharField(max_length=20)),
                ('supervisor', models.CharField(max_length=20)),
                ('monday', models.CharField(max_length=100)),
                ('tuesday', models.CharField(max_length=100)),
                ('wednessday', models.CharField(max_length=100)),
                ('thursday', models.CharField(max_length=100)),
                ('friday', models.CharField(max_length=100)),
                ('monday1', models.CharField(max_length=100)),
                ('tuesday1', models.CharField(max_length=100)),
                ('wednessday1', models.CharField(max_length=100)),
                ('thursday1', models.CharField(max_length=100)),
                ('friday1', models.CharField(max_length=100)),
                ('projects', models.IntegerField()),
                ('study_materials', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('challenges', models.CharField(max_length=100)),
                ('monday2', models.DateTimeField()),
                ('tuesday2', models.DateTimeField()),
                ('wednessday2', models.DateTimeField()),
                ('thursday2', models.DateTimeField()),
                ('friday2', models.DateTimeField()),
                ('whatsapp', models.IntegerField()),
                ('facebook', models.IntegerField()),
                ('twitter', models.IntegerField()),
                ('instagram', models.IntegerField()),
                ('monday3', models.CharField(max_length=100)),
                ('tuesday3', models.CharField(max_length=100)),
                ('wednessday3', models.CharField(max_length=100)),
                ('thursday3', models.CharField(max_length=100)),
                ('friday3', models.CharField(max_length=100)),
                ('sugestions', models.CharField(max_length=100)),
                ('total_weeks', models.CharField(max_length=20)),
                ('monday4', models.CharField(max_length=100)),
                ('tuesday4', models.CharField(max_length=100)),
                ('wednessday4', models.CharField(max_length=100)),
                ('thursday4', models.CharField(max_length=100)),
                ('friday4', models.CharField(max_length=100)),
            ],
        ),
    ]
