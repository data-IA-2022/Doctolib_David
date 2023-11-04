from doctolib.models import General_form_record, Stress_form_record
from django.core.management.base import BaseCommand
import pandas as pd


class Command(BaseCommand):
    help = 'Command Information'

    def handle(self, *args, **kwargs):
        result_general = {}
        result_stress = {}
        general_fields = [f.name for f in General_form_record._meta.fields]
        stress_fields = [f.name for f in Stress_form_record._meta.fields]
        for field in general_fields:
            data =\
                [q[0]for q in General_form_record.objects.values_list(field)]
            result_general[field] = data
        for field in stress_fields:
            data = [q[0]for q in Stress_form_record.objects.values_list(field)]
            result_stress[field] = data

        df_gen = pd.DataFrame.from_dict(result_general)
        df_stress = pd.DataFrame.from_dict(result_stress)
        df_gen.to_csv('/home/dakoro/Doctolib_David/csv_files/general.csv',
                      index=False)
        df_stress.to_csv('/home/dakoro/Doctolib_David/csv_files/stress.csv',
                         index=False)
