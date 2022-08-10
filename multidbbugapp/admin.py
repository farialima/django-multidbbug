from django.contrib.admin import ModelAdmin, site

from multidbbugapp.models import Parcel

# See https://docs.djangoproject.com/en/4.0/topics/db/multi-db/#exposing-multiple-databases-in-django-s-admin-interface  # noqa: E501
class MultiDBModelAdmin(ModelAdmin):
    using = 'other'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

site.register(Parcel, MultiDBModelAdmin)
