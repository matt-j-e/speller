# Generated by Django 3.1.2 on 2020-10-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(default=False, null=True),
        ),
    ]