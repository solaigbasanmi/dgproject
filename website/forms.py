from django import forms
from .models import DailyANCRegister,LabourDeliveryRegister, ChildImmunizationRegister, ContraceptiveStatistics,Category,StateCommodityMix, StateFPCommodity,CommodityList,StateImplementingPartner, StateBudget, FundingAgent,StateCostImplementationPlan, ThematicArea, DataSource,KeyActivities

class DailyANCRegisterForm(forms.ModelForm):
    class Meta:
        model = DailyANCRegister
        fields = [
            'state', 
            'lga', 
            'ward', 
            'facility_name', 
            'month', 
            'year', 
            'date', 
            'client_name', 
            'anc_card_number', 
            'age', 
            'parity', 
            'type_of_visit', 
            'number_of_visits', 
            'last_menstrual_period', 
            'gestation_age', 
            'weight', 
            'height', 
            'blood_pressure', 
            'group_anc', 
            
            'maternal_nutrition', 
            'multiple_micronutrient_supplement', 
            'maternal_mental_health', 
            'hygiene_in_pregnancy', 
            'gbv_fgm', 
            'early_initiation_of_breastfeeding', 
            'exclusive_breastfeeding', 
            'hiv_testing_services', 
            'malaria_in_pregnancy', 
            'vvf', 
            'family_planning_postpartum_fp', 
            'birth_registration', 
            'hiv_self_care_kit', 
            'hiv_testing', 
            'hpv_kit', 
            'syphilis_testing_result', 
            'hepatitis_b_result', 
            'hepatitis_c_result', 
            'haematology_test_result', 
            'urinalysis_result', 
            'haematinics_given', 
            'doses_of_IPT_given', 
            'tetanus_diphtheria', 
            'itn_given', 
            'associated_problems', 
            'outcome_of_visit'
        ]
        labels = {
            'client_name': 'Pregnant Woman’s Name',
            'anc_card_number': 'ANC Card Number',
            # Add custom labels for other fields as needed
        }
        help_texts = {
            'client_name': 'Enter the full name of the pregnant woman.',
            # Add help texts for other fields as needed
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
            'height': forms.NumberInput(attrs={'step': '0.01'}),
            # Customize widgets for other fields if necessary
        }


class LabourDeliveryRegisterForm(forms.ModelForm):
    class Meta:
        model = LabourDeliveryRegister
        fields = [
            'state',
            'lga',
            'ward',
            'facility_name',
            'month_year',
            'date',
            'client_name',
            'client_number',
            'age_group',
            'type_of_client',
            'time_taken_on_decision',
            'incoming_referral',
            'parity',
            'delivery_date',
            'delivery_mode',
            'labour_monitoring',
            'uterotonic_given',
            'oxytocin_given',
            'misoprostol_given',
            'heat_stable_carbetocin_given',
            'maternal_complication',
            'blood_loss_measurement_mls',
            'e_motive_provided',
            'post_abortion_care_provided',
            'admission_reason',
            'eclampsia_mgso4_provided',
            'discharge_date',
            'exclusive_breastfeeding_counselled',
            'ppfp_counselled',
            'accepted_ppfp_method',
            'referral_reason',
            'means_of_transport_in',
            'mother_dead',
            'maternal_death_audit_conducted',
            'maternal_death_audit_not_conducted',
            'induced_abortion',
            'spontaneous_abortion',
            'time_of_birth',
            'sex_of_baby',
            'stillbirth',
            'live_birth_weight',
            'still_birth',
            'still_birth_status',
            'pre_term',
            'admitted_to_kmc',
            'birth_asphyxia',
            'resuscitated_with_ambu_bag',
            'live_births_hiv_positive',
            'early_neonatal_death',
            'time_cord_clamped',
            'chx_gel_applied',
            'skin_to_skin_care_time',
            'temperature_at_1_hour',
            'breastfeeding_initiation_time',
            'delivery_skilled_birth_attendant',
            'name_of_delivery_attendant',
        ]
        labels = {
            'client_name': 'Client Name',
            'delivery_mode': 'Mode of Delivery',
            # Add custom labels for other fields as needed
        }
        help_texts = {
            'client_name': 'Enter the name of the client.',
            # Add help texts for other fields as needed
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'blood_loss_measurement_mls': forms.NumberInput(attrs={'step': '0.01'}),
            'temperature_at_1_hour': forms.NumberInput(attrs={'step': '0.01'}),
            # Customize widgets for other fields if necessary
        }

class ChildImmunizationRegisterForm(forms.ModelForm):
    class Meta:
        model = ChildImmunizationRegister
        fields = [
            'settlement',
            'name_of_facility',
            'year',
            'facility_name',
            'session_type',
            'session_name',
            'facility_type',
            'ward',
            'lga',
            'state',
            'date_of_visit',
            'client_name',
            'card_number',
            'sex',
            'follow_up_address',
            'phone_number',
            'date_of_birth',
            'hep_b_screening_0_24_hours',
            'hep_b_screening_above_24_hours',
            'opv_0_date',
            'bcg_date',
            'opv_1_date',
            'penta1_date',
            'pcv1_date',
            'rota_1_date',
            'ipv_1_date',
            'opv_2_date',
            'penta2_date',
            'pcv2_date',
            'rota_2_date',
            'opv_3_date',
            'penta3_date',
            'pcv3_date',
            'rota_3_date',
            'ipv_2_date',
            'malaria_1_date',
            'malaria_2_date',
            'vitamin_a_1_date',
            'malaria_3_date',
            'mr_1_date',
            'yellow_fever_date',
            'men_a_date',
            'mr_2_date',
            'malaria_4_date',
            'itn_given',
            'comments',
        ]
        labels = {
            'client_name': 'Child’s Name',
            'card_number': 'ANC Card Number',
            'date_of_visit': 'Date of Visit',
            # Add custom labels for other fields as needed
        }
        help_texts = {
            'client_name': 'Enter the name of the child receiving immunization.',
            # Add help texts for other fields as needed
        }
        widgets = {
            'date_of_visit': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # Customize widgets for other date fields if necessary
        }

class StateBudgetForm(forms.ModelForm):
    agency = forms.ModelChoiceField(queryset=FundingAgent.objects.all(), empty_label="Select Funding Agent")

    class Meta:
        model = StateBudget
        fields = [
            'state',
            'agency',
            'budget_line_item',
            'state_fp_budget',
            'state_fp_release',
            'year',
            'total_state_health_budget',
            'percent_srh_budget',
            'created_by',
           
        ]
        
class StateCostImplementationPlanForm(forms.ModelForm):
    funding_agent = forms.ModelChoiceField(queryset=FundingAgent.objects.all(), empty_label="Select Funding Agent")
    thematic_area = forms.ModelChoiceField(queryset=ThematicArea.objects.all(), empty_label="Select Thematic Area")
    data_source = forms.ModelChoiceField(queryset=DataSource.objects.all(), empty_label="Select Data Source")
    key_activities = forms.ModelChoiceField(queryset=KeyActivities.objects.all(), empty_label="Select Key Activity")

    class Meta:
        model = StateCostImplementationPlan
        fields = [
            'state',
            'funding_agent',
            'thematic_area',
            'data_source',
            'key_activities',
            'costed_in_state_plan',
            'year',
            'created_by'
        ]
        
class StateImplementingPartnerForm(forms.ModelForm):
    thematic_area = forms.ModelChoiceField(queryset=ThematicArea.objects.all(), empty_label="Select Thematic Area")
    funding_agent = forms.ModelChoiceField(queryset=FundingAgent.objects.all(), empty_label="Select Funding Agent")
    #data_source = forms.ModelChoiceField(queryset=DataSource.objects.all(), empty_label="Select Data Source")
    key_activities = forms.ModelChoiceField(queryset=KeyActivities.objects.all(), empty_label="Select Key Activity")
    class Meta:
        model = StateImplementingPartner
        fields = [
            'state',
            'funding_agent',
            'thematic_area',
            'key_activities',
            'actual_implementation_cost',
            'year',
            'created_by'
        ]
        widgets = {
            
            'year': forms.Select(choices=[(year, year) for year in range(2000, 2027)])  # Adjust year range as needed
        }
        
        
class StateFPCommodityForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=CommodityList.objects.all(), empty_label="Select Commodity Area")
    donor_agency = forms.ModelChoiceField(queryset=FundingAgent.objects.all(), empty_label="Select Funding Agent")
    
    class Meta:
        model = StateFPCommodity
        fields = [
            'name',
            'state',
            'funding_required',
            'funding_commitment',
            'fund_disbursed',
            'donor_agency',
            'year'
        ]
        widgets = {
            'year': forms.Select(choices=[(year, year) for year in range(2000, 2031)])  # Adjust year range as needed
        }
        
class StateCommodityMixForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=CommodityList.objects.all(), empty_label="Select Commodity Area")
    #donor_agency = forms.ModelChoiceField(queryset=FundingAgent.objects.all(), empty_label="Select Funding Agent")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category Funding Agent")
   
    class Meta:
        model = StateCommodityMix
        fields = [
            'name',
            'state',
            'category',
            'amount',
            'amount1',
           
            'year'
        ]
        widgets = {
            'year': forms.Select(choices=[(year, year) for year in range(2000, 2031)])  # Adjust year range as needed
        }
        
class ContraceptiveStatisticsForm(forms.ModelForm):
    class Meta:
        model = ContraceptiveStatistics
        fields = [
            'year',
            'state',
            'created_by',
            'women_receiving_contraceptive_care',
            'unintended_pregnancies_averted',
            'unplanned_births_averted',
            'unsafe_abortions_averted',
        ]
        widgets = {
            'year': forms.Select(choices=[(year, year) for year in range(2000, 2031)])  # Adjust year range as needed
        }