# Generated by Django 3.2.9 on 2021-12-05 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumb',
            new_name='picture',
        ),
    ]
