from django.contrib import admin

from .models import Conference, OrganizingCommittee, Submission
# Register your models here.

admin.site.register(Conference)
admin.site.register(OrganizingCommittee)
admin.site.register(Submission)