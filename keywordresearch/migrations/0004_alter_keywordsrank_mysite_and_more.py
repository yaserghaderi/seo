# Generated by Django 5.0.7 on 2024-07-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywordresearch', '0003_keywordsrank_mysite_keywordsrank_comparator1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordsrank',
            name='Mysite',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='keywordsrank',
            name='comparator1',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='keywordsrank',
            name='comparator2',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='keywordsrank',
            name='myrank',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='keywordsrank',
            name='rank_comparator1',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='keywordsrank',
            name='rank_comparator2',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
