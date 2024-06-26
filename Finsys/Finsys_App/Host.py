
#-------------------------------------urls.py------------------


path('create_new_employee/<int:id>/',Fin_createemployee),
path('create_new_bloodgroup/',Fin_createNewbloodgroup),
path('fetch_employee/<int:id>/',Fin_fetchemployee),
path('employee_save/',employee_save),
path('fetch_employee_details/<int:id>/',Fin_fetchEmployeeDetails),
path('change_Employee_status/',Fin_changeEmployeeStatus),
path('Fin_addEmployeeComment/',Fin_addEmployeeComment),
path('delete_employee_comment/<int:id>/',Fin_deleteemployeeComment),
path('delete_employee/<int:id>/',Fin_deleteemployee),
path('fetch_employee_history/<int:id>/',Fin_fetchemployeeHistory),
path('employee_transaction_pdf/<int:itemId>/<int:id>/',Fin_employTransactionPdf),
path('share_employee_transactions_email/',Fin_share_employ_TransactionsToEmail),
path('update_employee/',Fin_updateemployee),

#-------------------------------------serializers.py------------------


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
        
 #-------------------------------------models.py------------------ 
 #employee
class Employee(models.Model):
    upload_file = models.FileField(upload_to='file/',blank=True) 
    upload_image = models.ImageField(upload_to='media/',blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    alias = models.CharField(max_length=255,null=True,blank=True)
    employee_mail = models.EmailField(null=True,blank=True)
    employee_number = models.CharField(max_length=255,null=True,blank=True)
    employee_designation = models.CharField(max_length=255,null=True,blank=True)
    function = models.CharField(max_length=255,null=True,blank=True)
    employee_current_location = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    date_of_joining = models.DateField(null=True,blank=True)
    employee_salary_type = models.CharField(max_length=255,null=True,blank=True)
    salary_details = models.CharField(max_length=10,null=True,blank=True)
    salary_effective_from = models.CharField(max_length=255,null=True,blank=True)

    pay_head = models.CharField(max_length=255,null=True,blank=True)
    salary_amount = models.FloatField(null=True,blank=True)
    amount_per_hour = models.IntegerField(null=True,blank=True)
    total_working_hours = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=255,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    blood_group = models.CharField(max_length=255,null=True,blank=True)
    fathers_name_mothers_name = models.CharField(max_length=255,null=True,blank=True)
    spouse_name = models.CharField(max_length=255,null=True,blank=True)
    emergency_contact = models.CharField(max_length=255,null=True,blank=True)
    provide_bank_details = models.CharField(max_length=255,null=True,blank=True)
    account_number = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    name_of_bank = models.CharField(max_length=255,null=True,blank=True)
    branch_name = models.CharField(max_length=255,null=True,blank=True)
    bank_transaction_type = models.CharField(max_length=255,null=True,blank=True)
    tds_applicable = models.CharField(max_length=255,null=True,blank=True)
    tds_type = models.CharField(max_length=255,null=True,blank=True)
    percentage_amount = models.IntegerField(null=True,blank=True)
    pan_number = models.CharField(max_length=255,null=True,blank=True)
    income_tax_number = models.CharField(max_length=255,null=True,blank=True)
    aadhar_number = models.CharField(max_length=255,null=True,blank=True)
    universal_account_number = models.CharField(max_length=255,null=True,blank=True)
    pf_account_number = models.CharField(max_length=255,null=True,blank=True)
    pr_account_number = models.CharField(max_length=255,null=True,blank=True)
    esi_number = models.CharField(max_length=255,null=True,blank=True)

    street = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    temporary_street = models.CharField(max_length=255,null=True,blank=True)
    temporary_city = models.CharField(max_length=255,null=True,blank=True)
    temporary_state = models.CharField(max_length=255,null=True,blank=True)
    temporary_pincode = models.CharField(max_length=255,null=True,blank=True)
    temporary_country = models.CharField(max_length=255,null=True,blank=True)
    employee_status = models.CharField(max_length=30,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)

class Employee_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(null=True,blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)

class Employee_Comment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(default = date.today())
    
class Employee_Blood_Group(models.Model):
    blood_group = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)      
        
#-------------------------------------views.py------------------


@api_view(("GET",))
def Fin_createemployee(request, id):
    try:
        data = Fin_Login_Details.objects.get(id=id)
        if data.User_Type == 'Company':
            cmp = Fin_Company_Details.objects.get(Login_Id=id)
        else:
            cmp = Fin_Staff_Details.objects.get(Login_Id = id).company_id
        bloodgp = Employee_Blood_Group.objects.filter(company=cmp)
        serializer = EmployeeBloodgroupSerializer(bloodgp, many=True)
        return Response(
            {"status": True, "bloodgp": serializer.data}, status=status.HTTP_200_OK
        )
    except Exception as e:
        print(e)
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
        

@api_view(("POST",))
def Fin_createNewbloodgroup(request):
    try:
        s_id = request.data.get("Id")
        data = Fin_Login_Details.objects.get(id=s_id)
        print(data)
        blood_group = request.data.get("blood_group", "").upper()
        print(blood_group)
        if not blood_group:
            return Response(
                {"status": False, "message": "Blood group is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        invalid_groups = ['A+', 'A-', 'B+','B-','AB+','AB-', 'O+','O-']

        if blood_group in invalid_groups:
            return Response(
                {"status": False, "message": "Invalid blood group."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id=s_id)
        else:
            staff = Fin_Staff_Details.objects.get(Login_Id=s_id)
            com = staff.company_id
        
        request.data["Company"] = com.id
        if Employee_Blood_Group.objects.filter(company_id=com.id, blood_group=blood_group, login_id=s_id).exists():
            return Response(
                {"status": False, "message": "Blood group already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = EmployeeBloodgroupSerializer(data=request.data)
        print(serializer)
        
        if serializer.is_valid():
            Employee_Blood_Group.objects.create(
                company=com,
                login=data,
                blood_group=serializer.validated_data['blood_group'].upper(),
            )
            print("yes")
            return Response(
                {"status": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except Fin_Login_Details.DoesNotExist:
        return Response(
            {"status": False, "message": "Login details not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Fin_Company_Details.DoesNotExist:
        return Response(
            {"status": False, "message": "Company details not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Fin_Staff_Details.DoesNotExist:
        return Response(
            {"status": False, "message": "Staff details not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(("POST",))
def employee_save(request):
    if request.method == 'POST':
        try:
            # Make a mutable copy of request data
            data = request.data.copy()
            
            s_id = data.get("Id")
            datauser = Fin_Login_Details.objects.get(id=s_id)
            
            if datauser.User_Type == "Company":
                com = Fin_Company_Details.objects.get(Login_Id=s_id)
            else:
                staff = Fin_Staff_Details.objects.get(Login_Id=s_id)
                com = staff.company_id
            
            data["Company"] = com.id
            
            file = request.FILES.get('file')
            image = request.FILES.get('image')
            account_number= data.get('Account_Number')
            ifsc=data.get('IFSC')
            name_of_bank=data.get('Bank_Name')
            branch_name=data.get('Branch_Name')
            bank_transaction_type=data.get('Transaction_Type')
            print(account_number)
            print(ifsc)
            print(branch_name)
            print(name_of_bank)
            print(bank_transaction_type)
            provide_bank_details=data.get('Bank_Details')
            print(provide_bank_details)
            tds_applicable=data.get('TDS_Applicable')
            tds_type=data.get('TDS_Type')
            percentage_amount=data.get('TDS_Amount')
            percentage_amount2=data.get('TDS_Percentage')

            print(tds_applicable)
            print(tds_type)
            print(percentage_amount)
            print(percentage_amount2)


            present_address = json.loads(data.get('Present_Address'))
            permanent_address = json.loads(data.get('Permanent_Address'))
            salary_amount = data.get('Salary_Amount')
            if tds_type == 'Percentage':
                percentage_amount = data.get('TDS_Percentage')
            else:
                percentage_amount = data.get('TDS_Amount')
            if not salary_amount:
                salary_amount = None

            # Handling amount per hour
            amount_per_hour = data.get('Amount_Per_Hour')
            if not amount_per_hour or amount_per_hour == '0':
                amount_per_hour = 0

            # Handling working hours
            working_hours = data.get('Working_Hours')
            if not working_hours or working_hours == '0':
                working_hours = 0


            # Example of setting multiple fields from data
            employee_data = {
                "company": com,
                "login": datauser,
                "title": data.get('Title'),
                "first_name": data.get('First_Name'),
                "last_name": data.get('Last_Name'),
                "date_of_joining": data.get('Joining_Date'),
                "salary_effective_from": data.get('Salary_Date'),
                "employee_salary_type": data.get('Salary_Type'),
                "salary_amount": data.get('Salary_Amount'),
                "amount_per_hour": data.get('Amount_Per_Hour'),
                "total_working_hours": data.get('Working_Hours'),
                "alias": data.get('Alias'),
                "employee_number": data.get('Employee_Number'),
                "employee_designation": data.get('Designation'),
                "employee_current_location": data.get('Location'),
                "gender": data.get('Gender'),
                "date_of_birth": data.get('DOB'),
                "age": data.get('Age'),
                "blood_group": data.get('Blood_Group'),
                "mobile": data.get('Contact_Number'),
                "emergency_contact": data.get('Emergency_Contact_Number'),
                "employee_mail": data.get('Personal_Email'),
                "fathers_name_mothers_name": data.get('Parent_Name'),
                "spouse_name": data.get('Spouse_Name'),
                "upload_file": file,
                "provide_bank_details": data.get('Bank_Details'),
                "tds_applicable": data.get('TDS_Applicable'),
                "account_number": data.get('Account_Number'),
                "ifsc": data.get('IFSC'),
                "name_of_bank": data.get('Bank_Name'),
                "branch_name": data.get('Branch_Name'),
                "bank_transaction_type": data.get('Transaction_Type'),
                "tds_type": data.get('TDS_Type'),
                "percentage_amount": percentage_amount,
                "street": present_address.get('address'),
                "city": present_address.get('city'),
                "state": present_address.get('state'),
                "pincode": present_address.get('pincode'),
                "country": present_address.get('country'),
                "temporary_street": permanent_address.get('address'),
                "temporary_city": permanent_address.get('city'),
                "temporary_state": permanent_address.get('state'),
                "temporary_pincode": permanent_address.get('pincode'),
                "temporary_country": permanent_address.get('country'),
                "pan_number": data.get('PAN'),
                "income_tax_number": data.get('Income_Tax'),
                "aadhar_number": data.get('Aadhar'),
                "universal_account_number": data.get('UAN'),
                "pf_account_number": data.get('PF'),
                "pr_account_number": data.get('PR'),
                "upload_image": image,
                "employee_status": 'Active',
            }

            if employee_data["provide_bank_details"] == 'Yes':
                
                if employee_data["account_number"] and Employee.objects.filter(account_number=employee_data["account_number"], company_id=com.id).exists():
                    return JsonResponse({"status": False, "message": "Bank account number already exists"})
            elif Employee.objects.filter(employee_mail=employee_data["employee_mail"], mobile=employee_data["mobile"], employee_number=employee_data["employee_number"], company=com).exists():
                return JsonResponse({"status": False, "message": "User already exists"})
            elif Employee.objects.filter(mobile=employee_data["mobile"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Phone number already exists"})
            elif Employee.objects.filter(emergency_contact=employee_data["emergency_contact"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Emergency phone number already exists"})
            elif Employee.objects.filter(employee_mail=employee_data["employee_mail"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Email already exists"})
            elif Employee.objects.filter(employee_number=employee_data["employee_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Employee ID already exists"})
            elif employee_data["income_tax_number"] and Employee.objects.filter(income_tax_number=employee_data["income_tax_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Income Tax Number already exists"})
            elif employee_data["pf_account_number"] and Employee.objects.filter(pf_account_number=employee_data["pf_account_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "PF account number already exists"})
            elif employee_data["aadhar_number"] and Employee.objects.filter(aadhar_number=employee_data["aadhar_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Aadhar number already exists"})
            elif employee_data["pan_number"] and Employee.objects.filter(pan_number=employee_data["pan_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "PAN number already exists"})
            elif employee_data["universal_account_number"] and Employee.objects.filter(universal_account_number=employee_data["universal_account_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "Universal account number already exists"})
            elif employee_data["pr_account_number"] and Employee.objects.filter(pr_account_number=employee_data["pr_account_number"], company_id=com.id).exists():
                return JsonResponse({"status": False, "message": "PR account number already exists"})
            
            else:
                employee = Employee(**employee_data)
                employee.save()

                history = Employee_History(
                    company=com,
                    login=datauser,
                    employee=employee,
                    date=date.today(),
                    action='Created'
                )
                history.save()
                return Response(
                    {"status": True, 'message': 'Employee saved successfully.'}, status=status.HTTP_200_OK
                )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


@api_view(("GET",))
def Fin_fetchemployee(request, id):
    try:
        data = Fin_Login_Details.objects.get(id=id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id=id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id=id).company_id

        items = Employee.objects.filter(company=com)
        serializer = EmployeeSerializer(items, many=True)
        return Response(
            {"status": True, "items": serializer.data}, status=status.HTTP_200_OK
        )
    except Exception as e:
        print(e)
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(("GET",))
def Fin_fetchEmployeeDetails(request, id):
    try:
        item = Employee.objects.get(id=id)
        hist = Employee_History.objects.filter(employee=item).last()
        print(hist)
        his = None
        if hist:
            his = {
                "action": hist.action,
                "date": hist.date,
                "doneBy": hist.login.First_name
                + " "
                + hist.login.Last_name,
            }
        cmt = Employee_Comment.objects.filter(employee=item)
        itemSerializer = EmployeeSerializer(item)
        commentsSerializer = EmployeeCommentsSerializer(cmt, many=True)
        return Response(
            {
                "status": True,
                "item": itemSerializer.data,
                "history": his,
                "comments": commentsSerializer.data,
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(("POST",))
def Fin_changeEmployeeStatus(request):
    try:
        itemId = request.data["id"]
        data = Employee.objects.get(id=itemId)
        S=request.data["status"]
        data.employee_status = request.data["status"]
        print(S)
        data.save()
        return Response({"status": True}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
      

@api_view(("POST",))
def Fin_addEmployeeComment(request):
    try:
        id = request.data.get("Id")  # Retrieve 'Id' from request data
        data = Fin_Login_Details.objects.get(id=id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id=id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id=id).company_id

        # Prepare the data for the serializer
        serializer_data = {
            "comment": request.data.get("comments"),
            "employee": request.data.get("item"),  # Ensure this matches the serializer field
            "company": com.id,
            "login": data.id,
            # You can add 'date' or other fields if required
        }

        serializer = EmployeeCommentsSerializer(data=serializer_data)
        print(serializer)
        if serializer.is_valid():
            Employee_Comment.objects.create(
                company=com,
                login=data,
                comment=serializer.validated_data['comment'],
                employee=serializer.validated_data['employee'],  # Ensure this matches the model field
            )
            print("yes")
            return Response(
                {"status": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except Fin_Login_Details.DoesNotExist:
        return Response(
            {"status": False, "message": "Login details not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Fin_Company_Details.DoesNotExist:
        return Response(
            {"status": False, "message": "Company details not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Fin_Staff_Details.DoesNotExist:
        return Response(
            {"status": False, "message": "Staff details not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
@api_view(("DELETE",))
def Fin_deleteemployee(request, id):
    try:
        item = Employee.objects.get(id=id)
        item.delete()
        return Response({"status": True}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(("DELETE",))
def Fin_deleteemployeeComment(request, id):
    try:
        cmt = Employee_Comment.objects.get(id=id)
        cmt.delete()
        return Response({"status": True}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(("GET",))
def Fin_fetchemployeeHistory(request, id):
    try:
        item = Employee.objects.get(id=id)
        hist = Employee_History.objects.filter(employee=item)
        print(item)
        print(hist)
        
        his = []
        if hist:
            for i in hist:
                h = {
                    "action": i.action,
                    "date": i.date,
                    "name": i.login.First_name + " " + i.login.Last_name,
                }
                his.append(h)
        itemSerializer = EmployeeSerializer(item)
        return Response(
            {"status": True, "item": itemSerializer.data, "history": his},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(e)
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )



@api_view(("GET",))
def Fin_employTransactionPdf(request, itemId, id):
    try:
        data = Fin_Login_Details.objects.get(id=id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id=id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id=id).company_id

        item = Employee.objects.get(id=itemId)
        


        context = {"employ": item}

        template_path = "company/Fin_employee_Pdf.html"
        fname = "Employee_" + item.first_name
        # return render(request, 'company/Fin_Item_Transaction_Pdf.html',context)
        # Create a Django response object, and specify content_type as pdftemp_
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f"attachment; filename = {fname}.pdf"
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")
        return response
    except Exception as e:
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(("POST",))
def Fin_share_employ_TransactionsToEmail(request):
    try:
        id = request.data["Id"]
        data = Fin_Login_Details.objects.get(id=id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id=id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id=id).company_id

        itemId = request.data["itemId"]
        item = Employee.objects.get(id=itemId)
        emails_string = request.data["email_ids"]

        # Split the string by commas and remove any leading or trailing whitespace
        emails_list = [email.strip() for email in emails_string.split(",")]
        email_message = request.data["email_message"]
        # print(emails_list)

        

        context = {"employ": item}
        template_path = "company/Fin_employee_Pdf.html"
        template = get_template(template_path)

        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        pdf = result.getvalue()
        filename = f"Employee-{item.first_name}.pdf"
        subject = f"Employee_{item.first_name}"
        email = EmailMessage(
            subject,
            f"Hi,\nPlease find the attached Transaction details - Employee-{item.first_name}. \n{email_message}\n\n--\nRegards,\n{com.Company_name}\n{com.Address}\n{com.State} - {com.Country}\n{com.Contact}",
            from_email=settings.EMAIL_HOST_USER,
            to=emails_list,
        )
        email.attach(filename, pdf, "application/pdf")
        email.send(fail_silently=False)

        return Response({"status": True}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PUT"])
def Fin_updateemployee(request):
    try:
        s_id = request.data["Id"]
        data = Fin_Login_Details.objects.get(id=s_id)

        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id=s_id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id=s_id).company_id
        
        employee = Employee.objects.get(id=request.data['itemId'])

        account_number = request.data['Account_Number']
        ifsc = request.data['IFSC']
        name_of_bank = request.data['Bank_Name']
        branch_name = request.data['Branch_Name']
        bank_transaction_type = request.data['Transaction_Type']
        provide_bank_details = request.data['Bank_Details']
        tds_applicable = request.data['TDS_Applicable']
        tds_type = request.data['TDS_Type']
        percentage_amount = request.data['TDS_Amount']
        percentage_amount2 = request.data['TDS_Percentage']

        present_address = json.loads(request.data['Present_Address'])
        permanent_address = json.loads(request.data['Permanent_Address'])
        salary_amount = request.data['Salary_Amount']
        if tds_type == 'Percentage':
            percentage_amount = request.data['TDS_Percentage']
        else:
            percentage_amount = request.data['TDS_Amount']
        if not salary_amount:
            salary_amount = None

        # Handling amount per hour
        amount_per_hour = request.data['Amount_Per_Hour']
        if not amount_per_hour or amount_per_hour == '0':
            amount_per_hour = 0

        # Handling working hours
        working_hours = request.data.get('Working_Hours')
        if not working_hours or working_hours == '0':
            working_hours = 0

        # Extract fields from request data
        employee_data = {
            "company": com,
            "login": data,
            "title": request.data['Title'],
            "first_name": request.data['First_Name'],
            "last_name": request.data['Last_Name'],
            "date_of_joining": request.data['Joining_Date'],
            "salary_effective_from": request.data['Salary_Date'],
            "employee_salary_type": request.data['Salary_Type'],
            "salary_amount": request.data['Salary_Amount'],
            "amount_per_hour": request.data['Amount_Per_Hour'],
            "total_working_hours": request.data['Working_Hours'],
            "alias": request.data['Alias'],
            "employee_number": request.data['Employee_Number'],
            "employee_designation": request.data['Designation'],
            "employee_current_location": request.data['Location'],
            "gender": request.data['Gender'],
            "date_of_birth": request.data['DOB'],
            "age": request.data['Age'],
            "blood_group": request.data['Blood_Group'],
            "mobile": request.data['Contact_Number'],
            "emergency_contact": request.data['Emergency_Contact_Number'],
            "employee_mail": request.data['Personal_Email'],
            "fathers_name_mothers_name": request.data['Parent_Name'],
            "spouse_name": request.data['Spouse_Name'],
            "provide_bank_details": request.data['Bank_Details'],
            "tds_applicable": request.data['TDS_Applicable'],
            "account_number": request.data['Account_Number'],
            "ifsc": request.data['IFSC'],
            "name_of_bank": request.data['Bank_Name'],
            "branch_name": request.data['Branch_Name'],
            "bank_transaction_type": request.data['Transaction_Type'],
            "tds_type": request.data['TDS_Type'],
            "percentage_amount": percentage_amount,
            "street": present_address.get('address'),
            "city": present_address.get('city'),
            "state": present_address.get('state'),
            "pincode": present_address.get('pincode'),
            "country": present_address.get('country'),
            "temporary_street": permanent_address.get('address'),
            "temporary_city": permanent_address.get('city'),
            "temporary_state": permanent_address.get('state'),
            "temporary_pincode": permanent_address.get('pincode'),
            "temporary_country": permanent_address.get('country'),
            "pan_number": request.data['PAN'],
            "income_tax_number": request.data['Income_Tax'],
            "aadhar_number": request.data['Aadhar'],
            "universal_account_number": request.data['UAN'],
            "pf_account_number": request.data['PF'],
            "pr_account_number": request.data['PR'],
            "employee_status": 'Active',
        }

        # Handle file uploads
        if 'file' in request.FILES:
            employee.upload_file = request.FILES['file']
        if 'image' in request.FILES:
            employee.upload_image = request.FILES['image']

        # Uniqueness checks
        emp = Employee.objects.exclude(id=employee.id).filter(company_id=com.id)
        
        if emp.filter(mobile=employee_data['mobile']).exists():
            return JsonResponse({"status": False, "message": "Phone number already exists"})
        elif emp.filter(emergency_contact=employee_data['emergency_contact']).exists():
            return JsonResponse({"status": False, "message": "Emergency contact number already exists"})
        elif emp.filter(employee_mail=employee_data['employee_mail']).exists():
            return JsonResponse({"status": False, "message": "Email already exists"})
        elif emp.filter(employee_number=employee_data['employee_number']).exists():
            return JsonResponse({"status": False, "message": "Employee ID already exists"})
        elif employee_data['income_tax_number'] and emp.filter(income_tax_number=employee_data['income_tax_number']).exists():
            return JsonResponse({"status": False, "message": "Income Tax Number already exists"})
        elif employee_data['pf_account_number'] and emp.filter(pf_account_number=employee_data['pf_account_number']).exists():
            return JsonResponse({"status": False, "message": "PF account number already exists"})
        elif employee_data['aadhar_number'] and emp.filter(aadhar_number=employee_data['aadhar_number']).exists():
            return JsonResponse({"status": False, "message": "Aadhar number already exists"})
        elif employee_data['pan_number'] and emp.filter(pan_number=employee_data['pan_number']).exists():
            return JsonResponse({"status": False, "message": "PAN number already exists"})
        elif employee_data['universal_account_number'] and emp.filter(universal_account_number=employee_data['universal_account_number']).exists():
            return JsonResponse({"status": False, "message": "Universal account number already exists"})

        # Update employee fields
        for key, value in employee_data.items():
            setattr(employee, key, value)

        employee.save()
        
        history = Employee_History(
            company=com,
            employee=employee,
            login=data,
            date=date.today(),
            action='Edited'
        )
        history.save()

        return Response({"status": True, "message": "Employee updated successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"status": False, "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )