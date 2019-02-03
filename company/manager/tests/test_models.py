from django.test import TestCase

from ..models import Company
from .factories import CompanyFactory


class CompanyTestCase(TestCase):
    def test_str(self):
        """ Test for string reper"""
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)
