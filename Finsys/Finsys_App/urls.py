from django.urls import path
from Finsys_App.views import *

urlpatterns = [
    path('',home),
    path("companyReg_action/", Fin_companyReg_action, name="Fin_companyReg_action"),
    path('CompanyReg2_action2/',Fin_CompanyReg2_action2,name='Fin_CompanyReg2_action2'),
    path('Add_Modules/',Fin_Add_Modules,name='Fin_Add_Modules'),
    path('Distributor_Registration_Action/',Fin_DReg_Action,name='Fin_DReg_Action'),
    path('get_payment_terms/',Fin_getPaymentTerms,name='Fin_get_payment_terms'),
    path('get_distributor_data/<int:id>/',Fin_getDistributorData,name='Fin_get_distributor_data'),
    path('Distributor_Registration_Action2/',Fin_DReg2_Action2,name='Fin_DReg2_Action2'),
    path('Fin_staffReg_action/',Fin_staffReg_action,name='Fin_staffReg_action'),
    path('get_staff_data/<int:id>/',Fin_getStaffData,name='Fin_get_staff_data'),
    path('StaffReg2_Action/',Fin_StaffReg2_Action,name='Fin_StaffReg2_Action'),

    path('LogIn/',Fin_login,name='Fin_login'),
    path('add_payment_terms/',Fin_add_payment_terms,name='Fin_add_payment_terms'),
    path('delete_payment_term/<int:id>/',Fin_delete_payment_terms,name='Fin_delete_payment_terms'),
    path('get_distributors_requests/',Fin_getDistributorsRequests, name='Fin_getDistributorsRequests'),
    path('get_distributors/',Fin_getDistributors, name='Fin_getDistributors'),
    path('DReq_Accept/<int:id>/',Fin_DReq_Accept,name='Fin_DReq_Accept'),
    path('DReq_Reject/<int:id>/',Fin_DReq_Reject,name='Fin_DReq_Reject'),
    path('get_distributors_overview_data/<int:id>/',Fin_getDistributorsOverviewData, name='Fin_getDistributorsOverviewData'),
    path('get_clients_requests/',Fin_getClientsRequests, name='Fin_getClientsRequests'),
    path('get_clients/',Fin_getClients, name='Fin_getClients'),
    path('Client_Req_Accept/<int:id>/',Fin_Client_Req_Accept,name='Fin_Client_Req_Accept'),
    path('Client_Req_Reject/<int:id>/',Fin_Client_Req_Reject,name='Fin_Client_Req_Reject'),
    path('get_clients_overview_data/<int:id>/',Fin_getClientsOverviewData, name='Fin_getClientsOverviewData'),
    path('fetch_admin_notifications/',Fin_fetchAdminNotifications),
    path('admin_notification_overview/<int:id>/',Fin_getAdminNotificationOverview),
    path('accept_module_updation_request/', Fin_Module_Updation_Accept),
    path('reject_module_updation_request/', Fin_Module_Updation_Reject),

    path('user/<int:id>/',getSelfData),
    path('check_payment_term/<int:id>/',Fin_checkPaymentTerms),
    path('fetch_notifications/<int:id>/',Fin_fetchNotifications),
    path('fetch_min_stock_alerts/<int:id>/',minStock),
    path('fetch_dist_notifications/<int:id>/',Fin_fetchDistNotifications),
    path('get_profile_data/<int:id>/',getProfileData),
    path('get_distributor_clients_requests/<int:id>/',Fin_DClient_req,name='Fin_DClient_req'),
    path('get_distributor_clients/<int:id>/',Fin_DClients,name='Fin_DClients'),
    path('DClient_Req_Accept/<int:id>/',Fin_DClient_Req_Accept,name='Fin_DClient_Req_Accept'),
    path('DClient_Req_Reject/<int:id>/',Fin_DClient_Req_Reject,name='Fin_DClient_Req_Reject'),
    path('get_staff_requests/<int:id>/',Fin_getStaffRequests, name='Fin_getStaffRequests'),
    path('get_all_staffs/<int:id>/',Fin_getAllStaffs, name='Fin_getAllStaffs'),
    path('Staff_Req_Accept/<int:id>/',Fin_Staff_Req_Accept,name='Fin_Staff_Req_Accept'),
    path('Staff_Req_Reject/<int:id>/',Fin_Staff_Req_Reject,name='Fin_Staff_Req_Reject'),
    path('edit_company_profile/',Fin_editCompanyProfile),
    path('edit_staff_profile/',Fin_editStaffProfile),
    path('edit_gsttype/',company_gsttype_change,name='company_gsttype_change'),
    path('Change_payment_terms/',Fin_Change_payment_terms,name='Fin_Change_payment_terms'),
    path('get_distributor_profile_data/<int:id>/',getDistributorProfileData),
    path('check_distributor_payment_term/<int:id>/',Fin_checkDistributorPaymentTerms),
    path('Change_distributor_payment_terms/',Fin_Change_distributor_payment_terms,name='Fin_Change_distributor_payment_terms'),
    path('edit_distributor_profile/',Fin_editDistributorProfile),
    path('get_modules/<int:id>/',Fin_getModules),
    path('Edit_Modules/',Fin_EditModules),

    path('fetch_distributor_notifications/<int:id>/',Fin_fetchDistributorNotifications),
    path('distributor_notification_overview/<int:id>/',Fin_getDistributorNotificationOverview),
    path('accept_dmodule_updation_request/', Fin_DModule_Updation_Accept),
    path('reject_dmodule_updation_request/', Fin_DModule_Updation_Reject),

    # ITEMS
    path('get_company_item_units/<int:id>/',Fin_getCompanyItemUnits),
    path('get_company_accounts/<int:id>/',Fin_getCompanyAccounts),
    path('create_new_item/',Fin_createNewItem),
    path('update_item/',Fin_updateItem),
    path('create_new_unit/',Fin_createNewUnit),
    path('change_item_status/',Fin_changeItemStatus),
    path('fetch_items/<int:id>/',Fin_fetchItems),
    path('fetch_item_details/<int:id>/',Fin_fetchItemDetails),
    path('fetch_item_history/<int:id>/',Fin_fetchItemHistory),
    path('delete_item/<int:id>/',Fin_deleteItem),
    path('delete_item_comment/<int:id>/',Fin_deleteItemComment),
    path('item_transaction_pdf/<int:itemId>/<int:id>/',Fin_itemTransactionPdf),
    path('share_item_transactions_email/',Fin_shareItemTransactionsToEmail),
    path('add_item_comment/',Fin_addItemComment),
    path('check_accounts/',Fin_checkAccounts),
    path('create_new_account_from_items/',Fin_createNewAccountFromItems),

    path('create_new_employee/<int:id>/',Fin_createemployee),
    path('create_new_bloodgroup/',Fin_createNewbloodgroup),
    path('fetch_employee/<int:id>/',Fin_fetchemployee),
    path('employee_save/',employee_save),
    path('fetch_employee_details/<int:id>/',Fin_fetchEmployeeDetails),
    path('change_Employee_status/',Fin_changeEmployeeStatus),
    path('Fin_addEmployeeComment/',Fin_addEmployeeComment),
    path('delete_employee_comment/<int:id>/',Fin_deleteemployeeComment),
    path('delete_employee/<int:id>/',Fin_deleteemployee),









]
