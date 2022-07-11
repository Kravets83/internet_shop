# Generated by Django 4.0.6 on 2022-07-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='creator',
            field=models.CharField(default='', max_length=225),
        ),
    ]