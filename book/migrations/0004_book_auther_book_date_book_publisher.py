# Generated by Django 5.0.3 on 2024-04-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_table_alter_usermodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='auther',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
