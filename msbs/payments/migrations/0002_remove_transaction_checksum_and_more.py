# Generated by Django 4.2 on 2023-07-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='checksum',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='made_by',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='made_on',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='checksum_after',
            field=models.CharField(blank=True, default='NA', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='checksum_before',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='item',
            field=models.CharField(blank=True, default='MSBS', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.CharField(default='NA', max_length=36),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionID',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='userID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
