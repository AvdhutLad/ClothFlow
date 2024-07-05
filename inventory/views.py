from django.shortcuts import render ,HttpResponse
from django.contrib import messages
from .models import Section , Category , Brand ,Product
from django.contrib.auth.decorators import login_required
from home.models import staff

def add_section(request):
    return render(request,'section_admin.html')
def add_category(request):
    section_details = Section.objects.all()

    context = {
        'section_details': section_details
    }
    return render(request,'category_admin.html',context)


def store_section(request):
    if request.method == "POST":
        section_name = request.POST.get('section_name')
        location = request.POST.get('location')
        description = request.POST.get('description')

        # Create a new instance of the Section model with the provided data
        new_section = Section.objects.create(
            section_name=section_name,
            location=location,
            description=description
        )

        # Save the new section to the database
        new_section.save()

        # Optionally, you can redirect to a success page or render a success message
        messages.success(request, 'Section created successfully!')
        return add_section(request)
    else:
        # Handle GET request
        return add_section(request)




# def store_category(request):
#     if request.method == "POST":
#         section_name = request.POST.get('section_name')
#         category_name = request.POST.get('category_name')
#         description = request.POST.get('description')
#
#         print('inside store_category')
#
#         print(section_name)
#         print(category_name)
#         print(description)
#
#     return add_category(request)

def store_category(request):
    if request.method == "POST":
        section_name = request.POST.get('section_name')
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')

        # Retrieve the section object corresponding to the provided section name
        section = Section.objects.get(section_name=section_name)

        # Create a new instance of the Category model with the retrieved section object and other provided data
        new_category = Category.objects.create(
            section=section,
            category_name=category_name,
            description=description
        )

        # Save the new category instance to the database
        new_category.save()

        # Optionally, you can redirect to a success page or render a success message
        messages.success(request, 'Category created successfully!')
        return add_category(request)
    else:
        # Handle GET request
        return add_category(request)


# from .models import Section, Category
#
# def store_category(request):
#     if request.method == "POST":
#         section_id = request.POST.get('section_id')  # Get the section_id instead of section_name
#         category_name = request.POST.get('category_name')
#         description = request.POST.get('description')
#
#         try:
#             # Retrieve the section object corresponding to the provided section_id
#             section = Section.objects.get(pk=section_id)
#
#             # Create a new instance of the Category model with the retrieved section object and other provided data
#             new_category = Category.objects.create(
#                 section=section,
#                 category_name=category_name,
#                 description=description
#             )
#
#             # Save the new category instance to the database
#             new_category.save()
#
#             # Optionally, you can redirect to a success page or render a success message
#             messages.success(request, 'Category created successfully!')
#             return add_category(request)
#         except Section.DoesNotExist:
#             # Handle the case where the provided section_id does not exist
#             messages.error(request, 'Section matching query does not exist.')
#             return add_category(request)
#
#     else:
#         # Handle GET request
#         return add_category(request)








def view_section(request):
    section_details = Section.objects.all()

    context = {
        'section_details': section_details
    }
    return render(request,'view_section.html',context)



def view_category(request):
    section_details = Section.objects.all()
    category_details =   Category.objects.all()

    context = {
        'section_details': section_details,
        'category_details': category_details,
    }

    return render(request,'view_category.html',context)






def edit_section(request):
    if request.method == "POST":
        print('inside edit_section ')
        section_id = request.POST.get('section_id')
        section_details = Section.objects.get(section_id=section_id)
        print(section_id)
        print(section_details.section_name)
        print(section_details.location)
        print(section_details.description)
        # return view_section(request)
        context = {
            'section_details': section_details
        }

    return render(request,'edit_item_section.html',context)





def save_changes_section(request):
    if request.method == "POST":
        print('inside save_changes_section')
        section_id = request.POST.get('section_id')
        section_name = request.POST.get('section_name')
        location = request.POST.get('location')
        description = request.POST.get('description')


        section = Section.objects.get(section_id=section_id)

        # Update the attributes
        section.section_name = section_name
        section.location = location
        section.description = description

        # Save the changes
        section.save()


        messages.success(request, 'Section updated successfully!')
        return view_section(request)


from .models import Section  # Import the Section model

def delete_section(request):
    if request.method == "POST":
        print('inside delete_section')
        section_id = request.POST.get('section_id')
        print(section_id)

        # Retrieve the Section object
        try:
            section = Section.objects.get(section_id=section_id)
        except Section.DoesNotExist:
            print("Section does not exist")
            messages.success(request, 'Section Not Found!Or Already Deleted')
            return view_section(request)
            # Handle the case where the section with the given ID does not exist

        # Delete the section
        section.delete()
        print("Section deleted successfully")
        messages.success(request, 'Section deleted successfully!')

    return view_section(request)


from django.shortcuts import render
from .models import Section  # Import the Section model

def delete_alert_section(request):
    if request.method == "POST":
        print('inside delete_alert_section')
        section_id = request.POST.get('section_id')
        print(section_id)

        # You can optionally retrieve other information related to the section if needed
        try:
            section_details = Section.objects.get(section_id=section_id)
        except Section.DoesNotExist:
            section_details = None
            print("Section does not exist")
            messages.success(request, 'Section Not Found! Or Already Deleted')
            return view_section(request)

        context = {
            'section_details': section_details
        }
        return render(request, 'delete_alert_section.html', context)




def edit_category(request):
    if request.method == "POST":
        print('inside edit_category ')
        category_id = request.POST.get('category_id')

        try:
            category = Category.objects.get(category_id=category_id)
            section_details = Section.objects.filter(category=category)  # Fetch all section details
            # Retrieve all details related to the category
            category_details = {
                'category_id': category.category_id,
                'section_id': category.section_id,
                'category_name': category.category_name,
                'description': category.description,
            }
        except Category.DoesNotExist:
            category_details = None
            print("Category does not exist")
            messages.success(request, 'Category Not Found!')
            return view_category(request)

        context = {
            'category_details': category_details,
            'section_details': section_details
        }
    return render(request, 'edit_item_category.html', context)



def save_changes_category(request):
    if request.method == "POST":
        print('inside save_changes_category')
        category_id = request.POST.get('category_id')
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')

        print(category_id)
        print(category_name)
        print(description)

        category = Category.objects.get(category_id=category_id)

        # Update the attributes
        category.category_name = category_name
        category.description = description

        # Save the changes
        category.save()

        messages.success(request, 'Category updated successfully!')
        return view_category(request)



def delete_alert_category(request):
    if request.method == "POST":
        print('inside delete_alert_category')
        category_id = request.POST.get('category_id')
        print(category_id)




        # You can optionally retrieve other information related to the section if needed
        try:
            category_details = Category.objects.get(category_id=category_id)
        except Section.DoesNotExist:
            category_details = None
            print("category does not exist")
            messages.success(request, 'Category  Not Found! Or Already Deleted')
            return view_category(request)

        context = {
            'category_details': category_details
        }

        return render(request, 'delete_alert_category.html',context)




def delete_category(request):
    if request.method == "POST":
        print('inside delete_category')
        category_id = request.POST.get('category_id')
        print(category_id)

        # Retrieve the Section object
        try:
            category = Category.objects.get(category_id=category_id)
        except Section.DoesNotExist:
            print("category does not exist")
            messages.success(request, 'category Not Found! Or Already Deleted')
            return view_category(request)
            # Handle the case where the section with the given ID does not exist

        # Delete the section
        category.delete()
        print("category deleted successfully")
        messages.success(request, 'Category deleted successfully!')

    return view_category(request)





def add_brand(request):
    return render(request,'brand.html')


def store_brand(request):
    if request.method == "POST":
        brand_name = request.POST.get('brand_name')
        description = request.POST.get('description')

        print('inside store_brand')

        if Brand.objects.filter(brand_name=brand_name).exists():
            # If brand already exists, add a danger message
            messages.error(request, 'Brand Name already exists')
            return render(request, 'brand.html')



        # Create a new instance of the Brand model with the provided data
        new_brand = Brand.objects.create(
            brand_name=brand_name,
            description=description
        )

        # Save the new brand instance to the database
        new_brand.save()

        # Optionally, you can redirect to a success page or render a success message
        messages.success(request, 'Brand created successfully!')
        return add_brand(request)

    else:
        # Handle GET request
        return add_brand(request)



#
# def view_brand(request):
#     return render(request,'view_brand.html')
#


def view_brand(request):
    brand_details = Brand.objects.all()


    context = {
        'brand_details': brand_details,

    }

    return render(request,'view_brand.html',context)


def edit_brand(request):
    if request.method == "POST":
        print('inside edit_brand ')
        brand_id = request.POST.get('brand_id')
        brand_details = Brand.objects.get(brand_id=brand_id)

        context = {
            'brand_details': brand_details
        }

    return render(request,'edit_item_brand.html',context)






def save_changes_brand(request):
    if request.method == "POST":
        print('inside save_changes_brand')
        brand_id = request.POST.get('brand_id')
        brand_name = request.POST.get('brand_name')
        description = request.POST.get('description')


        print(brand_id)
        print(brand_name)
        print(description)


        if Brand.objects.filter(brand_name=brand_name).exists():
            # If brand already exists, add a danger message
            messages.error(request, 'Brand Name already exists')
            return view_brand(request)



        brand = Brand.objects.get(brand_id=brand_id)

        # Update the attributes
        brand.brand_name = brand_name
        brand.description = description

        # Save the changes
        brand.save()

        messages.success(request, 'Brand updated successfully!')
        return view_brand(request)

    return view_brand(request)



def delete_alert_brand(request):
    if request.method == "POST":
        print('inside delete_alert_brand')
        brand_id = request.POST.get('brand_id')
        print(brand_id)


        try:
            brand_details = Brand.objects.get(brand_id=brand_id)
        except Section.DoesNotExist:
            brand_details = None
            print("Brand does not exist")
            messages.success(request, 'Brand Not Found! Or Already Deleted')
            return view_brand(request)

        context = {
            'brand_details': brand_details
        }
        return render(request, 'delete_alert_brand.html', context)



def delete_brand(request):
    if request.method == "POST":
        print('inside delete_brand')
        brand_id = request.POST.get('brand_id')
        print(brand_id)

        # Retrieve the Section object
        try:
            brand = Brand.objects.get(brand_id=brand_id)
        except Brand.DoesNotExist:
            print("Brand does not exist")
            messages.success(request, 'Brand Not Found! Or Already Deleted')
            return view_brand(request)
            # Handle the case where the section with the given ID does not exist

        # Delete the section
        brand.delete()
        print("Brand deleted successfully")
        messages.success(request, 'Brand deleted successfully!')

    return view_brand(request)





def add_product(request):
    section_details = Section.objects.all()
    category_details = Category.objects.all()
    brand_details = Brand.objects.all()

    context = {
        'section_details': section_details,
        'category_details':category_details,
        'brand_details':brand_details
    }
    return render(request,'product.html',context)


from django.shortcuts import redirect
from django.contrib import messages

def store_product(request):
    if request.method == "POST":
        section_id = request.POST.get('section')
        category_id = request.POST.get('category')
        brand_id = request.POST.get('brand')
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        purchase_date = request.POST.get('purchase_date')
        supplier_name = request.POST.get('supplier_name')

        current_user = request.user

        print('inside store_product ')
        try:
            # Retrieve Section, Category, and Brand objects by primary keys
            section = Section.objects.get(pk=section_id)
            category = Category.objects.get(pk=category_id)
            brand = Brand.objects.get(pk=brand_id)

            # Check if product with the same name already exists
            if Product.objects.filter(product_name=product_name).exists():
                messages.error(request,'A product is already exists.')
                return add_product(request)

            # Create and save the new Product instance
            new_product = Product.objects.create(
                section=section,
                category=category,
                brand=brand,
                product_name=product_name,
                price=price,
                quantity=quantity,
                purchase_date=purchase_date,
                supplier_name=supplier_name,
                added_by=current_user.username,
                updated_by=current_user.username
            )
            messages.success(request, 'Product added successfully.')
        except Section.DoesNotExist:
            messages.error(request, 'Invalid section selected.')
        except Category.DoesNotExist:
            messages.error(request, 'Invalid category selected.')
        except Brand.DoesNotExist:
            messages.error(request, 'Invalid brand selected.')


    return add_product(request)


def view_product(request):
    product_details = Product.objects.all()

    context = {
        'product_details': product_details
    }
    return render(request,'view_product_list.html',context)


from django.shortcuts import render, get_object_or_404



def edit_product(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')

        print('inside edit_product')
        # Fetch the product object based on the product_id
        product = get_object_or_404(Product, pk=product_id)

        # Extract details from the product object
        section_id =product.section.section_id
        category_id =product.category.category_id
        brand_id =product.brand.brand_id

        section_name = product.section.section_name
        category_name = product.category.category_name
        brand_name = product.brand.brand_name
        product_name = product.product_name
        price = product.price
        quantity = product.quantity
        purchase_date = product.purchase_date
        supplier_name = product.supplier_name



        section_details = Section.objects.exclude(section_id=section_id)
        category_details = Category.objects.exclude(category_id=category_id)
        brand_details = Brand.objects.exclude(brand_id=brand_id)


        # Pass the details to the template
        context = {

            'section_details':section_details,
            'category_details':category_details,
            'brand_details':brand_details,

            'product_id':product_id,
            'section_id':section_id,
            'category_id':category_id,
            'brand_id':brand_id,

            'section_name': section_name,
            'category_name': category_name,
            'brand_name': brand_name,
            'product_name': product_name,
            'price': price,
            'quantity': quantity,
            'purchase_date': purchase_date,
            'supplier_name': supplier_name,
        }

        return render(request, 'edit_item_product.html', context)




from django.shortcuts import render, get_object_or_404


def save_changes_product(request):
    if request.method == "POST":
        print('inside save_changes_product')

        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        section_id = request.POST.get('section')
        category_id = request.POST.get('category')
        brand_id = request.POST.get('brand')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        purchase_date = request.POST.get('purchase_date')
        supplier_name = request.POST.get('supplier_name')
        update_note = request.POST.get('update_note')

        current_user = request.user

        # Fetch the product object
        product = get_object_or_404(Product, pk=product_id)

        # Fetch the related section, category, and brand objects
        section = get_object_or_404(Section, pk=section_id)
        category = get_object_or_404(Category, pk=category_id)
        brand = get_object_or_404(Brand, pk=brand_id)

        # Update the attributes
        product.product_name = product_name
        product.section = section
        product.category = category
        product.brand = brand
        product.price = price
        product.quantity = quantity
        product.purchase_date = purchase_date
        product.supplier_name = supplier_name
        product.update_note = update_note
        product.updated_by = current_user.username

        # Save the changes
        product.save()

        messages.success(request, 'Product updated successfully!')

    return view_product(request)




def delete_alert_product(request):
    if request.method == "POST":
        print('inside delete_alert_product')
        product_id = request.POST.get('product_id')
        print(product_id)

        # You can optionally retrieve other information related to the section if needed
        try:
            product_details = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            product_details = None
            print("Product does not exist")
            messages.success(request, 'Product Not Found! Or Already Deleted')
            return view_product(request)

        context = {
            'product_details': product_details
        }
        return render(request, 'delete_alert_product.html', context)




def delete_product(request):
    if request.method == "POST":
        print('inside delete_product')
        product_id = request.POST.get('product_id')
        print(product_id)

        # Retrieve the Section object
        try:
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            print("Product does not exist")
            messages.success(request, 'Product Not Found! Or Already Deleted ')
            return view_product(request)
            # Handle the case where the section with the given ID does not exist

        # Delete the section
        product.delete()
        print("Product deleted successfully")
        messages.success(request, 'Product deleted successfully!')


    return view_product(request)











def view_all_products(request):
    # Fetch all products
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'all_products.html', context)




import xlwt

def download_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="product_data.xls"'

    # Create Excel workbook and sheet
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Product Data')

    # Define column headers
    headers = [
        'SR. NO',
        'Product Name',
        'Price',
        'Quantity',
        'Purchase Date',
        'Supplier Name',
        'Added By',
        'Updated By',
        'Update Date Time',
        'Update Note',
        'Brand',
        'Category',
        'Section',
    ]

    # Write column headers to the first row
    for col_num, header in enumerate(headers):
        ws.write(0, col_num, header)

    # Write product data to rows
    products = Product.objects.all()
    for row_num, product in enumerate(products, start=1):
        ws.write(row_num, 0, row_num)  # SR. NO
        ws.write(row_num, 1, product.product_name)
        ws.write(row_num, 2, product.price)
        ws.write(row_num, 3, product.quantity)
        ws.write(row_num, 4, product.purchase_date.strftime('%Y-%m-%d'))  # Format date as needed
        ws.write(row_num, 5, product.supplier_name)
        ws.write(row_num, 6, product.added_by)
        ws.write(row_num, 7, product.updated_by)
        ws.write(row_num, 8, product.update_date_time.strftime('%Y-%m-%d %H:%M:%S'))  # Format date and time
        ws.write(row_num, 9, product.update_note)
        ws.write(row_num, 10, product.brand.brand_name)
        ws.write(row_num, 11, product.category.category_name)
        ws.write(row_num, 12, product.section.section_name)

    # Save the workbook to the response
    wb.save(response)
    return response





