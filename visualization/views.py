from django.shortcuts import render
from django.db.models import Sum
import json
from decimal import Decimal
from bills.models import Invoice
from home.models import staff
from inventory.models import Product , Category , Section
from attendance.models import Attendance

def invoice_chart(request):
    # Retrieve data
    print('inside invoice_chart')
    data = list(Invoice.objects.values('invoice_date').annotate(total_amount=Sum('final_amount')).order_by('invoice_date'))

    # Convert Decimal objects to float
    for item in data:
        item['total_amount'] = float(item['total_amount'])

    # Convert datetime.date to string
    for item in data:
        item['invoice_date'] = item['invoice_date'].strftime('%Y-%m-%d')

    # Serialize data
    serialized_data = json.dumps(data)

    return render(request, 'invoice_chart.html', {'data': serialized_data})




def inventory_levels(request):
    inventory_levels_data = list(
        Product.objects.values('product_name')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('total_quantity')[:7]
    )

    # Serialize data
    serialized_data_inventory_levels = json.dumps(inventory_levels_data)
    return render(request,'inventory_levels.html', {'data': serialized_data_inventory_levels})




from django.db.models import Count, Sum, Case, When, F, ExpressionWrapper, FloatField , IntegerField
from django.db.models.functions import ExtractHour, ExtractMinute, ExtractSecond
from django.shortcuts import render
from datetime import datetime
import json

def attendance_summary(request):
    # Define working hour and total hours in the month
    working_hour = 10  # 10 hours (9:00 AM - 7:00 PM)
    total_hrs_in_month = 260  # Assuming 260 hours in a month

    # Get the current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Query to calculate attendance summary for the current month
    attendance_summary = Attendance.objects \
        .filter(date__month=current_month, date__year=current_year) \
        .annotate(
            total_attendance=Count('attendance_id'),
            total_working_seconds=Sum(
                Case(
                    When(attendance_status='present', then=ExtractHour(F('outtime')) * 3600 +
                                                         ExtractMinute(F('outtime')) * 60 +
                                                         ExtractSecond(F('outtime')) -
                                                         ExtractHour(F('intime')) * 3600 -
                                                         ExtractMinute(F('intime')) * 60 -
                                                         ExtractSecond(F('intime'))),
                    default=0,
                    output_field=IntegerField(),
                )
            )
        ) \
        .values('staff__first_name', 'staff__last_name') \
        .annotate(
            total_working_hours=ExpressionWrapper(
                F('total_working_seconds') / 3600,
                output_field=FloatField()
            ),
            attendance_percentage=ExpressionWrapper(
                (F('total_working_hours') / total_hrs_in_month) * 100,
                output_field=FloatField()
            ),
        ) \
        .order_by('staff__first_name', 'staff__last_name')

    # Serialize data
    serialized_data = list(attendance_summary.values('staff__first_name', 'staff__last_name', 'total_working_hours', 'attendance_percentage'))

    # Convert attendance percentage to two digits after the decimal point
    for entry in serialized_data:
        entry['attendance_percentage'] = round(entry['attendance_percentage'], 2)

    # Serialize data
    serialized_data = json.dumps(list(attendance_summary))


    return render(request, 'attendance_summary.html', {'data': serialized_data})












def section_chart(request):
    # Retrieve data
    sections = Section.objects.annotate(num_categories=Count('category'))

    # Serialize data
    serialized_data = json.dumps([{'section_name': section.section_name, 'num_categories': section.num_categories} for section in sections])

    return render(request, 'section_chart.html', {'data': serialized_data})


def category_chart(request):
    # Retrieve data
    categories = Category.objects.annotate(num_products=Count('product'))

    # Serialize data
    serialized_data = json.dumps([{'category_name': category.category_name, 'num_products': category.num_products} for category in categories])
    # print(serialized_data)

    return render(request, 'category_chart.html', {'data': serialized_data})











# calculating panelty and bonuse Hours



from django.shortcuts import render

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

def attendance_chart(request):
    staff_hours = calculate_staff_hours()
    penalty_bonus = calculate_penalty_bonus(staff_hours)

    context = {
        'penalty_bonus': penalty_bonus
    }

    return render(request, 'attendance_chart.html', context)

