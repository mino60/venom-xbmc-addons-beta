#-*- coding: utf-8 -*-
#Venom.
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.util import cUtil

import os,unicodedata,re,sys
import urllib,re
import xbmc,xbmcgui

SITE_IDENTIFIER = 'cLibrary'
SITE_NAME = 'Library'

#sources.xml

class cLibrary:

    def __init__(self):
        self.__sMovieFolder = xbmc.translatePath(cConfig().getSetting('Library_folder_Movies'))
        self.__sTVFolder = xbmc.translatePath(cConfig().getSetting('Library_folder_TVs'))
        
        if not self.__sMovieFolder:
            PathCache = cConfig().getSettingCache()
            self.__sMovieFolder = os.path.join(PathCache,'Movie\\')
            cConfig().setSetting('Library_folder_Movies',self.__sMovieFolder)
        if not os.path.exists(self.__sMovieFolder):
                os.mkdir(self.__sMovieFolder)
                
        if not self.__sTVFolder:
            PathCache = cConfig().getSettingCache()
            self.__sTVFolder = os.path.join(PathCache,'TVs\\')
            cConfig().setSetting('Library_folder_TVs',self.__sTVFolder)
        if not os.path.exists(self.__sTVFolder):
                os.mkdir(self.__sTVFolder)
            
        self.__sTitle = ''

    def setLibrary(self):
        oInputParameterHandler = cInputParameterHandler()
        
        #sCat = oInputParameterHandler.getValue('sCat')
        #pas encore fiable comme methode
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Selectionner une categorie',['Film','Serie (Ne marche pas encore)'])
        if ret == 0:
            sCat = '1'
        elif ret == -1:
            return
        else:
            sCat = '2'
       
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        sFileName = oInputParameterHandler.getValue('sFileName')
        sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        
        #print oInputParameterHandler.getAllParameter()
        
        sLink = 'plugin://plugin.video.vstream/?function=play&site=cHosterGui&sFileName=' + sFileName + '&sMediaUrl=' + sMediaUrl + '&sHosterIdentifier=' + sHosterIdentifier
        
        sTitle = sFileName        
        #sTitle = xbmc.getInfoLabel('ListItem.title')
        #meta['icon'] = xbmc.getInfoLabel('ListItem.Art(thumb)')
        #meta['fanart'] =  xbmc.getInfoLabel('ListItem.Art(fanart)')
        
        folder = self.__sMovieFolder
        
        #film
        if sCat == '1':
            folder = self.__sMovieFolder
            
            sTitle = cUtil().CleanName(sTitle)
            
            try:
                print folder
                self.MakeFile(folder,sTitle,sLink)
                cConfig().showInfo('vStream', 'Element rajouté a la librairie')
                xbmc.executebuiltin('UpdateLibrary(video, '+ folder + ')')
            except:
                cConfig().showInfo('Erreur', 'Rajout impossible')
            
        #serie
        elif sCat == '2':
            folder = self.__sTVFolder
            
            sTitle = cUtil().FormatSerie(sTitle)
            sTitle = cUtil().CleanName(sTitle)
            sTitleGlobal = re.sub('((?:[s|e][0-9]+){1,2})','',sTitle)

            try:
                print folder
                folder2 = folder + '/' + sTitleGlobal + '/'
                
                if not os.path.exists(folder2):
                    os.mkdir(folder2)
                
                self.MakeFile(folder2,sTitle,sLink)
                cConfig().showInfo('vStream', 'Element rajouté a la librairie')
                xbmc.executebuiltin('UpdateLibrary(video, '+ folder + ')')
            except:
                cConfig().showInfo('Erreur', 'Rajout impossible')


    def MakeFile(self,folder,name,content):
        stream = os.path.join(folder, str(name) + '.strm')
        f = open(stream, 'w')
        f.write(str(content))
        f.close()
        
