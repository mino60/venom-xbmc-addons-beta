#-*- coding: utf-8 -*-
#From chataigne73

from resources.lib.config import cConfig
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.favourite import cFav
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import cUtil

import urllib, unicodedata, re, time
import xbmcgui
import xbmc

from resources.lib.dl_deprotect import DecryptDlProtect


SITE_IDENTIFIER = 'zone_telechargement_com' 
SITE_NAME = 'Zone-Telechargement.com' 
SITE_DESC = '' 

URL_MAIN = 'http://www.zone-telechargement.com/'

URL_SEARCH_MOVIES = (URL_MAIN + 'films-gratuit.html?q=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + 'telecharger-series.html?q=', 'showMovies')

FUNCTION_SEARCH = 'showMovies'

#MOVIE_NEWS = (URL_MAIN + 'films/dvdrip-bdrip/?showby=month', 'showMovies') # films nouveautés
MOVIE_NEWS = (URL_MAIN + 'films-gratuit.html', 'showMovies') # films nouveautés
MOVIE_EXCLUS = (URL_MAIN + 'exclus.html', 'showMovies') # exclus (films populaires)
MOVIE_VIEWS = (URL_MAIN + 'films-gratuit.html?tab=all&orderby_by=popular&orderby_order=desc', 'showMovies') # films + vus
MOVIE_NOTES = (URL_MAIN + 'films-gratuit.html?tab=all&orderby_by=rating&orderby_order=desc', 'showMovies') # films mieux notés
MOVIE_GENRES = (True, 'showGenre')
#MOVIE_VF = (URL_MAIN + 'langues/french', 'showMovies') # films VF
MOVIE_VOSTFR = (URL_MAIN + 'langues/vostfr', 'showMovies') # films VOSTFR
MOVIE_ANIME = (URL_MAIN + 'dessins-animes.html', 'showMovies') # dessins animes
SERIE_VF = (URL_MAIN + 'series-vf.html', 'showMovies') # serie VF
SERIE_VOSTFR = (URL_MAIN + 'series-vostfr.html', 'showMovies') # serie VOSTFR
BLURAY_NEWS = (URL_MAIN + 'films-bluray-hd.html', 'showMovies') # derniers Blu-Rays
#SERIE_GENRE = (True, 'showGenre')
DOCU_NEWS = (URL_MAIN + 'documentaires-gratuit.html', 'showMovies') # derniers docu
TV_NEWS = (URL_MAIN + 'emissions-tv.html', 'showMovies') # dernieres emissions tv
SPECT_NEWS = (URL_MAIN + 'spectacles.html', 'showMovies') # dernieres spectacles


def load(): 
    oGui = cGui() 

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EXCLUS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_EXCLUS[1], 'Exclus (Films populaires)', 'news.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Derniers Films ajoutes', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', BLURAY_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, BLURAY_NEWS[1], 'Derniers Blu-rays ajoutes', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VIEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Films Les plus vus', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NOTES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Films Les mieux notes', 'films.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ANIME[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Dessins Animes', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films Genre', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Dernieres Séries VF ajoutees', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Dernieres Series VOSTFR ajoutées', 'series.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/') 
    oGui.addDir(SITE_IDENTIFIER, 'showSearchMovies', 'Recherche de films', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearchSeries', 'Recherche de series', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', DOCU_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Deniers Documentaires', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', TV_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Dernieres Emissions TV', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SPECT_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Derniers Spectacles', 'films.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 

def showSearchMovies(): 
    oGui = cGui()
    #print 'ZT:showSearch'
    sSearchText = oGui.showKeyBoard() 
    if (sSearchText != False):
        sUrl = URL_SEARCH_MOVIES[0] + sSearchText +'&tab=all&orderby_by=date&orderby_order=desc&displaychangeto=thumb'
        #print sUrl
        showMovies(sUrl) 
        oGui.setEndOfDirectory()
        return  
    
def showSearchSeries(): 
    oGui = cGui()
    #print 'ZT:showSearch'
    sSearchText = oGui.showKeyBoard() 
    if (sSearchText != False):
        sUrl = URL_SEARCH_SERIES[0] + sSearchText +'&tab=all&orderby_by=date&orderby_order=desc&displaychangeto=thumb'
        #print sUrl
        showMovies(sUrl) 
        oGui.setEndOfDirectory()
        return  
    
    
def showGenre(): 
    oGui = cGui()
    
    liste = []
    liste.append( ['Action',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=1'] )
    liste.append( ['Animation',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=2'] )
    liste.append( ['Arts Martiaux',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=3'] )
    liste.append( ['Aventure',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=4'] )
    liste.append( ['Biopic',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=5'] )
    liste.append( ['Comedie Dramatique',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=7'] )
    liste.append( ['Comedie Musicale',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=8'] )
    liste.append( ['Comedie',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=9'] )
    liste.append( ['Divers',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=10'] )
    liste.append( ['Documentaires',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=11'] )
    liste.append( ['Drame',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=12'] )
    liste.append( ['Epouvante Horreur',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=13'] ) 
    liste.append( ['Espionnage',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=14'] )
    liste.append( ['Famille',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=15'] )
    liste.append( ['Fantastique',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=16'] )  
    liste.append( ['Guerre',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=17'] )
    liste.append( ['Historique',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=18'] )
    liste.append( ['Musical',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=19'] )
    liste.append( ['Peplum',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=6'] )
    liste.append( ['Policier',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=20'] )
    liste.append( ['Romance',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=21'] )
    liste.append( ['Science Fiction',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=22'] )
    liste.append( ['Thriller',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=23'] )
    liste.append( ['Western',URL_MAIN + 'films-dvdrip-bdrip.html?genrelist[]=24'] )
                
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)    
       
    oGui.setEndOfDirectory() 


def showMovies(sSearch = ''):
    oGui = cGui() 
    if sSearch:
      sUrl = sSearch
      #print "ZT:showmovies:venant de search"
      #print sUrl
    else:
        #print "ZT:showmovies"
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl') 
   
    oRequestHandler = cRequestHandler(sUrl) 
    sHtmlContent = oRequestHandler.request() 
    #sHtmlContent = sHtmlContent.replace('<span class="tr-dublaj"></span>', '').replace('<span class="tr-altyazi"></span>','')
    
    sPattern = '<div style="height:[0-9]{3}px;"><a title="" href="(.+?)" ><img class=.+?src="([^<]+)" width="[0-9]{3}" height="[0-9]{3}" border="0" .+?<div class="cover_infos_global toh"><div class="cover_infos_title"><a title="" href=".+?" >(.+?)<'
    
	#pour faire simple recherche ce bout de code dans le code source de l'url
    #- ([^<]+) je veut cette partie de code mais y a une suite
    #- .+? je ne veut pas cette partis et peux importe ceux qu'elle contient
    #- (.+?) je veut cette partis et c'est la fin
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    #print aResult 
    
    if (aResult[0] == True):
        total = len(aResult[1])        
        for aEntry in aResult[1]:
                        
            #L'array affiche vos info dans l'orde de sPattern en commencant a 0
            sTitle = str(aEntry[2])
            sUrl = aEntry[0]
            sFanart =aEntry[1]
            sThumbnail=aEntry[1]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl)) 
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle)) 
            oOutputParameterHandler.addParameter('disp', 'search1')
            oOutputParameterHandler.addParameter('sThumbnail', sThumbnail) #sortie du poster
            
            if 'series' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showSeriesLinks', sTitle, 'series.png', sThumbnail, sFanart, oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, 'films.png', sThumbnail, sFanart, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
            #Ajoute une entree pour le lien Next | pas de addMisc pas de poster et de description inutile donc

    #test pr chnagement mode
    xbmc.executebuiltin('Container.SetViewMode(500)')
    #bmcgui.ListItem.select(1)  
     
    if not sSearch:
        oGui.setEndOfDirectory() #ferme l'affichage


def __checkForNextPage(sHtmlContent): #cherche la page suivante
    oParser = cParser()
    sPattern = '<a style="margin-left:2%;" href="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult #affiche le result dans le log
    if (aResult[0] == True):
        #print aResult
        return aResult[1][0]
        
    return False
    
def showLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    #print "ZT:showLinks"
    print sUrl
	
    oRequestHandler = cRequestHandler(sUrl) #requete sur l'url
    sHtmlContent = oRequestHandler.request()
   
    oParser = cParser()
    
    #on recherche d'abord la qualité courante
    sPattern = '<b>(?:<strong>)*Qualité (.+?)<'
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult
    
    if (aResult[0]):

        dialog = cConfig().createDialog(SITE_NAME)
        
        sTitle = sMovieTitle +  ' - [COLOR skyblue]' + aResult[1][0] +'[/COLOR]' + ' Debug 1'
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
        oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
        oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)
	
    
    sPattern = '<a title="Téléchargez.+?en (.+?)" href="(.+?)"><button class="button_subcat"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult
	
    if (aResult[0] == True): #on regarde si dispo dans d'autres qualités
        total = len(aResult[1])
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            
            sTitle = sMovieTitle +  ' - [COLOR skyblue]' + aEntry[0]+'[/COLOR]' + 'Debug 2'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sUrl', aEntry[1])
            oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)             
    
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()  

def showSeriesLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    #print "ZT:showSeriesLinks"
	
    oRequestHandler = cRequestHandler(sUrl) #requete sur l'url
    sHtmlContent = oRequestHandler.request()

    #Mise àjour du titre
    oParser = cParser()
    sPattern = '<h1 style="font-family:\'Ubuntu Condensed\',\'Segoe UI\',Verdana,Helvetica,sans-serif;">(?:<span itemprop="name">)([^<]+?)<'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0]):
        sMovieTitle = aResult[1][0]
	
    
	#on recherche d'abord la qualité courante

    sPattern = '<span style="color:#[0-9a-z]{6}"><b>\[[^\]]+?\] ([^<]+?)</b></span>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    #print aResult
    if (aResult[0] == False):
        oParser = cParser()
        sPattern = '<span style="color:#[0-9a-z]{6}"><b><strong>\[[^\]]+?\] ([^<]+?)</strong></b></span>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        #print aResult   
	
    dialog = cConfig().createDialog(SITE_NAME)
	
    oGui.addText('','[COLOR olive]'+'Qualités disponibles pour cette saison :'+'[/COLOR]')
	
    sTitle = sMovieTitle +  ' - [COLOR skyblue]' + aResult[1][0]+'[/COLOR]'
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('sUrl', sUrl)
    oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
    oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
    oGui.addMovie(SITE_IDENTIFIER, 'showSeriesHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)
	

    sPattern1 = '<a title="Téléchargez.+?en ([^"]+?)" href="([^"]+?)"><button class="button_subcat"'
    aResult1 = oParser.parse(sHtmlContent, sPattern1)
    #print aResult1
    
    if (aResult1[0] == True): #on regarde si dispo dans d'autres qualités
        total = len(aResult1[1])
        
        for aEntry in aResult1[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            
            sTitle = sMovieTitle +  ' - [COLOR skyblue]' + aEntry[0]+'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sUrl', aEntry[1])
            oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addMovie(SITE_IDENTIFIER, 'showSeriesHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)             
    
        oGui.addText('','[COLOR olive]'+'Saisons aussi disponibles pour cette série :'+'[/COLOR]')
    
    oParser = cParser()
    sPattern2 = '<a title="Téléchargez[^"]+?" href="([^"]+?)"><button class="button_subcat" style="font-size: 12px;height: 26px;width:190px;color:666666;letter-spacing:0.05em">([^<]+?)</button>'
    aResult2 = oParser.parse(sHtmlContent, sPattern2)
    #print aResult2
	
    if (aResult2[0] == True): #on regarde si dispo d'autres saisons
        total = len(aResult2[1])
	
        for aEntry in aResult2[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            
            sTitle = '[COLOR skyblue]' + aEntry[1]+'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            #oGui.addMovie(SITE_IDENTIFIER, 'showSeriesLinks', sTitle, '', sThumbnail, '', oOutputParameterHandler)             
            oGui.addTV(SITE_IDENTIFIER, 'showSeriesLinks', sTitle, 'series.png', sThumbnail, '', oOutputParameterHandler)
	
	
	
    cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()  	
 
def showHosters():# recherche et affiche les hotes
    #print "ZT:showHosters"
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler() #apelle l'entree de paramettre
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('sUrl')
    sThumbnail=oInputParameterHandler.getValue('sThumbnail')
    
    print sUrl
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #Fonction pour recuperer uniquement les liens
    sHtmlContent = Cutlink(sHtmlContent)
   
    oParser = cParser()
    
    sPattern = '<span style="color:#.{6}">([^>]+?)<\/span>(?:.(?!color))+?<a href="([^<>"]+?)" target="_blank">Télécharger<\/a>|>\[(Liens Premium) \]<'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    print aResult
        
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
		
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            if aEntry[2]:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
                oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                oGui.addMisc(SITE_IDENTIFIER, 'showHosters', '[COLOR red]'+str(aEntry[2])+'[/COLOR]', '', '', '', oOutputParameterHandler)
            else:
                sTitle = '[COLOR skyblue]' + aEntry[0]+ '[/COLOR] ' + sMovieTitle
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('sUrl', aEntry[1])
                oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                oGui.addMovie(SITE_IDENTIFIER, 'Display_protected_link', sTitle, '', sThumbnail, '', oOutputParameterHandler)
   
            cConfig().finishDialog(dialog)

        oGui.setEndOfDirectory()

def showSeriesHosters():# recherche et affiche les hotes
    #print "ZT:showSeriesHosters"
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler() #apelle l'entree de paramettre
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('sUrl')
    sThumbnail=oInputParameterHandler.getValue('sThumbnail')
    print sUrl
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #Fonction pour recuperer uniquement les liens
    sHtmlContent = Cutlink(sHtmlContent)
   
    oParser = cParser()
    
    sPattern = '<a href="([^"]+?)" target="_blank">([^<]+)<\/a>|<span style="color:#.{6}">([^<]+)<\/span>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    print aResult
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
		
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            #print aEntry
            if dialog.iscanceled():
                break
            
            if aEntry[2]:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
                oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                oGui.addMisc(SITE_IDENTIFIER, 'showSeriesHosters', '[COLOR red]'+str(aEntry[2])+'[/COLOR]', '', '', '', oOutputParameterHandler)
            else:
                sTitle = sMovieTitle + ' ' + aEntry[1]
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('sUrl', aEntry[0])
                oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                oGui.addMovie(SITE_IDENTIFIER, 'Display_protected_link', sTitle, '', sThumbnail, '', oOutputParameterHandler)
   
            cConfig().finishDialog(dialog)

        oGui.setEndOfDirectory()
        
def Display_protected_link():
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('sUrl')
    sThumbnail=oInputParameterHandler.getValue('sThumbnail')

    oParser = cParser()
    
    sHtmlContent = DecryptDlProtect(sUrl)
    print sHtmlContent
    
    if sHtmlContent:

        sPattern_dlprotect = '><a href="(.+?)" target="_blank">'
        aResult_dlprotect = oParser.parse(sHtmlContent, sPattern_dlprotect)
        print aResult_dlprotect
        
        if (aResult_dlprotect[0]):
            for aEntry in aResult_dlprotect[1]:
                sHosterUrl = aEntry
                print sHosterUrl
                
                oHoster = cHosterGui().checkHoster(sHosterUrl)
                if (oHoster != False):
                    sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                    oHoster.setDisplayName(sDisplayTitle)
                    oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
                        
    oGui.setEndOfDirectory()
    
def Cutlink(sHtmlContent):
    oParser = cParser()
    sPattern = '<img src="http:\/\/www\.zone-telechargement\.com\/prez\/style\/v1\/liens\.png"(.+?)<div class="divinnews"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0]):
        return aResult[1][0]
    
    return ''
    
