from rest_framework import serializers
from . import models

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biodata
        fields = '__all__'

class RisksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Risks
        fields = '__all__'

class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recommendaions
        fields = '__all__'

class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriptions
        fields = '__all__'

class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rewards
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payments
        fields = '__all__'

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Files
        fields = '__all__'

class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CSV
        fields = '__all__'

class DiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diabetes
        fields = '__all__'

class CVDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CVD
        fields = '__all__'

class StrokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stroke
        fields = '__all__'

class Breast_cancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breast_cancer
        fields = '__all__'

class Chronic_kidney_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chronic_kidney_disease
        fields = '__all__'




class Coronary_artery_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coronary_artery_disease
        fields = '__all__'

class Alzheimers_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alzheimers_disease
        fields = '__all__'

class Stroke_P_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stroke_P
        fields = '__all__'


class Cancer_trachea_bronchi_lungsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cancer_trachea_bronchi_lungs
        fields = '__all__'

class Lower_Respiratory_Tract_InfectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lower_Respiratory_Tract_Infections
        fields = '__all__'


class Colon_rectal_cancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Colon_rectal_cancer
        fields = '__all__'

class Kidney_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kidney_disease
        fields = '__all__'

class Hypertensive_heart_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hypertensive_heart_disease
        fields = '__all__'


class Diabetes_P_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diabetes_P
        fields = '__all__'

class Chronic_obstructive_pulmonarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chronic_obstructive_pulmonary
        fields = '__all__'





class Stomach_cancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stomach_cancer
        fields = '__all__'

class Intestinal_infectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Intestinal_infections
        fields = '__all__'

class TuberculosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tuberculosis
        fields = '__all__'


class Cirrhosis_liverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cirrhosis_liver
        fields = '__all__'

class Parkinson_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parkinson_disease
        fields = '__all__'


class HIV_AIDSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HIV_AIDS
        fields = '__all__'

class MalariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Malaria
        fields = '__all__'

class Liver_cancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Liver_cancer
        fields = '__all__'


class Hepatitis_BSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hepatitis_B
        fields = '__all__'

class MeningitisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meningitis
        fields = '__all__'
