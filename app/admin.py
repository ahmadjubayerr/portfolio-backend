from django.contrib import admin
from .models import (
    MyProfile,
    Experience,
    Education,
    Certification,
    Project,
    Achievement,
    Contact
)
from django.shortcuts import redirect, reverse


@admin.register(MyProfile)
class MyProfileAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("achievement_images_gallery",)
    def has_add_permission(self, request):
        return not MyProfile.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = MyProfile.objects.first()
        if obj:
            url = reverse(
                'admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),
                args=[obj.pk]
            )
            return redirect(url)
        app_label = MyProfile._meta.app_label
        model_name = MyProfile._meta.model_name
        print(app_label, model_name)
        return redirect(reverse(f'admin:{app_label}_{model_name}_add'))

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "tag")
    list_filter = ("category",)
    search_fields = ("title", "tag")


admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Achievement)
admin.site.register(Contact)
