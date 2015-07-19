#-*- coding: utf-8 -*-
#Venom.
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.config import cConfig
from resources.lib.parser import cParser
from resources.lib.util import cUtil
from resources.lib.player import cPlayer
import re,urllib2,urllib
 
SITE_IDENTIFIER = 'film_streaming_co'
SITE_NAME = 'Film-streaming.co'
SITE_DESC = 'Le seul site de streaming en HD 720p 100% Gratuit'
 
URL_MAIN = 'http://www.film-streaming.co/'
 
MOVIE_NEWS = ('http://www.film-streaming.co/index.php', 'showMovies')
MOVIE_FILMS = ('http://www.film-streaming.co/films.php', 'showMovies')
MOVIE_TOP = ('http://www.film-streaming.co/top.php', 'showMovies')
 
 
MOVIE_GENRES = (True, 'showGenre')
 
 
URL_SEARCH = ('http://www.film-streaming.co/search.php?movie=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'
 
 
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)
 
 
 
   
def DecoTitle(string):
    #pr les tag
    string = re.sub('([\[\(].{1,7}[\)\]])','[COLOR coral]\\1[/COLOR]', str(string))
    #pr les saisons
    string = re.sub('(?i)(.*)(saison [0-9]+)','\\1[COLOR coral]\\2[/COLOR]', str(string))
    return string
   
def load():
    oGui = cGui()
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Films Nouveautés', 'news.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TOP[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Top Films', 'top.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_FILMS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Tout Les Films', 'films.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', 'Films Genre', 'genres.png', oOutputParameterHandler)
           
    oGui.setEndOfDirectory()
 
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = 'http://www.film-streaming.co/search.php?movie='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  
 
 
   
def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    liste = []
    liste.append( ['Animation','http://www.film-streaming.co/genre.php?g=Animation'] )    
    liste.append( ['Action','http://www.film-streaming.co/genre.php?g=Action'] )
    liste.append( ['Arts Martiaux','http://www.film-streaming.co/genre.php?g=Arts%20Martiaux'] )
    liste.append( ['Aventure','http://www.film-streaming.co/genre.php?g=Aventure'] )
    liste.append( ['Biopic','http://www.film-streaming.co/genre.php?g=Biopic'] )
    liste.append( ['Comedie','http://www.film-streaming.co/genre.php?g=Com%C3%A9die'] )
    liste.append( ['Comedie Dramatique','http://www.film-streaming.co/genre.php?g=Com%C3%A9die%20dramatique'] )
    liste.append( ['Documentaire','http://www.film-streaming.co/genre.php?g=Documentaire'] )
    liste.append( ['Drame','http://www.film-streaming.co/genre.php?g=Drame'] )
    liste.append( ['Epouvante Horreur','http://www.film-streaming.co/genre.php?g=Epouvante-horreur'] )
    liste.append( ['Espionage','http://www.film-streaming.co/genre.php?g=Espionnage'] )  
    liste.append( ['Fantastique','http://www.film-streaming.co/genre.php?g=Fantastique'] )
    liste.append( ['Famille','http://www.film-streaming.co/genre.php?g=Famille'] )
    liste.append( ['Guerre','http://www.film-streaming.co/genre.php?g=Guerre'] )
    liste.append( ['Historique','http://www.film-streaming.co/genre.php?g=Historique'] )
    liste.append( ['Musical','http://www.film-streaming.co/genre.php?g=Musical'] )
    liste.append( ['Policier','http://www.film-streaming.co/genre.php?g=Policier'] )
    liste.append( ['Romance','http://www.film-streaming.co/genre.php?g=Romance'] )
    liste.append( ['Sciense Fiction','http://www.film-streaming.co/genre.php?g=Science%20fiction'] )
    liste.append( ['Thriller','http://www.film-streaming.co/genre.php?g=Thriller'] )
    liste.append( ['Western','http://www.film-streaming.co/genre.php?g=Western'] )
               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
   
   
def showMovies(sSearch=''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<span class="likeThis">', '').replace('</span>','')
 
    sPattern = '<td.+?class="over_modul">.+?<a href="(.+?)"><img src="(.+?)" border="0" alt="(.+?)\sstreaming".+?</a>'    
 
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sThumbnail = URL_MAIN+str(aEntry[1])
            sUrl = URL_MAIN+str(aEntry[0])
 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[2]))
            oOutputParameterHandler.addParameter('sThumbnail', sThumbnail)            
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', aEntry[2], 'films.png', sThumbnail, '', oOutputParameterHandler)
           
        cConfig().finishDialog(dialog)
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
 
    if not sSearch:
        oGui.setEndOfDirectory()
         
def __checkForNextPage(sHtmlContent):
    sPattern = '(?:<span class="btn btn-default active">|<strong class="current">.+?</strong>).+?<a class="btn btn-default" href="(.+?)">.+?</a>'
 
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    print aResult
 
    if (aResult[0] == True):
        return URL_MAIN + aResult[1][0]
 
    return False
 
def showHosters():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
     
    url = ''
   
    oParser = cParser()
    sPattern = 'document.write\(unescape\("(.+?)"\)\);'
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    if (aResult[0] == True):
        chainedecrypte = urllib.unquote(aResult[1][0])
        sPattern = 'file: "(http.+?mp4)"'
        aResult = re.findall(sPattern,chainedecrypte)
        if (aResult):
            url = aResult[0]
   
    #dialogue final
    if (url):
 
        sHosterUrl = str(url)
        oHoster = cHosterGui().checkHoster(sHosterUrl)
       
        if (oHoster != False):
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, '')
             
        #cConfig().finishDialog(dialog)
 
    oGui.setEndOfDirectory()
