from django.test import TestCase

from ..serializers import CompanySerializer
from .factories import CompanyFactory


class CompanySerializer(TestCase):
    def test_model_fields(self):
        def test_model_fields(self):
            """Serializer data matchers the Company object for each field."""
            company = CompanyFactory()
            for field in [
                'id', 'name', 'website', 'street_line_1', 'street_line_2',
                'city', 'state', 'zipcode'
            ]:
                self.assertEqual(
                    serializer.data[field_name],
                    getattr(company, field_name),
                )
