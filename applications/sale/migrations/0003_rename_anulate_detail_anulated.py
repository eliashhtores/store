# Generated by Django 3.2.10 on 2022-01-26 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='anulate',
            new_name='anulated',
        ),
    ]
