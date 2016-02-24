#-*- coding: utf-8 -*-
from resources.lib.gui.gui import cGui
from time import time
from base64 import urlsafe_b64encode
import urllib2,xbmc,urllib,re
from urllib2 import URLError

def get_response(img):
    import xbmcgui,xbmc
    try:
        img = xbmcgui.ControlImage(450, 0, 400, 130, img)
        wdlg = xbmcgui.WindowDialog()
        wdlg.addControl(img)
        wdlg.show()
        #xbmc.sleep(3000)
        kb = xbmc.Keyboard('', 'Type the letters in the image', False)
        kb.doModal()
        if (kb.isConfirmed()):
            solution = kb.getText()
            if solution == '':
                raise Exception('You must enter text in the image to access video')
            else:
                return solution
        else:
            raise Exception('Captcha Error')
    finally:
        wdlg.close()


def DecryptDlProtect(url):

    if not (url): return ''
    
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Referer' : url ,
    'Host' : 'www.dl-protect.com',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-gb, en;q=0.9',
    'Pragma' : '',
    'Accept-Charset' : '',
    }
    
    request = urllib2.Request(url,None,headers)
    try: 
        reponse = urllib2.urlopen(request)
    except URLError, e:
        print e.read()
        print e.reason
        return ''
    
    #Si redirection
    UrlRedirect = reponse.geturl()
    if not(UrlRedirect == url):
        reponse.close()
        return UrlRedirect
        
    sHtmlContent = reponse.read()
    
    #Recuperatioen et traitement cookies ???
    cookies=reponse.info()['Set-Cookie']
    c2 = re.findall('__cfduid=(.+?); .+? cu=(.+?);.+?PHPSESSID=(.+?);',cookies)
    cookies = '__cfduid=' + str(c2[0][0]) + ';cu=' + str(c2[0][1]) + ';PHPSESSID=' + str(c2[0][2])
    
    reponse.close()
    
    #test si captcha demande
    if '<td align=center> Please enter the characters from the picture to see the links </td>' in sHtmlContent:
        print 'captcha'
        print url
        s = re.findall('<img id="captcha" alt="Security code" src="([^<>"]+?)"',sHtmlContent)
        image = 'http://www.dl-protect.com' + s[0]
        
        captcha = get_response(image)
        
        key = re.findall('name="key" value="(.+?)"',sHtmlContent)
        
        #Ce parametre ne sert pas encore
        mstime = int(round(time() * 1000))
        b64time = "_" + urlsafe_b64encode(str(mstime)).replace("=", "%3D")
        
        query_args = ( ('key' , key[0] ) , ( 'i' , b64time) , ('secure' , captcha ), ( 'submitform' , 'Valider')  )
        print query_args
        
        data = urllib.urlencode(query_args)
    
        #rajout des cookies
        headers.update({'Cookie': cookies})

        request = urllib2.Request(url,data,headers)

        try: 
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
            
        sHtmlContent = reponse.read()
        reponse.close()
        
        #fh = open('c:\\test.txt', "w")
        #fh.write(sHtmlContent)
        #fh.close()
        
        return sHtmlContent
    

    if 'Please click on continue to see' in sHtmlContent:
        
        key = re.findall('input name="key" value="(.+?)"',sHtmlContent)
    
        #Ce parametre ne sert pas encore pour le moment
        mstime = int(round(time() * 1000))
        b64time = "_" + urlsafe_b64encode(str(mstime)).replace("=", "%3D")
        
        #fh = open('c:\\test.txt', "w")
        #fh.write(sHtmlContent)
        #fh.close()
              
        #tempo necessaire
        cGui().showInfo("Patientez", 'Decodage en cours' , 2)
        xbmc.sleep(1000)
        
        query_args = ( ('submitform' , '' ) , ( 'key' , key[0] ) , ('i' , b64time ), ( 'submitform' , 'Continuer')  )
        data = urllib.urlencode(query_args)
        
        #rajout des cookies
        headers.update({'Cookie': cookies})

        request = urllib2.Request(url,data,headers)

        try: 
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
            
        sHtmlContent = reponse.read()
        
        reponse.close()
    
        return sHtmlContent
        
    return ''
        
 
