from django.contrib import admin

from reconciliation.admin import work
from reconciliation.admin import contributor
from reconciliation import models

admin.site.register(models.Work, work.WorkAdmin)
admin.site.register(models.Contributor, contributor.ContributorAdmin)
