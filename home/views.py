from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import staff
from django.contrib.auth.decorators import login_required
from .models import leave_request
from inventory.models import Product ,Section , Category
from attendance.models import Attendance

from django.contrib.auth import authenticate ,login, alogin , logout



from django.db.models import Count, Case, When, IntegerField, F, Sum
from django.http import JsonResponse
from django.shortcuts import render
import json
from datetime import datetime


from dateutil.relativedelta import relativedelta



from django.db.models import Sum
from datetime import date

from bills.models import Invoice
import pytz


from django.utils import timezone
from django.db.models import Sum
import json
from django.db.models import Count, Sum, Case, When, F, ExpressionWrapper, FloatField , IntegerField
from django.db.models.functions import ExtractHour, ExtractMinute, ExtractSecond


from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum, F, ExpressionWrapper, DurationField
import pytz

def calculate_staff_hours():
    staff_hours = {}

    # Get the current timezone and date
    tz = pytz.timezone('Asia/Kolkata')
    now = timezone.now().astimezone(tz)
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Calculate the worked hours for the current month
    attendances = Attendance.objects.filter(
        date__gte=start_of_month
    ).annotate(
        worked_hours=ExpressionWrapper(
            F('outtime') - F('intime'),
            output_field=DurationField()
        )
    ).values('staff', 'staff__first_name').annotate(
        total_hours=Sum('worked_hours')
    )

    for attendance in attendances:
        staff_hours[attendance['staff__first_name']] = attendance['total_hours']

    return staff_hours

def calculate_penalty_bonus(staff_hours):
    penalty_bonus = {}
    threshold_hours = timedelta(hours=260)

    for staff_name, total_hours in staff_hours.items():
        if total_hours < threshold_hours:
            penalty_hours = threshold_hours - total_hours
            penalty_bonus[staff_name] = {
                'total_hours': total_hours.total_seconds() / 3600,  # Convert to hours
                'penalty_hours': (threshold_hours - total_hours).total_seconds() / 3600,  # Convert to hours
                'bonus_hours': 0
            }
        else:
            bonus_hours = total_hours - threshold_hours
            penalty_bonus[staff_name] = {
                'total_hours': total_hours.total_seconds() / 3600,  # Convert to hours
                'penalty_hours': 0,
                'bonus_hours': bonus_hours.total_seconds() / 3600  # Convert to hours
            }

    return penalty_bonus







@login_required
def index(request):

    now_in_mumbai = timezone.localtime(timezone.now(), timezone=pytz.timezone('Asia/Kolkata'))

    # Calculate the start of the current month
    current_month_start = now_in_mumbai.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Calculate the end of the current month
    next_month_start = current_month_start.replace(month=current_month_start.month % 12 + 1, day=1)
    current_month_end = next_month_start - timezone.timedelta(days=1)


    # Fetch and aggregate data for the current month only
    data = list(
        Invoice.objects.filter(invoice_date__gte=current_month_start, invoice_date__lte=current_month_end)
            .values('invoice_date')
            .annotate(total_amount=Sum('final_amount'))
            .order_by('invoice_date')
    )





    # for inventroy levels visualizations
    inventory_levels_data = list(
        Product.objects.values('product_name')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('total_quantity')[:5]
    )

    # Serialize data
    serialized_data_inventory_levels = json.dumps(inventory_levels_data)

    # sales visulaitioan end here

    # -------------------------------------------------------------------------------------------------------------------------

    #attendance visulaition are start here

    staff_hours = calculate_staff_hours()
    penalty_bonus = calculate_penalty_bonus(staff_hours)



    #attendance visulaition are end  here

    # -------------------------------------------------------------------------------------------------------------------------

    # section visulizatio start here

    # sections = Section.objects.annotate(num_categories=Count('category'))
    #
    # # Serialize data
    # serialized_data_section = json.dumps(
    #     [{'section_name': section.section_name, 'num_categories': section.num_categories} for section in sections])


    # section visulizatio end here

    # -------------------------------------------------------------------------------------------------------------------------
    # Category visulizatio Start here
    categories = Category.objects.annotate(num_products=Count('product'))

    # Serialize data
    serialized_data_Category = json.dumps(
        [{'category_name': category.category_name, 'num_products': category.num_products} for category in categories])
    # print(serialized_data)


    # Category visulizatio end here

    # -------------------------------------------------------------------------------------------------------------------------





    # Convert Decimal objects to float
    for item in data:
        item['total_amount'] = float(item['total_amount'])

    # Convert datetime.date to string
    for item in data:
        item['invoice_date'] = item['invoice_date'].strftime('%d')

    # Serialize data
    serialized_data = json.dumps(data)




    # Fetch all the final_amount values from the Invoice model
    final_amounts = Invoice.objects.aggregate(total_sales=Sum('final_amount'))['total_sales'] or 0

    today = date.today()

    # Calculate today's sales
    today_sales = Invoice.objects.filter(invoice_date=today).aggregate(today_sales=Sum('final_amount'))[
                      'today_sales'] or 0

    # Prepare context to pass to the template
    context = {
        'total_sales': final_amounts,
        'today_sales': today_sales,
        'data' : serialized_data,
        'serialized_data_inventory_levels' : serialized_data_inventory_levels,
        'penalty_bonus' : penalty_bonus,
        # 'serialized_data_section' : serialized_data_section,
        'serialized_data_Category' : serialized_data_Category,


    }
    # Render the index.html template with the context
    return render(request, 'index.html', context)



from advertisement.models import Advertisement
from datetime import datetime


def landing(request):
    current_date = datetime.now().date()
    advertisements = Advertisement.objects.filter(start_date__lte=current_date, end_date__gte=current_date)

    context = {
        'advertisements': advertisements
    }

    return render(request, 'landing.html', context)




def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')




def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        middle_name = request.POST.get('midname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')

        password = request.POST.get('password')

        role = request.POST.get('userType')

        print("fname => ",first_name)
        print("midname => ", middle_name)
        print("lname => ", last_name)
        print("email => ",email)
        print("password =>  ",password)
        print("role =>",  role)

        # Check if the email already exists
        if staff.objects.filter(email=email).exists():
            # If email already exists, add a danger message
            messages.error(request, 'Email address already exists')
            return render(request, 'signup.html')


        if User.objects.filter(username=email).exists():
            # If email already exists, add a danger message
            messages.error(request, 'Email address already exists')
            return render(request, 'signup.html')

        try:
            # create user
            myuser = User.objects.create_user(username=email, email=email, password=password)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()

            # create staff
            registration = staff.objects.create(user=myuser, first_name=first_name, middle_name=middle_name,
                                                last_name=last_name, email=email, role=role, password=password,status='active')
            registration.save()
        except Exception as e:
            messages.error(request, 'Error occurred')
            # Handle any exceptions here
            print("An error occurred:", e)


        subject = 'Welcome to ClothFlow ERP - Your Login Credentials'
        message = "Hi {} {},\n\nWelcome to Shri Collection! We're excited to have you join our team.\n\nYour account for our ERP system, ClothFlow, has been created. Below are your login credentials:\n\nUsername: {}\nPassword: {}\n\nPlease keep this information secure. We recommend changing your password after logging in to ensure your account's security.\n\nHere's how to log in and change your password:\n1. Go to the ClothFlow login page.\n2. Enter your username and password to log in.\n3. Navigate to 'Edit Profile' to update your password to something secure and memorable.\n4. If prompted, follow any additional setup instructions.\n\nIf you have any questions or need assistance, please contact Admin.\n\nWe look forward to working with you at Shri Collection!\n\nBest regards,\nVidya Shivaji Lad\nOwner / Admin\nShri Collection".format(
            first_name, last_name, email, password
        )

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)



    return index(request)


from django.contrib.auth import authenticate, login as alogin

from django.contrib.auth import authenticate


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        print(username)
        print(password)

        print('super user ',request.user.is_superuser)

        if username != 'admin@gmail.com':
        # if not request.user.is_superuser:
            try:
                staff_instance = staff.objects.get(email=username)
            except staff.DoesNotExist:
                messages.error(request, "User not found")
                return render(request, 'signin.html')

            if staff_instance.status == 'deactivate':
                messages.error(request, "Access Denied!")
                return render(request, 'signin.html')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            alogin(request, user)
            print("User logged in successfully: ", username)
            return redirect('index')
        else:
            print("Invalid credentials")
            messages.error(request, "Invalid credentials")
            return render(request, 'signin.html')




def logout_user(request):
    logout(request)
    return render(request, 'signin.html')





def forgot_password(request):
    print('inside forgot_password')
    return render(request,'forgot_password.html')





from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_passwords = request.POST.get('new_password')
        conform_password = request.POST.get('conform_password')


        if new_passwords != conform_password:
            messages.error(request, 'New Password and Conform Password Not Matched ')
            return render(request, 'forgot_password.html')

        try:
            user = User.objects.get(username=username)
            # You can generate a new password here or implement your own logic
            # For simplicity, let's assume you're resetting the password to a default one
            new_password = new_passwords
            user.set_password(new_password)
            user.save()

            staff_instance = staff.objects.get(email=username)

            staff_instance.password = new_password
            staff_instance.save()

            # Optionally, you can also update the user's session authentication hash
            update_session_auth_hash(request, user)
            messages.success(request, 'Password reset successful. Please login with your new password.')
            return signin(request) # Redirect to login page after password reset
        except User.DoesNotExist:
            messages.error(request, 'User with the provided username does not exist.')
            return render(request, 'forgot_password.html')
    else:
        return render(request, 'forgot_password.html')






















def employee_details(request):

    all_staff = staff.objects.all()

    print("user details is following ")
    print(all_staff)



    return render(request,'view_Employee_details.html', {'all_staff': all_staff})



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import staff ,account_details

def edit_profile_user(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')

        # Fetch staff member using staff_id
        staff_member = get_object_or_404(staff, staff_id=staff_id)

        print("inside edit_profile_user function  ")
        print(staff_member.email)
        print(staff_member.first_name)
        print(staff_member.last_name)

        context = {
            'staff_member': staff_member,
        }

        return render(request, 'edit_profile.html',  context)




def changes(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')


        education  = request.POST.get('education')

        role = request.POST.get('role')

        address = request.POST.get('address')
        phone = request.POST.get('phone')


        print("inside change function ")
        print("fname => ",first_name)
        print("midname => ", middle_name)
        print("lname => ", last_name)
        print("email => ",email)
        print("education =>  ",education)
        print("role =>",  role)
        print("address =>", address)
        print("phone =>", phone)
        print("staff_id =>", staff_id)

        all_staff = staff.objects.all()

        staff_instance = get_object_or_404(staff, pk=staff_id)

        # Update the staff instance fields
        staff_instance.first_name = first_name
        staff_instance.middle_name = middle_name
        staff_instance.last_name = last_name


        if staff_instance.email != email:
            staff_instance.email = email
        staff_instance.education = education

        if role == "STAFF":
            staff_instance.role = 1
        elif role == "HR":
            staff_instance.role = 2

        staff_instance.address = address

        existing_staff = staff.objects.filter(phone=phone).exclude(staff_id=staff_id)
        if existing_staff.exists():
            # If email already exists, add a danger message
            messages.error(request, 'Phone Number is already  exist')
            return edit_profile_user(request)

        staff_instance.phone = phone

        # Save the changes
        staff_instance.save()

        print("Changes save")

    messages.success(request, 'Profile Edited Successfully')
    return employee_details(request)




def edit_my_profile(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')

        # Fetch staff member using staff_id
        staff_member = get_object_or_404(staff, staff_id=staff_id)

        print("inside edit_my_profile function  ")
        print(staff_member.email)
        print(staff_member.first_name)
        print(staff_member.last_name)

        context = {
            'staff_member': staff_member,
        }

        return render(request, 'my_profile.html',  context)





def changes_my_profile(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')


        education  = request.POST.get('education')

        role = request.POST.get('role')

        address = request.POST.get('address')
        phone = request.POST.get('phone')


        print("inside changes_my_profile function ")
        print("fname => ",first_name)
        print("midname => ", middle_name)
        print("lname => ", last_name)
        print("email => ",email)
        print("education =>  ",education)
        print("role =>",  role)
        print("address =>", address)
        print("phone =>", phone)
        print("staff_id =>", staff_id)

        all_staff = staff.objects.all()

        staff_instance = get_object_or_404(staff, pk=staff_id)

        # Update the staff instance fields
        staff_instance.first_name = first_name
        staff_instance.middle_name = middle_name
        staff_instance.last_name = last_name


        if staff_instance.email != email:
            staff_instance.email = email
        staff_instance.education = education

        if role == "STAFF":
            staff_instance.role = 1
        elif role == "HR":
            staff_instance.role = 2

        staff_instance.address = address

        existing_staff = staff.objects.filter(phone=phone).exclude(staff_id=staff_id)
        if existing_staff.exists():
            # If email already exists, add a danger message
            messages.error(request, 'Phone Number is already  exist')
            return edit_my_profile(request)

        staff_instance.phone = phone

        # Save the changes
        staff_instance.save()

        print("Changes save")

    messages.success(request, 'Profile Edited Successfully')
    return edit_my_profile(request)






















from .models import staff, account_details

def account_details_edit(request):

    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        bank_name = request.POST.get('bank_name')
        branch_name = request.POST.get('branch_name')
        ifsc_code = request.POST.get('ifsc_code')
        account_no = request.POST.get('account_no')
        pan_no = request.POST.get('pan_no')
        adhar_no = request.POST.get('adhar_no')

        # Fetch staff instance
        print("inside the account_details_edit")
        print("staff id ", staff_id)
        print("bank name ", bank_name)
        print("branch name ", branch_name)
        print("ifsc code ", ifsc_code)
        print("account no", account_no)
        print("pan no ", pan_no)
        print("adhar no", adhar_no)

        # Fetch staff instance
        staff_member = get_object_or_404(staff, staff_id=staff_id)

        # Fetch account details associated with the staff
        account_details_instance = account_details.objects.filter(staff_id=staff_member).first()





        context = {
            'staff_member': staff_member,
            'account_details': account_details_instance,
        }

        return render(request, 'edit_account.html', context)








def changes_account(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        bank_name = request.POST.get('bank_name')
        branch_name = request.POST.get('branch_name')
        ifsc_code = request.POST.get('ifsc_code')
        account_no = request.POST.get('account_no')
        pan_no = request.POST.get('pan_no')
        adhar_no = request.POST.get('adhar_no')

        base_salary = request.POST.get('base_salary')

        # Fetch staff instance
        print("inside the changes_account ")
        print("staff id ", staff_id)
        print("bank name ", bank_name)
        print("branch name ", branch_name)
        print("ifsc code ", ifsc_code)
        print("account no", account_no)
        print("pan no ", pan_no)
        print("adhar no", adhar_no)

        print('base_salary ',base_salary)

        # Fetch staff instance
        staff_instance = staff.objects.get(staff_id=staff_id)

        # Check for existing records for each field
        if ifsc_code and account_details.objects.filter(ifsc_code=ifsc_code).exclude(staff_id=staff_instance).exists():
            messages.error(request, 'IFSC code already exists.')
            return account_details_edit(request)
            # return render(request, 'edit_account.html')

        if account_no and account_details.objects.filter(account_no=account_no).exclude(
                staff_id=staff_instance).exists():
            messages.error(request, 'Account number already exists.')
            return account_details_edit(request)
            # return render(request, 'edit_account.html')

        if pan_no and account_details.objects.filter(pan_no=pan_no).exclude(staff_id=staff_instance).exists():
            messages.error(request, 'PAN number already exists.')
            return account_details_edit(request)
            # return render(request, 'edit_account.html')

        if adhar_no and account_details.objects.filter(adhar_no=adhar_no).exclude(staff_id=staff_instance).exists():
            messages.error(request, 'Aadhar number already exists.')
            return account_details_edit(request)
            # return render(request, 'edit_account.html')

        # Update account_details instance
        account_details_instance, created = account_details.objects.get_or_create(staff_id=staff_instance)
        if bank_name:
            account_details_instance.bank_name = bank_name
        if branch_name:
            account_details_instance.branch_name = branch_name
        if ifsc_code:
            account_details_instance.ifsc_code = ifsc_code
        if account_no:
            account_details_instance.account_no = account_no
        if pan_no:
            account_details_instance.pan_no = pan_no
        if adhar_no:
            account_details_instance.adhar_no = adhar_no

        if base_salary:
            account_details_instance.base_salary_per_hr = base_salary

        account_details_instance.save()

        messages.success(request, 'Account Details  Successfully')
        return employee_details(request)







from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

import os

# Assuming the path to your user image directory
USER_IMG_DIR = 'D:/ClothFlow/ClothFlow/static/user_img'

def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage(location=USER_IMG_DIR)


        # Assuming you have authenticated user and accessed via request.user

        staff_id = request.POST.get('staff_id')

        user = staff.objects.get(staff_id=staff_id)
        user.profile_image = image
        user.save()

        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        messages.success(request, 'Image uploaded successfully: ')
    else:
        messages.error(request, 'No image file uploaded.')
    return edit_profile_user(request)







from django.http import HttpResponse
from .models import leave_request
from .models import staff
from django.utils import timezone
from django.contrib import messages

def leave_request_submit(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        reason = request.POST.get('reason')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = 'pending'

        # Retrieve the staff object
        staff_obj = staff.objects.get(staff_id=staff_id)

        # Check if there are overlapping leave requests
        overlapping_leave_requests = leave_request.objects.filter(
            staff=staff_obj,
            start_date__lte=end_date,
            end_date__gte=start_date
        )

        if overlapping_leave_requests.exists():
            # Overlapping leave requests found, show appropriate message
            messages.error(request, 'You already have leave scheduled during this period.')
        else:
            # No overlapping leave requests, create a new leave request instance
            new_leave_request = leave_request.objects.create(
                staff=staff_obj,
                reason=reason,
                start_date=start_date,
                end_date=end_date,
                status=status
            )
            new_leave_request.save()
            messages.success(request, 'Leave request submitted successfully!')

    # Redirect back to the page where leave request was submitted from
    return display_leave_request(request)






def display_leave_request(request):
    current_user = request.user
    staff_member = staff.objects.get(user=current_user)

    print('inside leave_request ')


    context = {
        'staff_member': staff_member
    }

    return render(request,'leave_request.html',context)



def leave_request_list_display_staff(request):
    current_user = request.user
    staff_member = staff.objects.get(user=current_user)
    staff_id = staff_member.staff_id

    # Fetch all leave requests for the current staff member
    leave_content = leave_request.objects.filter(staff_id=staff_id)

    print('inside leave_request_list_display_staff')
    # print(staff_id)
    # for leave in leave_content:
    #     print(leave.reason)

    context = {
        'staff_member': staff_member,
        'leave_content': leave_content
    }

    return render(request, 'leave_request_list_staff.html', context)





def leave_request_list_display_hr(request):
    current_user = request.user
    staff_member = staff.objects.get(user=current_user)

    # Exclude leave requests where the staff is the currently logged-in user
    leave_content = leave_request.objects.exclude(staff=staff_member)

    print('inside leave_request_list_display_hr')

    context = {
        'leave_content': leave_content
    }

    return render(request, 'leave_request_list_hr.html', context)

from django.core.mail import send_mail
from django.conf import settings

def leave_approve_reject_from_hr(request):
    if request.method == "POST":
        leave_id = request.POST.get('leave_id')
        canceled = request.POST.get('canceled')
        approved = request.POST.get('approved')
        message = request.POST.get('message')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        print('inside leave_approve_reject_from_hr')
        print(leave_id)
        print(canceled)
        print(approved)
        print(message)

        # Fetch the leave request object based on staff_id
        leave_request_instance = leave_request.objects.get(leave_id=leave_id)
        leave_request_instance.reject_reason = message

        first_name = leave_request_instance.staff.first_name
        last_name = leave_request_instance.staff.last_name
        contact_no = leave_request_instance.staff.phone
        reason = leave_request_instance.reason

        email = leave_request_instance.staff.email


        # Update the status field based on the received values
        if canceled is not None:
            leave_request_instance.status = 'canceled'
            leave_request_instance.review_by = 'HR'

            subject = 'Leave Request Approved'
            email_message = "Hi {} {},\n\nYour leave request for {} from {} to {} has been approved.\n\nWe hope you enjoy your time off and return refreshed. If you have any further questions or require additional information, please contact HR at {}.\n\nPlease remember to complete any necessary tasks or handover procedures before your leave begins.\n\nThank you, and have a great day!\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection".format(
                first_name,last_name,reason,start_date,end_date , contact_no
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]  # Assuming staff member has an email field
            send_mail(subject, email_message, from_email, recipient_list)

        elif approved is not None:
            leave_request_instance.status = 'approved'
            leave_request_instance.review_by = 'HR'

            subject = 'Leave Request Approved'
            email_message = "Hi {} {},\n\nYour leave request for {} from {} to {} has been approved.\n\nWe hope you enjoy your time off and return refreshed. If you have any further questions or require additional information, please contact HR at {}.\n\nPlease remember to complete any necessary tasks or handover procedures before your leave begins.\n\nThank you, and have a great day!\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection".format(
                first_name,last_name, reason , start_date,end_date , contact_no
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]  # Assuming staff member has an email field
            send_mail(subject, email_message, from_email, recipient_list)

        # Save the updated leave request object
        leave_request_instance.save()

        # Redirect to the HR leave request list display page
        return leave_request_list_display_hr(request)



def leave_request_list_display_admin(request):

    leave_content = leave_request.objects.all()

    print('inside leave_request_list_display_hr')

    context = {
        'leave_content': leave_content
    }

    return render(request, 'leave_request_list_admin.html', context)




def leave_approve_reject_from_admin(request):
    if request.method == "POST":
        leave_id = request.POST.get('leave_id')
        canceled = request.POST.get('canceled')
        approved = request.POST.get('approved')
        message = request.POST.get('message')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')


        # print('inside leave_approve_reject_from_admin')
        # print(leave_id)
        # print(canceled)
        # print(approved)

        # Fetch the leave request object based on staff_id
        leave_request_instance = leave_request.objects.get(leave_id=leave_id)
        leave_request_instance.reject_reason = message

        first_name = leave_request_instance.staff.first_name
        last_name = leave_request_instance.staff.last_name
        reason = leave_request_instance.reason

        email = leave_request_instance.staff.email

        # Update the status field based on the received values
        if canceled is not None:
            leave_request_instance.status = 'canceled'
            leave_request_instance.review_by = 'Admin'

            subject = 'Leave Request Rejected'
            email_message = "Hi {} {},\n\nWe regret to inform you that your leave request for {} from {} to {} has been rejected.\n\n Reason for Rejection: {}.\n\nWe understand this might be disappointing, and we encourage you to discuss alternative dates or other options with [Contact Person/HR Department] at 9657827062 .\n\nThank you for your understanding, and please let us know if you have any questions or concerns.\n\nThank you, and have a great day!\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection".format(
                first_name, last_name, reason, start_date, end_date , message
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]  # Assuming staff member has an email field
            send_mail(subject, email_message, from_email, recipient_list)



        elif approved is not None:
            leave_request_instance.status = 'approved'
            leave_request_instance.review_by = 'Admin'



            subject = 'Leave Request Approved'
            email_message = "Hi {} {},\n\nYour leave request for {} from {} to {} has been approved.\n\nWe hope you enjoy your time off and return refreshed. If you have any further questions or require additional information, please contact Admin at 9657827062.\n\nPlease remember to complete any necessary tasks or handover procedures before your leave begins.\n\nThank you, and have a great day!\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection".format(
                first_name, last_name, reason, start_date, end_date
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, email_message, from_email, recipient_list)



        # Save the updated leave request object
        leave_request_instance.save()

        # Redirect to the HR leave request list display page
        return leave_request_list_display_admin(request)



def display_total_employees(request):

    print("inside display_total_staff")
    all_staff = staff.objects.all()

    context = {
        'all_staff': all_staff
    }

    return render(request,'display_total_employees.html',context)



import xlwt

def download_staff_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="staff_data.xls"'

    # Create Excel workbook and sheet
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Staff Data')

    # Define column headers
    headers = [
        'SR. NO',
        'First Name',
        'Middle Name',
        'Last Name',
        'Email',
        'Role',
        'Phone',
        'Address',
        'Education',
    ]

    # Write column headers to the first row
    for col_num, header in enumerate(headers):
        ws.write(0, col_num, header)

    # Write staff data to rows
    staff_data = staff.objects.all()
    for row_num, staff_member in enumerate(staff_data, start=1):
        ws.write(row_num, 0, row_num)  # SR. NO
        ws.write(row_num, 1, staff_member.first_name)
        ws.write(row_num, 2, staff_member.middle_name)
        ws.write(row_num, 3, staff_member.last_name)
        ws.write(row_num, 4, staff_member.email)
        if staff_member.role == 1:
            ws.write(row_num, 5, 'STAFF')
        else:
            ws.write(row_num, 5, 'HR')
        ws.write(row_num, 6, staff_member.phone)
        ws.write(row_num, 7, staff_member.address)
        ws.write(row_num, 8, staff_member.education)

    # Save the workbook to the response
    wb.save(response)
    return response







def custom_404_view(request, exception):
    return render(request, '404.html', status=404)



