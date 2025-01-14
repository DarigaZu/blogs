# Generated by Django 5.1.1 on 2024-09-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tag text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('blogs', models.ManyToManyField(related_name='tags', to='blogs.blog', verbose_name='блог')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
    ]
