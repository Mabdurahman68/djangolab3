# Generated by Django 3.2.3 on 2021-05-18 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osMansoura', '0003_auto_20210518_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_track',
            field=models.ForeignKey(default='sd', on_delete=django.db.models.deletion.CASCADE, to='osMansoura.track'),
        ),
    ]
