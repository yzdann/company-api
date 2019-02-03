from django.test import TestCase

from ..models import Company
from .factories import CompanyFactory


class CompanyTestCase(TestCase):
    """ Test for string reper"""
    def test_str(self):
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)
