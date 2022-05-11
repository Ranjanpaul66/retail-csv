from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .forms import *
from .custom_logger import setup_logger

logger = setup_logger("App_logger", "logs/app.log")

def index2(request):
    if request.method == 'POST' and request.FILES['filename']:
        myfile = request.FILES['filename']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
    return render(request, 'index.html')


def index(request):
    data = {}
    if "GET" == request.method:
        return render(request, "index.html")
    try:
        csv_file = request.FILES["filename"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return HttpResponseRedirect(reverse("index"))
        # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("myapp:upload_csv"))

        """ save your file in local storage"""
        file_data = csv_file.read().decode("utf-8")
        fs = FileSystemStorage()
        fs.save(csv_file.name, csv_file)


        lines = file_data.split("\n")
        # loop over the lines and save them in db. If error , store as string and then display
        count = 0
        for line in lines:
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["first_name"] = fields[1]
            data_dict["address_street"] = fields[2]
            data_dict["phone"] = fields[3]
            data_dict["address_zipcode"] = fields[4]
            data_dict["address_city"] = fields[5]
            data_dict["address_country"] = fields[6]
            data_dict["bank_account_no"] = fields[7]
            data_dict["bank_name"] = fields[8]
            data_dict["email"] = fields[9]
            try:

                form = CustomerForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    logger.warning("Invalid Form")
                count = count + 1
                print('Success ', count)
            except Exception as e:
                count = count + 1
                print('failed ', count)
                logger.warning(e)
                pass
        messages.success(request, 'Data has dumped!')
        logger.warning("Database Has dumped!")
    except Exception as e:
        logger.warning("Unable to upload!")
        messages.error(request, "Unable to upload file. Please try Again.")

    return HttpResponseRedirect(reverse("index"))
