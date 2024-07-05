from django.shortcuts import render
from django.core.files.storage import FileSystemStorage



from django.contrib import messages
from .models import Advertisement
USER_IMG_DIR = "D:\ClothFlow\ClothFlow\static\Advertisement_images"

def uploadadvertisement(request):
    if request.method == 'POST' and 'image' in request.FILES:

        print('inside advertisemnt ')
        image = request.FILES['image']
        fs = FileSystemStorage(location=USER_IMG_DIR)
        filename = fs.save(image.name, image)

        title = request.POST.get('title')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        description = request.POST.get('description')
        terms = request.POST.get('terms')

        # Construct the file path for the uploaded image
        uploaded_file_url = fs.url(filename)

        # Create Advertisement instance and save to database
        advertisement_instance = Advertisement.objects.create(
            title=title,
            start_date=startDate,
            end_date=endDate,
            upload_image=uploaded_file_url,  # Save the image URL
            description=description,
            clauses=terms
        )

        messages.success(request, 'Advertisement uploaded successfully.')

    # Render the advertisementupload.html template
    return render(request, 'advertisementupload.html')