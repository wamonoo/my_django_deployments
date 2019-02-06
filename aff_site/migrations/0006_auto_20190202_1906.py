# Generated by Django 2.1.4 on 2019-02-03 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aff_site', '0005_auto_20190201_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aff_site.City'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aff_site.Country'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aff_site.Address'),
        ),
    ]
