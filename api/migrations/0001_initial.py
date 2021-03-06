# Generated by Django 3.0.7 on 2022-06-13 04:37

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.CharField(max_length=100)),
                ('sub1', models.CharField(blank=True, max_length=100, null=True)),
                ('sub2', models.CharField(blank=True, max_length=100, null=True)),
                ('sub3', models.CharField(blank=True, max_length=100, null=True)),
                ('sub4', models.CharField(blank=True, max_length=100, null=True)),
                ('sub6', models.CharField(blank=True, max_length=100, null=True)),
                ('sub7', models.CharField(blank=True, max_length=100, null=True)),
                ('sub8', models.CharField(blank=True, max_length=100, null=True)),
                ('sub9', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('todo1_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo1_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo2_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo3_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo4_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo6_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo7_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo8_9', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_1', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_2', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_3', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_4', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_6', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_7', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_8', models.CharField(blank=True, max_length=50, null=True)),
                ('todo9_9', models.CharField(blank=True, max_length=50, null=True)),
                ('liked', models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('userTarget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTarget', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=api.models.upload_avator_path)),
                ('userProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Target')),
                ('userComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userComment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
