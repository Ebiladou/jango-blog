# Generated by Django 3.2.25 on 2025-02-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='category',
            field=models.CharField(choices=[('law', 'Law'), ('finance', 'Finance'), ('tech', 'Tech'), ('randoms', 'Randoms')], default='randoms', max_length=20),
        ),
        migrations.DeleteModel(
            name='Blog_category',
        ),
    ]
