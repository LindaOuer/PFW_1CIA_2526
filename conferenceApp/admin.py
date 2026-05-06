from django.contrib import admin

from .models import Conference, OrganizingCommittee, Submission
# Register your models here.


class ConferenceFilterDate(admin.SimpleListFilter):
    title = "Conference Date"
    parameter_name = "Conference_Date"

    def lookups(self, request, model_admin):
        return (
            ("upcoming", "Upcoming"),
            ("ongoing", "Ongoing"),
            ("past", "Past"),
        )

    def queryset(self, request, queryset):
        from django.utils.timezone import now

        today = now().date()
        if self.value() == "upcoming":
            return queryset.filter(start_date__gt=today)
        elif self.value() == "ongoing":
            return queryset.filter(start_date__lte=today, end_date__gte=today)
        elif self.value() == "past":
            return queryset.filter(end_date__lt=today)
        return queryset


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "start_date", "end_date", "theme")
    search_fields = ("name", "location", "theme")
    list_filter = ("theme", ConferenceFilterDate)
    ordering = ("-start_date",)
    list_per_page = 1
    fieldsets = (
        (None, {"fields": ("name", "location", "theme")}),
        ("Description", {"fields": ("description",), "classes": ("collapse",)}),
        (
            "dates",
            {
                "fields": (
                    "start_date",
                    "end_date",
                )
            },
        ),
    )
    exclude = ("created_at", "updated_at")

    actions = ["set_location"]

    def set_location(self, request, queryset):
        queryset.update(location="London")
        self.message_user(request, "Selected conferences have been updated to London.")

    set_location.short_description = "Set location to London for selected conferences"


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(OrganizingCommittee)
admin.site.register(Submission)
