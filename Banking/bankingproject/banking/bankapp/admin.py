from django.contrib import admin
from. models import Application,District,Branches
# Register your models here.
admin.site.register(Application)
admin.site.register(District)
admin.site.register(Branches)
class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ["id","name", "DOB", "age", "gender", "email", "phonenumber", "address","district","branch"
            "state","pincode","accounttype","materials_provided"]
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
class BranchesModelAdmin(admin.ModelAdmin):
    list_display = ["name"]