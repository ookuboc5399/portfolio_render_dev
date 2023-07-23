# Generated by Django 3.1.14 on 2023-07-23 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100, verbose_name='コース')),
                ('school', models.CharField(max_length=100, verbose_name='学校')),
                ('place', models.CharField(max_length=100, verbose_name='場所')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=100, verbose_name='職種')),
                ('company', models.CharField(max_length=100, verbose_name='会社')),
                ('description', models.TextField(verbose_name='説明')),
                ('place', models.CharField(max_length=100, verbose_name='場所')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='タイトル')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='サブタイトル')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('job', models.TextField(verbose_name='仕事')),
                ('introduction', models.TextField(verbose_name='自己紹介')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='linkedin')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='facebook')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram')),
                ('topimage', models.ImageField(upload_to='images', verbose_name='トップ画像')),
                ('subimage', models.ImageField(upload_to='images', verbose_name='サブ画像')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ソフトウェア')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.IntegerField(verbose_name='パーセンテージ')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='テクニカル')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.IntegerField(verbose_name='パーセンテージ')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='images', verbose_name='イメージ画像')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='サムネイル')),
                ('skill', models.CharField(max_length=100, verbose_name='スキル')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('created', models.DateField(verbose_name='作成日時')),
                ('description', models.TextField(verbose_name='説明')),
            ],
        ),
    ]