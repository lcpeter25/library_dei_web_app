# Generated by Django 4.0.6 on 2022-08-05 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_workflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='characters',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.characters'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
