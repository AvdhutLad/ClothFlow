from django.shortcuts import render
from home.models import staff, account_details

from attendance.models import Attendance
from .models import Salary
from django.db.models import Sum
from datetime import datetime , time
from django.contrib import messages


#
# def calculate_total_hours(intime, outtime):
#     intime_datetime = datetime.combine(datetime.today(), intime)
#     outtime_datetime = datetime.combine(datetime.today(), outtime)
#     # total_hours = (outtime_datetime - intime_datetime).seconds / 3600
#     total_hours = round((outtime_datetime - intime_datetime).seconds / 3600, 2)
#
#     return total_hours
#
#
# def salary_list(request):
#     if request.method == "POST":
#         month = int(request.POST.get('month'))
#         year = int(request.POST.get('year'))
#
#         print('inside salary_list')
#         print('month ',month)
#         print('year ',year)
#
#         try:
#
#
#             salaries = []
#             account_detail = account_details.objects.all()
#
#             for account in account_detail:
#                 staff = account.staff_id
#                 base_salary_per_hr = float(account.base_salary_per_hr)
#                 total_working_hours = 0
#                 total_amount = 0
#
#                 attendances = Attendance.objects.filter(staff=staff, date__month=month, date__year=year)
#                 for attendance in attendances:
#                     total_hours = calculate_total_hours(attendance.intime, attendance.outtime)
#                     total_working_hours += total_hours
#
#                 total_amount = round((total_working_hours * base_salary_per_hr),3)
#
#
#
#                 salaries.append({
#                     'account_id': account.account_id,
#                     'staff_id' : staff.staff_id,
#                     'first_name': staff.first_name,
#                     'last_name': staff.last_name,
#                     'role': staff.role,
#                     'total_working_hours':"{:.2f}".format(total_working_hours),
#                     'total_amount': "{:.2f}".format(total_amount)
#                 })
#
#             context = {
#                 'salaries': salaries,
#                 'month': month,
#                 'year': year
#             }
#             # print(salaries)
#         except:
#             messages.error(request, 'Error Occured!!.')
#             return render(request, 'salary_list.html')
#
#         return render(request, 'salary_list.html', context)
#
#     return render(request, 'salary_list.html')
#


def calculate_total_hours(intime, outtime):
    try:
        intime_datetime = datetime.strptime(str(intime), '%H:%M:%S')
        outtime_datetime = datetime.strptime(str(outtime), '%H:%M:%S')
        total_hours = (outtime_datetime - intime_datetime).seconds / 3600
        return total_hours
    except ValueError:
        return 0  # or handle the error as needed

def salary_list(request):
    if request.method == "POST":
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))

        print('inside salary_list')
        print(month)
        print(year)

        try:
            salaries = []
            account_details_list = account_details.objects.all()

            for account in account_details_list:
                staff = account.staff_id
                base_salary_per_hr = float(account.base_salary_per_hr)
                total_working_hours = 0
                total_amount = 0

                attendances = Attendance.objects.filter(staff=staff, date__month=month, date__year=year)
                for attendance in attendances:
                    total_hours = calculate_total_hours(attendance.intime, attendance.outtime)
                    total_working_hours += total_hours

                total_amount = round((total_working_hours * base_salary_per_hr), 2)

                salaries.append({
                    'account_id': account.account_id,
                    'staff_id': staff.staff_id,
                    'first_name': staff.first_name,
                    'last_name': staff.last_name,
                    'role': staff.role,
                    'total_working_hours': "{:.2f}".format(total_working_hours),
                    'total_amount': "{:.2f}".format(total_amount)
                })

            context = {
                'salaries': salaries,
                'month': month,
                'year': year
            }
        except Exception as e:
            messages.error(request, 'Error occurred: {}'.format(e))
            return render(request, 'salary_list.html')

        return render(request, 'salary_list.html', context)

    return render(request, 'salary_list.html')






def salary_slip(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        account_id = request.POST.get('account_id')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        total_working_hours = float(request.POST.get('total_working_hours'))
        total_amount = float(request.POST.get('total_amount'))




        try:
            staff_detail = staff.objects.get(staff_id=staff_id)
            account_detail = account_details.objects.get(account_id=account_id)




        except staff.DoesNotExist or account_details.DoesNotExist:
            messages.error(request, 'Staff or account details not found.')
            return render(request, 'salary_slip.html')

            # Constants
        hours_per_day = 10
        work_days_per_month = 26
        total_month_hours = hours_per_day * work_days_per_month

        # Calculate penalty hours and extra time hours
        if total_working_hours < total_month_hours:
            penalty_hours = total_month_hours - total_working_hours
            penalty_amount = penalty_hours * (float(account_detail.base_salary_per_hr) * 0.1)  # Apply 10% penalty rate
            extra_hours = 0
            extra_amount = 0
        elif total_working_hours > total_month_hours:
            penalty_hours = 0
            penalty_amount = 0
            extra_hours = total_working_hours - total_month_hours
            extra_amount = extra_hours * (float(account_detail.base_salary_per_hr) * 1.4)  # Apply 40% increase
        else:
            penalty_amount = 0
            penalty_hours = 0
            extra_hours = 0
            extra_amount = 0

        # Calculate gross salary
        gross_salary = total_amount - penalty_amount + extra_amount



        try:
            # Create a Salary instance and save it to the database
            salary_instance = Salary.objects.create(
                staff=staff_detail,
                account=account_detail,


                based_salary=account_detail.base_salary_per_hr,
                daily_working_hours=hours_per_day,
                month_hours=work_days_per_month,
                penalty_hours=round(penalty_hours , 3),
                penalty_amount=penalty_amount,
                extra_time=round(extra_hours , 3),
                bonus_amount=extra_amount,
                total_salary=total_amount,
                gross_salary=gross_salary,

            )
            salary_instance.save()
        except (staff.DoesNotExist, account_details.DoesNotExist, AttributeError) as e:
            messages.error(request, 'Error occurred: {}'.format(e))
            return render(request, 'salary_list.html')




        context = {
            'first_name':first_name,
            'last_name': last_name,
            'staff_id': staff_id,
            'email': staff_detail.email,
            'bank_name': account_detail.bank_name,
            'account_no': account_detail.account_no,
            'pan_no': account_detail.pan_no,
            'base_salary_per_hr': account_detail.base_salary_per_hr,
            'total_working_hours': total_working_hours,
            'penalty_hours':"{:.2f}".format( penalty_hours),
            'extra_hours':"{:.2f}".format( extra_hours),
            'penalty_amount' : "{:.2f}".format( penalty_amount ),
            'extra_amount': "{:.2f}".format(extra_amount),
            'total_amount' : "{:.2f}".format( total_amount),
            'gross_salary': "{:.2f}".format(gross_salary)
        }


        return render(request, 'salary_slip.html',context)




    return render(request,'salary_slip.html')



