# Generated by Django 2.2 on 2020-07-30 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Date of post')),
                ('content', models.TextField(help_text='Enter your post here.', max_length=1000)),
                ('title', models.CharField(help_text='Title of post', max_length=100)),
                ('author', models.ForeignKey(help_text='Author of post', on_delete=django.db.models.deletion.CASCADE, to='blog.Blogger')),
            ],
            options={
                'ordering': ['-date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(help_text='Date and time of comment')),
                ('comment', models.TextField(help_text='Enter your comment here', max_length=200)),
                ('blog_post', models.ForeignKey(help_text='Blog post of the comment', on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
                ('commentor', models.ForeignKey(help_text='Author of comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_time', 'commentor'],
            },
        ),
    ]