# Generated by Django 3.1 on 2021-05-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automated_logging', '0018_decoratoroverrideexclusiontest_foreignkeytest_fullclassbasedexclusiontest_fulldecoratorbasedexclusio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelevent',
            name='user',
            field=models.IntegerField(help_text='User ID from the Authentication system', null=True),
        ),
        migrations.AlterField(
            model_name='requestevent',
            name='user',
            field=models.IntegerField(help_text='User ID from the Authentication system', null=True),
        ),
    ]
