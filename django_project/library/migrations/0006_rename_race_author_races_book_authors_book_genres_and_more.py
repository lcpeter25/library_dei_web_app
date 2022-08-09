# Generated by Django 4.0.6 on 2022-07-16 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_remove_author_gender_author_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='race',
            new_name='races',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(null=True, to='library.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(null=True, to='library.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='shelving_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.shelvingcategory'),
        ),
        migrations.AddField(
            model_name='characters',
            name='authors',
            field=models.ManyToManyField(null=True, to='library.author'),
        ),
    ]