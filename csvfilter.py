import sys
from csvfilter import Processor


def contains_cheese(row):
    return 'cheese' in row 

processor = Processor(fields=[1,2,3])
processor.add_validator(contains_cheese)
generator = processor.process(sys.stdin)

for cheesy_row in generator:
    do_something(cheesy_row)
