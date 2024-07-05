from django.urls import path
from . import views
from django.conf.urls import handler404
from attendance import views as v
from inventory import views as iv
from bills import views as bv
from advertisement import views as ad
from visualization import views as vis
from salary import views as sl
urlpatterns = [
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('', views.landing, name='landing'),

    path('signup', views.signup, name='signup'),
    path('registration', views.registration, name='registration'),
    path('login',views.login, name='login'),
    path('logout_user',views.logout_user, name='logout_user'),
    path('employee_details',views.employee_details, name='employee_details'),


    path('edit_my_profile',views.edit_my_profile,name='edit_my_profile'),

    path('forgot_password', views.forgot_password, name='forgot_password'),

    path('reset_password', views.reset_password, name='reset_password'),




    path('edit_profile_user', views.edit_profile_user, name='edit_profile_user'),

    path('changes', views.changes, name='changes'),

    path('changes_my_profile', views.changes_my_profile, name='changes_my_profile'),




    path('changes_account',views.changes_account,name='changes_account'),

    path('account_details_edit',views.account_details_edit,name='account_details_edit'),

    path('upload_image',views.upload_image,name='upload_image'),
    path('display_leave_request',views.display_leave_request,name='display_leave_request'),

    path('leave_request_submit',views.leave_request_submit,name='leave_request_submit'),

    path('leave_request_list_display_staff',views.leave_request_list_display_staff,name='leave_request_list_display_staff'),

    path('leave_request_list_display_hr',views.leave_request_list_display_hr,name='leave_request_list_display_hr'),
    path('leave_request_list_display_admin',views.leave_request_list_display_admin,name='leave_request_list_display_admin'),

    path('leave_approve_reject_from_hr', views.leave_approve_reject_from_hr, name='leave_approve_reject_from_hr'),
    path('leave_approve_reject_from_admin', views.leave_approve_reject_from_admin, name='leave_approve_reject_from_admin'),

    path('display_total_employees', views.display_total_employees, name='display_total_employees'),


    path('mark_attendance',v.mark_attendance,name='mark_attendance'),

    path('display_attendance',v.display_attendance,name='display_attendance'),

    path('add_section', iv.add_section, name='add_section'),

    path('add_category', iv.add_category, name='add_category'),

    path('store_section', iv.store_section, name='store_section'),

    path('store_category', iv.store_category, name='store_category'),


    path('add_brand', iv.add_brand, name='add_brand'),







    # SECTION URLS

    path('view_section', iv.view_section, name='view_section'),

    path('edit_section', iv.edit_section, name='edit_section'),

    path('save_changes_section', iv.save_changes_section, name='save_changes_section'),

    path('delete_section', iv.delete_section, name='delete_section'),

    path('delete_alert_section', iv.delete_alert_section, name='delete_alert_section'),


    # CATEGORY URLS

    path('view_category', iv.view_category, name='view_category'),

    path('edit_category', iv.edit_category, name='edit_category'),

    path('save_changes_category', iv.save_changes_category, name='save_changes_category'),

    path('delete_category', iv.delete_category, name='delete_category'),

    path('delete_alert_category', iv.delete_alert_category, name='delete_alert_category'),


    path('store_brand', iv.store_brand, name='store_brand'),



    # # BRAND URL

    path('view_brand', iv.view_brand, name='view_brand'),

    path('edit_brand', iv.edit_brand, name='edit_brand'),

    path('save_changes_brand', iv.save_changes_brand, name='save_changes_brand'),

    path('delete_brand', iv.delete_brand, name='delete_brand'),

    path('delete_alert_brand', iv.delete_alert_brand, name='delete_alert_category'),



    # PRODUCT URLS

    path('view_product', iv.view_product, name='view_product'),

    path('add_product', iv.add_product, name='add_product'),

    path('edit_product', iv.edit_product, name='edit_product'),

    path('save_changes_product', iv.save_changes_product, name='save_changes_product'),

    path('store_product', iv.store_product, name='store_product'),


    path('delete_alert_product', iv.delete_alert_product, name='delete_alert_product'),

    path('delete_product', iv.delete_product, name='delete_product'),






    path('view_all_products', iv.view_all_products, name='view_all_products'),




    # download the excle files
    path('download-excel/', iv.download_excel, name='download_excel'),

    path('download-staff-excel/', views.download_staff_excel, name='download_staff_excel'),



    # billing views


    path('generate_invoice', bv.generate_invoice, name='generate_invoice'),

    path('get_product_price', bv.get_product_price, name='get_product_price'),

    path('get_product_quantity', bv.get_product_quantity, name='get_product_quantity'),

    path('submit_invoice', bv.submit_invoice, name='submit_invoice'),

    path('customer_details', bv.customer_details, name='customer_details'),

    path('search_customer', bv.search_customer, name='search_customer'),

    path('pay_invoice', bv.pay_invoice, name='pay_invoice'),



    path('refund', bv.refund, name='refund'),

    path('store_return_and_refund', bv.store_return_and_refund, name='store_return_and_refund'),

    path('refund_request', bv.refund_request, name='refund_request'),

    path('refund_request_approve_reject', bv.refund_request_approve_reject, name='refund_request_approve_reject'),



    path('refund_history', bv.refund_history, name='refund_history'),

    path('invoices', bv.invoices, name='invoices'),



    # Attendance
    path('save_attendance', v.save_attendance, name='save_attendance'),

    path('view_attendance', v.view_attendance, name='view_attendance'),

    path('download_attendance_excel', v.download_attendance_excel, name='download_attendance_excel'),

    path('download_attendance_excel_year', v.download_attendance_excel_year, name='download_attendance_excel_year'),



    # advertisement

    path('uploadadvertisement', ad.uploadadvertisement, name='uploadadvertisement'),


    # visualization
    path('invoice/chart/', vis.invoice_chart, name='invoice_chart'),
    path('inventory_levels', vis.inventory_levels, name='inventory_levels'),
    path('attendance_summary', vis.attendance_summary, name='attendance_summary'),
    path('section_chart', vis.section_chart, name='section_chart'),
    path('category_chart', vis.category_chart, name='category_chart'),

    path('attendance_chart', vis.attendance_chart, name='attendance_chart'),


    # salary
    path('salary_list', sl.salary_list, name='salary_list'),
    path('salary_slip', sl.salary_slip, name='salary_slip'),






]
handler404 = views.custom_404_view