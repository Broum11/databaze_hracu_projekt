# Generated by Django 5.1.4 on 2025-01-22 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chance_liga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='matches_played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='chart',
            name='points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='chart',
            name='position',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('B', 'Brankář'), ('O', 'Obránce'), ('Z', 'Záložník'), ('Ú', 'Útočník')], default='neznámé', max_length=1)),
                ('country', models.CharField(default='neznámé', max_length=100)),
                ('name', models.CharField(default='neznámé', max_length=100)),
                ('number', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='Chance_liga.team')),
            ],
        ),
    ]
