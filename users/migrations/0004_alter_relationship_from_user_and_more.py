# Generated by Django 4.0.2 on 2022-03-12 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='users.profile'),
        ),
    ]
