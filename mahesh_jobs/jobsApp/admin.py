from django.contrib import admin

from jobsApp.models import HydJobs, PuneJobs, BangJobs


# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']


class BangJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']


class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']


admin.site.register(HydJobs, HydJobsAdmin)

admin.site.register(PuneJobs, PuneJobsAdmin)

admin.site.register(BangJobs, BangJobsAdmin)
