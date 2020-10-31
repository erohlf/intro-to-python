import unittest
import finder_funcs


class TestString(unittest.TestCase):

    def test_get_rows_1(self):
        puzzle = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
        rows =  ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        self.assertEqual(finder_funcs.get_rows(puzzle), rows)


    def test_get_columns_1(self):
        puzzle = 'EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'
        columns = ['EZAACBEABB', 'OERANOEBOO', 'ABRCANRCIA', 'RRABBITEOA', 'BACRORCRRK', 'RECRZBBIOR', 'NBOCOBRCRK', 'IROHBNARCE', 'ABNEKCIHCA', 'BHRCAAAROR']
        self.assertEqual(finder_funcs.get_columns(puzzle), columns)

    def test_backwards_string_1(self):
        string = 'hello'
        reverse_string = 'olleh'
        self.assertEqual(finder_funcs.backwards_string(string), reverse_string)

    def test_word_in_rows_1(self):
        puzzle = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
        word = 'VIM'
        self.assertEqual(finder_funcs.word_in_rows(puzzle, word), 'VIM: (BACKWARD) row: 1 column: 4')

    def test_word_in_rows_2(self):
        puzzle = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
        word = 'TEST'
        self.assertFalse(finder_funcs.word_in_rows(puzzle, word))

    def test_word_in_columns_1(self):
        puzzle = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
        word = 'CALPOLY'
        self.assertEqual(finder_funcs.word_in_columns(puzzle, word), 'CALPOLY: (DOWN) row: 1 column: 0')

    def test_word_in_columns_2(self):
        puzzle = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
        word = 'GCC'
        self.assertFalse(finder_funcs.word_in_columns(puzzle, word))

if __name__ == '__main__':
    unittest.main()
