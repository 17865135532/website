# Generated by Django 2.0.12 on 2020-06-09 11:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='dynamic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='内容')),
                ('image', models.ImageField(blank=True, null=True, upload_to='course/%Y%m%d')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('location', models.CharField(max_length=50, verbose_name='位置')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '话题',
                'verbose_name_plural': '话题',
                'ordering': ('-add_time',),
            },
        ),
        migrations.CreateModel(
            name='dynamicCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='话题')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.ManyToManyField(to='dynamic.dynamic')),
            ],
            options={
                'verbose_name': '话题',
                'verbose_name_plural': '话题',
                'ordering': ('-add_time',),
            },
        ),
        migrations.CreateModel(
            name='dynamicComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(verbose_name='评论')),
                ('url', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('dynamic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic.dynamic', verbose_name='话题')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '话题评论',
                'verbose_name_plural': '话题评论',
                'ordering': ('-add_time',),
            },
        ),
        migrations.CreateModel(
            name='dynamicCommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(verbose_name='回复内容')),
                ('url', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('aomments_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic.dynamicComment', verbose_name='回复id')),
                ('dynamicToUser', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dynamicToUser', to=settings.AUTH_USER_MODEL, verbose_name='目标用户')),
                ('dynamicUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dynamicUser', to=settings.AUTH_USER_MODEL, verbose_name='当前用户')),
            ],
        ),
    ]
