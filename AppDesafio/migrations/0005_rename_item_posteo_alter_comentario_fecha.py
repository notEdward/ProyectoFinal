# Generated by Django 4.0.4 on 2022-06-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0004_comentario_user_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Posteo',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
