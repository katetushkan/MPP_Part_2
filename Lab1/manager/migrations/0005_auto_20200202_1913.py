# Generated by Django 3.0.2 on 2020-02-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20200202_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(null=True, upload_to='attachments/'),
        ),
    ]
