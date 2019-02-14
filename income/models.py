from django.db import models


# Create your models here.
class Adult(models.Model):
    AGE_CHOICES = (
        ('Age', '5'),
        ('Age', '10'),
        ('Age', '15'),
        ('Age', '20'),
        ('Age', '25'),
        ('Age', '30'),
        ('Age', '35'),
        ('Age', '40'),
        ('Age', '45'),
        ('Age', '50'),
        ('Age', '55'),
        ('Age', '60'),
        ('Age', '65'),
        ('Age', '70'),
        ('Age', '75'),
        ('Age', '80'),
        ('Age', '85'),
        ('Age', '90'),
        ('Age', '95'),
        ('Age', '100'),       
        )
    age = models.CharField(max_length=2, choices=AGE_CHOICES)

    EDU_CHOICES = (
        ('Edu', '1st-4th'),
        ('Edu', '5th-6th'),
        ('Edu', '7th-8th'),
        ('Edu', '9th'),
        ('Edu', '10th'),
        ('Edu', '11th'),
        ('Edu', '12th'),
        ('Edu', 'HS-grad'),
        ('Edu', 'Some-college'),
        ('Edu', 'Assoc-voc'),
        ('Edu', 'Assoc-acdm'),
        ('Edu', 'Prof-school'),
        ('Edu', 'Bachelors'),
        ('Edu', 'Masters'),
        ('Edu', 'Doctorate'),
    )    
    education = models.CharField(max_length=12, choices=EDU_CHOICES)

    NUM_CHOICES = (
        ('Num', '1'),
        ('Num', '2'),
        ('Num', '3'),
        ('Num', '4'),
        ('Num', '5'),
        ('Num', '6'),
        ('Num', '7'),
        ('Num', '8'),
        ('Num', '9'),
        ('Num', '10'),
        ('Num', '11'),
        ('Num', '12'),
        ('Num', '13'),
        ('Num', '14'),
        ('Num', '15'),
        ('Num', '16'),
        ('Num', '17'),
        ('Num', '18'),
        ('Num', '19'),
        ('Num', '20'),
    )
    years_education = models.CharField(max_length=2, choices=NUM_CHOICES)

    STA_CHOICES = (
        ('Sta', 'Never-married'),
        ('Sta', 'Married-civ-spouse'),
        ('Sta', 'Married-AF-spouse'),
        ('Sta', 'Married-spouse-absent'),
        ('Sta', 'Separated'),
        ('Sta', 'Divorced'),
        ('Sta', 'Widowed'),
    )
    marital_status = models.CharField(max_length=21, choices=STA_CHOICES)

    OCC_CHOICES = (
        ('Occ', 'Adm-clerical'),
        ('Occ', 'Armed-Forces'),
        ('Occ', 'Craft-repair'),
        ('Occ', 'Exec-managerial'),
        ('Occ', 'Farming-fishing'),
        ('Occ', 'Handlers-cleaners'),
        ('Occ', 'Machine-op-inspct'),
        ('Occ', 'Priv-house-serv'),
        ('Occ', 'Prof-specialty'),
        ('Occ', 'Protective-serv'),
        ('Occ', 'Sales'),
        ('Occ', 'Tech-support'),
        ('Occ', 'Transport-moving'),
        ('Occ', 'Other-service'),
    )
    occupation = models.CharField(max_length=17, choices=OCC_CHOICES)

    REL_CHOICES = (
        ('Rel', 'Husband'),
        ('Rel', 'Wife'),
        ('Rel', 'Not-in-family'),
        ('Rel', 'Own-child'),
        ('Rel', 'Other-relative'),
        ('Rel', 'Unmarried'),
    )
    relationship = models.CharField(max_length=14, choices=REL_CHOICES)

    RAC_CHOICES = (
        ('Rac', 'White'),
        ('Rac', 'Black'),
        ('Rac', 'Asian-Pac-Islander'),
        ('Rac', 'Amer-Indian-Eskimo'),
        ('Rac', 'Other'),
    )
    race = models.CharField(max_length=19, choices=RAC_CHOICES)

    SEX_CHOICES = (
        ('Sex', 'Female'),
        ('Sex', 'Male'),
    )
    gender = models.CharField(max_length=6, choices=SEX_CHOICES)

    HRS_CHOICES = (
        ('Hrs', '5'),
        ('Hrs', '10'),
        ('Hrs', '15'),
        ('Hrs', '20'),
        ('Hrs', '25'),
        ('Hrs', '30'),
        ('Hrs', '35'),
        ('Hrs', '40'),
        ('Hrs', '45'),
        ('Hrs', '50'),
        ('Hrs', '55'),
        ('Hrs', '60'),
        ('Hrs', '65'),
        ('Hrs', '70'),
        ('Hrs', '75'),
        ('Hrs', '80'),
        ('Hrs', '85'),
        ('Hrs', '90'),
        ('Hrs', '95'),
        ('Hrs', '100'),

    )
    hours_per_week = models.CharField(max_length=2, choices=HRS_CHOICES)