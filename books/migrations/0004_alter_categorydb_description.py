# Generated by Django 4.1.3 on 2022-11-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_user_categorydb_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydb',
            name='Description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]