# Generated by Django 3.2.9 on 2022-01-11 06:49

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='none', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=60)),
                ('image_path', models.URLField(null=True)),
                ('description', models.TextField(null=True)),
                ('page_count', models.IntegerField(null=True)),
                ('publisher', models.CharField(max_length=60, null=True)),
                ('date_published', models.CharField(max_length=10)),
                ('checkout_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BookTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=70)),
                ('profile_image_url', models.URLField()),
                ('background_image_url', models.URLField(default='')),
                ('subscriber', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReadingGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_pages', models.IntegerField(null=True)),
                ('number_of_books', models.IntegerField(null=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(null=True)),
                ('review', models.TextField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('finish_date', models.DateField(null=True)),
                ('current_page', models.IntegerField(null=True)),
                ('book', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='librogramapi.book')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='librogramapi.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('label',), name='unique_tag'),
        ),
        migrations.AddField(
            model_name='readinggoal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reader',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='librogramapi.book'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booktag',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librogramapi.book'),
        ),
        migrations.AddField(
            model_name='booktag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librogramapi.tag'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librogramapi.author'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librogramapi.book'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='librogramapi.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='librogramapi.Tag'),
        ),
    ]
