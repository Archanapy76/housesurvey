from django.db import models



class  Avilabe_data(models.Model):
    new_wardno =models.IntegerField()
    new_doorno = models.IntegerField()
    new_subno =models.CharField(max_length=10)
    owner_address =models.CharField(max_length=200)
    floor_area =models.CharField(max_length=50)
    buliding_usage = models.CharField(max_length=50)
    zone =models.CharField(max_length=50)
    road_type =models.CharField(max_length=50)
    road_name = models.CharField(max_length=50)
    buliding_age =models.CharField(max_length=25)
    roof_details = models.CharField(max_length=200)
    floor_details =models.CharField(max_length=200)
    Ac=models.CharField(max_length=20,null=True)
    modification= models.CharField(max_length=10,null=True)
    location =models.CharField(max_length=50,null=True)
    code =models.CharField(max_length=50,null=True)
    owner_PhoneNumber =models.CharField(max_length=20,null=True)
    occupier_address = models.CharField(max_length=200,null=True)
    ground_floor = models.CharField(max_length=50,null=True)
    first_floor = models.CharField(max_length=50,null=True)
    total = models.CharField(max_length=50,null=True)
    difference =models.CharField(max_length=50,null=True)
    percent_difference=models.CharField(max_length=50,null=True)
    building_usage =models.CharField(max_length=50,null=True)
    remark =models.CharField(max_length=255,null=True)
    class Meta:
            constraints =[
            models.UniqueConstraint(fields=['new_wardno','new_doorno','new_subno'],name='unique_warno_doorno_subno')
         ]    








class Field(models.Model):
    S_date =models.DateField(null=True)
    ward_no=models.IntegerField(null=True)
    building_type=models.CharField(max_length=20,null=True)
    code =models.CharField(max_length=25,null=True)
    village =models.CharField(max_length=100,null=True)
    building_no =models.IntegerField(null=True)
    survey_no = models.IntegerField(null=True)
    ownership=models.CharField(max_length=50,null=True)
    no_of_persons =models.IntegerField(null=True)
    owners_name =models.CharField(max_length=100,null=True)
    owner_address =models.TextField()
    email =models.EmailField(null=True)
    aadhar_no=models.IntegerField(null=True)
    ph_number =models.IntegerField()
    occupier_address =models.TextField()
    occupier_phno =models.IntegerField(null=True)
    floor_area =models.CharField(max_length=200)
    ground_floorarea =models.CharField(max_length=200)
    first_floorarea = models.CharField(max_length=200)
    Total =models.CharField(max_length=200)
    bulding_usage = models.TextField()
    modification = models.CharField(max_length=255)
    numberoffloor=models.IntegerField(null=True)
    currentroofdetails =models.CharField(max_length=200,null=True)
    exservice_men =models.CharField(max_length=50,null=True)
    remark =models.CharField(max_length=255,null=True)
    building_age_year =models.CharField(max_length=50,null=True)
    tax_exemption =models.CharField(max_length=20,null=True)
    swimmingpool =models.CharField(max_length=20,null=True)
    nearby_roadname=models.CharField(max_length=50,null=True)
    road_width=models.CharField(max_length=25,null=True)
    road_category =models.CharField(max_length=25,null=True)
    road_surfacetype=models.CharField(max_length=25,null=True)









  