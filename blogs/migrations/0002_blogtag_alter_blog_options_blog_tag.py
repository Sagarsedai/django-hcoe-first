# Generated by Django 5.0.3 on 2024-03-10 05:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('cdb21093-3161-42c6-8ea5-abf287a832e0'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Blog Tag',
                'verbose_name_plural': 'Blog Tag(s)',
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blog(s)'},
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='blogs', to='blogs.blogtag'),
            preserve_default=False,
        ),
    ]
