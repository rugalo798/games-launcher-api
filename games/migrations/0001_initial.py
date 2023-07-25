# Generated by Django 4.2.3 on 2023-07-25 01:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id_game', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='games')),
                ('release_date', models.DateField()),
                ('link', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]