#-*- coding: utf-8 -*-
#Venom.
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.siteHandler import cSiteHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.db import cDb
import os
import urllib

SITE_IDENTIFIER = 'cHome'
SITE_NAME = 'Home'
color_cherches = cConfig().getSetting('color_cherches')
color_films = cConfig().getSetting('color_films')
color_series = cConfig().getSetting('color_series')
color_anims = cConfig().getSetting('color_anims')
color_tvs = cConfig().getSetting('color_tvs')
color_sports = cConfig().getSetting('color_sports')
color_docs = cConfig().getSetting('color_docs')
color_videos = cConfig().getSetting('color_videos')

oPath = cConfig().getAddonPath()
movie_fanart = os.path.join(oPath,'resources','art','movie_fanart.jpg')
serie_fanart = os.path.join(oPath,'resources','art','serie_fanart.jpg')
movie_fanart = os.path.join(oPath,'resources','art','movie_fanart.jpg')
anim_fanart = os.path.join(oPath,'resources','art','anim_fanart.jpg')
search_fanart = os.path.join(oPath,'resources','art','search_fanart.jpg')
tv_fanart = os.path.join(oPath,'resources','art','tv_fanart.jpg')
doc_fanart = os.path.join(oPath,'resources','art','doc_fanart.jpg')
sport_fanart = os.path.join(oPath,'resources','art','sport_fanart.jpg')
buzz_fanart = os.path.join(oPath,'resources','art','buzz_fanart.jpg')

class cHome:
      

    def load(self):
        oGui = cGui()

        if (cConfig().getSetting('home_cherches') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', search_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'showSearch', '[COLOR '+color_cherches+']'+cConfig().getlanguage(30076)+'[/COLOR]', 'search.png', oOutputParameterHandler)
        
        if (cConfig().getSetting('home_cherchev') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', search_fanart)
            oGui.addDir('themoviedb_org', 'load', '[COLOR '+color_cherches+']'+cConfig().getlanguage(30088)+'[/COLOR]', 'searchtmdb.png', oOutputParameterHandler)
            
        if (cConfig().getSetting('home_tvs') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', tv_fanart)
            oGui.addDir('freebox', 'load', '[COLOR '+color_tvs+']'+cConfig().getlanguage(30115)+'[/COLOR]', 'tv.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_films') == 'true'):
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', movie_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR '+color_films+']'+cConfig().getlanguage(30120)+'[/COLOR]', 'films.png', oOutputParameterHandler)
            

        if (cConfig().getSetting('home_series') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', serie_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR '+color_series+']'+cConfig().getlanguage(30121)+'[/COLOR]', 'series.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_anims') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', anim_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'showAnimes', '[COLOR '+color_anims+']'+cConfig().getlanguage(30122)+'[/COLOR]', 'animes.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_docs') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', doc_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'docDocs', '[COLOR '+color_docs+']'+cConfig().getlanguage(30112)+'[/COLOR]', 'doc.png', oOutputParameterHandler)
        
        if (cConfig().getSetting('home_sports') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', sport_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'sportSports', '[COLOR '+color_sports+']'+cConfig().getlanguage(30113)+'[/COLOR]', 'sport.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_videos') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oOutputParameterHandler.addParameter('sFanart', buzz_fanart)
            oGui.addDir(SITE_IDENTIFIER, 'movieNets', '[COLOR '+color_videos+']'+cConfig().getlanguage(30114)+'[/COLOR]', 'buzz.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('cFav', 'getFavourites', '[COLOR teal]'+cConfig().getlanguage(30210)+'[/COLOR]', 'mark.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showSources', cConfig().getlanguage(30116), 'host.png', oOutputParameterHandler)


        
        oGui.setEndOfDirectory()
    
    def showTV(self):
        oGui = cGui()
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('freebox', 'load', '[COLOR '+color_tvs+']Télévision Box[/COLOR]', 'tv.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('chaine_tv', 'load', '[COLOR '+color_tvs+']Tv du net[/COLOR]', 'tv.png', oOutputParameterHandler)
        
        oGui.setEndOfDirectory()
        
    def showMovies(self):
        oGui = cGui()
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'movieNews', '[COLOR '+color_films+']'+cConfig().getlanguage(30101)+'[/COLOR]', 'news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'movieViews', '[COLOR '+color_films+']'+cConfig().getlanguage(30102)+'[/COLOR]', 'views.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'movieComments', '[COLOR '+color_films+']'+cConfig().getlanguage(30103)+'[/COLOR]', 'comments.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'movieNotes', '[COLOR '+color_films+']'+cConfig().getlanguage(30104)+'[/COLOR]', 'notes.png', oOutputParameterHandler)
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'movieGenres', '[COLOR '+color_films+']'+cConfig().getlanguage(30105)+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        
        oGui.setEndOfDirectory()
        
    def showSeries(self):
        oGui = cGui()
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'serieSeries', '[COLOR '+color_series+']'+cConfig().getlanguage(30106)+'[/COLOR]', 'series.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'serieVfs', '[COLOR '+color_series+']'+cConfig().getlanguage(30107)+'[/COLOR]', 'seriesvf.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'serieVostfrs', '[COLOR '+color_series+']'+cConfig().getlanguage(30108)+'[/COLOR]', 'seriesvostfr.png', oOutputParameterHandler)
        
        oGui.setEndOfDirectory()
        
    def showAnimes(self):
        oGui = cGui()
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'animAnims', '[COLOR '+color_anims+']'+cConfig().getlanguage(30109)+'[/COLOR]', 'animes.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'animVfs', '[COLOR '+color_anims+']'+cConfig().getlanguage(30110)+'[/COLOR]', 'animesvf.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'animVostfrs', '[COLOR '+color_anims+']'+cConfig().getlanguage(30111)+'[/COLOR]', 'animesvostfr.png', oOutputParameterHandler)
        
        oGui.setEndOfDirectory()

    def showSources(self):
        oGui = cGui()
        
        oPluginHandler = cPluginHandler()
        aPlugins = oPluginHandler.getAvailablePlugins()
        for aPlugin in aPlugins:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            oGui.addDir(aPlugin[1], 'load', aPlugin[0], 'tv.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()


    def movieNews(self):
        self.__callpluging('MOVIE_NEWS', '[COLOR '+color_films+']Films Nouveautés[/COLOR]', 'news.png')

    def movieViews(self):
        self.__callpluging('MOVIE_VIEWS', '[COLOR '+color_films+']Films Les Plus Vus[/COLOR]', 'views.png')

    def movieComments(self):
        self.__callpluging('MOVIE_COMMENTS', '[COLOR '+color_films+']Films Les Plus Commentés[/COLOR]', 'comments.png')

    def movieNotes(self):
        self.__callpluging('MOVIE_NOTES', '[COLOR '+color_films+']Films Les Mieux Notés[/COLOR]', 'notes.png')

    def movieGenres(self):
        self.__callpluging('MOVIE_GENRES', '[COLOR '+color_films+']Films Par Genres[/COLOR]', 'genres.png')

    def serieSeries(self):
        self.__callpluging('SERIE_SERIES', '[COLOR '+color_series+']Séries Nouveautés[/COLOR]', 'series.png')

    def serieVfs(self):
        self.__callpluging('SERIE_VFS', '[COLOR '+color_series+']Séries VF[/COLOR]', 'series.png')

    def serieVostfrs(self):
        self.__callpluging('SERIE_VOSTFRS', '[COLOR '+color_series+']Séries VOSTFR[/COLOR]', 'series.png')

    def animAnims(self):
        self.__callpluging('ANIM_ANIMS', '[COLOR '+color_anims+']Animes Nouveautés[/COLOR]', 'animes.png')

    def animVfs(self):
        self.__callpluging('ANIM_VFS', '[COLOR '+color_anims+']Animes VF[/COLOR]', 'animes.png')

    def animVostfrs(self):
        self.__callpluging('ANIM_VOSTFRS', '[COLOR '+color_anims+']Animes VOSTFR[/COLOR]', 'animes.png')

    def animMovies(self):
        self.__callpluging('ANIM_MOVIES', '[COLOR '+color_anims+']Animes OAVS/Films[/COLOR]', 'animes.png')

    def docDocs(self):
        self.__callpluging('DOC_DOCS', '[COLOR '+color_docs+']Documentaires[/COLOR]', 'doc.png')

    def sportSports(self):
        self.__callpluging('SPORT_SPORTS', '[COLOR '+color_sports+']Sport[/COLOR]', 'sport.png')

    def movieNets(self):
        self.__callpluging('MOVIE_NETS', '[COLOR '+color_videos+']Vidéo du Net[/COLOR]', 'buzz.png')
        
    def showSearch(self):

        if (cConfig().getSetting("history-view") == 'true'):
            readdb = 'True'
        else:
            readdb = 'False'

        oGui = cGui()
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('disp', 'search1')
        oOutputParameterHandler.addParameter('readdb', readdb)
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', cConfig().getSetting('search1_label'), 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('disp', 'search2')
        oOutputParameterHandler.addParameter('readdb', readdb)
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', cConfig().getSetting('search2_label'), 'search.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('disp', 'search3')
        oOutputParameterHandler.addParameter('readdb', readdb)
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', cConfig().getSetting('search3_label'), 'search.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('disp', 'search4')
        oOutputParameterHandler.addParameter('readdb', readdb)
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', cConfig().getSetting('search4_label'), 'search.png', oOutputParameterHandler)
        

        #history
        if (cConfig().getSetting("history-view") == 'true'):

            row = cDb().get_history()
            for match in row:
                
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', 'http://venom')      
                oOutputParameterHandler.addParameter('searchtext', match[1])
                oOutputParameterHandler.addParameter('disp', match[2])
                oOutputParameterHandler.addParameter('readdb', 'False')
                oGui.addDir(SITE_IDENTIFIER, 'searchMovie', match[1], 'search.png', oOutputParameterHandler)
             
            if row:

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                oGui.addDir(SITE_IDENTIFIER, 'delSearch', '[COLOR red]Supprimer l\'historique[/COLOR]', 'search.png', oOutputParameterHandler)
                

        oGui.setEndOfDirectory()

    def searchMovie2(self):
        oInputParameterHandler = cInputParameterHandler()
        sDisp = oInputParameterHandler.getValue('disp')
        oHandler = cRechercheHandler()
        liste = oHandler.getAvailablePlugins(sDisp)
        self.__callsearch(liste, sDisp)

    def delSearch(self):
        cDb().del_history()
        return True
        

    def __callpluging(self, sVar, sTitle, sIcon):
        oGui = cGui()
        oPluginHandler = cSiteHandler()
        aPlugins = oPluginHandler.getAvailablePlugins(sVar)
        for aPlugin in aPlugins:
            try:
                #exec "import "+aPlugin[1]
                #exec "sSiteUrl = "+aPlugin[1]+"."+sVar
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', aPlugin[0])
                oGui.addDir(aPlugin[2], aPlugin[3], sTitle+' - [COLOR azure]'+aPlugin[1]+'[/COLOR]', sIcon, oOutputParameterHandler)
            except:        
                pass

        oGui.setEndOfDirectory()

    def searchMovie(self):
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('searchtext')
        sReadDB = oInputParameterHandler.getValue('readdb')
        sDisp = oInputParameterHandler.getValue('disp')

        oHandler = cRechercheHandler()
        aPlugins = oHandler.getAvailablePlugins(sDisp)
        if not sSearchText:
            sSearchText = oGui.showKeyBoard()
            sSearchText = urllib.quote(sSearchText)
        if (sSearchText != False):
            if (sReadDB != 'False'):
                meta = {}      
                meta['title'] = sSearchText
                meta['disp'] = sDisp
                cDb().insert_history(meta)
            #print aPlugins
            for aPlugin in aPlugins:
                    try:                   
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                        oGui.addDir(SITE_IDENTIFIER, 'showSearch', '[COLOR olive]'+ aPlugin[1] +'[/COLOR]', 'search.png', oOutputParameterHandler)
                    
                        exec "from resources.sites import "+aPlugin[1]+" as search"
                        sUrl = aPlugin[0]+sSearchText
                        searchUrl = "search.%s('%s')" % (aPlugin[2], sUrl)
                        exec searchUrl
                    except:       
                        pass
        else: return
        oGui.setEndOfDirectory()

