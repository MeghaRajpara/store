# Generated by Django 4.2.3 on 2023-07-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]
