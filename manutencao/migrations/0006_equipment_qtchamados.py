# Generated by Django 2.2.24 on 2021-09-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0005_auto_20210921_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='qtchamados',
            field=models.IntegerField(null=True),
        ),
    ]