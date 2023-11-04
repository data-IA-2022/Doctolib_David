"""Admin module"""

from django.contrib import admin
from doctolib.models import General_form_record, Stress_form_record

admin.site.register(General_form_record)
admin.site.register(Stress_form_record)


# Register your models here.
