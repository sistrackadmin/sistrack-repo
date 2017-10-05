from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Location, Device, DeviceType, TestInstance, Document, Interlock, Ipl
# Create your views here.

def index(request):
    devcount = Device.objects.all().count()
    ipl_count = Ipl.objects.all().count()
    interlock_count = Interlock.objects.all().count()
    doc_count = Document.objects.all().count()
    location_count = Location.objects.all().count()
    failedcount = TestInstance.objects.filter(result='f').count()
    test_count = TestInstance.objects.filter(test_date__year=2017).count()
    testedthismonth = TestInstance.objects.all().count()
    testedthisyear = TestInstance.objects.filter(test_date__year=2017).count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'index.html', {'devcount':devcount, 'failedcount':failedcount, 'testedthismonth':testedthismonth, 'testedthisyear':testedthisyear, 'num_visits':num_visits, 'ipl_count':ipl_count, 'interlock_count':interlock_count, 'doc_count':doc_count, 'location_count':location_count, 'test_count':test_count})

class DeviceListView(generic.ListView):
    model = Device
    paginate_by = 10

class DeviceDetailView(generic.DetailView):
    model = Device

class DeviceTestedByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing devices tested by current user.
    """
    model = TestInstance
    template_name ='inspections/testinstance_list_tested_user.html'
    paginate_by = 10

    def get_queryset(self):
        return TestInstance.objects.filter(inspector=self.request.user).filter(status__exact='s').order_by('due_date')

class AllDevicesTestedListView(PermissionRequiredMixin,generic.ListView):
    """
    Generic class-based view listing all devices tested.
    """
    permission_required = 'inspections.can_mark_approved'
    model = TestInstance
    template_name ='inspections/all_devices_tested.html'
    paginate_by = 10

    def get_queryset(self):
        return TestInstance.objects.filter(status__exact='s').order_by('due_date')
