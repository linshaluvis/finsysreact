
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
            A=employee_data["provide_bank_details"]
            print(A)
            if Employee.objects.filter(employee_mail=employee_data["employee_mail"], mobile=employee_data["mobile"], employee_number=employee_data["employee_number"], company=com).exists():
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
