"""Admin module"""

from django.contrib import admin
from doctolib.models import GeneralFormRecord, StressFormRecord

admin.site.register(GeneralFormRecord)
admin.site.register(StressFormRecord)


# Register your models here.
