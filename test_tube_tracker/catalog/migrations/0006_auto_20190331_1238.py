# Generated by Django 2.1.7 on 2019-03-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190331_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='Location',
            field=models.CharField(blank=True, default='', help_text='Enter the index of the sample in the freezer', max_length=20, null=True),
        ),
    ]
