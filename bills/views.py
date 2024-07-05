from django.shortcuts import render
from home.models import staff
from inventory.models import Section , Category , Brand ,Product
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from .models import Customer, Invoice, InvoiceItem
def generate_invoice(request):
    product_details = Product.objects.all()
    context = {
        'product_details': product_details,
    }
    return render(request, 'billing.html', context)



def get_product_price(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
            return JsonResponse({'price': product.price})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)



def get_product_quantity(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
            return JsonResponse({'quantity': product.quantity})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)







def search_customer(request):
    if request.method == 'GET':
        customer_email = request.GET.get('email')
        try:
            customer = Customer.objects.get(email=customer_email)
            data = {
                'customer_name': customer.customer_name,
                'contacts': customer.contact
            }
            return JsonResponse(data)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)






from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Billing



from .models import Invoice, InvoiceItem
from django.shortcuts import get_object_or_404

@login_required
def submit_invoice(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        prices = request.POST.getlist('price')
        quantities = request.POST.getlist('quantity')
        product_ids = request.POST.getlist('product_id')

        print('submit_invoice')
        # Get the customer instance based on the provided customer_name
        customer = Customer.objects.get(email=email)

        user = request.user
        staff_instance = staff.objects.get(user=user)
        staff_id = staff_instance.staff_id

        # Calculate total_amount
        total_amount = sum(float(price) for price in prices)

        # Set final_amount initially as total_amount (assuming no discounts or taxes)
        final_amount = total_amount

        # Create the Invoice instance with the current date
        invoice = Invoice.objects.create(
            invoice_date=timezone.now(),
            total_amount=total_amount,
            final_amount=final_amount,
            payment_status='UNPAID',
            customer_id=customer.customer_id,
            staff_id=staff_id
        )


        total_amount = 0  # Total amount for the invoice

        # Iterate over each product
        for price, quantity, product_id in zip(prices, quantities, product_ids):
            product = get_object_or_404(Product, pk=product_id)
            price = float(price)
            quantity = int(quantity)

            total = price * quantity
            total_amount += total  # Increment total amount for the invoice

            # Update product quantity
            product.quantity -= quantity

            # Warn if quantity is low
            if product.quantity < 0:
                print("Warning: Quantity for {} is low!".format(product.product_name))
                messages.success(request, "Warning: Quantity for {} is low!".format(product.product_name))
                return generate_invoice(request)

            product.save()

            # Create InvoiceItem instance for each product
            InvoiceItem.objects.create(
                invoice=invoice,
                product=product,
                product_name=product.product_name,
                unit_price=price,
                quantity=quantity,
                total_price=total
            )

        # Update the total amount for the invoice
        invoice.total_amount = total_amount
        invoice.final_amount = total_amount  # Assuming no discount or tax initially
        invoice.save()

        print('Invoice and Invoice Items created successfully')


        return invoice_details(request,invoice.invoice_id, customer.customer_id)






from django.db.models import Sum
from decimal import Decimal
from .models import Customer, Invoice, InvoiceItem

from django.shortcuts import get_object_or_404

def invoice_details(request, invoice_id,customer_id):
    # Fetch customer details
    customer = get_object_or_404(Customer, customer_id=customer_id)

    # Fetch invoice details for the specified customer
    invoices = Invoice.objects.filter(invoice_id=invoice_id)

    # Prepare a list to store all invoice details
    all_invoice_details = []

    # Calculate tax amount for the first invoice (assuming only one invoice)
    tax_amount = invoices.first().final_amount * Decimal('0.12')  # 12% tax rate
    tax_amount = tax_amount.quantize(Decimal('0.00'))
    # Iterate over each invoice
    for invoice in invoices:
        # Fetch invoice items related to the invoice
        invoice_items = InvoiceItem.objects.filter(invoice=invoice)

        # Prepare a list to store the details for each invoice item
        items = []
        for item in invoice_items:
            items.append({
                'product_name': item.product_name,
                'unit_price': item.unit_price,
                'quantity': item.quantity,
                'total_price': item.total_price
            })

        # Append invoice details to the list
        invoice_details = {
            'invoice_id': invoice.invoice_id,
            'invoice_date': invoice.invoice_date,
            'total_amount': invoice.total_amount,
            'final_amount': invoice.final_amount,
            'payment_status': invoice.payment_status,
            'invoice_items': items
        }

        all_invoice_details.append(invoice_details)

    # Prepare context to pass to the template
    context = {
        'invoice_id':invoice_id,
        'customer_name': customer.customer_name,
        'email': customer.email,
        'contacts': customer.contact,
        'invoice_details': all_invoice_details,
        'tax_amount': tax_amount,

    }

    # Render the invoice.html template with the context
    return render(request, 'invoice.html', context)






from .models import Customer

def customer_details(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_mobile = request.POST.get('customer_mobile')

        try:
            # Check if the email already exists
            existing_customer = Customer.objects.get(email=customer_email)
            # If customer with the same email exists, show a message
            messages.error(request, "Customer with email {} already exists!".format(customer_email))
        except Customer.DoesNotExist:
            # Create a new customer object
            new_customer = Customer.objects.create(
                customer_name=customer_name,
                email=customer_email,
                contact=customer_mobile
            )
            # Show success message
            messages.success(request, "Customer  {} added successfully!".format(customer_name))

    return generate_invoice(request)




import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def pay_invoice(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id')
        discount = float(request.POST.get('discount', 0))
        tax_amount = float(request.POST.get('tax_amount', 0))
        sub_total = float(request.POST.get('sub_total', 0))

        print('inside pay_invoice')
        # Fetch the invoice object
        invoice = get_object_or_404(Invoice, invoice_id=invoice_id)

        # Update invoice details
        invoice.discount = discount
        invoice.tax = tax_amount

        discount = sub_total * (discount / 100)

        # Calculate after_discount
        invoice.after_discount = sub_total - discount

        # Calculate final_amount
        invoice.final_amount = sub_total + tax_amount - discount

        # Update payment status
        invoice.payment_status = 'PAID'

        invoice.payment_date = datetime.now().date()
        # Save the changes to the database
        invoice.save()


        # creating start

        return render(request,'ThankYou.html')
    else:
        # If the request method is not POST, handle accordingly
        messages.error(request,'Payment Fail')
        return generate_invoice(request)






# from django.shortcuts import render
# from .models import Invoice
# from django.db.models import Sum
# import json
# from decimal import Decimal
#
# def invoice_chart(request):
#     # Retrieve data
#     data = list(Invoice.objects.values('invoice_date').annotate(total_amount=Sum('final_amount')).order_by('invoice_date'))
#
#     # Convert Decimal objects to float
#     for item in data:
#         item['total_amount'] = float(item['total_amount'])
#
#     # Convert datetime.date to string
#     for item in data:
#         item['invoice_date'] = item['invoice_date'].strftime('%Y-%m-%d')
#
#     # Serialize data
#     serialized_data = json.dumps(data)
#
#     return render(request, 'invoice_chart.html', {'data': serialized_data})
#
#
#


#
# from django.shortcuts import render
# from django.contrib import messages
#
#
# def refund(request):
#     if request.method == 'POST':
#         bill_number = request.POST.get('billNumber')
#
#         if bill_number:
#             try:
#                 invoice = Invoice.objects.get(invoice_id=bill_number)
#
#                 # Access customer information
#                 customer_name = invoice.customer.customer_name
#                 email_address = invoice.customer.email
#
#                 # Purchase bill amount
#                 purchase_bill_amount = invoice.final_amount
#
#                 # Purchase date
#                 purchase_date = invoice.invoice_date
#
#                 # Access invoice items
#                 invoice_items = InvoiceItem.objects.filter(invoice=invoice)
#                 items_data = [{'product_name': item.product_name, 'quantity': item.quantity} for item in invoice_items]
#
#                 context = {
#                     'customer_name': customer_name,
#                     'email_address': email_address,
#                     'purchase_bill_amount': purchase_bill_amount,
#                     'purchase_date': purchase_date,
#                     'invoice_items': items_data
#                 }
#
#                 return render(request, 'refund.html', context)
#             except Invoice.DoesNotExist:
#                 messages.error(request, 'Invoice with the provided bill number does not exist.')
#         else:
#             messages.error(request, 'Please enter a bill number.')
#
#     return render(request, 'refund.html')
#
from django.http import JsonResponse

def refund(request):
    if request.method == 'POST':
        bill_number = request.POST.get('billNumber')

        if bill_number:
            try:
                invoice = Invoice.objects.get(invoice_id=bill_number)

                # Access customer information
                customer_name = invoice.customer.customer_name
                email_address = invoice.customer.email

                # Purchase bill amount
                purchase_bill_amount = invoice.final_amount

                # Purchase date
                purchase_date = invoice.invoice_date


                # Access invoice items
                invoice_items = InvoiceItem.objects.filter(invoice=invoice)
                items_data = [{'product_name': item.product_name, 'quantity': item.quantity, 'amount': item.unit_price} for
                              item in invoice_items]

                # # Access invoice items
                # invoice_items = InvoiceItem.objects.filter(invoice=invoice)
                # items_data = [{'product_name': item.product_name, 'quantity': item.quantity } for item in invoice_items]

                context = {
                    'customer_name': customer_name,
                    'email_address': email_address,
                    'purchase_bill_amount': purchase_bill_amount,
                    'purchase_date': purchase_date,
                    'invoice_items': items_data
                }

                return JsonResponse(context)
            except Invoice.DoesNotExist:
                return JsonResponse({'error': 'Invoice with the provided bill number does not exist!'}, status=404)
        else:
            return JsonResponse({'error': 'Please enter a bill number.'}, status=400)

    return render(request, 'refund.html')









from django.shortcuts import render
from .models import Return_and_refund , Defective
from .models import Invoice, Customer
from django.contrib import messages
from datetime import datetime

def store_return_and_refund(request):
    if request.method == 'POST':
        # Get data from the form
        # Get data from the form
        bill_number = request.POST.get('billNumber')
        customer_name = request.POST.get('customerName')
        email_address = request.POST.get('email')
        purchase_bill_amount = request.POST.get('billAmount')
        purchase_date = request.POST.get('purchasedDate')
        product_name = request.POST.get('product')
        quantity = request.POST.get('quantity')
        action = request.POST.get('whatdoyouwanttodo')
        reason = request.POST.get('reason')
        # return_amount = request.POST.get('returnAmount')
        return_amount = request.POST.get('returnAmount',)
        # rejected_reason = request.POST.get('reason')
        transaction_complete_date = request.POST.get('purchasedDate')
        status = 'pending'

        # Convert date strings to datetime objects
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d').date()
        transaction_complete_date = datetime.strptime(transaction_complete_date, '%Y-%m-%d').date() if transaction_complete_date else None

        if return_amount == '':
            return_amount = 0




        # Get invoice and customer objects
        try:
            invoice = Invoice.objects.get(invoice_id=bill_number)
        except Invoice.DoesNotExist:
            messages.error(request, 'Invoice with the provided bill number does not exist.')
            return render(request, 'your_template.html')

        try:
            customer = Customer.objects.get(customer_name=customer_name, email=email_address)
        except Customer.DoesNotExist:
            messages.error(request, 'Customer with the provided name and email address does not exist.')
            return render(request, 'your_template.html')

        # Save data to the database
        try:
            Return_and_refund.objects.create(
                date=datetime.now().date(),
                invoice=invoice,
                customer=customer,
                product_name=product_name,
                quantity=int(quantity),
                action=action,
                reason=reason,
                return_amount=float(return_amount),
                # rejected_reason=rejected_reason,
                status = status,
                transaction_complete_date=transaction_complete_date
            )
            messages.success(request, 'Return and refund request send successfully!')
            return render(request, 'landing.html')

        except Exception as e:
            print(e)
            messages.error(request, 'An error occurred: {}'.format(str(e)))

    return render(request, 'refund.html')







def refund_request(request):

    refunds = Return_and_refund.objects.all()


    refund_data = []


    for refund in refunds:
        # Extract data
        transaction_id = refund.transaction_id

        customer_name = refund.customer.customer_name
        bill_number = refund.invoice.invoice_id
        purchase_date = refund.invoice.invoice_date
        product_name = refund.product_name
        quantity = refund.quantity
        purchase_amount = refund.invoice.final_amount
        action = refund.get_action_display()  # Get display value for action field
        reason = refund.reason
        return_amount = refund.return_amount
        status = refund.status

        # Append data to refund_data list
        refund_data.append({
            'transaction_id' : transaction_id,
            'customer_name': customer_name,
            'bill_number': bill_number,
            'purchase_date': purchase_date,
            'product_name': product_name,
            'quantity': quantity,
            'purchase_amount': purchase_amount,
            'action': action,
            'reason': reason,
            'return_amount': return_amount,
            'status': status,
        })

    # Pass refund_data to the template context
    context = {
        'refund_data': refund_data
    }

    return render(request, 'refund_request.html', context)


def refund_history(request):
    refunds = Return_and_refund.objects.all()
    refund_data = []


    for refund in refunds:
        # Extract data
        transaction_id = refund.transaction_id

        customer_name = refund.customer.customer_name
        bill_number = refund.invoice.invoice_id
        purchase_date = refund.invoice.invoice_date
        product_name = refund.product_name
        quantity = refund.quantity
        purchase_amount = refund.invoice.final_amount
        action = refund.get_action_display()  # Get display value for action field
        reason = refund.reason
        return_amount = refund.return_amount
        status = refund.status
        rejected_reason = refund.rejected_reason

        # Append data to refund_data list
        refund_data.append({
            'transaction_id' : transaction_id,
            'customer_name': customer_name,
            'bill_number': bill_number,
            'purchase_date': purchase_date,
            'product_name': product_name,
            'quantity': quantity,
            'purchase_amount': purchase_amount,
            'action': action,
            'reason': reason,
            'return_amount': return_amount,
            'status': status,
            'rejected_reason': rejected_reason,
        })

    # Pass refund_data to the template context
    context = {
        'refund_data': refund_data
    }

    return render(request, 'refund_history.html', context)



from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta


def refund_request_approve_reject(request):
    if request.method == "POST":
        transaction_id = request.POST.get('transaction_id')
        canceled = request.POST.get('canceled')
        approved = request.POST.get('approved')
        message = request.POST.get('message')
        action = request.POST.get('action')
        quantity = int(request.POST.get('quantity'))
        product_name = request.POST.get('product_name')


        print('inside refund_request_approve_reject ')
        # print('trasaction id ' , transaction_id)
        # print('cancled' ,canceled)
        # print('approved', approved)
        # print('message  ',message)
        # print('action   ',action)
        # print('quantity ',quantity)
        # print('product_name ',product_name)

        if message == '':
            message = None




        return_and_refund_instance = Return_and_refund.objects.get(transaction_id=transaction_id)

        product_instance = Product.objects.get(product_name=product_name)


        customer_name = return_and_refund_instance.customer.customer_name
        invoice_id = return_and_refund_instance.invoice.invoice_id

        email = return_and_refund_instance.customer.email
        print('Data Form Mailing ')
        print('customer name    ',customer_name)
        print('invoice_id  ',invoice_id)
        print('quantity  ',quantity)
        print('action  ',action)
        print('product_name ',product_name)

        if canceled is not None:

            subject = 'Your {} Request Has Been Rejected - Invoice #{}'.format(action,invoice_id)
            email_message = "Hi {},\n\nAfter reviewing your {} request for the following item(s), we regret to inform you that it has been rejected:\n\nProduct Name: {}\nQuantity: {}\n\nReason for Rejection: {}\n\nIf you believe this decision is incorrect or you have additional information that could change our assessment, please contact us at 9657827062. Our team will be happy to assist you.\n\nWe apologize for any inconvenience this may cause and appreciate your understanding.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection".format(
                customer_name, action,product_name,quantity,message
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]  # Assuming customer has an email field
            send_mail(subject, email_message, from_email, recipient_list)







            return_and_refund_instance.status = 'canceled'
            if action == 'Exchange':
                defective = Defective.objects.create(
                    transaction=return_and_refund_instance,
                    product_name=product_name,
                    quantity=quantity,
                    description=message
                )
                defective.save()
                return_and_refund_instance.rejected_reason = message

        elif approved is not None:

            start_date = datetime.now().strftime("%Y-%m-%d")
            end_date = (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")

            subject = 'Your {} Request Has Been Approved - Invoice #{}'.format(action,invoice_id)
            email_message = "Hi {},\n\nWe're pleased to inform you that your {} request for the following item(s) has been approved.\n\nProduct Name: {}\nQuantity: {}\n\nTo complete the {}, please visit our shop at Shri Collection between {} and {}. Be sure to bring a copy of your invoice or a form of identification to verify your request.\n\nIf you have any questions or need further assistance, feel free to contact us at 9657827062.\n\nThank you for choosing Shri Collection. We look forward to assisting you.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection".format(
                customer_name , action ,product_name,quantity,start_date,end_date,action
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, email_message, from_email, recipient_list)


            if action == 'Exchange':
                defective = Defective.objects.create(
                    transaction=return_and_refund_instance,
                    product_name=product_name,
                    quantity=quantity,
                    description=message
                )
                defective.save()

                if product_instance.quantity < quantity:
                    messages.error(request, 'Quantity is Low For {}'.format(product_name))
                    return refund_request(request)
                else:
                    print('inside action exchage approved quantity --')
                    product_instance.quantity = product_instance.quantity - quantity
                    product_instance.save()


            elif action == 'Refund':
                print('inside action exchage approved quantity ++ ')
                product_instance.quantity = product_instance.quantity + quantity
                product_instance.save()

            return_and_refund_instance.status = 'approved'


        return_and_refund_instance.save()

    return refund_request(request)




def invoices(request):
    invoice = Invoice.objects.all()
    context = {
        'invoice' : invoice
    }

    return render(request,'invoices.html' , context)
