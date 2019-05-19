import collections
import csv


class WorksMetadata(object):

    class WorkMetadataLine(
        collections.namedtuple(
            'WorkMetadataLine', ['title', 'raw_contributors', 'iswc']
        )
    ):
        @property
        def contributors(self):
            return self.raw_contributors.split('|')

    DELIMITER = ','

    @classmethod
    def parse(cls, csv_path):
        with open(csv_path, 'rU') as data:
            data.readline()
            reader = csv.reader(
                data,
                delimiter=cls.DELIMITER
            )
            for line in map(cls.WorkMetadataLine._make, reader):
                yield line
