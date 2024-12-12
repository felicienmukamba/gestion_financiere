# Generated by Django 4.2.17 on 2024-12-09 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("designation", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ("designation",),
            },
        ),
        migrations.CreateModel(
            name="Promotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("designation", models.CharField(max_length=50)),
                ("actif", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("designation",),
            },
        ),
        migrations.CreateModel(
            name="Qualite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("designation", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ("designation",),
            },
        ),
        migrations.CreateModel(
            name="Etudiant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("matricule", models.CharField(max_length=10)),
                ("nom", models.CharField(max_length=50)),
                ("postnom", models.CharField(max_length=50)),
                ("prenom", models.CharField(blank=True, max_length=50)),
                (
                    "sexe",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Feminin")], max_length=50
                    ),
                ),
                ("telephone", models.CharField(max_length=15, unique=True)),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="section.departement",
                    ),
                ),
                (
                    "promotion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="section.promotion",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="departement",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="section.section"
            ),
        ),
        migrations.CreateModel(
            name="Beneficiere",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=50)),
                ("postnom", models.CharField(max_length=50)),
                ("prenom", models.CharField(blank=True, max_length=50)),
                (
                    "sexe",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Feminin")], max_length=50
                    ),
                ),
                ("qualite", models.ManyToManyField(to="section.qualite")),
            ],
        ),
    ]
