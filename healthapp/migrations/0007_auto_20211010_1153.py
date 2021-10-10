# Generated by Django 3.2.4 on 2021-10-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0006_alzheimers_disease_bio_pathologiest_breast_cancer_cancer_trachea_bronchi_lungs_chronic_kidney_diseas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes_P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(max_length=255, null=True)),
                ('glucose_level', models.CharField(max_length=255, null=True)),
                ('cholesterol', models.CharField(max_length=255, null=True)),
                ('glycated_hemoglobin', models.CharField(max_length=255, null=True)),
                ('insulin', models.CharField(max_length=255, null=True)),
                ('C_peptide', models.CharField(max_length=255, null=True)),
                ('dihydroceramides', models.CharField(max_length=255, null=True)),
                ('autoantibodie_decarboxylase', models.CharField(max_length=255, null=True)),
                ('C_reactive_protein', models.CharField(max_length=255, null=True)),
                ('natriuretic_peptide', models.CharField(max_length=255, null=True)),
                ('vitamin_D', models.CharField(max_length=255, null=True)),
                ('Uric_acid', models.CharField(max_length=255, null=True)),
                ('VOC', models.CharField(max_length=255, null=True)),
                ('userid', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stroke_P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(max_length=255, null=True)),
                ('platelet_count', models.CharField(max_length=255, null=True)),
                ('brain_natriuretic_peptide', models.CharField(max_length=255, null=True)),
                ('S100B_IL6', models.CharField(max_length=255, null=True)),
                ('linoleic_acid', models.CharField(max_length=255, null=True)),
                ('D_dimer', models.CharField(max_length=255, null=True)),
                ('fibrinogen_levels', models.CharField(max_length=255, null=True)),
                ('erythrocyte_sedimentation_rate', models.CharField(max_length=255, null=True)),
                ('Lp_PLA2', models.CharField(max_length=255, null=True)),
                ('C_reactive_protein', models.CharField(max_length=255, null=True)),
                ('P_selectin', models.CharField(max_length=255, null=True)),
                ('fibrinogen', models.CharField(max_length=255, null=True)),
                ('troponin', models.CharField(max_length=255, null=True)),
                ('glutamate', models.CharField(max_length=255, null=True)),
                ('GFAP', models.CharField(max_length=255, null=True)),
                ('NDKA', models.CharField(max_length=255, null=True)),
                ('MMP_9', models.CharField(max_length=255, null=True)),
                ('userid', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='C_peptide',
            new_name='BMI',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='C_reactive_protein',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='Uric_acid',
            new_name='albumin',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='VOC',
            new_name='bilirubin',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='autoantibodie_decarboxylase',
            new_name='blood_pressure',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='dihydroceramides',
            new_name='creatinine',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='glucose_level',
            new_name='d_dimer',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='glycated_hemoglobin',
            new_name='di_id',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='insulin',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='name_id',
            new_name='globulin',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='natriuretic_peptide',
            new_name='glucose',
        ),
        migrations.RenameField(
            model_name='diabetes',
            old_name='vitamin_D',
            new_name='hematocrit',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='C_reactive_protein',
            new_name='BMI',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='D_dimer',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='GFAP',
            new_name='albumin',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='Lp_PLA2',
            new_name='bicarbonate',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='MMP_9',
            new_name='bilirubin',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='NDKA',
            new_name='blood_pressure',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='P_selectin',
            new_name='calcium',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='S100B_IL6',
            new_name='cholesterol',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='brain_natriuretic_peptide',
            new_name='d_dimer',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='erythrocyte_sedimentation_rate',
            new_name='di_id',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='fibrinogen',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='fibrinogen_levels',
            new_name='globulin',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='glutamate',
            new_name='glucose',
        ),
        migrations.RenameField(
            model_name='stroke',
            old_name='linoleic_acid',
            new_name='hematocrit',
        ),
        migrations.RemoveField(
            model_name='stroke',
            name='name_id',
        ),
        migrations.RemoveField(
            model_name='stroke',
            name='troponin',
        ),
        migrations.AddField(
            model_name='diabetes',
            name='hemoglobin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diabetes',
            name='platelet_count',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diabetes',
            name='potassium',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diabetes',
            name='red_blood_cells',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diabetes',
            name='sodium',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diabetes',
            name='uric_acid',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='diabetes',
            name='white_blood_cells',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='lymphocytes',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='neutrophils',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='potassium',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='red_blood_cells',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='sodium',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='troponin_t',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='urea_nitrogen',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stroke',
            name='white_blood_cells',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
