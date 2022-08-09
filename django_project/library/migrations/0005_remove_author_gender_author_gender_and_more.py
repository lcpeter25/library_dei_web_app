# Generated by Django 4.0.6 on 2022-07-16 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_book_characters_author_gender_author_race_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='gender',
        ),
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.gender'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_verse',
            field=models.BooleanField(verbose_name='Is written in verse'),
        ),
    ]