# Generated by Django 4.2.5 on 2023-10-05 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0008_rename_accounttype_application_accounttype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['name']},
        ),
    ]