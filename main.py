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
   poseList.append(start)

   diff = [0] * 6
   for index in range(6):
      diff[index] = stop[index] - start[index]
   m = max(diff)
   steps = int(m / 0.1)

   for step in range(steps):
      jointValues = [0] * 6
      percentage = step / steps
      for index in range(6):
         addValue = percentage * diff[index]
         jointValues[index] = start[index] + addValue
      hsCol = com.hasCollision(jointValues)
      clr = com.clearance(jointValues)
      print(hsCol, clr)
      poseList.append(jointValues)

   poseList.append(stop)
   return poseList

   
if __name__ == '__main__':
   com._mainLoop(compilePath)
