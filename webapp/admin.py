from django.contrib import admin

# Import the classes we need
from .models import Organisation
from .models import OrganisationHistory
from .models import Facility
from .models import FacilityHistory
from .models import Department
from .models import DepartmentHistory
from .models import Contact
from .models import WorkOrder
from .models import PurchaseOrder
from .models import Asset
from .models import Service

# Register your models here.
admin.site.register(Organisation)
admin.site.register(OrganisationHistory)
admin.site.register(Facility)
admin.site.register(FacilityHistory)
admin.site.register(Department)
admin.site.register(DepartmentHistory)
admin.site.register(Contact)
admin.site.register(WorkOrder)
admin.site.register(PurchaseOrder)
admin.site.register(Asset)
admin.site.register(Service)