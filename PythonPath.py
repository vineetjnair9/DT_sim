#!/usr/bin/env python3

from typing import List
JointValues = List[float]
JointValuesList = List[JointValues]

from pylib import Communication
com = Communication()

def compilePath(start: JointValues, stop: JointValues) -> JointValuesList:

   print('start = ', start)
   print('stop = ', stop)
   if len(start) != 6 or len(stop) != 6:
      print('Array length mismatch')
      return None

   poseList = list()

   # fill in the poses

   return poseList

   
if __name__ == '__main__':
   com._mainLoop(compilePath)
