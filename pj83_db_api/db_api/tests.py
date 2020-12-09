from django.test import TestCase
from db_api.models import DomainListall, DomainTestLog
# Create your tests here.

class DomainListAlltest(TestCase):
    def setUp(self):
        DomainListall.objects.create(
            AgentID="testcase",
            CodeToMatch="testcase",
            DomainListAPP="testcase",
            DomainListInner="testcase",
            DomainListOuter="testcase",
            DomainType="2",
        )

class DomainTestLogtest(TestCase):
    def setUp(self):
        DomainTestLog.objects.create(
            TestTime="2020-11-19 00:00:00.000",
            UrlIn="Ttse01",
            UrlOut="Ttse",
            MyIP="Ttse",
            MyZone="Ttse",
            CDN="Ttse",
            CDNIP="Ttse",
            PageLoadTime=12,
            Status="Ttse",
            IPScreenshot="Ttse",
            ProductScreenshot1="Ttse",
            ProductScreenshot2="Ttse",
            ProductScreenshot3="Ttse",
            ProductScreenshot4="Ttse",
            DomainType="2",
        )