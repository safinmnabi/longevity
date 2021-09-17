from django.shortcuts import render
from rest_framework.decorators import api_view
from healthapp.serializers import BiodataSerializer, RisksSerializer, RecommendationsSerializer
from rest_framework.response import Response
from healthapp.models import Biodata, Risks, Recommendaions
import json

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
			
			if 'wight' in request.POST:
				weight = int(request.data['wight'])
			

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