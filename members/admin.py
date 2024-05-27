from django.contrib import admin
from members.models import Avilabe_data,Field
from import_export.admin import ImportExportModelAdmin
class field(ImportExportModelAdmin):
    list_display=('S_date','ward_no','building_type','code','village','building_no','survey_no','ownership','owners_name','owner_address','email','aadhar_no','ph_number','occupier_address','occupier_phno','floor_area','ground_floorarea','first_floorarea','Total','bulding_usage','modification','numberoffloor','currentroofdetails','exservice_men','remark','building_age_year','tax_exemption','swimmingpool','nearby_roadname','road_width','road_category','road_surfacetype')
    

admin.site.register(Field,field)
class Avilable_data_display( ImportExportModelAdmin):
    list_display =('new_wardno','new_doorno','new_subno','owner_address','floor_area','buliding_usage','zone','road_type','road_name','buliding_age','roof_details','floor_details','Ac','modification','owner_PhoneNumber','occupier_address','ground_floor','ground_floor','first_floor','total','difference','percent_difference','buliding_usage','remark')
admin.site.register(Avilabe_data,Avilable_data_display)   



