# Generated by Django 4.1.7 on 2023-03-06 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_orderitem_image_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=100)),
                ('Cemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
