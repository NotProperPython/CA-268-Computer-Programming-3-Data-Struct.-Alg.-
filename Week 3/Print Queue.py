#!/usr/bin/env python

def print_queue(l, a, b):
   if len(l) == b+1:
      print(l[a])
   else:
      for i in l[a:]:
         print(i)

      for i in l[:b]:
         print(i)