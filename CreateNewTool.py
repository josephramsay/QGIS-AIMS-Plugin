################################################################################
#
# Copyright 2015 Crown copyright (c)
# Land Information New Zealand and the New Zealand Government.
# All rights reserved
#
# This program is released under the terms of the 3 clause BSD license. See the 
# LICENSE file for more information.
#
################################################################################

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from AimsClient.Gui import Controller
from AimsClient.Address import Address
from AimsClient.Gui.NewAddressDialog import NewAddressDialog



class CreateNewTool( QgsMapTool ):
    ''' tool for creating new address information ''' 
    
    def __init__( self, iface, controller ):
        
        QgsMapTool.__init__(self, iface.mapCanvas())
   
        self._iface = iface
        self._controller = controller
        self.activate()

    def activate( self ):
        QgsMapTool.activate(self)
        sb = self._iface.mainWindow().statusBar()
        sb.showMessage("Click map to create point")
    
    def deactivate( self ):
        sb = self._iface.mainWindow().statusBar()
        sb.clearMessage()

    def setEnabled( self, enabled ):
        self._enabled = enabled
        if enabled:
            self.activate()
        else:
            self.deactivate()
 
    def canvasReleaseEvent(self,e):
        if not e.button() == Qt.LeftButton:
            return
        
        if not self._enabled:
            QMessageBox.warning(self._iface.mainWindow(),"Create Address Point", "Not enabled")
            return
        
        pt = e.pos()
        coords = self.toMapCoordinates(QPoint(pt.x(), pt.y()))
        
        # Open new address form
        addDetials = NewAddressDialog.newAddress(self._iface.mainWindow())
        