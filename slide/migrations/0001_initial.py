# Generated by Django 4.1 on 2025-02-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(help_text='最佳尺寸为1920*1080', upload_to='slide', verbose_name='幻灯片名字')),
                ('title', models.CharField(help_text='一级标题', max_length=200, verbose_name='标题')),
                ('content', models.CharField(help_text='二级标题', max_length=200, verbose_name='内容')),
            ],
            options={
                'verbose_name': '幻灯片管理',
                'verbose_name_plural': '幻灯片管理',
            },
        ),
    ]
