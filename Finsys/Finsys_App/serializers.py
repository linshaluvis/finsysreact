from rest_framework import serializers
from Finsys_App.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Login_Details
        fields = '__all__'

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Company_Details
        fields = '__all__'

class DistributorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Distributors_Details
        fields = '__all__'

class StaffDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Staff_Details
        fields = '__all__'

class ModulesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Modules_List
        fields = '__all__'

class PaymentTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Payment_Terms
        fields = '__all__'

class CNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_CNotification
        fields = '__all__'

class ANotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_ANotification
        fields = '__all__'

class DNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_DNotification
        fields = '__all__'

class ItemUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Units
        fields = '__all__'

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Chart_Of_Account
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Items
        fields = '__all__'

class ItemHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Items_Transaction_History
        fields = '__all__'

class ItemCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fin_Items_Comments
        fields = '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class EmployeeBloodgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Blood_Group
        fields = '__all__'
class EmployeeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_History
        fields = '__all__'

class EmployeeCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Comment
        fields = '__all__'