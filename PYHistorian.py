# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PHistorian.ui'
#
# Created: Wed Feb 05 22:49:50 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import sqlite3
import OpenOPC
import os
import time
import PYHistorianUI

#import Phistorianresources_rc

class PYHistorian(QtGui.QMainWindow,PYHistorianUI.Ui_PHistorianUI):
    def __init__(self,*args,**kwargs):
        super(PYHistorian,self).__init__()
        print( "init is called")
        self.setupUi(self)
        self.listWidgetOPCTags.setSelectionMode(3) 
        self.listWidgetPYTags.setSelectionMode(3)
#        selction mode 3 enables both  shift and ctrl keys , 2 only shift 
        self.actionConnect.triggered.connect(self.queryOPC)        
        self.actionStartCollect.triggered.connect(self.datacollectStart)
        self.actionStopCollect.triggered.connect(self.datacollectstop)
        self.pushButtonAddTags.clicked.connect(self.addTagsPYHistorian)
        self.pushButtonRemoveTags.clicked.connect(self.removeTagsPYHistorian)
        self.stopdatacollection = 0
        

    
    def queryOPC(self):
            
      self.connectOPC()
# todo: later modify the code to accept the settings from the dialog
            
            
        
        
    def connectOPC(self):
        self.opc = OpenOPC.client()
        # modify the code later to get the text from the selcted item.         
        self.opc.connect('Matrikon.OPC.Simulation.1')

#        self.opc.connect(self.listWidgetServers.selectedItems.text())
        print ("OPC server connected")

        self.tagbrowse()
         
    def tagbrowse(self):
        self.taglist = self.opc.list(recursive = True) 
        self.listWidgetOPCTags.addItems(self.taglist)
#        for tag in self.taglist:
#            itemTag = QtGui.QListWidgetItem(tag)
#   
#            self.listWidgetOPCTags.addItems(itemTag)
            
        
    def addTagsPYHistorian(self):
        selectedItems = self.listWidgetOPCTags.selectedItems()
        
#        selecteditems in qlistwidget is a list of  Qlistwidetitem objects
#it must be converted to string to use with add item method.
        for  selectedItem in selectedItems:
            
            self.listWidgetPYTags.addItem(selectedItem.text())
    
    def removeTagsPYHistorian(self):
        print self.listWidgetPYTags.count() 
        
        selecteditemsPYTags = self.listWidgetPYTags.selectedItems()
        
        for item in selecteditemsPYTags:
            self.listWidgetPYTags.takeItem(self.listWidgetPYTags.row(item))
        print self.listWidgetPYTags.count()
        
    def datacollectstop(self):
        self.stopdatacollection = 1
    def datacollectStart(self):
        
       
          
        dbfile='historian.db'
        
        tagnames = []
        tablenames =[]
        

        
        

        dbexist = os.path.exists(dbfile)
        db = sqlite3.connect(dbfile)
        cur = db.cursor()
        for i in range(self.listWidgetPYTags.count()):
            
            tagnames.append(self.listWidgetPYTags.item(i).text())
            #        create as many table names as there are tags, remove all the spaces and the dots. 
            tablenames = ["opcdata" + str(tagnames[i]).translate(None," ,.") for i in range(len(tagnames))]
            sqlstring = "CREATE TABLE IF NOT EXISTS " + tablenames[i]+ " (id INTEGER PRIMARY KEY, tag TEXT, val TEXT, stat TEXT, datetime TEXT, atime TEXT)"
            print sqlstring            
            cur.execute(sqlstring)
            db.commit()
            
        while(not self.stopdatacollection): # infinite loop kill with Ctrl-C
            for i in range(self.listWidgetPYTags.count()):
                print str(tagnames[i])
                (opcvalue,opcstat,opctime) = self.opc.read(str(tagnames[i]))
            
    #the above code throws error OpenOPC.OPCError: AddGroup: Unspecified error
                 
    #            self.opc.close()
                atime = time.asctime() # current computer time as float
                sqlstringsInsert = 'INSERT INTO '+tablenames[i]+' (id, tag, val, stat, datetime, atime) VALUES(NULL, "%s", "%f", "%s", "%s", "%s")'%(tagnames[i],opcvalue,opcstat,opctime,atime)
                cur.execute(sqlstringsInsert)
                db.commit()
                cur.execute("SELECT * FROM " +tablenames[i])
                dbvalues = cur.fetchall()
                dblen = len(dbvalues)
                i += 1
                print i            
                print dbvalues[dblen-1] # print newest value in database
            time.sleep(5)
        
# end of while loop
    def fetchdata(self):
        
        sql
    
    
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    PY = PYHistorian()
    PY.show()
    sys.exit(app.exec_())

