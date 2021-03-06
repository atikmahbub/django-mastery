# Generated by Django 4.0.2 on 2022-05-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
                'get_latest_by': 'price',
            },
        ),
    ]
