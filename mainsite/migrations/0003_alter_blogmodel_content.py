# Generated by Django 4.2.1 on 2023-05-20 17:40

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_alter_blogmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]