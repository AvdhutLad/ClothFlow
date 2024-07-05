from django.shortcuts import render
from home.models import staff  # Import the staff model
from .models import Attendance
from django.utils import timezone
from django.contrib import messages
from datetime import date

# def display_attendance(request):
#     all_staff = staff.objects.all()
#     attendance_records = Attendance.objects.filter(date=date.today())
#
#     print("inside display_attendance ")
#     context = {
#         'staff_members': all_staff,
#         'attendance_records': attendance_records
#     }
#
#     return render(request, 'attendance.html', context)
#




from datetime import date

def display_attendance(request):
    all_staff = staff.objects.all()
    selected_date = date.today()
    attendance_records = Attendance.objects.filter(date=selected_date)

    attendance_dict = {}  # Dictionary to store attendance records with staff_id as keys
    for attendance_record in attendance_records:
        attendance_dict[attendance_record.staff_id] = attendance_record

    context = {
        'staff_members': all_staff,
        'attendance_dict': attendance_dict,
        'selected_date': selected_date,
    }

    return render(request, 'attendance.html', context)




def mark_attendance(request):
    all_staff = staff.objects.all()

    context = {
        'staff_members': all_staff  # Rename to 'staff_members' for clarity
    }

    return render(request, 'attendance.html', context)


from django.utils import timezone


from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from .models import Attendance  # Make sure to import your Attendance model

def save_attendance(request):
    if request.method == 'POST':
        date = request.POST.get('date')  # Get the date from the form
        staff_members = request.POST.getlist('staff_id')  # Get the list of staff IDs from the form

        for staff_id in staff_members:
            in_time = request.POST.get('inTime_{}'.format(staff_id))  # Get the in-time for the current staff member
            out_time = request.POST.get('outTime_{}'.format(staff_id))  # Get the out-time for the current staff member
            attendance_status = request.POST.get('attendance_{}'.format(staff_id))  # Get the attendance status for the current staff member

            # Check if an attendance record exists for the staff member on the given date
            attendance_record = Attendance.objects.filter(date=date, staff_id=staff_id).first()

            if attendance_record:
                # Update the existing attendance record
                attendance_record.intime = in_time
                attendance_record.outtime = out_time
                attendance_record.attendance_status = attendance_status
                attendance_record.save()
            else:
                # Create a new attendance record
                Attendance.objects.create(
                    staff_id=staff_id,
                    date=date,
                    intime=in_time,
                    outtime=out_time,
                    attendance_status=attendance_status,
                    created_at=timezone.now()
                )

        # Redirect to a success page or render a success message
        messages.success(request, "Attendance saved successfully!")
        return redirect('view_attendance')  # Change to your actual view name or URL

    # If the request method is not POST, redirect to the display attendance page
    return redirect('display_attendance')  # Change to your actual view name or URL











# from django.shortcuts import redirect
# from django.contrib import messages
# from django.utils import timezone
#
# def save_attendance(request):
#     if request.method == 'POST':
#         date = request.POST.get('date')  # Get the date from the form
#         staff_members = request.POST.getlist('staff_id')  # Get the list of staff IDs from the form
#
#         # Check if attendance records exist for the selected date
#         existing_attendance_records = Attendance.objects.filter(date=date)
#
#         if existing_attendance_records.exists():
#             # Update existing attendance records
#             for staff_id in staff_members:
#                 in_time = request.POST.get('inTime_{}'.format(staff_id))  # Get the in-time for the current staff member
#                 out_time = request.POST.get('outTime_{}'.format(staff_id))  # Get the out-time for the current staff member
#                 attendance_status = request.POST.get('attendance_{}'.format(staff_id))  # Get the attendance status for the current staff member
#
#                 # Update the existing attendance record
#                 attendance_record = existing_attendance_records.filter(staff_id=staff_id).first()
#                 if attendance_record:
#                     attendance_record.intime = in_time
#                     attendance_record.outtime = out_time
#                     attendance_record.attendance_status = attendance_status
#                     attendance_record.save()
#                 else:
#                     # Handle case where there's no existing record for the staff member
#                     # Optionally, you could create a new record or log this case
#                     messages.warning(request, "No existing attendance record found for staff ID {} on {}".format(staff_id,date))
#         else:
#             # Create new attendance records
#             for staff_id in staff_members:
#                 in_time = request.POST.get('inTime_{}'.format(staff_id))  # Get the in-time for the current staff member
#                 out_time = request.POST.get('outTime_{}'.format(staff_id))  # Get the out-time for the current staff member
#                 attendance_status = request.POST.get('attendance_{}'.format(staff_id))  # Get the attendance status for the current staff member
#
#                 # Create and save the attendance record
#                 Attendance.objects.create(
#                     staff_id=staff_id,
#                     date=date,
#                     intime=in_time,
#                     outtime=out_time,
#                     attendance_status=attendance_status,
#                     created_at=timezone.now()
#                 )
#
#                 # Optionally, you can perform additional processing or validation here
#
#         # Redirect to a success page or render a success message
#         messages.success(request, "Attendance saved successfully!")
#         return redirect('view_attendance')  # Change to your actual view name or URL
#
#     # If the request method is not POST, redirect to the display attendance page
#     return redirect('display_attendance')  # Change to your actual view name or URL


#
# def save_attendance(request):
#     if request.method == 'POST':
#         date = request.POST.get('date')  # Get the date from the form
#         staff_members = request.POST.getlist('staff_id')  # Get the list of staff IDs from the form
#
#         # Check if attendance records exist for the selected date
#         existing_attendance_records = Attendance.objects.filter(date=date)
#
#         if existing_attendance_records.exists():
#             # Update existing attendance records
#             for staff_id in staff_members:
#                 in_time = request.POST.get('inTime_{}'.format(staff_id))  # Get the in-time for the current staff member
#                 out_time = request.POST.get('outTime_{}'.format(staff_id))  # Get the out-time for the current staff member
#                 attendance_status = request.POST.get('attendance_{}'.format(staff_id))  # Get the attendance status for the current staff member
#
#                 # Update the existing attendance record
#                 attendance_record = existing_attendance_records.filter(staff_id=staff_id).first()
#                 attendance_record.intime = in_time
#                 attendance_record.outtime = out_time
#                 attendance_record.attendance_status = attendance_status
#                 attendance_record.save()
#         else:
#             # Create new attendance records
#             for staff_id in staff_members:
#                 in_time = request.POST.get('inTime_{}'.format(staff_id))  # Get the in-time for the current staff member
#                 out_time = request.POST.get('outTime_{}'.format(staff_id))  # Get the out-time for the current staff member
#                 attendance_status = request.POST.get('attendance_{}'.format(staff_id))  # Get the attendance status for the current staff member
#
#                 # Create and save the attendance record
#                 attendance = Attendance.objects.create(
#                     staff_id=staff_id,
#                     date=date,
#                     intime=in_time,
#                     outtime=out_time,
#                     attendance_status=attendance_status,
#                     created_at=timezone.now()
#                 )
#
#                 # Optionally, you can perform additional processing or validation here
#
#         # Redirect to a success page or render a success message
#         messages.success(request, "Attendance saved successfully!")
#         return view_attendance(request)
#
#     # If the request method is not POST, redirect to the display attendance page
#     return display_attendance(request)
#








from datetime import datetime
from datetime import date

def view_attendance(request):
    if request.method == 'POST':
        print('inside view_attendance')
        date = request.POST.get('date')

        if date:
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d').date()

                attendance_records = Attendance.objects.filter(date=date_obj)
                if attendance_records.exists():
                    context = {'attendance_records': attendance_records,
                               'date': date_obj
                               }
                    return render(request, 'view_attendance.html', context)
                else:
                    messages.info(request, 'No attendance records found for the selected date.')
            except ValueError:
                messages.error(request, 'Invalid date format. Please enter the date in yyyy-mm-dd format.')
        else:
            messages.error(request, 'Please provide a date.')


    else:

        date = datetime.today().date()  # Get today's date

        attendance_records = Attendance.objects.filter(date=date)

        if attendance_records.exists():

            context = {

                'attendance_records': attendance_records,

                'date': date

            }

            return render(request, 'view_attendance.html', context)

        else:

            messages.info(request, 'No attendance records found for the selected date.')

    return render(request, 'view_attendance.html')


# views.py

from django.http import HttpResponse
import pandas as pd


def download_attendance_excel(request):
    month = request.GET.get('month')

    # Filter attendance data based on the input month
    attendance_data = Attendance.objects.filter(date__month=month)

    # Define column names
    columns = ['SR.NO', 'Employee ID', 'Employee Name', 'Employee Role', 'Date','In Time', 'Out Time', 'Attendance']

    # Initialize data for Excel sheet
    data = []
    for idx, attendance in enumerate(attendance_data, start=1):
        # Determine the employee role
        employee_role = 'STAFF' if attendance.staff.role == 1 else 'HR'

        # Combine first name and last name for employee name
        employee_name = "{} {}".format(attendance.staff.first_name,attendance.staff.last_name)
        # print("emp name ",employee_name,"   role ",employee_role)
        data.append([
            idx,
            attendance.staff.staff_id,
            employee_name,
            employee_role,
            attendance.date,
            attendance.intime.strftime('%H:%M'),  # Format time as HH:MM
            attendance.outtime.strftime('%H:%M'),  # Format time as HH:MM
            attendance.attendance_status.capitalize()  # Capitalize attendance status
        ])

    # Create DataFrame from data
    df = pd.DataFrame(data, columns=columns)

    # Create Excel file
    excel_file_path = 'attendance_data.xlsx'
    df.to_excel(excel_file_path, index=False)

    # Prepare response with the Excel file
    response = HttpResponse(open(excel_file_path, 'rb'), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="attendance_data.xlsx"'

    return response





def download_attendance_excel_year(request):

    current_year = datetime.now().year
    print('in download_attendance_excel_year')
    # Filter attendance data based on the input month
    attendance_data = Attendance.objects.filter(date__year=current_year)

    # Define column names
    columns = ['SR.NO', 'Employee ID', 'Employee Name', 'Employee Role', 'Date','In Time', 'Out Time', 'Attendance']

    # Initialize data for Excel sheet
    data = []
    for idx, attendance in enumerate(attendance_data, start=1):
        # Determine the employee role
        employee_role = 'STAFF' if attendance.staff.role == 1 else 'HR'

        # Combine first name and last name for employee name
        employee_name = "{} {}".format(attendance.staff.first_name,attendance.staff.last_name)
        # print("emp name ",employee_name,"   role ",employee_role)
        data.append([
            idx,
            attendance.staff.staff_id,
            employee_name,
            employee_role,
            attendance.date,
            attendance.intime.strftime('%H:%M'),  # Format time as HH:MM
            attendance.outtime.strftime('%H:%M'),  # Format time as HH:MM
            attendance.attendance_status.capitalize()  # Capitalize attendance status
        ])

    # Create DataFrame from data
    df = pd.DataFrame(data, columns=columns)

    # Create Excel file
    excel_file_path = 'attendance_data_yearly.xlsx'
    df.to_excel(excel_file_path, index=False)

    # Prepare response with the Excel file
    response = HttpResponse(open(excel_file_path, 'rb'), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="attendance_data_yearly.xlsx"'

    return response