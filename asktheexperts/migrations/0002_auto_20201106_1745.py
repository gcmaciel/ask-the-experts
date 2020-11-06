# Generated by Django 3.1.3 on 2020-11-06 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asktheexperts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questioned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('selected', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answered_question', to='asktheexperts.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answered_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='vote_answer',
            field=models.ManyToManyField(related_name='answer_voted', to='asktheexperts.Answer'),
        ),
        migrations.AddField(
            model_name='user',
            name='vote_question',
            field=models.ManyToManyField(related_name='question_voted', to='asktheexperts.Question'),
        ),
    ]
