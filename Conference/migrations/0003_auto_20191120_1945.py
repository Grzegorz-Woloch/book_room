# Generated by Django 2.2.6 on 2019-11-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conference', '0002_auto_20191120_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]