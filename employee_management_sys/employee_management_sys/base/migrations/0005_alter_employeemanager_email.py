# Generated by Django 4.1.3 on 2022-12-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_employeemanager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemanager',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]