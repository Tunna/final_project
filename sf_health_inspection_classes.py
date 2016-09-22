class HealthInspection(object):
	def __init__(self, business_name="", business_address="", inspection_date="", inspection_score="", violation_description="", risk_category=""):
		self.business_name = business_name
		self.business_address = business_address 
		self.inspection_date = inspection_date
		self.inspection_score = inspection_score 
		self.violation_description = violation_description
		self.risk_category = risk_category

