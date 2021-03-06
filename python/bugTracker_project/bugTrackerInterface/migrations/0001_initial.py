# Generated by Django 3.0.5 on 2020-04-20 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('snippet', models.CharField(default='No Snippet Available', max_length=100)),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished', models.BooleanField(default=False)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
