# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 12:09:33 2014
@description:  diskdatacollector
@author: christopherupkes
@owner: Stratatron,LLC

"""
from systemdatacollector import SystemDataCollector




class DiskDataCollector( SystemDataCollector ) :
    def __init__(self, agentName, diskInfoFile, start=False) :
        SystemDataCollector.__init__(self, agentName, diskInfoFile, start)
        
        self._diskInfoFile = diskInfoFile
        self._counter = 0
        
        
        
    def collectReportData(self):
        SystemDataCollector.fileScanner(self._counter, self._diskINfoFile.fileName, self.processLine)
    
    def processLine(self, counter, line):
        # parse line    
        newRecord = False
        parsedLine = line.split(":")
        diskInfo = str(parsedLine[1])
        
        if 'c' in diskInfo[0] and 't' in diskInfo[3] : newRecord = True
        if newRecord :
            self._record = []
            dtype =  'SSD' if str(parsedLine[2]) == '<SSD>' else 'HDD'
            self._record.append(counter)
            self._record.append(dtype)
            self._record.append(str(pardseldLine[2]))
            
            
            # save disk ID value
            # parse diskType from parsedLine[2]
        elif '<SHELF' in diskInfo :
            self._record.append(str(parseldLine[1]))
            self._record.append(str(parsedLine[2]))
            self._record.append(str(parsedLine[3]))
            self._records.append(self._record)
            
        else:
            print("not a disk")
        
        
