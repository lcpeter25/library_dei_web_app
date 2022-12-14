# Generated by Django 4.0.6 on 2022-07-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_remove_book_authors_remove_characters_authors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characters',
            name='genders',
        ),
        migrations.RemoveField(
            model_name='characters',
            name='races',
        ),
        migrations.AddField(
            model_name='chargenderconn',
            name='character_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.characters'),
        ),
        migrations.AddField(
            model_name='charraceconn',
            name='character_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.characters'),
        ),
    ]
