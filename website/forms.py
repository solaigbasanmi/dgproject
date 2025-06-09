from django import forms
from .models import DailyANCRegister,LabourDeliveryRegister, ChildImmunizationRegister,State
from django.core.validators import RegexValidator
from django import forms
from .models import ChildImmunizationTally
from django.forms import DateInput

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
             'last_menstrual_period': forms.DateInput(attrs={'type': 'date'}),
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
            'discharge_date': forms.DateInput(attrs={'type': 'date'}),
            
            'time_of_birth': forms.TimeInput(attrs={'type': 'time'}),
             'time_cord_clamped': forms.TimeInput(attrs={'type': 'time'}),
            
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
            'date_of_birth': 'Date of Birth',
            # Add custom labels for other fields as needed
        }
        help_texts = {
            'client_name': 'Enter the name of the child receiving immunization.',
            # Add help texts for other fields as needed
        }
        widgets = {
            'date_of_visit': forms.DateTimeInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'date'}),
            'opv_0_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'bcg_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'opv_1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'penta1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'pcv1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'rota_1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'ipv_1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'opv_2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'penta2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'pcv2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'rota_2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'opv_3_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'penta3_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'pcv3_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'rota_3_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'ipv_2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'malaria_1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'malaria_2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'vitamin_a_1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'malaria_3_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'mr_1_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'yellow_fever_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'men_a_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'mr_2_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'malaria_4_date': forms.DateTimeInput(attrs={'type': 'date'}),
            # Customize widgets for other fields if necessary
        }


from django import forms
from .models import ChildImmunizationTally

class ChildImmunizationTallyForm(forms.ModelForm):
    class Meta:
        model = ChildImmunizationTally
        fields = [
            'facility_name',
            'ward',
            'lga',
            'state',
            'facility_type',
            'date_of_visit',
            'session_type',
            'site_name',
            'hep_b_0_24_hours',
            'hep_b_above_24_hours',
            'opv_0',
            'bcg',
            'opv_1',
            'penta1',
            'pcv1',
            'rota1',
            'ipv1',
            'opv2',
            'penta2',
            'pcv2',
            'rota2',
            'opv3',
            'penta3',
            'pcv3',
            'rota3',
            'ipv2',
            'malaria1',
            'malaria2',
            'vitamin_a_6_11',
            'vitamin_a_12_23',
            'malaria3',
            'mr1',
            'yellow_fever',
            'men_a',
            'mr2',
            'malaria4',
            'comments',
            'health_officer_name',
            'health_officer_signature_date',
            'health_officer_phone',
            'head_of_unit_name',
            'head_of_unit_signature_date',
            'head_of_unit_phone',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set date fields as optional
        date_fields = [
            'hep_b_0_24_hours',
            'hep_b_above_24_hours',
            'opv_0',
            'bcg',
            'opv_1',
            'penta1',
            'pcv1',
            'rota1',
            'ipv1',
            'opv2',
            'penta2',
            'pcv2',
            'rota2',
            'opv3',
            'penta3',
            'pcv3',
            'rota3',
            'ipv2',
            'malaria1',
            'malaria2',
            'vitamin_a_6_11',
            'vitamin_a_12_23',
            'malaria3',
            'mr1',
            'yellow_fever',
            'men_a',
            'mr2',
            'malaria4',
        ]
        
        for field in date_fields:
            self.fields[field].required = False  # Make these fields optional