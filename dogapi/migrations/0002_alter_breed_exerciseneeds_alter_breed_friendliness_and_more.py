# Generated by Django 5.1.1 on 2024-09-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
