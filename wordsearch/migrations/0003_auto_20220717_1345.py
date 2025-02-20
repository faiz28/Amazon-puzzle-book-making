# Generated by Django 3.1.7 on 2022-07-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0002_auto_20220717_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordsearch_inner_page',
            name='rectangle_l_r_i',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='wordsearch_inner_page',
            name='rectangle_u_d_i',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='wordsearch_inner_page',
            name='alphabate_left_right_space',
            field=models.FloatField(default=0.4),
        ),
        migrations.AlterField(
            model_name='wordsearch_inner_page',
            name='alphabate_up_down_space',
            field=models.FloatField(default=0.4),
        ),
    ]
