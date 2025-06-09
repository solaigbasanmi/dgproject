from django.contrib import admin

# Register your models here.
from .models import DailyANCRegister, LabourDeliveryRegister,ChildImmunizationRegister ,State,ChildImmunizationTally

admin.site.register(ChildImmunizationTally)
admin.site.register(DailyANCRegister)
admin.site.register(State)
admin.site.register(LabourDeliveryRegister)
admin.site.register(ChildImmunizationRegister)


