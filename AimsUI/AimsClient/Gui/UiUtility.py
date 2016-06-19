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

import sip
sip.setapi('QString', 2)

from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QRegExp 
import re
import time

from AIMSDataManager.AimsLogging import Logger
from matplotlib.cbook import Null

uilog = None

class UiUtility (object):
    """
    Where modular UI methods live and are leveraged 
    """

    # logging
    global uilog
    uilog = Logger.setup(lf='uiLog')
    
    retainInfo = [ 'v0005', 'v0006', 'v0007', 'v0012', 'v0023', 'RP001', 'RP002' ]
        
    uiObjMappings = {'uWarning':['_warning','setWarnings', '_getEntities' ],
                    'uNotes':['_workflow_sourceReason','setSourceReason', ''],
                    'uAddressType':['_components_addressType','setAddressType', ''], 
                    'ulifeCycle':['_components_lifecycle','setLifecycle', ''],   
                    'uLevelType':['_components_levelType','setLevelType', ''], 
                    'uLevelValue':['_components_levelValue','setLevelValue', ''], 
                    'uUnitType':['_components_unitType','setUnitType', ''],
                    'uUnit':['_components_unitValue','setUnitValue', ''],
                    'uPrefix':['_components_addressNumberPrefix','setAddressNumberPrefix', ''],
                    'uBase':['_components_addressNumber','setAddressNumber', ''],
                    'uAlpha':['_components_addressNumberSuffix','setAddressNumberSuffix', ''],
                    'uHigh':['_components_addressNumberHigh','setAddressNumberHigh', ''],
                    'uExternalIdScheme':['_components_externalAddressIdScheme','setExternalAddressIdScheme', ''],
                    'uExternalAddId':['_components_externalAddressId','setExternalAddressId', ''], 
                    'uRclId':['_components_roadCentrelineId','setRoadCentrelineId', ''],
                    'uRoadPrefix':['_components_addressNumberPrefix','setRoadPrefix', ''],
                    'uRoadName':['_components_roadName','setRoadName', ''], 
                    'uRoadTypeName':['_components_roadType','setRoadType', ''],   
                    'uRoadSuffix':['_components_roadSuffix','setRoadSuffix', ''], 
                    'uWaterName':['_components_waterName','setWaterName', ''], 
                    'uWaterRouteName':['_components_waterRoute','setWaterRoute', ''],
                    'uObjectType':['_addressedObject_objectType','setObjectType', ''],
                    'uObjectName':['_addressedObject_objectName','setObjectName', ''],
                    #'uPositionType':['_addressedObject_addressPositions[0]','_addressedObject_addressPositions[0].setPositionType',''],
                    'uExtObjectIdScheme':['_addressedObject_externalObjectIdScheme','setExternalObjectIdScheme', ''],
                    'uExternalObjectId':['_addressedObject_externalObjectId','setExternalObjectId', ''],
                    'uValuationReference':['_addressedObject_valuationReference','setValuationReference', ''],
                    'uCertificateOfTitle':['_addressedObject_certificateOfTitle','setCertificateOfTitle', ''],
                    'uAppellation':['_addressedObject_appellation','setAppellation', ''],
                    'uMblkOverride':['_codes_meshblock','setMeshblock', '']
                    }
    
    @staticmethod
    def transform (iface, coords, tgt=4167):
        """
        Ensure point coordinates are in terms of AIMS system
        spatial reference system (4167)

        @param iface: QgisInterface Abstract base class defining interfaces exposed by QgisApp  
        @type iface: Qgisinterface Object
        @param coords: Point
        @type  coords: QgsPoint
        @param tgt: Srs to transform to
        @type  tgt: integer
        """
  
        src_crs = iface.mapCanvas().mapSettings().destinationCrs()
        tgt_crs = QgsCoordinateReferenceSystem()
        tgt_crs.createFromOgcWmsCrs('EPSG:{}'.format(tgt))
        transform = QgsCoordinateTransform( src_crs, tgt_crs )
        return transform.transform( coords.x(), coords.y() ) 
            
    @staticmethod
    def setFormCombos(self):
        """
        Set combo boxes to defualt values 
        """
        
        # set from the parent
        self.uAddressType.addItems(['Road', 'Water'])
        self.ulifeCycle.addItems(['Current', 'Proposed', 'Retired'])
        self.uUnitType.addItems([None, 'Apartment', 'Kiosk', 'Room', 'Shop', 'Suite', 'Villa',  'Flat', 'Unit'])
        self.uLevelType.addItems([None, 'Floor', "Level"])
        self.uObjectType.addItems(['Parcel', 'Building'])
        self.uPositionType.addItems(['Unknown', 'Centroid', 'Label', 'Set Back off Road'])

    @staticmethod
    def formMask(self): 
        """
        Mask form input values
        """   
            
        intValidator = QIntValidator()    
        self.uExternalAddId.setValidator(intValidator)
        self.uBase.setValidator(intValidator)
        self.uHigh.setValidator(intValidator)
        self.uAlpha.setValidator(QRegExpValidator(QRegExp(r'^[A-Za-z]{0,3}'), self))
        self.uUnit.setValidator(QRegExpValidator(QRegExp(r'^\w+'), self))
        self.uPrefix.setValidator(QRegExpValidator(QRegExp(r'^\w+'), self))
    
    @staticmethod
    def toUpper (uInput, UiElement): 
        """
        Converts lower case to upper case user input information
        for UI elements that are required to be upper case when submitted to API 
        
        @param uInput: User input to a UI component
        @type  uInput: string
        @param UiElement: UI Component
        @type  UiElement: QtGui.QLineEdit | QtGui.QCombo 

        @return: User input cast tp upper case where required
        @rtype: string 
        """

        if UiElement.objectName() in ('uAlpha', 'uUnit', 'uLevelValue', 'uPrefix') :
            return uInput.upper()
        else: return uInput
    
    @staticmethod
    def nullEqualsNone (uInput): #Now also handling NULL
        """
        Cast whitespace or 'NULL' to None

        @rtype: string 
        """
        
        if uInput == '' or uInput == 'NULL':
            return None
        else: return uInput
            
    @staticmethod
    def extractFlatProperty(feature, property, getter):
        """
        Return the require property for an object

        @param feature: Aims Address object
        @type  feature: AIMSDataManager.Address
        @param property: Required features property 
        @type  property: string
        @param getter: Properties Getter
        @type  getter: string
        """

        #if hasattr(feature, property) or hasattr(feature, getter):                                     
        if getter: 
            # use getter
            if getattr(feature, getter)() != 'None':
                prop = (getattr(feature, getter)())
            else: prop = ''
        else:
            # go straight for the objects property 
            if unicode(getattr(feature, property)) != 'None':
                prop = unicode(getattr(feature, property)) 
            else: prop = ''
        return prop

# commented out 14/06/2016    
#     @staticmethod
#     def extractNestedProperty(feature, property):
#         ''' fetch the require property for an obj '''
#         pass
    
    @staticmethod
    def featureToUi(self, parent = None):
    #def featureToUi(self, parent = None):
        """ 
        Populates update form and review editor queue from aims obj 
        """
        
        UiUtility.setEditability(self)
        UiUtility.clearForm(self)
        
        for ui, objProp in UiUtility.uiObjMappings.items():
            # Test the UI has the relative UI component 
            if hasattr(self, ui):
                uiElement = getattr(self, ui)
            else: 
                continue
            # Test the object has the required property or a getter
            #UiUtility.getProperty(self.feature, objProp[0])
            if self.feature._changeType in ( 'Retire' ,'Replace', 'AddLineage', 'ParcelReferenceData' ):
                if hasattr(self.feature, objProp[0]) or hasattr(self.feature, objProp[2]):
                    prop = UiUtility.extractFlatProperty(self.feature, objProp[0],objProp[2])
                elif hasattr(getattr(getattr(self.feature, 'meta'), '_entities')[0],objProp[0]):                    
                    prop = getattr(getattr(getattr(self.feature, 'meta'), '_entities')[0],objProp[0])     
                else : continue
            else: 
                if hasattr(self.feature, objProp[0]) or hasattr(self.feature, objProp[2]):
                    prop = UiUtility.extractFlatProperty(self.feature, objProp[0],objProp[2])
                else: continue
            
            # populate relvant UI components
            if isinstance(uiElement, QLineEdit) or isinstance(uiElement, QLabel):
                if ui == 'uWarning':
                    warnings = ''                        
                    for i in prop:
                        if hasattr(i,'_severity'):
                            warnings += i._severity.upper()+': '+ i._description+('\n'*2)              
                            uiElement.setText(warnings)

                # New MBLK overwrite flag implemented in API
                elif ui == 'uMblkOverride' and parent == 'update' and self.feature._codes_isMeshblockOverride != True:
                    continue
                else: 
                    uiElement.setText(unicode(prop))
            elif isinstance(uiElement, QComboBox):
                uiElement.setCurrentIndex(0)  
                uiElement.setCurrentIndex(QComboBox.findText(uiElement, prop))
        if self.feature._changeType not in ( 'Retire' ): #Therefore flat
            posType = self.feature._addressedObject_addressPositions[0]._positionType
        else:
            posType = self.feature.meta.entities[0]._addressedObject_addressPositions[0]._positionType
        self.uPositionType.setCurrentIndex(QComboBox.findText(self.uPositionType, posType))
 
    @staticmethod
    def formToObj(self):  
        """
        Maps user input from the new and update form
        as well as queue editor widget to an AIMS object
        """

        try: 
            form = self.uQueueEditor 
        except: 
            form = self
        
        for uiElement, objProp in UiUtility.uiObjMappings.items():
            #user can not mod warnings ... continiue              
            if uiElement == 'uWarning':            
                continue            
            # test if the ui widget/ form ... has the ui component
            if hasattr(form, uiElement): 
                uiElement = getattr(form, uiElement)                   
                setter = getattr(self.feature, objProp[1])
                if isinstance(uiElement, QLineEdit):# and uiElement.text() != '' and uiElement.text() != 'NULL':
                    setter(UiUtility.toUpper(uiElement.text(),uiElement))
                elif isinstance(uiElement, QComboBox):# and uiElement.currentText() != '' and uiElement.currentText() != 'NULL':
                    setter(uiElement.currentText())
                elif isinstance(uiElement, QPlainTextEdit):#and uiElement.toPlainText() != '' and uiElement.toPlainText() != 'NULL':
                    setter(uiElement.toPlainText())
        self.feature._addressedObject_addressPositions[0].setPositionType(getattr(form, 'uPositionType').currentText())
                        
    @staticmethod 
    def clearForm(self):
        """
        Resets and clears data from UI forms
        """
           
        widgetChildern = self.findChildren(QWidget, QRegExp(r'^u.*'))
        for child in widgetChildern:
            child.setEnabled(True)
            if isinstance(child, QLineEdit) or isinstance(child, QLabel):
                child.clear()
            elif isinstance(child, QComboBox) and child.objectName() != 'uAddressType':
                child.setCurrentIndex(0)
            elif isinstance(child, QPlainTextEdit):
                child.clear()
        
    @staticmethod               
    def setEditability(self):  
        """
        Toggle editable fields depending 
        on the objects Address Type (road or water) 
        """

        for child in self.findChildren(QWidget):
            child.setEnabled(True)
                             
        if self.uAddressType.currentText() == 'Road':
            waterChildern = self.findChildren(QWidget, QRegExp(r'Water.*'))
            for child in waterChildern:
                child.clear() 
                child.setDisabled(True)
                
        elif self.uAddressType.currentText() == 'Water':
            roadChildern = self.findChildren(QWidget, QRegExp(r'Road.*'))
            for child in roadChildern:
                child.clear() 
                child.setDisabled(True)

    @staticmethod
    def fullNumChanged(obj, newnumber):
        """
        Splits a full (user inputted) address string into address components

        @param obj: The UI class that the user is editing
        @type  obj: e.g. AimsUI.AimsClient.Gui.EditFeatureWidget
        @param newnumber: User input to uFullNum field
        @type  newnumber: string
        """
        
        # Set address components to None
        [i.setText(None) for i in ([obj.uPrefix, obj.uUnit, obj.uBase, obj.uAlpha, obj.uHigh])]
        # Split full address into components
        if '-' not in newnumber: 
            p = re.compile(r'^(?P<flat_prefix>[A-Z]+)?(?:\s)?(?P<flat>[0-9]+/\s*|^[A-Z]{,2}/\s*)?(?P<base>[0-9]+)(?P<alpha>[A-Z]+)?$') 
            m = p.match(newnumber.upper())
            try:
                if m.group('flat_prefix') is not None: obj.uPrefix.setText(m.group('flat_prefix'))
                if m.group('flat') is not None: obj.uUnit.setText(m.group('flat').strip('/'))
                if m.group('base') is not None: obj.uBase.setText(m.group('base'))
                if m.group('alpha') is not None: obj.uAlpha.setText(m.group('alpha'))
            except:
                pass #silently  
        else:
            p = re.compile(r'^(?P<flat_prefix>[A-Z]+)?(?:\s)?(?P<flat>[0-9]+/\s*|^[A-Z]{,2}/\s*)?(?P<base>[0-9]+)(?:-)(?P<high>[0-9]+)(?P<alpha>[A-Z]+)?$') 
            m = p.match(newnumber.upper())
            try:
                if m.group('flat_prefix') is not None: obj.uPrefix.setText(m.group('flat_prefix'))
                if m.group('flat') is not None: obj.uUnit.setText(m.group('flat').strip('/'))
                if m.group('base') is not None: obj.uBase.setText(m.group('base'))
                if m.group('high') is not None: obj.uHigh.setText(m.group('high'))
                if m.group('alpha') is not None: obj.uAlpha.setText(m.group('alpha'))
            except:
                pass #silently  
    