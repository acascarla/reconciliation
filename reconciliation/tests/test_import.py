from django.test import TestCase
from django.core import management

from reconciliation.importers import WorksMetadata, WorkMetadataLine
from reconciliation.models import Work, Contributor


class ImportTestCase(TestCase):

    def setUp(self):
        self.rows = WorksMetadata.parse('data_samples/works_metadata.csv')

    def test_importer(self):
        expected_rows = [
            WorkMetadataLine(
                title='Shape of You',
                raw_contributors='Edward Christopher Sheeran',
                iswc='T9204649558',
            ),
            WorkMetadataLine(
                title='Adventure of a Lifetime',
                raw_contributors=(
                    'O Brien Edward John|Yorke Thomas Edward|Greenwood Colin '
                    'Charles'),
                iswc='T0101974597',
            ),
            WorkMetadataLine(
                title='Adventure of a Lifetime',
                raw_contributors='O Brien Edward John|Selway Philip James',
                iswc='T0101974597',
            ),
            WorkMetadataLine(
                title='Me Enamoré',
                raw_contributors=(
                    'Rayo Gibo Antonio|Ripoll Shakira Isabel Mebarak'),
                iswc='T9214745718',
            ),
            WorkMetadataLine(
                title='Je ne sais pas',
                raw_contributors=(
                    'Obispo Pascal Michel|Florence Lionel Jacques'),
                iswc='',
            ),
            WorkMetadataLine(
                title='Je ne sais pas',
                raw_contributors=(
                    'Obispo Pascal Michel|Florence Lionel Jacques'),
                iswc='T0046951705',
            ),
        ]
        self.assertEqual(list(self.rows), expected_rows)

    def test_reconciliation(self):
        works_count = Work.objects.count()
        self.assertEqual(works_count, 0)
        contributors_count = Contributor.objects.count()
        self.assertEqual(contributors_count, 0)
        management.call_command('import_works_metadata')
        contributors_count = Contributor.objects.count()
        self.assertEqual(contributors_count, 9)
        expected_works = [
            ('Shape of You', 'T9204649558'),
            ('Adventure of a Lifetime', 'T0101974597'),
            ('Me Enamoré', 'T9214745718'),
            ('Je ne sais pas', 'T0046951705'),
        ]
        works = Work.objects.all().values_list('title', 'iswc')
        self.assertEqual(list(works), expected_works)
        work_adv = Work.objects.get(title='Adventure of a Lifetime')
        self.assertEqual(len(work_adv.contributors.all()), 4)
