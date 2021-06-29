# Generated by Django 3.2.3 on 2021-06-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default=True, max_length=2, verbose_name=[('politics', 'politics'), ('technology', 'technology'), ('sports', 'sports'), ('literature', 'literature'), ('langauge', 'langauge'), ('humanities', 'humanities'), ('environment', 'environment')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
