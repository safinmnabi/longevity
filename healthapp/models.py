from django.db import models

class Biodata(models.Model):
	userid = models.CharField(max_length=255, null=True)
	sex = models.CharField(max_length=255, null=True)
	nationality = models.CharField(max_length=255, null=True)
	height = models.CharField(max_length=255, null=True)
	wight = models.CharField(max_length=255, null=True)
	hip_circumference = models.CharField(max_length=255, null=True)
	waist = models.CharField(max_length=255, null=True)
	wrist_circumference = models.CharField(max_length=255, null=True)
	blood_pressure = models.CharField(max_length=255, null=True)
	heart_rate_variability = models.CharField(max_length=255, null=True)
	heart_rate_alone = models.CharField(max_length=255, null=True)
	vo2max = models.CharField(max_length=255, null=True)
	body_temparature = models.CharField(max_length=255, null=True)
	common_diseases = models.CharField(max_length=255, null=True)
	blood_glucose_level = models.CharField(max_length=255, null=True)
	movement_sleep_pattern = models.CharField(max_length=255, null=True)
	libido = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.nationality
class Risks(models.Model):
	riskdes = models.TextField()

	def __str__(self):
		return self.riskdes

class Recommendaions(models.Model):
	recommdes = models.TextField()

	def __str__(self):
		return self.recommdes