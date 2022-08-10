from django.db import migrations, models

TRACKING_ID_BY_DB = {
    "default": ["one", "two"],
    "other": ["two-duplicate"],
}


def insert_some_data(apps, schema_editor):
    db = schema_editor.connection.alias
    Parcel = apps.get_model("multidbbugapp", "Parcel")
    print("")
    for tracking_id in TRACKING_ID_BY_DB[db]:
        obj = Parcel.objects.using(db).create(tracking_id=tracking_id)
        print(f"Added object {obj} with in DB {db}")


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parcel",
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.CharField(blank=True, max_length=40, null=True, unique=True)),
            ],
            options={
                "db_table": "parcel",
            },
        ),
        migrations.RunPython(insert_some_data, reverse_code=migrations.RunPython.noop),
    ]
