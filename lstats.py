#!/usr/bin/env python3
""" Calculate stats from matching lines of text files.

    Usage:
    
        lstats.py PATTERN FILE ...
    e.g.

       head -n -1 mtx-roce.sh.out | ./lstats.py '\d+,\d+,([\d.]+),' -

    where:
       PATTERN is a python regex including capturing groups
       FILE is a path to file(s) or - for stdin
   
    Stats calculated from matching groups.
"""
import fileinput, sys, re, statistics

def run():
  pattern, *paths = sys.argv[1:]
  vals = []
  rx = re.compile(pattern)
  for line in fileinput.input(paths):
    m = rx.search(line)
    if m:
       vals.extend(float(v) for v in m.groups())
       #print(line.strip(), m.groups())
  tot = sum(vals)
  n = len(vals)
  print(f'n: {n}')
  print('min: %f' % min(vals))
  print('max: %f' % max(vals))
  print('mean: %f' % statistics.mean(vals))
  print('stdev: %f' % statistics.stdev(vals))

  # TODO: how to print lines which are outside 1 stddev
 
if __name__ == '__main__':
  run()
