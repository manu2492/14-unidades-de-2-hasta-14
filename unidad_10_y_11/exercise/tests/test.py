import unittest
import sys
import os
import datetime
from datetime import datetime
from pathlib import Path
sys.path.append('/home/manu/desktop2/python/prismarun/tema11/exercise')
from docs_from_tests.instrument_call_hierarchy import instrument_and_import_package,initialise_call_hierarchy,finalise_call_hierarchy
import functions.functions as f
from assets.text_append import append_text, sequence_diagram_filename


instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(),
                              '..', 'functions'), 'functions')


class TestCalculator(unittest.TestCase):

    # addition
    def test_addition(self):
        # start sequence
        initialise_call_hierarchy('start')

        self.assertEqual(f.addition(3.0, 4.0), 7.0)
        self.assertAlmostEqual(f.addition(3.0, 4.0), 7.001, places=2)
        self.assertGreater(f.addition(4.0, 4.0), 7.0)

        # stop sequence
        root_call = finalise_call_hierarchy()
        # return diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Append diagram
        append_text(Path(sequence_diagram_filename), sequence_diagram)

    # division
    def test_division(self):
        # Start sequence
        initialise_call_hierarchy('start')

        self.assertEqual(f.division(4.0, 2.0), 2.0)
        self.assertAlmostEqual(f.division(4.0, 2.0), 2.001, places=2)
        self.assertGreater(f.division(4.0, 2.0), 1.0)

        # Stop sequence
        root_call = finalise_call_hierarchy()
        # Return diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Append diagram
        append_text(Path(sequence_diagram_filename), sequence_diagram)

    # subtraction
    def test_subtraction(self):
        # Start sequence
        initialise_call_hierarchy('start')

        self.assertEqual(f.subtraction(4.0, 2.0), 2.0)
        self.assertAlmostEqual(f.subtraction(4.0, 2.0), 2.001, places=2)
        self.assertGreater(f.subtraction(4.0, 2.0), 1.0)

        # Stop sequence
        root_call = finalise_call_hierarchy()
        # Return diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Append diagram
        append_text(Path(sequence_diagram_filename), sequence_diagram)

    # multiplication
    def test_multiplication(self):
        # Start sequence
        initialise_call_hierarchy('start')

        self.assertEqual(f.multiplication(4.0, 2.0), 8.0)
        self.assertAlmostEqual(f.multiplication(4.0, 2.0), 8.001, places=2)
        self.assertGreater(f.multiplication(4.0, 2.0), 7.0)

        # Stop sequence
        root_call = finalise_call_hierarchy()
        # Return diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Append diagram
        append_text(Path(sequence_diagram_filename), sequence_diagram)


# create text to document the testing
def insert_header(j):
    j.write('\n')
    j.write('******************TESTING**************************')
    j.write('\n')
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    j.write(date_time)
    j.write('\n')
    return j


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    unittest.main()
    with open('exercise/text/testing.txt', 'a') as j:
        j = insert_header(j)
        main(j)

