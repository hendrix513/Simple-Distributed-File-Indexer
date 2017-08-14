from file_indexer import blobToWords, topTenWordCounts
from unittest import TestCase

class FileIndexerTests(TestCase):
    def test_blob2Words0(self):
        self.assertEqual(list(blobToWords('')), [])

    def test_blob2Words1(self):
        self.assertEqual(list(blobToWords('\n  >>>')), [])

    def test_blob2Words2(self):
        self.assertEqual(list(blobToWords('B 12\\k')), ['B', '12', 'k'])

    def test_blob2Words3(self):
        self.assertEqual(list(blobToWords('B 12\\k\n')), ['B', '12', 'k'])

    def test_blob2Words4(self):
        self.assertEqual(list(blobToWords('\nB 12\\k\n')), ['B', '12', 'k'])

    def test_blob2Words3(self):
        self.assertEqual(list(blobToWords('\nB 12\\k\n')), ['B', '12', 'k'])

    def test_topTenWordCounts0(self):
        self.assertEqual(topTenWordCounts([]), [])

    def test_topTenWordCounts1(self):
        self.assertEqual(topTenWordCounts(['a', 'A', 'b']),
                         [('a', 2), ('b', 1)])

    def test_topTenWordCounts2(self):
        self.assertEqual(set(topTenWordCounts(['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                           'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c',
                                           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                           'a', 'b', 'c', 'd', 'f', 'g',
                                           'h', 'j'])),
                         set([('a', 3), ('b', 3), ('c', 3), ('d', 3), ('e', 2),
                             ('f', 3), ('g', 3), ('h', 3), ('i', 2), ('j', 3)]))
