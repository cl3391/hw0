#Name: Changtai Liu, UNI: cl3391
#Status: Still on the waitlist,pending approval

import re

with open('iowa-liquor-sample.csv') as sample:
  num = 0
  for row in sample:
    if re.search('single malt scotch', row, re.IGNORECASE):
      num += 1
  print "Number of records = %d" % num
