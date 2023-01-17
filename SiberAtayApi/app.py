from flask import Flask, jsonify
from bs4 import BeautifulSoup as btu
import requests as req



urlThread = "https://threatpost.com/"
urlHelp = "https://www.helpnetsecurity.com/view/news/"
urlThe = "https://thehackernews.com/?m=1"
urlVetur = "https://venturebeat.com/feed/"
urlCom = "https://www.computerworld.com/index.rss"
urlNal = "https://tech.co/feed"
urlNeo = "https://www.neowin.net/news/rss/"
urlRadar = "https://www.techradar.com/rss"
urlNex = "https://thenextweb.com/feed"

headers = {
    "User-Agnet": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"
}

def appThread():
    WebDATA = []
    istekNewsThread = req.get(urlThread)
    htmlNewsThread = istekNewsThread.text
    soupNewsThread = btu(htmlNewsThread, "html.parser")
    divNewsThread = soupNewsThread.find_all("figure")
    for iNewsThread in divNewsThread:
        linkThread = iNewsThread.find("a").get('href')
        resimNewsThread = iNewsThread.find("a").find("img").get("src")
        requests__Thread = req.get(linkThread)
        htmlNewsThread = requests__Thread.text
        soupNewsThread = btu(htmlNewsThread, 'html.parser')
        TitleNewsThread = soupNewsThread.find("h1", {"class": "c-article__title"}).text
        try:
            DataTimeNewsThread = soupNewsThread.find("time").text
        except:
            pass
        contentThread = soupNewsThread.find_all("div", {"class": "c-article__content"})
        ContentEndThread = ' '.join(e.text for p in contentThread for e in p.findAll(text=True))
        WebDATA.append({
                "title": TitleNewsThread,
                "link": linkThread,
                "resim": resimNewsThread,
                "date": DataTimeNewsThread,
                "text": ContentEndThread,
        })


    istekNewsThe = req.get(urlThe)
    htmlNewsThe = istekNewsThe.text
    soupNewsThe = btu(htmlNewsThe, "lxml")
    divNewsThe = soupNewsThe.find_all("div", {"class": "body-post clear"})
    for iNewsThe in divNewsThe:
        linkNewsThe = iNewsThe.find("a", {"class": "story-link"}).get("href")
        istek2NewsThe = req.get(linkNewsThe)
        html2NewsThe = istek2NewsThe.text
        soup2NewsThe = btu(html2NewsThe, "lxml")
        try:
            titleNewsThe = soup2NewsThe.find("h1", {"class": "story-title"}).text  # Title
            DateNewsThe = soup2NewsThe.find("span", {"class": "author"}).text  # Date
            resimNewsThe = soup2NewsThe.find("div", {"class": "articlebody clear cf"}).find("div",{"class": "separator"}).find("a").get("href")
            contentNewsThe = soup2NewsThe.find_all("p")
        except:
            pass
        ContentEndNewsThe = ' '.join(NewsPageText.text for The in contentNewsThe for NewsPageText in The.findAll(text=True))
        WebDATA.append({"title": titleNewsThe,
                        "link": linkNewsThe,
                        "resim": resimNewsThe,
                        "date": DateNewsThe,
                        "icerik": ContentEndNewsThe})


    istekNewsVetur = req.get(urlVetur)
    htmlNewsVetur = istekNewsVetur.text
    soupNewsVetur = btu(htmlNewsVetur, features="xml")
    linkNewsVetur = soupNewsVetur.find_all("link")[3:]
    for iNewsVetur in linkNewsVetur:
        __linkNewsVetur = iNewsVetur.text
        __istekNewsVetur = req.get(__linkNewsVetur)
        __htmlNewsVetur = __istekNewsVetur.text
        __soupNewsVetur = btu(__htmlNewsVetur, "lxml")
        titleNewsVetur = __soupNewsVetur.find("div", {"class": "Article__header-top"}).find("h1").text
        timeNewsVetur = __soupNewsVetur.find("time").text
        imgNewsVetur = __soupNewsVetur.find("img").get("src")
        contentNewsVetur = __soupNewsVetur.find("div", {"class": "article-content"}).text
        WebDATA.append({
                "title": titleNewsVetur,
                "link": __linkNewsVetur,
                "resim": imgNewsVetur,
                "date": timeNewsVetur,
                "content":contentNewsVetur
        })


    istekNewsCom = req.get(urlCom, headers=headers)
    htmlNewsCom = istekNewsCom.text
    soupNewsCom = btu(htmlNewsCom, features="xml")
    linkNewsCom = soupNewsCom.find_all("link")[2:]
    for iNewsCom in linkNewsCom:
        try:
            _NewsRequests = iNewsCom.text
            _istekNewsCom = req.get(_NewsRequests)
            _htmlNewsCom = _istekNewsCom.text
            _soupNewsCom = btu(_htmlNewsCom, "lxml")
            titleNewsCom = _soupNewsCom.find("h1", {"itemprop": "headline"}).text
            imgNewsCom = _soupNewsCom.find("figure", {"itemprop": "image"}).find("img").get("src")
            dateNewsCom = _soupNewsCom.find('span', {"class": "pub-date"}).get("content")
            contentNewsCom = _soupNewsCom.find_all("div", {"itemprop": "articleBody"})
        except:
            pass
        EndContentCom = ''.join(com.text for iCom in contentNewsCom for com in iCom.findAll(text=True))
        WebDATA.append({
            "title": titleNewsCom,
            "link": _NewsRequests,
            "date": dateNewsCom,
            "img": imgNewsCom,
            "content":EndContentCom
        })


    istekNewsNal = req.get(urlNal)
    htmlNewsNal = istekNewsNal.text
    soupNewsNal = btu(htmlNewsNal, features="xml")
    linkNewsNal = soupNewsNal.find_all("link")[2:]
    for iNewsNal in linkNewsNal:
        nalNewslink = iNewsNal.text
        nalNewsistek = req.get(nalNewslink)
        htmlNews_nal = nalNewsistek.text
        soupNews_nal = btu(htmlNews_nal, "lxml")
        titleNewsNal = soupNews_nal.find("h1", {"class": "entry-header-title"}).text
        timeNewsNal = soupNews_nal.find("time", {"class": "date"}).text
        imgNewsNal = soupNews_nal.find("div", {"class": "post-thumbnail entry-thumbnail"}).find("img", {
            "class": "no-lazy-loading"}).get("srcset")
        resimNewsNal = imgNewsNal.split(",")[0]
        contentNewsNal = soupNews_nal.find("div", {"class": "entry-content"})
        EndContentNewsNal = ''.join(iNal.text for iNal in contentNewsNal)
        WebDATA.append({
            "title": titleNewsNal,
            "date": timeNewsNal,
            "link": nalNewslink,
            "img": resimNewsNal,
            "content": EndContentNewsNal
        })


    istekNewsNeo = req.get(urlNeo, headers=headers)
    htmlNewsNeo = istekNewsNeo.text
    soupNewsNeo = btu(htmlNewsNeo, features="xml")
    linkNewsNeo = soupNewsNeo.find_all("link")[5:]
    resimNewsNeo = soupNewsNeo.find_all("description")[5:]
    imgNeo = []
    sayac = 0
    for resimNewsNeo in resimNewsNeo:
        textimgNeo = resimNewsNeo.text
        imgSoupNeo = btu(textimgNeo, "lxml")
        imgNewsNeo = imgSoupNeo.find("img").get("src")
        imgNeo.append(imgNewsNeo)
    for iNewsNeo in linkNewsNeo:
        NewslinkNeo = iNewsNeo.text
        istekNews_Neo = req.get(NewslinkNeo)
        htmlNews_Neo = istekNews_Neo.text
        soupNews_Neo = btu(htmlNews_Neo, "lxml")
        titleNewsNeo = soupNews_Neo.find("h1", {"class": "article-title"}).text.strip()
        timeNewsNeo = soupNews_Neo.find("time", {"class": "published"}).get("datetime")
        imgNews_Neo = imgNeo[sayac]
        contentNewsNeo = soupNews_Neo.find_all("div", {"class": "article-content"})
        contentEndNewsNeo = ''.join(neo.text for iNeo in contentNewsNeo for neo in iNeo.findAll(text=True))
        WebDATA.append({"title":titleNewsNeo,
                        "link":NewslinkNeo,
                        "date":timeNewsNeo,
                        "img":imgNews_Neo,
                        "content":contentEndNewsNeo})


    istekNewsHelp = req.get(urlHelp, headers=headers)
    htmlNewsHelp = istekNewsHelp.text
    soupNewsHelp = btu(htmlNewsHelp, "html.parser")
    divNewsHelp = soupNewsHelp.find_all("article", {"class": "entry-preview entry-variant-A"})
    for iNewsHelp in divNewsHelp:
        linkNewsHelp = iNewsHelp.find("a").get("href")  # Link
        resimNewsHelp = iNewsHelp.find("div", {'class': "entry-preview__media"}).find("a").find("img").get("src")
        istek_2NewsHelp = req.get(linkNewsHelp)
        html_2NewsHelp = istek_2NewsHelp.text
        soup_2NewsHelp = btu(html_2NewsHelp, "html.parser")
        timeNewsHelp = soup_2NewsHelp.find("time").text  # DataTime
        contentNewsHelp = soup_2NewsHelp.find_all("div", {"class": "entry-content"})  # Content
        TitleNewsHelp = soup_2NewsHelp.find("h1", class_="entry-title").text  # Title
        ContentEndHelp = ' '.join(w_3.text for w_2 in contentNewsHelp for w_3 in w_2.findAll(text=True))
        WebDATA.append({
            "title": TitleNewsHelp,
            "link": linkNewsHelp,
            "resim": resimNewsHelp,
            "date": timeNewsHelp,
            "icerik": ContentEndHelp
        })


    istekNewsRadar = req.get(urlRadar, headers=headers)
    htmlNewsRadar = istekNewsRadar.text
    soupNewsRadar = btu(htmlNewsRadar, features="xml")
    linkNewsRadar = soupNewsRadar.find_all("link")[2:]
    for iNewsRadar in linkNewsRadar:
        linkNews_Radar = iNewsRadar.text
        istekNews_Radar = req.get(linkNews_Radar)
        htmlNews_Radar = istekNews_Radar.text
        soupNews_Radar = btu(htmlNews_Radar, "lxml")
        titleRadar = soupNews_Radar.find("h1").text
        resimRadar = soupNews_Radar.find("a", {"data-component-tracking-label": "Pinterest"}).get("href").split("&")[1].replace("media=", "")
        pubdateRadar = soupNews_Radar.find("time", {"class": "relative-date"}).text
        contentRadar = soupNews_Radar.find_all("div", {"class": "text-copy bodyCopy auto"})
        EndContentRadar = ''.join(iRadar.text for i_radar in contentRadar for iRadar in i_radar.findAll(text=True))
        WebDATA.append({"title":titleRadar,
                        "resim":resimRadar,
                        "date":pubdateRadar,
                        "content":EndContentRadar})


    return WebDATA




app = Flask(__name__)
@app.route("/")
def index():
    return jsonify(appThread())

if __name__=="__main__":
    app.run(debug=True)