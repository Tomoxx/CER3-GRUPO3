# Generated by Django 4.1.2 on 2022-12-09 21:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_remove_evolucion_padre_reciennacido_padre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciennacido',
            name='padre',
        ),
        migrations.AddField(
            model_name='reciennacido',
            name='padres',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Padres'}, related_name='Padres', to=settings.AUTH_USER_MODEL),
        ),
    ]
