# Generated by Django 4.1 on 2022-10-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_factsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='teacher_level',
            field=models.CharField(choices=[('Senior', 'Senior'), ('Middle', 'Middle'), ('Junior', 'Junior')], max_length=255),
        ),
    ]