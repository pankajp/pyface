#-------------------------------------------------------------------------------
#  
#  Defines the IFeatureTool interface which allows objects dragged using the
#  DockWindowFeature API to control the drag target and drop events. Useful for
#  implementing tools which can be dropped onto compatible view objects.
#  
#  Written by: David C. Morrill
#  
#  Date: 02/07/2007
#  
#  (c) Copyright 2007 by Enthought, Inc.
#  
#-------------------------------------------------------------------------------
    
#-------------------------------------------------------------------------------
#  'IFeatureTool' class:  
#-------------------------------------------------------------------------------

class IFeatureTool ( object ):
    
    #---------------------------------------------------------------------------
    #  Returns whether or not the object being dragged (i.e. self) can be 
    #  dropped on the specified target object:
    #---------------------------------------------------------------------------
        
    def feature_can_drop_on ( self, object ):
        """ Returns whether or not the object being dragged (i.e. self) can be 
            dropped on the specified target object.
        """
        return False
    
    #---------------------------------------------------------------------------
    #  Returns whether or not the object being dragged (i.e. self) can be 
    #  dropped on the specified target object's DockControl:
    #---------------------------------------------------------------------------
        
    def feature_can_drop_on_dock_control ( self, dock_control ):
        """ Returns whether or not the object being dragged (i.e. self) can be 
            dropped on the specified target object's DockControl.
        """
        return False
        
    #---------------------------------------------------------------------------
    #  Allows the dragged object (i.e. self) to handle being dropped on the
    #  specified target object:
    #---------------------------------------------------------------------------
                    
    def feature_dropped_on ( self, object ):
        """ Allows the dragged object (i.e. self) to handle being dropped on the
            specified target object.
        """
        return        
        
    #---------------------------------------------------------------------------
    #  Allows the dragged object (i.e. self) to handle being dropped on the
    #  specified target object's DockControl:
    #---------------------------------------------------------------------------
                    
    def feature_dropped_on_dock_control ( self, dock_control ):
        """ Allows the dragged object (i.e. self) to handle being dropped on the
            specified target object's DockControl.
        """
        return        
