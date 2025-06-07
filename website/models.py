# models.py in your 'website' app

from django.db import models


class Category(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	def __str__(self):
		return(f"{self.name} ")
class State(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	def __str__(self):
		return(f"{self.name} ")

class DataSource(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.name} ")



class State(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.name} ")

class FundingAgent(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.name} ")

class CommodityList(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.name} ")


class KeyActivities(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return(f"{self.name} ")
class ThematicArea(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.name} ")



class StateImplementingPartner(models.Model):
    state = models.CharField(max_length=100)
    funding_agent = models.CharField(max_length=100)
    thematic_area = models.CharField(max_length=100)
    key_activities = models.TextField()
    actual_implementation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for last update
    is_deleted = models.BooleanField(default=False)        # Soft delete flag

class StateCostImplementationPlan(models.Model):
    state = models.CharField(max_length=100)
    funding_agent = models.CharField(max_length=100)
    thematic_area = models.CharField(max_length=100)
    data_source = models.CharField(max_length=100)
    key_activities = models.TextField()
    costed_in_state_plan = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for last update
    is_deleted = models.BooleanField(default=False)        # Soft delete flag

class StateBudget(models.Model):
    state = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    budget_line_item = models.CharField(max_length=100)
    state_fp_budget = models.DecimalField(max_digits=10, decimal_places=2)
    state_fp_release = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    total_state_health_budget = models.DecimalField(max_digits=10, decimal_places=2)
    percent_srh_budget = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for last update
    is_deleted = models.BooleanField(default=False)        # Soft delete flag
    
class StateFPCommodity(models.Model):
    state = models.CharField(max_length=100)
    name = models.CharField(max_length=100)  # Name of the commodity
    funding_required = models.DecimalField(max_digits=10, decimal_places=2)  # Total funding required
    funding_commitment = models.DecimalField(max_digits=10, decimal_places=2)  # Amount committed for funding
    fund_disbursed = models.DecimalField(max_digits=10, decimal_places=2)  # Amount disbursed
    donor_agency = models.CharField(max_length=100)  # Name of the donor agency
    year = models.IntegerField()  # Year of the funding requirement
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for last update
    is_deleted = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.name} - Year: {self.year} - Donor: {self.donor_agency}"
    
class StateCommodityMix(models.Model):
    state = models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    name = models.CharField(max_length=100)  # Name of the commodity
       # funding_required = models.DecimalField(max_digits=10, decimal_places=2)  # Total funding required
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount committed for funding
    amount1 = models.DecimalField(max_digits=10, decimal_places=2)  # Amount disbursed
        
    year = models.IntegerField()  # Year of the funding requirement
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for last update
    is_deleted = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.name} - Year: {self.year} - Amount: {self.amount} -Category {self.category}"
    
class ContraceptiveStatistics(models.Model):
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
    state = models.CharField(max_length=100)
    year = models.PositiveIntegerField(unique=True)
    women_receiving_contraceptive_care = models.PositiveIntegerField()
    unintended_pregnancies_averted = models.PositiveIntegerField()
    unplanned_births_averted = models.PositiveIntegerField()
    unsafe_abortions_averted = models.PositiveIntegerField()
    is_deleted = models.BooleanField(default=False)  
    def __str__(self):
        return f"Statistics for {self.year}"
    
    

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
    
    SYPHILIS_TESTING_CHOICES = [
        ('Not Done', 'Not Done'),
        ('Negative', 'Negative'),
        ('Positive', 'Positive'),
        ('Treated', 'Treated'),
    ]

    hepatitis_b_choices = [
        ('Not Done', 'Not Done'),
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Referred', 'Referred out for treatment'),
    ]

    hepatitis_c_choices = [
        ('Not Done', 'Not Done'),
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Referred', 'Referred out for treatment'),
    ]

    hematology_choices = [
        ('HB/PCV', 'HB/PCV (in g/dl or %)'),
        ('Sugar', 'Sugar (Gestational Diabetes)'),
    ]

    urinalysis_choices = [
        ('Proteins', 'Proteins'),
        ('Sugar', 'Sugar'),
    ]

    haematinics_given_choices = [
        ('IFAS', 'Iron and Folic Acid Supplement (IFAS)'),
        ('MMS', 'Multiple Micronutrient Supplement (MMS)'),
    ]

    syphilis_testing_result = models.CharField(max_length=20, choices=SYPHILIS_TESTING_CHOICES, blank=True, null=True)
    hepatitis_b_result = models.CharField(max_length=20, choices=hepatitis_b_choices, blank=True, null=True)
    hepatitis_c_result = models.CharField(max_length=20, choices=hepatitis_c_choices, blank=True, null=True)
    haematology_test_result = models.CharField(max_length=20, choices=hematology_choices, blank=True, null=True)
    urinalysis_result = models.CharField(max_length=20, choices=urinalysis_choices, blank=True, null=True)
    haematinics_given = models.CharField(max_length=20, choices=haematinics_given_choices, blank=True, null=True)
    IPT_CHOICES = [
        ('IPT1', 'IPT 1'),
        ('IPT2', 'IPT 2'),
        ('IPT3', 'IPT 3'),
        ('IPT4', 'IPT ≥4'),
    ]

    doses_of_IPT_given = models.CharField(max_length=5, choices=IPT_CHOICES, blank=True, null=True)

    tetanus_diphtheria = models.CharField(max_length=10)  # Td1, Td2, etc.
    itn_given = models.BooleanField(default=False)  # ITN given during ANC visit
    associated_problems = models.TextField(blank=True, null=True)  # Associated problems
    outcome_of_visit = models.TextField(blank=True, null=True)  # Outcome of visit 

    def __str__(self):
        return f"{self.client_name} - {self.date}"

class Uterotonic(models.Model):
    name = models.CharField(max_length=50)

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
    AGE_CHOICES = [
        ('10-14', '10 - 14 years'),
        ('15-19', '15 - 19 years'),
        ('20-24', '20 - 24 years'),
        ('25-35', '25 - 35 years'),
        ('36-49', '36 - 49 years'),
        ('50+', '≥ 50 years'),
    ]

    age_group = models.CharField(max_length=5, choices=AGE_CHOICES, blank=True, null=True)

    type_of_client = models.CharField(max_length=50)  # Booked/Unbooked
    DECISION_TIME_CHOICES = [
        ('<24hrs', '< 24 hours'),
        ('≥24hrs', '≥ 24 hours'),
    ]

    time_taken_on_decision = models.CharField(max_length=10, choices=DECISION_TIME_CHOICES, blank=True, null=True)
    
    Labour_monitoring_options = [
        ('Partograph Used', 'Partograph Used'),
        ('Labour Care Guide Use', 'Labour Care Guide Use'),
       
    ]

    
    incoming_referral = models.CharField(max_length=50)  # Referral source
    parity = models.IntegerField()  # Number of pregnancies beyond 28 weeks
    delivery_date = models.DateField()  # Date of delivery
    delivery_mode = models.CharField(max_length=20)  # SVD, CS, AD, etc.

    labour_monitoring = models.CharField(max_length=200, choices=Labour_monitoring_options, blank=True, null=True)
   
    # 19a. Pregnant women given an uterotonic
    uterotonic_given = models.BooleanField(default=False)  # True for Yes, False for No
    oxytocin_given = models.BooleanField(default=False)
    misoprostol_given = models.BooleanField(default=False)
    heat_stable_carbetocin_given = models.BooleanField(default=False)

    # Uterotonic administered
    maternal_complication = models.CharField(max_length=50, blank=True, null=True)  # Complications seen
    blood_loss_measurement_mls = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
   #Management of Postpartum Haemorrhage	
	#blood_loss_measurement_mls = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # E-MOTIVE Provided
    e_motive_provided = models.BooleanField(default=False)


    # a. Post abortion care provided
    post_abortion_care_provided = models.BooleanField(default=False)

    # b. Admitted (using codes)
    admission_reason = models.CharField(max_length=100, blank=True, null=True)

    # c. Pregnant woman admitted with Eclampsia received MgSO4
    eclampsia_mgso4_provided = models.BooleanField(default=False)

    # d. Discharged (write date if Yes)
    discharge_date = models.DateField(blank=True, null=True)

    # e. Counselled on Exclusive Breast Feeding
    exclusive_breastfeeding_counselled = models.BooleanField(default=False)

    # f. Counselled on Postpartum Family Planning - PPFP
    ppfp_counselled = models.BooleanField(default=False)

    # g. Accepted PPFP (indicate method using codes)
    accepted_ppfp_method = models.CharField(max_length=100, blank=True, null=True)

    # h. Referred out (write reasons)
    referral_reason = models.TextField(blank=True, null=True)
    TRANSPORT_CHOICES = [
        ('Vehicle', 'Vehicle'),
        ('Ambulance', 'Ambulance'),
        ('Others', 'Others'),
    ]

    
    means_of_transport_in = models.CharField(max_length=20, choices=TRANSPORT_CHOICES, blank=True, null=True)

    # 23. Mother Dead
    mother_dead = models.BooleanField(default=False)

    # Audit Status
    maternal_death_audit_conducted = models.BooleanField(default=False)
    maternal_death_audit_not_conducted = models.BooleanField(default=False)


     # Induced Abortion
    induced_abortion = models.BooleanField(default=False)

    # Spontaneous Abortion
    spontaneous_abortion = models.BooleanField(default=False)

    # Time of birth/delivery
    time_of_birth = models.TimeField(null=True, blank=True)

    # Sex of Baby
    sex_of_baby = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)

    # Live Baby Weight
    

    
    stillbirth = models.BooleanField(default=False)

     # Live Birth Weight
    live_baby_weight = [
        ('<1.0 Kg', '< 1.0 Kg'),
        ('1.0-1.5 Kg', '1.0 - < 1.5 Kg'),
        ('1.5-2.5 Kg', '1.5 - < 2.5 Kg'),
        ('≥2.5 Kg', '≥ 2.5 Kg'),
    ]
    live_birth_weight = models.CharField(max_length=10, choices=live_baby_weight, blank=True, null=True)

    still_birth = models.BooleanField(default=False)  # Stillbirth indicator
    
    still_birth_status = models.CharField(max_length=255)

     # Pre-term Birth
    PRE_TERM_CHOICES = [
        ('<28 weeks', '< 28 weeks'),
        ('28-32 weeks', '28 - < 32 weeks'),
        ('32-34 weeks', '32 - < 34 weeks'),
        ('34-37 weeks', '34 - < 37 weeks'),
    ]
    pre_term = models.CharField(max_length=15, choices=PRE_TERM_CHOICES, blank=True, null=True)

    admitted_to_kmc = models.BooleanField(default=False)

    # g. Birth Asphyxia
    birth_asphyxia = models.CharField(max_length=2, choices=[
        ('NB', 'Not Breathing'),
        ('NC', 'Not Crying'),
    ], blank=True, null=True)

    # h. Not Breathing at Birth successfully resuscitated
    resuscitated_with_ambu_bag = models.BooleanField(default=False)

    # i. Live Births by HIV positive women only
    live_births_hiv_positive = models.BooleanField(default=False)

    # j. Referred - out (write reasons for referral)
    referral_reason = models.TextField(blank=True, null=True)

     # k. Early neonatal death
    early_neonatal_death = models.BooleanField(default=False)

    # a. Time cord was clamped
    time_cord_clamped = models.TimeField(null=True, blank=True)

    # b. 4% CHX gel is applied to cord at birth
    chx_gel_applied = models.BooleanField(default=False)

    skin_to_skin_care_time = models.CharField(max_length=50, choices=[
        ('within_1_hour', 'Within 1 Hour'),
        ('after_1_hour', 'After 1 Hour'),
    ], blank=True, null=True)

    # Temperature at 1 Hour
    temperature_at_1_hour = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Baby is put to breast
    breastfeeding_initiation_time = models.CharField(max_length=50, choices=[
        ('within_1_hour', 'Initiation of breastfeeding within 1 hour'),
        ('after_1_hour', 'Initiation of breastfeeding after 1 hour'),
    ], blank=True, null=True)

    # Delivery taken by Skilled Birth Attendant
    delivery_skilled_birth_attendant = models.CharField(max_length=50, choices=[
        ('SBA: Doctor, Midwife or Nurse, MLSS-trained CHEW', 'SBA: Doctor, Midwife or Nurse, MLSS-trained CHEW'),
        ('Others', 'others'),
    ], blank=True, null=True)
   
    # Additional fields for outcomes and management
    # 28. Name of Person who took the delivery
    name_of_delivery_attendant = models.CharField(max_length=100, blank=True, null=True)
   
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
    date_of_visit = models.DateTimeField()  # Changed to DateTimeField
    client_name = models.CharField(max_length=255)  # Name of the child
    card_number = models.CharField(max_length=50)  # ANC Card Number
    sex = models.CharField(max_length=6)  # Male/Female
    follow_up_address = models.TextField(blank=True, null=True)  # Follow-up address
    phone_number = models.CharField(max_length=20)  # Phone number
    date_of_birth = models.DateTimeField()  # Changed to DateTimeField

    # Vaccine dates
    hep_b_screening_0_24_hours = models.BooleanField(default=False)
    hep_b_screening_above_24_hours = models.BooleanField(default=False)
    opv_0_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    bcg_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    opv_1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    penta1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    pcv1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    rota_1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    ipv_1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    opv_2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    penta2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    pcv2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    rota_2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    opv_3_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    penta3_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    pcv3_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    rota_3_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    ipv_2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    malaria_1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    malaria_2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    vitamin_a_1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    malaria_3_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    mr_1_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    yellow_fever_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    men_a_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    mr_2_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    malaria_4_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField
    itn_given = models.BooleanField(default=False)  # ITN given
    comments = models.TextField(blank=True, null=True)  # Comments

    def __str__(self):
        return f"{self.client_name} - {self.date_of_visit}"