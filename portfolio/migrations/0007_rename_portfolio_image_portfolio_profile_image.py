# Generated by Django 4.0.6 on 2022-08-30 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_rename_profile_images_portfolio_portfolio_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='portfolio_image',
            new_name='profile_image',
        ),
    ]
