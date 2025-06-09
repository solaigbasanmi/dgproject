from datetime import datetime, timedelta
from calendar import monthrange
from collections import defaultdict
import logging

logger = logging.getLogger('myapp')

class ChildImmunizationTally:
    """
    Computed immunization tally (not a Django model)
    """
    def __init__(self, month_year_str):
        self.month_year_str = month_year_str
        self.start_date, self.end_date = self._parse_month_year(month_year_str)
        self.daily_counts = defaultdict(dict)
        self.monthly_totals = defaultdict(int)
    
    def _parse_month_year(self, month_year_str):
        """Parse MM-YYYY format and return first/last day of month"""
        try:
            month, year = map(int, month_year_str.split('-'))
            _, last_day = monthrange(year, month)
            start_date = datetime(year, month, 1).date()
            end_date = datetime(year, month, last_day).date()
            return start_date, end_date
        except (ValueError, IndexError) as e:
            logger.error(f"Error parsing month/year: {e}")
            raise ValueError("Invalid date format. Expected 'MM-YYYY'")

    @classmethod
    def generate(cls, month_year_str):
        """
        Factory method to generate computed tallies for each day in the month
        """
        from .models import ChildImmunizationRegister  # Import your actual register model
        
        tally = cls(month_year_str)
        
        # Get all register entries for the month
        register_entries = ChildImmunizationRegister.objects.filter(
            created_at__date__range=(tally.start_date, tally.end_date)
        )

        # Define all immunization fields to track
        IMMUNIZATION_FIELDS = [
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
        ]

        # List to hold daily tallies
        daily_tallies = []

        # Calculate counts for each day in the month
        current_date = tally.start_date
        while current_date <= tally.end_date:
            date_str = current_date.strftime('%d-%m-%Y')
            
            # Get entries for this specific day
            day_entries = register_entries.filter(created_at__date=current_date)
            
            # Create a new tally for the current day
            daily_tally = ChildImmunizationTally(month_year_str)
            
            # Count each immunization type for this day
            for field in IMMUNIZATION_FIELDS:
                count = day_entries.filter(**{f"{field}__isnull": False}).count()
                daily_tally.daily_counts[date_str][field] = count
                daily_tally.monthly_totals[field] += count
            
            # Append the daily tally to the list
            daily_tallies.append(daily_tally)
            
            # Move to the next day
            current_date += timedelta(days=1)

        return daily_tallies

    def get_monthly_total(self, field_name):
        """Get total count for a specific immunization type"""
        return self.monthly_totals.get(field_name, 0)

    def get_daily_count(self, date_str, field_name):
        """Get count for a specific day and immunization type"""
        return self.daily_counts.get(date_str, {}).get(field_name, 0)