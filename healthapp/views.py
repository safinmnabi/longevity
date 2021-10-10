from django.shortcuts import render
from rest_framework.decorators import api_view
from healthapp.serializers import BiodataSerializer, RisksSerializer, RecommendationsSerializer, SubscriptionsSerializer, RewardsSerializer, PaymentsSerializer, FilesSerializer, CSVSerializer, DiabetesSerializer, CVDSerializer, StrokeSerializer, Breast_cancerSerializer, Chronic_kidney_diseaseSerializer, Coronary_artery_diseaseSerializer, Alzheimers_diseaseSerializer, Stroke_P_Serializer, Cancer_trachea_bronchi_lungsSerializer, Lower_Respiratory_Tract_InfectionsSerializer, Colon_rectal_cancerSerializer, Kidney_diseaseSerializer, Hypertensive_heart_diseaseSerializer, Diabetes_P_Serializer, Chronic_obstructive_pulmonarySerializer, Stomach_cancerSerializer, Intestinal_infectionsSerializer, TuberculosisSerializer, Cirrhosis_liverSerializer, Parkinson_diseaseSerializer, HIV_AIDSSerializer, MalariaSerializer, Liver_cancerSerializer, Hepatitis_BSerializer, MeningitisSerializer, Risks_Recommendation_Model_Serializer
from rest_framework.response import Response
from healthapp.models import Biodata, Risks, Recommendaions, Subscriptions, Rewards, Payments, Files, CSV, Diabetes, CVD, Stroke, Breast_cancer, Chronic_kidney_disease, Coronary_artery_disease, Alzheimers_disease, Stroke_P, Cancer_trachea_bronchi_lungs, Lower_Respiratory_Tract_Infections, Colon_rectal_cancer, Kidney_disease, Hypertensive_heart_disease, Diabetes_P, Chronic_obstructive_pulmonary, Stomach_cancer, Intestinal_infections, Tuberculosis, Cirrhosis_liver, Parkinson_disease, HIV_AIDS, Malaria, Liver_cancer, Hepatitis_B, Meningitis, Risks_Recommendation_Model
import json, csv, os
from django.conf import settings

@api_view(['GET'])		
def index(request):
	if request.method == 'GET':		
		try:
			users = Biodata.objects.all()
			person_serializer = BiodataSerializer(users, many=True)
			return Response(person_serializer.data)
		except:
			return Response({"message":"no data found"})


@api_view(['POST'])
def createbiodata(request): 
	if request.method == 'POST':
		person_serializer = BiodataSerializer(data = request.data)
		if person_serializer.is_valid():
			person_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")

@api_view(['POST'])
def updatebiodata(request, id):
	users = Biodata.objects.get(id=id)
	recom_to_user = []
	BPF = 1
	weight = 0
	if request.method == 'POST':
		person_serializer = BiodataSerializer(users, data = request.data, many=False, partial=True)
		if person_serializer.is_valid():
			person_serializer.save()
			
			if 'weight' in request.POST:
				weight = int(request.data['weight'])
			

			if 'blood_pressure' in request.POST:
				blood_split = request.data['blood_pressure'].split("/")
				if (int(blood_split[0]) >= 90 and int(blood_split[1]) >= 60) and (int(blood_split[0]) <= 120 and int(blood_split[1]) <= 80):
					BPF = 1
				elif int(blood_split[0]) < 90 or int(blood_split[1]) < 60:
					BPF = 0
				elif int(blood_split[0]) > 120  or int(blood_split[1]) > 80:
					BPF = 2

			

			recom  =  fetch_recom()
			for x in range(len(recom)):
				if recom[x]['id'] == 1:
					if BPF == 0 or (weight < 50 and weight != 0):
						recom_to_user.append(recom[x]['recommdes'])
				elif recom[x]['id'] == 2:
					if weight < 50:
						recom_to_user.append(recom[x]['recommdes'])


				# print(recom[x])
			
			# return Response({"message":"success", "result":"true"})
			return Response({"message":recom_to_user,"BPF":BPF})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")


@api_view(['GET'])		
def risksindex(request):
	if request.method == 'GET':		
		try:
			users = Risks.objects.all()
			risk_serializer = RisksSerializer(users, many=True)
			return Response(risk_serializer.data)
		except:
			return Response({"message":"no data found"})

@api_view(['POST'])
def createrisk(request): 
	if request.method == 'POST':
		risk_serializer = RisksSerializer(data = request.data)
		if risk_serializer.is_valid():
			risk_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")


@api_view(['GET'])		
def recommindex(request):
	if request.method == 'GET':		
		return Response(fetch_recom())

def fetch_recom():
	try:
		users = Recommendaions.objects.all()
		print(users)
		risk_serializer = RecommendationsSerializer(users, many=True)
		return risk_serializer.data
	except:
		return {"message":"no data found"}

@api_view(['POST'])
def createrecomm(request): 
	if request.method == 'POST':
		risk_serializer = RecommendationsSerializer(data = request.data)
		if risk_serializer.is_valid():
			risk_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")

@api_view(['POST'])
def buysubscription(request, id):
	users = Subscriptions.objects.get(userid=id)
	if request.method == 'POST':
		sub_serializer = SubscriptionsSerializer(users,data = request.data, many=False, partial=True)
		if sub_serializer.is_valid():
			sub_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")


@api_view(['GET'])		
def fetch_subpack(request):
	if request.method == 'GET':
		try:
			users = Subscriptions.objects.filter(userid='james')
			# users = Subscriptions.objects.get()
			print(users)
			sub_serializer = SubscriptionsSerializer(users, many=True)
			return Response(sub_serializer.data)
		except:
			return Response({"message":"no data found"}) 
	else:
		return Response("wrong method")

@api_view(['POST'])
def createpack(request): 
	if request.method == 'POST':
		pack_serializer = SubscriptionsSerializer(data = request.data)
		if pack_serializer.is_valid():
			pack_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")

@api_view(['DELETE'])
def delete(request, id):
	users = Subscriptions.objects.get(id=id)
	users.delete()
	return Response("Delete succes")


@api_view(['POST'])
def rewards(request):	
	if request.method == 'POST':
		reward_serializer = RewardsSerializer(data = request.data)
		if reward_serializer.is_valid():
			reward_serializer.save()
			pid = reward_serializer.data['userid']
			aid = reward_serializer.data['r_amt']
			users = Subscriptions.objects.get(userid=pid)
			sub_sez = SubscriptionsSerializer(users, many=False)
			userid_sub = sub_sez.data['id']
			userid_amt = sub_sez.data['long_coin']
			tl = int(userid_amt) + int(aid)
			user_update = Subscriptions(id = userid_sub,  userid = pid, long_coin=tl, pack_name = sub_sez.data['pack_name'],  pack_exp = sub_sez.data['pack_exp'], cost_per_recom = sub_sez.data['cost_per_recom'])
			user_update.save()
			print(user_update)

			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")
	

@api_view(['GET'])		
def fetch_reward(request):
	if request.method == 'GET':
		try:
			users = Rewards.objects.filter(userid='james')
			print(users)
			sub_serializer = RewardsSerializer(users, many=True)
			return Response(sub_serializer.data)
		except:
			return Response({"message":"no data found"}) 
	else:
		return Response("wrong method")

@api_view(['GET'])		
def fetch_pay(request):
	if request.method == 'GET':
		try:
			users = Payments.objects.filter(userid='james')
			print(users)
			pay_serializer = PaymentsSerializer(users, many=True)
			return Response(pay_serializer.data)
		except:
			return Response({"message":"no data found"}) 
	else:
		return Response("wrong method")

@api_view(['POST'])
def payments(request):	
	if request.method == 'POST':
		pay_serializer = PaymentsSerializer(data = request.data)
		if pay_serializer.is_valid():
			pay_serializer.save()
			pid = pay_serializer.data['userid']
			aid = pay_serializer.data['p_amt']
			users = Subscriptions.objects.get(userid=pid)
			sub_sez = SubscriptionsSerializer(users, many=False)
			userid_sub = sub_sez.data['id']
			userid_amt = sub_sez.data['long_coin']
			tl = int(userid_amt) - int(aid)
			user_update = Subscriptions(id = userid_sub,  userid = pid, long_coin=tl, pack_name = sub_sez.data['pack_name'],  pack_exp = sub_sez.data['pack_exp'], cost_per_recom = sub_sez.data['cost_per_recom'])
			user_update.save()

			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response("wrong method")


@api_view(['POST'])
def filepost(request):
	file_serializer = FilesSerializer(data = request.data)
	if file_serializer.is_valid():
		file_serializer.save()
		return Response({"message":"success", "result":"true"})
	else:
		return Response({"message":"failed", "result":"false"})



@api_view(['GET'])
def filelist(request):
	if request.method == 'GET':		
		try:
			users = Files.objects.all()
			file_serializer = FilesSerializer(users, many=True)
			return Response(file_serializer.data)
		except:
			return Response({"message":"no data found"})

def run():
	# text = open(os.path.join(settings.MEDIA_ROOT, 'new.csv'), 'rb')
	with open(os.path.join(settings.MEDIA_ROOT, 'new.csv')) as f:
		reader = csv.reader(f)
		for row in reader:
			# print(row[0])
			CSV.objects.create(name = row[0], age = row[1])
# run()

@api_view(['GET'])
def getcsv(request):
	if request.method == 'GET':		
		try:
			users = CSV.objects.all()
			csv_serializer = CSVSerializer(users, many=True)
			return Response(csv_serializer.data)
		except:
			return Response({"message":"no data found"})


 # --------------------------------------------Disease Model----------------------------------#

@api_view(['POST'])
def dismod(request, did):

	if did == 'Diabetes':
		dia_serializer = DiabetesSerializer(data = request.data)
		if dia_serializer.is_valid():
			dia_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'CVD':
		cvd_serializer = CVDSerializer(data = request.data)
		if cvd_serializer.is_valid():
			cvd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	if did == 'Stroke':
		str_serializer = StrokeSerializer(data = request.data)
		if str_serializer.is_valid():
			str_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'BreastCancer':
		bre_serializer = Breast_cancerSerializer(data = request.data)
		if bre_serializer.is_valid():
			bre_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'CKD':
		ckd_serializer = Chronic_kidney_diseaseSerializer(data = request.data)
		if ckd_serializer.is_valid():
			ckd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response({"messgae": "Not found disease in DB"})


@api_view(['GET'])
def getdismod(request, did, uid):
	if request.method == 'GET':		
		if did == 'Diabetes' :
			dusers = Diabetes.objects.filter(userid=uid)
			dia_serializer = DiabetesSerializer(dusers, many=True)
			return Response(dia_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'CVD' :
			cusers = CVD.objects.filter(userid=uid)
			cvd_serializer = CVDSerializer(cusers, many=True)
			return Response(cvd_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Stroke' :
			susers = Stroke.objects.filter(userid=uid)
			str_serializer = StrokeSerializer(susers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'BreastCancer' :
			busers = Breast_cancer.objects.filter(userid=uid)
			str_serializer = Breast_cancerSerializer(busers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'CKD' :
			ckusers = Chronic_kidney_disease.objects.filter(userid=uid)
			str_serializer = Chronic_kidney_diseaseSerializer(ckusers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})

 # --------------------------------------------Disease Pathology Model----------------------------------#

@api_view(['POST'])
def postpathology(request, did):

	if did == 'Coronary_artery':
		dia_serializer = Coronary_artery_diseaseSerializer(data = request.data)
		if dia_serializer.is_valid():
			dia_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Alzheimers_disease':
		cvd_serializer = Alzheimers_diseaseSerializer(data = request.data)
		if cvd_serializer.is_valid():
			cvd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	if did == 'Stroke_P':
		str_serializer = Stroke_P_Serializer(data = request.data)
		if str_serializer.is_valid():
			str_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Cancer_trachea_bronchi_lungs':
		bre_serializer = Cancer_trachea_bronchi_lungsSerializer(data = request.data)
		if bre_serializer.is_valid():
			bre_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Lower_Respiratory_Tract_Infections':
		ckd_serializer = Lower_Respiratory_Tract_InfectionsSerializer(data = request.data)
		if ckd_serializer.is_valid():
			ckd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Colon_rectal_cancer':
		dia_serializer = Colon_rectal_cancerSerializer(data = request.data)
		if dia_serializer.is_valid():
			dia_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Kidney_disease':
		cvd_serializer = Kidney_diseaseSerializer(data = request.data)
		if cvd_serializer.is_valid():
			cvd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	if did == 'Hypertensive_heart_disease':
		str_serializer = Hypertensive_heart_diseaseSerializer(data = request.data)
		if str_serializer.is_valid():
			str_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Diabetes_P':
		bre_serializer = Diabetes_P_Serializer(data = request.data)
		if bre_serializer.is_valid():
			bre_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Chronic_obstructive_pulmonary':
		ckd_serializer = Chronic_obstructive_pulmonarySerializer(data = request.data)
		if ckd_serializer.is_valid():
			ckd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	if did == 'Stomach_cancer':
		dia_serializer = Stomach_cancerSerializer(data = request.data)
		if dia_serializer.is_valid():
			dia_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Intestinal_infections':
		cvd_serializer = Intestinal_infectionsSerializer(data = request.data)
		if cvd_serializer.is_valid():
			cvd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	if did == 'Tuberculosis':
		str_serializer = TuberculosisSerializer(data = request.data)
		if str_serializer.is_valid():
			str_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Cirrhosis_liver':
		bre_serializer = Cirrhosis_liverSerializer(data = request.data)
		if bre_serializer.is_valid():
			bre_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Parkinson_disease':
		ckd_serializer = Parkinson_diseaseSerializer(data = request.data)
		if ckd_serializer.is_valid():
			ckd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'HIV_AIDS':
		dia_serializer = HIV_AIDSSerializer(data = request.data)
		if dia_serializer.is_valid():
			dia_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Malaria':
		cvd_serializer = MalariaSerializer(data = request.data)
		if cvd_serializer.is_valid():
			cvd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	if did == 'Liver_cancer':
		str_serializer = Liver_cancerSerializer(data = request.data)
		if str_serializer.is_valid():
			str_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Hepatitis_B':
		bre_serializer = Hepatitis_BSerializer(data = request.data)
		if bre_serializer.is_valid():
			bre_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})

	if did == 'Meningitis':
		ckd_serializer = MeningitisSerializer(data = request.data)
		if ckd_serializer.is_valid():
			ckd_serializer.save()
			return Response({"message":"success", "result":"true"})
		else:
			return Response({"message":"failed", "result":"false"})
	else:
		return Response({"messgae": "Not found disease in DB"})


@api_view(['GET'])
def getpathology(request, did, uid):
	if request.method == 'GET':		
		if did == 'Coronary_artery' :
			dusers = Coronary_artery_disease.objects.filter(userid=uid)
			dia_serializer = Coronary_artery_diseaseSerializer(dusers, many=True)
			return Response(dia_serializer.data)

		if did == 'Alzheimers_disease' :
			cusers = Alzheimers_disease.objects.filter(userid=uid)
			cvd_serializer = Alzheimers_diseaseSerializer(cusers, many=True)
			return Response(cvd_serializer.data)


		if did == 'Stroke_P' :
			susers = Stroke_P.objects.filter(userid=uid)
			str_serializer = Stroke_P_Serializer(susers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Cancer_trachea_bronchi_lungs' :
			busers = Cancer_trachea_bronchi_lungs.objects.filter(userid=uid)
			str_serializer = Cancer_trachea_bronchi_lungsSerializer(busers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Lower_Respiratory_Tract_Infections' :
			ckusers = Lower_Respiratory_Tract_Infections.objects.filter(userid=uid)
			str_serializer = Lower_Respiratory_Tract_InfectionsSerializer(ckusers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Colon_rectal_cancer' :
			dusers = Colon_rectal_cancer.objects.filter(userid=uid)
			dia_serializer = Colon_rectal_cancerSerializer(dusers, many=True)
			return Response(dia_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Kidney_disease' :
			cusers = Kidney_disease.objects.filter(userid=uid)
			cvd_serializer = Kidney_diseaseSerializer(cusers, many=True)
			return Response(cvd_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Hypertensive_heart_disease' :
			susers = Hypertensive_heart_disease.objects.filter(userid=uid)
			str_serializer = Hypertensive_heart_diseaseSerializer(susers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Diabetes_P' :
			busers = Diabetes_P.objects.filter(userid=uid)
			str_serializer = Diabetes_P_Serializer(busers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Chronic_obstructive_pulmonary' :
			ckusers = Chronic_obstructive_pulmonary.objects.filter(userid=uid)
			str_serializer = Chronic_obstructive_pulmonarySerializer(ckusers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Stomach_cancer' :
			dusers = Stomach_cancer.objects.filter(userid=uid)
			dia_serializer = Stomach_cancerSerializer(dusers, many=True)
			return Response(dia_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Intestinal_infections' :
			cusers = Intestinal_infections.objects.filter(userid=uid)
			cvd_serializer = Intestinal_infectionsSerializer(cusers, many=True)
			return Response(cvd_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Tuberculosis' :
			susers = Tuberculosis.objects.filter(userid=uid)
			str_serializer = TuberculosisSerializer(susers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Cirrhosis_liver' :
			busers = Cirrhosis_liver.objects.filter(userid=uid)
			str_serializer = Cirrhosis_liverSerializer(busers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Parkinson_disease' :
			ckusers = Parkinson_disease.objects.filter(userid=uid)
			str_serializer = Parkinson_diseaseSerializer(ckusers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'HIV_AIDS' :
			dusers = HIV_AIDS.objects.filter(userid=uid)
			dia_serializer = HIV_AIDSSerializer(dusers, many=True)
			return Response(dia_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Malaria' :
			cusers = Malaria.objects.filter(userid=uid)
			cvd_serializer = MalariaSerializer(cusers, many=True)
			return Response(cvd_serializer.data)
		else:
			return Response({"message":"no data found"})

		if did == 'Liver_cancer' :
			susers = Liver_cancer.objects.filter(userid=uid)
			str_serializer = Liver_cancerSerializer(susers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'BreastCaHepatitis_Bncer' :
			busers = Hepatitis_B.objects.filter(userid=uid)
			str_serializer = Hepatitis_BSerializer(busers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})
		if did == 'Meningitis' :
			ckusers = Meningitis.objects.filter(userid=uid)
			str_serializer = MeningitisSerializer(ckusers, many=True)
			return Response(str_serializer.data)
		else:
			return Response({"message":"no data found"})

@api_view(['DELETE'])
def deletep(request, id):
	users = Alzheimers_disease.objects.get(id=id)
	users.delete()
	return Response("Delete succes")