# Gnu General Public License - see LICENSE.TXT

import urllib
import sys
import os
import time
import json
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

from resources.lib.kodi_utils import HomeWindow
from resources.lib.views import DefaultViews, loadSkinDefaults
from resources.lib.simple_logging import SimpleLogging
from resources.lib.translation import i18n

__addon__ = xbmcaddon.Addon(id='script.viewmaster')
__addondir__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__cwd__ = __addon__.getAddonInfo('path')
PLUGINPATH = xbmc.translatePath(os.path.join(__cwd__))

log = SimpleLogging(__name__)

kodi_version = int(xbmc.getInfoLabel('System.BuildVersion')[:2])

def mainEntryPoint():
    log.info("===== ViewMaster START =====")

    log.info("Running Python: " + str(sys.version_info))
    log.info("Kodi BuildVersion: " + xbmc.getInfoLabel("System.BuildVersion"))
    log.info("Kodi Version: " + str(kodi_version))
    log.info("Script argument data: " + str(sys.argv))

    try:
        params = get_params(sys.argv[2])
    except:
        params = {}

    if (len(params) == 0):
        home_window = HomeWindow()
        windowParams = home_window.getProperty("Params")
        log.info("windowParams : " + windowParams)
        # home_window.clearProperty("Params")
        if (windowParams):
            try:
                params = get_params(windowParams)
            except:
                params = {}

    log.info("Script params = " + str(params))

    home_window = HomeWindow()

    try: 
        setView(sys.argv[1])
    except:
        showSetViews()

    log.info("===== ViewMaster FINISHED =====")

def setView(viewType):
    defaultData = loadSkinDefaults()

    defaultViewData = defaultData.get("view", {})
    viewNum = defaultViewData.get(viewType)
    log.info("SETTING_VIEW : " + str(viewType) + " : " + str(viewNum))
    if viewNum is not None and viewNum != -1:
        xbmc.executebuiltin("Container.SetViewMode(%s)" % int(viewNum))

def showSetViews():
    log.info("showSetViews Called")
    log.info(__cwd__)
    settings = xbmcaddon.Addon(id='script.viewmaster')
    settings. setSetting('init', 'true')    
    defaultViews = DefaultViews("DefaultViews.xml", __cwd__, "default", "720p")
    defaultViews.doModal()
    del defaultViews


