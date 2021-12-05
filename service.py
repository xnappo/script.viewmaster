import xbmc
import AddonSignals
from resources.lib.functions import setView
def viewNotification(notificationData):
   xbmc.log("ViewMasterService viewNotification called:" + notificationData['view_type'])
   setView(notificationData['view_type'])

AddonSignals.registerSlot('embycon', 'display_items', viewNotification)
monitor = xbmc.Monitor()
while not monitor.abortRequested:
    xbmc.sleep(1000)
