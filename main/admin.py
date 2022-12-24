from django.contrib import admin
from .models import Models
from .models import Users
from .models import DonationPerMonth

admin.site.register(Models)
admin.site.register(Users)
admin.site.register(DonationPerMonth)