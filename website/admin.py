from django.contrib import admin

# Register your models here.
from .models import DailyANCRegister, LabourDeliveryRegister,ChildImmunizationRegister, ContraceptiveStatistics, StateCommodityMix, FundingAgent,State,CommodityList,DataSource,ThematicArea,KeyActivities,StateFPCommodity,Category

admin.site.register(DailyANCRegister)
admin.site.register(State)
admin.site.register(LabourDeliveryRegister)
admin.site.register(ChildImmunizationRegister)


