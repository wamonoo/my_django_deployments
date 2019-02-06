# Generated by Django 2.1.4 on 2019-02-01 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aff_site', '0004_auto_20190201_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aff_site.City'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aff_site.Country'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aff_site.Address'),
        ),
    ]
