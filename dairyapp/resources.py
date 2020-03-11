
from import_export import resources
from dairyapp.models import Vendor

class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
        fields=('vendorname','managername','joiningdate','vendorcontact')
        export_order=fields