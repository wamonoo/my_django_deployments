from django.contrib import admin
from aff_site.models import Participant, Portal_user #, City, Country, Address

#change default admin site header
admin.site.site_header = 'AFF SITE ADMIN'

#admin.site.register(Participant)
admin.site.register(Portal_user)

#customize admin features
class ParticipantsAdmin(admin.ModelAdmin):
    #add filter to admin page for participants
    list_filter = ['city', 'country']
    #add search field
    search_fields = ['city', 'country']
    #add fields to display
    list_display = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'country','created_at']
admin.site.register(Participant, ParticipantsAdmin)


#    return patterns('', (r'report/admin.site.admin_view(self.report_view))) + urls


#admin.site.register(City)
#admin.site.register(Country)
#admin.site.register(Participant)
# Register your models here.
