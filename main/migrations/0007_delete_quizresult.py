# Generated by Django 4.0.1 on 2023-04-28 12:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_quizresult"),
    ]

    operations = [
        migrations.DeleteModel(
            name="QuizResult",
        ),
    ]
