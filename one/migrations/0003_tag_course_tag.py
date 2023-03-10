# Generated by Django 4.1.7 on 2023-02-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_category_course_admin_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.ManyToManyField(to='one.tag'),
        ),
    ]
