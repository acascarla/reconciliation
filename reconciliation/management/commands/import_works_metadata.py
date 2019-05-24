from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction

from reconciliation import importers
from reconciliation import models


class Command(BaseCommand):
    help = 'Imports works metadata from a csv'

    def add_arguments(self, parser):
        parser.add_argument(
            '-f', '--file', default='data_samples/works_metadata.csv')

    def handle(self, *args, **options):
        self._import(options['file'])

    def _import(self, csv_path):
        rows = importers.WorksMetadata.parse(csv_path)
        for row in rows:
            contributors = self._create_contributors(row.contributors)
            try:
                work = self._work_by_iswc(row.iswc)
            except ObjectDoesNotExist:
                work = self._work_by_title_and_contributor(row)
                if not work:
                    work = self._new_work(row)
            except MultipleObjectsReturned as e:
                raise CommandError('There are duplicated iswc in DB.') from e
            self._update_work(work, row)
            work.contributors.add(*contributors)
        self.stdout.write(self.style.SUCCESS('Imported succesfully.'))

    @transaction.atomic
    def _create_contributors(self, contributors):
        return [
            models.Contributor.objects.get_or_create(
                name=contributor_name
            )[0]  # ignore created flag of get_or_create
            for contributor_name in contributors
        ]

    def _work_by_iswc(self, iswc):
        return models.Work.objects.get(iswc=iswc)

    def _update_work(self, work, row):
        work.iswc = row.iswc
        work.title = row.title
        work.save()

    @transaction.atomic
    def _work_by_title_and_contributor(self, row):
        works = models.Work.objects.filter(title=row.title)
        for work in works:
            work_contrib_set = set(c.name for c in work.contributors.all())
            row_contrib_set = set(row.contributors)
            if work_contrib_set & row_contrib_set:
                return work
        return None

    def _new_work(self, row):
        return models.Work.objects.create(
            title=row.title,
            iswc=row.iswc,
        )
