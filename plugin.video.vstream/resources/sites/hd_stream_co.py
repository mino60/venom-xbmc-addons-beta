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
import re,urllib2,urllib
 
SITE_IDENTIFIER = 'hd_stream_co'
SITE_NAME = 'Hd-stream.co'
SITE_DESC = "Le seul site de streaming en HD 720p 100% Gratuit, regardez tous les films que vous desirez en streaming HD en illmit? sur film streaming.ws"
 
URL_MAIN = 'http://www.hd-stream.co/'
 
MOVIE_NEWS = ('http://www.hd-stream.co/index.php', 'showMovies')
MOVIE_FILMS = ('http://www.hd-stream.co/films.php', 'showMovies')
 
 
MOVIE_GENRES = (True, 'showGenre')
 
 
URL_SEARCH = ('http://www.hd-stream.co/search.php?movie=', 'showMovies')
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
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = 'http://www.hd-stream.co/search.php?movie='+sSearchText  
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  
 
 
def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    liste = []
    liste.append( ['Animation','http://www.hd-stream.co/genre.php?g=Animation'] )    
    liste.append( ['Action','http://www.film-streaming.ws/genre.php?g=Action'] )
    liste.append( ['Arts Martiaux','http://www.film-streaming.ws/genre.php?g=Arts%20Martiaux'] )
    liste.append( ['Aventure','http://www.film-streaming.ws/genre.php?g=Aventure'] )
    liste.append( ['Biopic','http://www.film-streaming.ws/genre.php?g=Biopic'] )
    liste.append( ['Comedie','http://www.film-streaming.ws/genre.php?g=Com%C3%A9die'] )
    liste.append( ['Comedie Dramatique','http://www.film-streaming.ws/genre.php?g=Com%C3%A9die%20dramatique'] )
    liste.append( ['Comedie Musicale','http://full-stream.me/films-en-vk-streaming/comedie-musicale/'] )
    liste.append( ['Documentaire','http://www.film-streaming.ws/genre.php?g=Documentaire'] )
    liste.append( ['Drame','http://www.film-streaming.ws/genre.php?g=Drame'] )
    liste.append( ['Epouvante Horreur','http://www.film-streaming.ws/genre.php?g=Epouvante-horreur'] )
    liste.append( ['Espionage','http://www.film-streaming.ws/genre.php?g=Espionnage'] )  
    liste.append( ['Fantastique','http://www.film-streaming.ws/genre.php?g=Fantastique'] )
    liste.append( ['Famille','http://www.film-streaming.ws/genre.php?g=Famille'] )
    liste.append( ['Guerre','http://www.film-streaming.ws/genre.php?g=Guerre'] )
    liste.append( ['Historique','http://www.film-streaming.ws/genre.php?g=Historique'] )
    liste.append( ['Musical','http://www.film-streaming.ws/genre.php?g=Musical'] )
    liste.append( ['Policier','http://www.film-streaming.ws/genre.php?g=Policier'] )
    liste.append( ['Romance','http://www.film-streaming.ws/genre.php?g=Romance'] )
    liste.append( ['Sciense Fiction','http://www.film-streaming.ws/genre.php?g=Science%20fiction'] )
    liste.append( ['Thriller','http://www.film-streaming.ws/genre.php?g=Thriller'] )
    liste.append( ['Western','http://www.film-streaming.ws/genre.php?g=Western'] )
               
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
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<span class="likeThis">', '').replace('</span>','')
    #if 'hd' in sUrl:
    #sPattern = '<div class="view view-third">.*?<img src="(.+?)" alt="(.+?)"><a href="(.+?)" style=".+?"><div class="mask"><h2>.+?</h2><p>(.+?)</p>'
    #sPattern = '<div class="view view-third">.*?<img src="(.+?)" alt="(.+?)"><div class="mask"><h2>.+?</h2><p>(.+?)</p>'  #regex pour Top films
   # else:
    sPattern = '<div class="view view-third">.*?<img src="(.+?)" alt="(.+?)"><a href="(.+?)" style=".+?"><div class="mask"><h2>.+?</h2><p>'
 
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
 
    print aResult
   
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = aEntry[1].decode('latin-1').encode("utf-8")
            sThumbnail = 'http://www.hd-stream.co/'+str(aEntry[0])
            #sUrl = 'http://www.film-streaming.co/'+str(aEntry[2])
            sUrl = str(aEntry[2])
            if not 'http://www.film-streaming.co/' in sUrl:
                 sUrl = 'http://www.film-streaming.co/' + sUrl
            #print sThumbnail
            #sThumbnail = str(aEntry[1])
            #if not 'http://www.film-streaming.ws/' in sThumbnail:
                  #sThumbnail = 'http://www.film-streaming.ws/' + sThumbnail
            #print sThumbnail
 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + str(aEntry[2]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sThumbnail', (sThumbnail))            
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', aEntry[1], '', sThumbnail, '', oOutputParameterHandler)
           
        cConfig().finishDialog(dialog)
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
 
    if not sSearch:
        oGui.setEndOfDirectory()
         
def __checkForNextPage(sHtmlContent):
    sPattern = 'href="([^<>]+?)"> Page Suivante >></a>'
 
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
 
    if (aResult[0] == True):
        return URL_MAIN + aResult[1][0]
 
    return False
 
def showHosters():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    #recuperation urls
    headers = {'Host' : 'www.hd-stream.co',
               'User-Agent': 'Mozilla/5.0',
               'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language' : 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3'}
    request = urllib2.Request(sUrl,None,headers)
    try:
        reponse = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        print e.code
        print e.msg
        print e.headers
        print e.fp.read()
 
    sHtmlContent = reponse.read()
   
 
    reponse.close()
 
   
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
