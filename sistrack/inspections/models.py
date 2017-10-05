from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid # Required for unique test instances

# Create your models here.

class Document(models.Model):
    doc_unit = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True)
    doc_number = models.CharField(max_length=50)
    doc_name = models.CharField(max_length=50)

    DOC_TYPE = (
        ('c','Cause and Effect'),
        ('d','Data Sheet'),
        ('p','P&ID'),
        ('o','other'),
    )

    doc_type = models.CharField(max_length=50, choices=DOC_TYPE, blank=True, default='o')

    class Meta:
        ordering = ["doc_number"]

    def __str__(self):
        return '{0}-{1}'.format(self.doc_number,self.doc_type)


class Location(models.Model):
    facility = models.CharField(max_length=50)
    plant = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ["unit"]

    def __str__(self):
        return '{0}'.format('Unit ' + self.unit)


class DeviceType(models.Model):
    name = models.CharField(max_length=50)
    CATEGORY = (
        ('i','Input Element'),
        ('o','Output Element'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY)

    class Meta:
        ordering = ["category"]

    def __str__(self):
        return '{0}-({1})'.format(self.name,self.category)


class Device(models.Model):
    tagnumber = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    devicetype = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["tagnumber"]

    def __str__(self):
        return self.tagnumber

    def get_absolute_url(self):
        return reverse('device-detail', args=[str(self.id)])


class TestInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular device test")
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    test_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    inspector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_date and date.today() > self.due_date:
            return True
        return False

    TEST_STATUS = (
    ('o', 'Overdue'),
    ('s', 'Scheduled'),
    )

    TEST_RESULT = (
    ('p', 'Passed'),
    ('f', 'Failed'),
    )

    status = models.CharField(max_length=1, choices=TEST_STATUS, blank=True, default='s')
    result = models.CharField(max_length=1, choices=TEST_RESULT, blank=True)
    comments = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ["due_date"]
        permissions = (("can_mark_approved", "Mark test as approved"),)

    def __str__(self):
        return '%s (%s)' % (self.id,self.device.tagnumber)


class Interlock(models.Model):
    interlock_unit = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    interlock_number = models.CharField(max_length=50)
    interlock_description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ["interlock_number"]

    def __str__(self):
        return '{0}'.format(self.interlock_number)


class Ipl(models.Model):
    ipl_unit = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    initiator = models.CharField(max_length=50)
    ipl_description = models.CharField(max_length=300)
    ipl_narrative = models.TextField(blank=True)
    ipl_interlock_number = models.ForeignKey(Interlock, on_delete=models.SET_NULL, blank=True, null=True)
    ipl_doc_references = models.ManyToManyField(Document, blank=True, verbose_name="IPL reference documents")
    input_elements = models.ManyToManyField(Device, blank=True, related_name='+', related_query_name="IPL input elements")
    output_elements = models.ManyToManyField(Device, blank=True, related_name='+', related_query_name="IPL output elements")

    class Meta:
        ordering = ["ipl_unit"]

    def __str__(self):
        return '{0}-{1}'.format(self.initiator,self.ipl_description)
