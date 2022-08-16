# Generated by Django 4.0 on 2022-01-01 12:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0008_auto_20211219_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyPostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(max_length=200, null=True)),
                ('date_send', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
            ],
        ),
    ]
