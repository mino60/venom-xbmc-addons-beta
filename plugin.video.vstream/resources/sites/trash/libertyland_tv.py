#-*- coding: utf-8 -*-
# Par chataigne73
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import cUtil
from resources.lib.config import cConfig
import re, urllib, urllib2

SITE_IDENTIFIER = 'libertyland_tv'
SITE_NAME = 'Libertyland'
SITE_DESC = 'Les films recent en streaming et en telechargement'

URL_MAIN = 'http://www.libertyland.tv/'

URL_SEARCH = ('http://www.libertyland.tv/v2/recherche/', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

MOVIE_NEWS = (URL_MAIN + 'films/nouveautes/', 'showMovies') # films nouveautés
MOVIE_VIEWS = (URL_MAIN + 'films/plus-vus-mois/', 'showMovies') # films + plus
MOVIE_NOTES = (URL_MAIN + 'films/les-mieux-notes/', 'showMovies') # films mieux notés
MOVIE_GENRES = (True, 'showGenre')
MOVIE_VOSTFR = (URL_MAIN + 'films/films-vostfr/', 'showMovies') # films VOSTFR

SERIE_SERIES = (URL_MAIN + 'series/', 'showMovies')

ANIM_ANIMS = (URL_MAIN + 'http://www.libertyland.tv/v2/mangas/', 'showMovies')

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films Nouveautes', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VIEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VIEWS[1], 'Films Les plus vus', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NOTES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NOTES[1], 'Films Les mieux notes', 'films.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films Genre', 'genres.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Series', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_ANIMS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_ANIMS[1], 'Series', 'series.png', oOutputParameterHandler)
              
    oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()
    print 'libertyland:showSearch'
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  
    
    
def showGenre():
    oGui = cGui()
 
    liste = []
    liste.append( ['Action','http://www.libertyland.tv/films/genre/action.html'] )
    liste.append( ['Animation','http://www.libertyland.tv/films/genre/animation.html'] )
    liste.append( ['Aventure','http://www.libertyland.tv/films/genre/aventure.html/'] )
    liste.append( ['Biopic','http://www.libertyland.tv/films/genre/biopic.html'] )
    liste.append( ['Comedie','http://www.libertyland.tv/films/genre/comedie.html'] )
    liste.append( ['Comedie Dramatique','http://www.libertyland.tv/films/genre/comedie-dramatique.html'] )
    liste.append( ['Comedie Musicale','http://www.libertyland.tv/films/genre/comedie-musicale.html'] )
    liste.append( ['Drame','http://www.libertyland.tv/films/genre/drame.html'] )
    liste.append( ['Epouvante Horreur','http://www.libertyland.tv/films/genre/epouvante-horreur.html'] ) 
    liste.append( ['Espionnage','http://www.libertyland.tv/films/genre/espionnage.html'] )
    liste.append( ['Famille','http://www.libertyland.tv/films/genre/famille.html'] )
    liste.append( ['Fantastique','http://www.libertyland.tv/films/genre/fantastique.html'] )  
    liste.append( ['Guerre','http://www.libertyland.tv/films/genre/guerre.html'] )
    liste.append( ['Historique','http://www.libertyland.tv/films/genre/historique.html'] )
    liste.append( ['Judiciaire','http://www.libertyland.tv/films/genre/historique.html'] )
    liste.append( ['Medical','http://www.libertyland.tv/films/genre/musical.html'] )
    liste.append( ['Policier','http://www.libertyland.tv/films/genre/policier.html'] )
    liste.append( ['Peplum','http://www.libertyland.tv/films/genre/peplum.html'] )
    liste.append( ['Romance','http://www.libertyland.tv/films/genre/romance.html'] )
    liste.append( ['Science Fiction','http://www.libertyland.tv/films/genre/science-fiction.html'] )
    liste.append( ['Thriller','http://www.libertyland.tv/films/genre/thriller.html'] )
    liste.append( ['Western','http://www.libertyland.tv/films/genre/western.html'] )
                
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory() 


def showMovies(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    if sSearch:
        sPOST = 'categorie=films&mot_search='+sSearch
        request = urllib2.Request(URL_SEARCH,sPOST)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
        try: 
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
        sHtmlContent = reponse.read()
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
    
    sPattern = 'charger ([^<]+)<\/a>.+?<img class="img-responsive" *src="([^<]+)" *alt.+?<font color="#00CC00">(.+?)<\/font>.+?<div class="divstreaming"><a href="(.+?)">'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            
            sTitle = aEntry[0]
            sQual = aEntry[2]
            sQual = sQual.decode("utf-8").replace(u' qualit\u00E9','').replace('et ','/')
            sQual = sQual.replace('Bonne','MQ').replace('Haute','HQ').replace('Mauvaise','SD').encode("utf-8")
            sDisplayTitle = sTitle + ' ('+ sQual + ')'
            sDisplayTitle = cUtil().DecoTitle(sDisplayTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[3]))
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumbnail', aEntry[1])

            oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sDisplayTitle, '', aEntry[1], '', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)
           
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
            
    if not sSearch:
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent): 
    oParser = cParser()
    sPattern = '</a></li><li class="active"><a href=\'#\'>.+?<\/a><\/li><li><a href="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return aResult[1][0]

    return False
    
def showLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    #sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/','').replace('<iframe src=\'http://creative.rev2pub.com','').replace('&nbsp;','').replace('nbsp;','')
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    sPattern = 'src="http:\/\/www\.libertyland\.tv\/v2\/hebergeur\/[^<>]+?"> (.+?) <font style=\'color:#f00\'>(.+?)<\/font><\/h4>.+?data-fancybox-type="ajax" href="(.+?)" class="fancybox fancybox\.iframe">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            sUrlLink = URL_MAIN+aEntry[2]
            
            sTitle = ' (' + aEntry[1] + ')' + ' - [COLOR skyblue]' + aEntry[0] +'[/COLOR] ' + sMovieTitle
            #sDisplayTitle = cUtil().DecoTitle(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sUrl', sUrlLink)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)             
    
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()  
 
 
def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('sUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    oParser = cParser()
    sPattern = '<iframe.+?src="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    	
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            
            sHosterUrl = str(aEntry)
            
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail) 
                
    oGui.setEndOfDirectory()
   
def seriesHosters():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/','').replace('<iframe src=\'http://creative.rev2pub.com','')
               
    sPattern = '<dd><a href="([^<]+)" class="zoombox.+?" title="(.+?)"><button class="btn">.+?</button></a></dd>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            
            sHosterUrl = str(aEntry[0])
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(aEntry[1])
                oHoster.setFileName(aEntry[1])
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail) 
                
    oGui.setEndOfDirectory()
    
