# Generated by Django 4.0.6 on 2022-07-16 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_characters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='characters',
        ),
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.ManyToManyField(null=True, to='library.gender'),
        ),
        migrations.AddField(
            model_name='author',
            name='race',
            field=models.ManyToManyField(null=True, to='library.race'),
        ),
        migrations.AddField(
            model_name='characters',
            name='book',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_verse',
            field=models.BooleanField(verbose_name='Author First Name'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='addiction',
            field=models.IntegerField(null=True, verbose_name='Number of characters who are experiencing addiction'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='adverse_mental_health_trauma_response',
            field=models.IntegerField(null=True, verbose_name='Number of characters who are experiencing adverse mental health or trauma response'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='disabled',
            field=models.IntegerField(null=True, verbose_name='Number of disabled characters'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='experiencing_homelessness_low_income',
            field=models.IntegerField(null=True, verbose_name='Number of characters who are experiencing homelessness or low-income'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='immigrants',
            field=models.IntegerField(null=True, verbose_name='Number of characters who are immigrants'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='lgbtqia',
            field=models.IntegerField(null=True, verbose_name='Number of LGBTQIA+ characters'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='neurodiverse',
            field=models.IntegerField(null=True, verbose_name='Number of neurodiverse characters'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='non_humans',
            field=models.IntegerField(null=True, verbose_name='Number of non-human characters'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='plus_size',
            field=models.IntegerField(null=True, verbose_name='Number of plus-size characters'),
        ),
    ]