from urllib2 import urlopen
from json import load
from sf_health_inspection_classes import *

inspection_list = []

def load_inspection_data():
	#sf open data source: food health inspections in sf
	apiUrl = "https://data.sfgov.org/resource/sipz-fjte.json"

	#open url and assign to variable
	response = urlopen(apiUrl)
	json_obj = load(response)

	business_name = ""
	business_address = ""
	inspection_date = ""
	inspection_score = ""
	violation_description = ""
	risk_category = ""

# print json_obj
	for business in json_obj:
		if "business_name" in business:
			business_name = str(business['business_name'])
		if "business_address" in business:
			business_address = str(business['business_address'])
		if "inspection_date" in business:
			inspection_date = str(business['inspection_date'])
		if "inspection_score" in business:
			inspection_score = str(business['inspection_score'])
		if "violation_description" in business:
			violation_description = str(business['violation_description'])
		if "risk_category" in business:
			risk_category = str(business['risk_category'])

		new_inspection = HealthInspection(business_name=business_name, business_address=business_address, inspection_date=inspection_date, inspection_score=inspection_score,violation_description=violation_description, risk_category=risk_category)
		inspection_list.append(new_inspection)

		response.close()
		return inspection_list


def get_inspection_info_by_business(business_name):
		inspection_list_by_business = []
		for info in inspection_list:
			if info.business_name == business_name:
				inspection_list_by_business.append(info)
		return inspection_list_by_business

def get_business_name_list():
	business_name_list = []
	for info in inspection_list:
		business_name_list.append(info.business_name)		

	unique_set = set(business_name_list)
	new_list = list(unique_set)


def main():

	load_inspection_data()

	for info in inspection_list:
		print "business_name - " + info.business_name
		print "business_address - " + info.business_address
		print "inspection_date - " + info.inspection_date
		print "inspection_score - " + info.inspection_score
		print "violation_description - " + info.violation_description
		print "risk_category - " + info.risk_category

	print get_inspection_info_by_business(chowders)
	print get_business_name_list()

if __name__ == '__main__':
	main()