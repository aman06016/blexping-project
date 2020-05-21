# Generated by Django 2.2 on 2020-05-18 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200518_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
