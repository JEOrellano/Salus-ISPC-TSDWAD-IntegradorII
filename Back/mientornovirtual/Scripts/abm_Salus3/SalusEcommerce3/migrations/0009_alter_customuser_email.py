# Generated by Django 4.2.2 on 2023-06-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalusEcommerce3', '0008_remove_detallesventas_id_sxm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='correo electronico'),
        ),
    ]