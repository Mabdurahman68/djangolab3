# Generated by Django 3.2.3 on 2021-05-18 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osMansoura', '0004_alter_student_student_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_track',
            field=models.ForeignKey(default='os', on_delete=django.db.models.deletion.CASCADE, to='osMansoura.track'),
        ),
    ]
