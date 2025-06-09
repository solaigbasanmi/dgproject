from django.db import models
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from calendar import monthrange

from collections import defaultdict

class State(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class DataSource(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class DailyANCRegister(models.Model):
    state = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    facility_name = models.CharField(max_length=255)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    date = models.DateField()
    client_name = models.CharField(max_length=255)  # Pregnant woman's name
    anc_card_number = models.CharField(max_length=50)
    age = models.IntegerField()  # Exact age
    parity = models.IntegerField()  # Number of pregnancies beyond 28 weeks
    type_of_visit = models.CharField(max_length=50)  # Type of ANC attendance
    number_of_visits = models.IntegerField()  # Number of ANC visits to date
    last_menstrual_period = models.DateField()  # LMP
    gestation_age = models.IntegerField()  # Age of pregnancy in weeks
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Weight in Kg
    height = models.DecimalField(max_digits=3, decimal_places=2)  # Height in M
    blood_pressure = models.CharField(max_length=20)  # Blood pressure reading
    group_anc = models.BooleanField(default=False)  # Group ANC provided
    maternal_nutrition = models.BooleanField(default=False)
    multiple_micronutrient_supplement = models.BooleanField(default=False)
    maternal_mental_health = models.BooleanField(default=False)
    hygiene_in_pregnancy = models.BooleanField(default=False)  # WASH
    gbv_fgm = models.BooleanField(default=False)  # GBV/Female Genital Mutilation
    early_initiation_of_breastfeeding = models.BooleanField(default=False)
    exclusive_breastfeeding = models.BooleanField(default=False)
    hiv_testing_services = models.BooleanField(default=False)
    malaria_in_pregnancy = models.BooleanField(default=False)
    vvf = models.BooleanField(default=False)  # Vesicovaginal Fistula
    family_planning_postpartum_fp = models.BooleanField(default=False)
    birth_registration = models.BooleanField(default=False)

    hiv_self_care_kit = models.BooleanField(default=False)  # HIV self-care kit given
    hiv_testing = models.BooleanField(default=False)  # HIV testing done
    hpv_kit = models.BooleanField(default=False)  # HPV kit given
    
    syphilis_testing_result = models.CharField(max_length=20, choices=[
        ('Not Done', 'Not Done'),
        ('Negative', 'Negative'),
        ('Positive', 'Positive'),
        ('Treated', 'Treated'),
    ], blank=True, null=True)

    hepatitis_b_result = models.CharField(max_length=20, choices=[
        ('Not Done', 'Not Done'),
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Referred', 'Referred out for treatment'),
    ], blank=True, null=True)

    hepatitis_c_result = models.CharField(max_length=20, choices=[
        ('Not Done', 'Not Done'),
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Referred', 'Referred out for treatment'),
    ], blank=True, null=True)

    haematology_test_result = models.CharField(max_length=20, choices=[
        ('HB/PCV', 'HB/PCV (in g/dl or %)'),
        ('Sugar', 'Sugar (Gestational Diabetes)'),
    ], blank=True, null=True)

    urinalysis_result = models.CharField(max_length=20, choices=[
        ('Proteins', 'Proteins'),
        ('Sugar', 'Sugar'),
    ], blank=True, null=True)

    haematinics_given = models.CharField(max_length=20, choices=[
        ('IFAS', 'Iron and Folic Acid Supplement (IFAS)'),
        ('MMS', 'Multiple Micronutrient Supplement (MMS)'),
    ], blank=True, null=True)

    doses_of_IPT_given = models.CharField(max_length=5, choices=[
        ('IPT1', 'IPT 1'),
        ('IPT2', 'IPT 2'),
        ('IPT3', 'IPT 3'),
        ('IPT4', 'IPT ≥4'),
    ], blank=True, null=True)

    tetanus_diphtheria = models.CharField(max_length=10)  # Td1, Td2, etc.
    itn_given = models.BooleanField(default=False)  # ITN given during ANC visit
    associated_problems = models.TextField(blank=True, null=True)  # Associated problems
    outcome_of_visit = models.TextField(blank=True, null=True)  # Outcome of visit 
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_name} - {self.date}"


class Uterotonic(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class LabourDeliveryRegister(models.Model):
    state = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    facility_name = models.CharField(max_length=255)
    month_year = models.CharField(max_length=7)  # MM/YYYY
    date = models.DateField()

    client_name = models.CharField(max_length=255)  # Name of the client
    client_number = models.CharField(max_length=50)  # Client or Patient number
    age_group = models.CharField(max_length=5, choices=[
        ('10-14', '10 - 14 years'),
        ('15-19', '15 - 19 years'),
        ('20-24', '20 - 24 years'),
        ('25-35', '25 - 35 years'),
        ('36-49', '36 - 49 years'),
        ('50+', '≥ 50 years'),
    ], blank=True, null=True)

    type_of_client = models.CharField(max_length=50)  # Booked/Unbooked
    time_taken_on_decision = models.CharField(max_length=10, choices=[
        ('<24hrs', '< 24 hours'),
        ('≥24hrs', '≥ 24 hours'),
    ], blank=True, null=True)
    
    labour_monitoring = models.CharField(max_length=200, choices=[
        ('Partograph Used', 'Partograph Used'),
        ('Labour Care Guide Use', 'Labour Care Guide Use'),
    ], blank=True, null=True)

    incoming_referral = models.CharField(max_length=50)  # Referral source
    parity = models.IntegerField()  # Number of pregnancies beyond 28 weeks
    delivery_date = models.DateField()  # Date of delivery
    delivery_mode = models.CharField(max_length=20)  # SVD, CS, AD, etc.
    uterotonic_given = models.BooleanField(default=False)  # True for Yes, False for No
    oxytocin_given = models.BooleanField(default=False)
    misoprostol_given = models.BooleanField(default=False)
    heat_stable_carbetocin_given = models.BooleanField(default=False)

    maternal_complication = models.CharField(max_length=50, blank=True, null=True)  # Complications seen
    blood_loss_measurement_mls = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    e_motive_provided = models.BooleanField(default=False)

    post_abortion_care_provided = models.BooleanField(default=False)
    admission_reason = models.CharField(max_length=100, blank=True, null=True)
    eclampsia_mgso4_provided = models.BooleanField(default=False)
    discharge_date = models.DateField(blank=True, null=True)
    exclusive_breastfeeding_counselled = models.BooleanField(default=False)
    ppfp_counselled = models.BooleanField(default=False)
    accepted_ppfp_method = models.CharField(max_length=100, blank=True, null=True)
    referral_reason = models.TextField(blank=True, null=True)
    means_of_transport_in = models.CharField(max_length=20, choices=[
        ('Vehicle', 'Vehicle'),
        ('Ambulance', 'Ambulance'),
        ('Others', 'Others'),
    ], blank=True, null=True)

    mother_dead = models.BooleanField(default=False)
    maternal_death_audit_conducted = models.BooleanField(default=False)
    maternal_death_audit_not_conducted = models.BooleanField(default=False)
    induced_abortion = models.BooleanField(default=False)
    spontaneous_abortion = models.BooleanField(default=False)
    time_of_birth = models.TimeField(null=True, blank=True)
    sex_of_baby = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)
    stillbirth = models.BooleanField(default=False)
    live_birth_weight = models.CharField(max_length=10, choices=[
        ('<1.0 Kg', '< 1.0 Kg'),
        ('1.0-1.5 Kg', '1.0 - < 1.5 Kg'),
        ('1.5-2.5 Kg', '1.5 - < 2.5 Kg'),
        ('≥2.5 Kg', '≥ 2.5 Kg'),
    ], blank=True, null=True)
    still_birth = models.BooleanField(default=False)  # Stillbirth indicator
    still_birth_status = models.CharField(max_length=255)
    pre_term = models.CharField(max_length=15, choices=[
        ('<28 weeks', '< 28 weeks'),
        ('28-32 weeks', '28 - < 32 weeks'),
        ('32-34 weeks', '32 - < 34 weeks'),
        ('34-37 weeks', '34 - < 37 weeks'),
    ], blank=True, null=True)

    admitted_to_kmc = models.BooleanField(default=False)
    birth_asphyxia = models.CharField(max_length=2, choices=[
        ('NB', 'Not Breathing'),
        ('NC', 'Not Crying'),
    ], blank=True, null=True)

    resuscitated_with_ambu_bag = models.BooleanField(default=False)
    live_births_hiv_positive = models.BooleanField(default=False)
    early_neonatal_death = models.BooleanField(default=False)
    time_cord_clamped = models.TimeField(null=True, blank=True)
    chx_gel_applied = models.BooleanField(default=False)
    skin_to_skin_care_time = models.CharField(max_length=50, choices=[
        ('within_1_hour', 'Within 1 Hour'),
        ('after_1_hour', 'After 1 Hour'),
    ], blank=True, null=True)
    temperature_at_1_hour = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    breastfeeding_initiation_time = models.CharField(max_length=50, choices=[
        ('within_1_hour', 'Initiation of breastfeeding within 1 hour'),
        ('after_1_hour', 'Initiation of breastfeeding after 1 hour'),
    ], blank=True, null=True)
    delivery_skilled_birth_attendant = models.CharField(max_length=50, choices=[
        ('SBA: Doctor, Midwife or Nurse, MLSS-trained CHEW', 'SBA: Doctor, Midwife or Nurse, MLSS-trained CHEW'),
        ('Others', 'others'),
    ], blank=True, null=True)
    name_of_delivery_attendant = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_name} - {self.delivery_date}"


class ChildImmunizationRegister(models.Model):
    settlement = models.CharField(max_length=255)
    name_of_facility = models.CharField(max_length=255)
    year = models.IntegerField()
    facility_name = models.CharField(max_length=255)
    session_type = models.CharField(max_length=255)
    session_name = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=50)  # Public/Private
    ward = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    date_of_visit = models.DateTimeField(blank=True, null=True)  # Allow null
    client_name = models.CharField(max_length=255)  # Name of the child
    card_number = models.CharField(max_length=50)  # ANC Card Number
    sex = models.CharField(max_length=6)  # Male/Female
    follow_up_address = models.TextField(blank=True, null=True)  # Follow-up address
    phone_number = models.CharField(max_length=20)  # Phone number
    date_of_birth = models.DateTimeField(blank=True, null=True)  # Allow null

    # Vaccine dates
    hep_b_screening_0_24_hours = models.BooleanField(default=False)
    hep_b_screening_above_24_hours = models.BooleanField(default=False)
    opv_0_date = models.DateTimeField(blank=True, null=True)  # Allow null
    bcg_date = models.DateTimeField(blank=True, null=True)  # Allow null
    opv_1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    penta1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    pcv1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    rota_1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    ipv_1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    opv_2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    penta2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    pcv2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    rota_2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    opv_3_date = models.DateTimeField(blank=True, null=True)  # Allow null
    penta3_date = models.DateTimeField(blank=True, null=True)  # Allow null
    pcv3_date = models.DateTimeField(blank=True, null=True)  # Allow null
    rota_3_date = models.DateTimeField(blank=True, null=True)  # Allow null
    ipv_2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    malaria_1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    malaria_2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    vitamin_a_1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    malaria_3_date = models.DateTimeField(blank=True, null=True)  # Allow null
    mr_1_date = models.DateTimeField(blank=True, null=True)  # Allow null
    yellow_fever_date = models.DateTimeField(blank=True, null=True)  # Allow null
    men_a_date = models.DateTimeField(blank=True, null=True)  # Allow null
    mr_2_date = models.DateTimeField(blank=True, null=True)  # Allow null
    malaria_4_date = models.DateTimeField(blank=True, null=True)  # Allow null
    itn_given = models.BooleanField(default=False)  # ITN given
    comments = models.TextField(blank=True, null=True)  # Comments
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_name} - {self.date_of_visit}"

from django.db import models

class ChildImmunizationTally(models.Model):
    # General Information
    facility_name = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=50, choices=[('Public', 'Public'), ('Private', 'Private')])

    # Visit Details
    date_of_visit = models.DateField()
    session_type = models.CharField(max_length=50, choices=[('Fixed', 'Fixed'), ('Outreach', 'Outreach'), ('Mobile', 'Mobile')])
    site_name = models.CharField(max_length=255, blank=True, null=True)

    # Vaccination Counts
    hep_b_0_24_hours = models.DateTimeField(null=True)  # Hep.B 0 (0 - 24 HOURS)
    hep_b_above_24_hours = models.DateTimeField(null=True)  # Hep.B 0 (>24 HOURS - 2 WEEKS)
    opv_0 = models.DateTimeField(null=True)  # OPV 0 (0 - 2 WEEKS)
    bcg = models.DateTimeField(null=True)  # BCG (0 - 11 MONTHS)
    opv_1 = models.DateTimeField(null=True)  # OPV 1 (6 WEEKS - 11 MONTHS)
    penta1 = models.DateTimeField(null=True)  # PENTA1 (6 WEEKS - 11 MONTHS)
    pcv1 = models.DateTimeField(null=True)  # PCV1 (6 WEEKS - 11 MONTHS)
    rota1 = models.DateTimeField(null=True)  # ROTA 1 (6 WEEKS - 11 MONTHS)
    ipv1 = models.DateTimeField(null=True)  # IPV 1 (6 WEEKS - 11 MONTHS)
    opv2 = models.DateTimeField(null=True)  # OPV2 (10 WEEKS - 11 MONTHS)
    penta2 = models.DateTimeField(null=True)  # PENTA2 (10 WEEKS - 11 MONTHS)
    pcv2 = models.DateTimeField(null=True)  # PCV2 (10 WEEKS - 11 MONTHS)
    rota2 = models.DateTimeField(null=True)  # ROTA 2 (10 WEEKS - 11 MONTHS)
    opv3 = models.DateTimeField(null=True)  # OPV3 (14 WEEKS - 11 MONTHS)
    penta3 = models.DateTimeField(null=True)  # PENTA3 (14 WEEKS - 11 MONTHS)
    pcv3 = models.DateTimeField(null=True)  # PCV3 (14 WEEKS - 11 MONTHS)
    rota3 = models.DateTimeField(null=True)  # ROTA 3 (14 WEEKS - 11 MONTHS)
    ipv2 = models.DateTimeField(null=True)  # IPV2 (14 WEEKS - 11 MONTHS)
    malaria1 = models.DateTimeField(null=True)  # MALARIA 1 (5 - 11 MONTHS)
    malaria2 = models.DateTimeField(null=True)  # MALARIA 2 (6 - 12 MONTHS)
    vitamin_a_6_11 = models.DateTimeField(null=True)  # VITAMIN A (6 - 11 MONTHS - 100,000 IU)
    vitamin_a_12_23 = models.DateTimeField(null=True)  # VITAMIN A (12 - 23 MONTHS - 200,000 IU)
    malaria3 = models.DateTimeField(null=True)  # MALARIA 3 (7 - 13 MONTHS)
    mr1 = models.DateTimeField(null=True)  # MR 1 (9 - 11 MONTHS)
    yellow_fever = models.DateTimeField(null=True)  # YELLOW FEVER (9 - 11 MONTHS)
    men_a = models.DateTimeField(null=True)  # Men A (9 - 11 MONTHS)
    mr2 = models.DateTimeField(null=True)  # MR 2 (12 - 23 MONTHS)
    malaria4 = models.DateTimeField(null=True)  # MALARIA 4 (15 - 23 MONTHS)

    # Comments
    comments = models.TextField(blank=True, null=True)

    # Health officer details
    health_officer_name = models.CharField(max_length=255)  # Health officer full name
    health_officer_signature_date = models.DateField()  # Signature & date
    health_officer_phone = models.CharField(max_length=20)  # Phone number

    # Head of unit details
    head_of_unit_name = models.CharField(max_length=255)  # Head of unit full name
    head_of_unit_signature_date = models.DateField()  # Signature & date
    head_of_unit_phone = models.CharField(max_length=20)  # Phone number

    class Meta:
        verbose_name = "Child Immunization Tally"
        verbose_name_plural = "Child Immunization Tallies"

    def __str__(self):
        return f"{self.facility_name} - {self.date_of_visit}"