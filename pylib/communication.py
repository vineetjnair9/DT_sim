#!/usr/env/bin python3

import json, socket, sys, time

class Communication:

   def __init__(self):

      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
         self.client.connect(('127.0.0.1', 4321))
      except ConnectionRefusedError:
         print('verosim is not available')
         sys.exit(1)

   def hasCollision(self, jointValues):

      sendDict = {
         'type': 'hasCollision'
         , 'jointValues': jointValues
      }

      receiveDict = self._communicate(sendDict)
      if not receiveDict:
         return False

      value = bool(receiveDict['result'])
      return value

   def clearance(self, jointValues):

      sendDict = {
         'type': 'clearance'
         , 'jointValues': jointValues
      }

      receiveDict = self._communicate(sendDict)
      if not receiveDict:
         return False

      value = float(receiveDict['result'])
      return value      

   def _mainLoop(self, compilePathFunction):

      while True:
         if self._startOperation():
            start = self._getStartPose()
            stop = self._getEndPose()

            poseList = compilePathFunction(start, stop)
            self._sendPoseList(poseList)
         else:
            time.sleep(1.0)         

   def _startOperation(self):

      receiveDict = self._communicate({'type': 'startOperation'})
      if not receiveDict:
         return False

      value = bool(receiveDict['result'])
      return value

   def _getStartPose(self):

      receiveDict = self._communicate({'type': 'getStartJointValues'})
      if not receiveDict:
         return None

      jointValues = receiveDict['jointValues']
      return jointValues

   def _getEndPose(self):

      receiveDict = self._communicate({'type': 'getEndJointValues'})
      if not receiveDict:
         return None

      jointValues = receiveDict['jointValues']
      return jointValues

   def _sendPoseList(self, poseList):

      if not poseList:
         return

      self._communicate({'type': 'startPoseList'})
      for index, jointValues in enumerate(poseList):
         sendDict = {
            'type': 'addPose'
            , 'jointValues': jointValues
         }
         self._communicate(sendDict)

      self._communicate({'type': 'endPoseList'})

   def _communicate(self, sendDict):

      sendData = json.dumps(sendDict).encode()
      try:
         self.client.send(sendData)
         receiveData = self.client.recv(1024).decode()      
      except ConnectionRefusedError:
         print('verosim is not available')
         sys.exit(1)

      if not receiveData:
         print('verosim is not available')
         sys.exit(1)

      receiveDict = json.loads(receiveData)

      if 'error' in receiveDict:
         error = receiveDict['error']
         print('ERROR:', error)
         return None

      return receiveDict
      