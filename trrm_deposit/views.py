from django.shortcuts import render


def home(request):
	return render(request, 'index.html')

def getPredictions(age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign):
	import pickle
	import numpy as np
	import os
	from django.conf import settings
	filename = os.path.join(settings.BASE_DIR, 'knn.sav')
	
	with open(filename, 'rb') as  fil:
		model = pickle.load(fil)
	
	
	classes_names = {'job': ['admin','blue-collar','entrepreneur','housemaid','management','retired',
	'self-employed','services','student','technician','unemployed','unknown'],
	 'marital': ['divorced', 'married', 'single'],
	 'education': ['primary', 'secondary', 'tertiary', 'unknown'],
	 'default': ['no', 'yes'],
	 'housing': ['no', 'yes'],
	 'loan': ['no', 'yes'],
	 'contact': ['cellular', 'telephone', 'unknown'],
	 'month': ['apr','aug','dec','feb','jan','jul','jun','mar','may','nov','oct'],
	 'y': ['no', 'yes']}

	job = classes_names['job'].index(job)
	marital = classes_names['marital'].index(marital)
	education = classes_names['education'].index(education)
	default = classes_names['default'].index(default)
	housing = classes_names['housing'].index(housing)
	loan = classes_names['loan'].index(loan)
	contact = classes_names['contact'].index(contact)
	month = classes_names['month'].index(month)

	client_info = np.array([age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign])
	client_info = np.expand_dims(client_info, axis=0)

	pred = model.predict(client_info)
	return classes_names['y'][pred[0]]

	
def result(request):
	age_at = request.GET['age']
	job_at = request.GET['job']
	marital_at = request.GET['marital']
	education_at = request.GET['education']
	default_at = request.GET['default']
	balance_at = request.GET['balance']
	housing_at = request.GET['housing']
	loan_at = request.GET['loan']
	contact_at = request.GET['contact']
	day_at = request.GET['day']
	month_at = request.GET['month']
	duration_at = request.GET['duration']
	campaign_at = request.GET['campaign']

	result = getPredictions(age_at, job_at, marital_at, education_at,default_at,
		balance_at,housing_at,loan_at,contact_at,day_at,month_at,duration_at,campaign_at)

	return render(request, 'result.html', {'result':result})