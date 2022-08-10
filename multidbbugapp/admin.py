from django.apps import apps
from django.urls import path
from django.contrib.admin import AdminSite, ModelAdmin

from django.conf import settings


from multidbbugapp.models import Parcel

# See https://docs.djangoproject.com/en/4.0/topics/db/multi-db/#exposing-multiple-databases-in-django-s-admin-interface  # noqa: E501
class CustomDatabaseModelAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        print(f"saving {obj} in {self.admin_site.database}")
        obj.save(using=self.admin_site.database)

    def delete_model(self, request, obj):
        print(f"deleting {obj} in {self.admin_site.database}")
        obj.delete(using=self.admin_site.database)

    def get_queryset(self, request):
        print(f"querying in {self.admin_site.database}")
        return super().get_queryset(request).using(self.admin_site.database)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(
            db_field, request, using=self.admin_site.database, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(
            db_field, request, using=self.admin_site.database, **kwargs
        )


class CustomDatabaseAdminSite(AdminSite):
    def __init__(self, database):
        super().__init__(database)
        self.database = database
        self.register(Parcel, CustomDatabaseModelAdmin)

        self.site_header = "Admin for " + settings.DATABASE_DISPLAY_NAMES[database]


admin_urls = [
    path("admin-" + database + "/", CustomDatabaseAdminSite(database).urls)
    for database in settings.DATABASES
]
