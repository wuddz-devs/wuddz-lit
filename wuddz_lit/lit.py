"""\033[1;32;40m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░██╗░░░░░░░██╗██╗░░░██╗██████╗░██████╗░███████╗░░░░░░██╗░░░░░██╗████████╗░░░░░░░░░
░░░░░░░░░██║░░██╗░░██║██║░░░██║██╔══██╗██╔══██╗╚════██║░░░░░░██║░░░░░██║╚══██╔══╝░░░░░░░░░
░░░░░░░░░╚██╗████╗██╔╝██║░░░██║██║░░██║██║░░██║░░███╔═╝█████╗██║░░░░░██║░░░██║░░░░░░░░░░░░
░░░░░░░░░░████╔═████║░██║░░░██║██║░░██║██║░░██║██╔══╝░░╚════╝██║░░░░░██║░░░██║░░░░░░░░░░░░
░░░░░░░░░░╚██╔╝░╚██╔╝░╚██████╔╝██████╔╝██████╔╝███████╗░░░░░░███████╗██║░░░██║░░░░░░░░░░░░
░░░░░░░░░░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░╚═════╝░╚══════╝░░░░░░╚══════╝╚═╝░░░╚═╝░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
[*]Descr:     WUDDZ-LIT IS AN AWESOME & QUITE EFFICIENT LITEROTICA.COM STORIES DOWNLOADER 
              & SEARCH, DOWNLOAD AND LIST AUTHOR/CATEGORY/AUDIO/ILLUSTRATION STORIES FOR  
              OFFLINE VIEWING AS TEXT OR HTML WITH EASY NAVIGATION, SEARCH FOR USERNAMES  
              OR FIND A STORY WITH MATCHING TEXT/EXCERPT.                                 
[*]Email:     wuddz_devs@protonmail.com                                                   
[*]Github:    https://github.com/wuddz-devs                                               
[*]Donation:                                                                              
    BTC   ->  bc1qa7ssx0e4l6lytqawrnceu6hf5990x4r2uwuead                                  
    ERC20 ->  0xbF4d5309Bc633d95B6a8fe60E6AF490F11ed2Dd1                                  
    LTC   ->  LdbcFiQVUMTfc9eJdc5Gw2nZgyo6WjKCj7                                          
    TRON  ->  TY6e3dWGpqyn2wUgnA5q63c88PJzfDmQAD                                          
    DOGE  ->  DFwLwtcam7n2JreSpq1r2rtkA48Vos5Hgm                                          
\033[1;33;40m                                                                             
[*]LITEROTICA CATEGORIES:                                                                 
   (2) erotic-couplings            (15) adult-romance         (37) anal-sex-stories          
   (3) reviews-and-essays          (16) masturbation-stories  (38) science-fiction-fantasy   
   (4) exhibitionist-voyeur        (17) erotic-poetry         (39) audio-sex-stories         
   (5) fetish-stories              (26) mature-sex            (40) first-time-sex-stories    
   (6) gay-sex-stories             (27) celebrity-stories     (45) illustrated-erotic-fiction
   (7) group-sex-stories           (28) chain-stories         (46) erotic-audio-poetry       
   (8) adult-how-to                (29) mind-control          (47) illustrated-poetry        
   (9) taboo-sex-stories           (31) bdsm-stories          (48) transgender-crossdressers 
  (10) interracial-erotic-stories  (32) non-english-stories   (51) erotic-horror             
  (11) lesbian-sex-stories         (33) erotic-novels         (53) erotic-letters            
  (12) loving-wives                (34) adult-humor           (55) erotic-art                
  (13) non-consent-stories         (35) non-erotic-stories    (56) adult-comics              
  (14) non-human-stories           (36) non-erotic-poetry                                    
\033[0m"""

import argparse, requests, re, sys, textwrap
from time import sleep
from os import path, mkdir, name, system, getpid, kill
from concurrent.futures import ThreadPoolExecutor, as_completed
from signal import SIGTERM
system('')


class LitErotica:
    """
    Search, Download & Save Author/Category/Audio/Illustration(Art) Stories From Literotica.com.
    :param out: Optional String Output Directory Or Default Used.
    :param prx: Optional String Proxy:Port Address (e.g socks5://localhost:80).
    """
    def __init__(self, out:str=None, prx:str=''):
        """
        LitErotica Class With Optional Output Directory (If None Default Used) & Proxy If Specified.
        :param out: Optional String Output Directory Or Default Used.
        :param prx: Optional String Proxy:Port Address (e.g socks5://localhost:80).
        """
        hd = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.usl = []
        self.gl = 0
        self.gs = 0
        self.pid = getpid()
        self.req = requests.Session()
        self.req.headers.update(hd)
        self.dsl = re.findall(r'\((\d+)\) (\S+)',str(__doc__))                 #List Containing Category ID & Name Tuples From __doc__
        self.out = path.join(path.expanduser('~'), 'Desktop', 'Lit')           #Default Output Directory
        if out and path.isdir(path.dirname(path.abspath(out))):self.out = out  #Specified Output Directory
        if prx:self.req.proxies.update({'http': prx, 'https': prx})            #Update Requests Session With Proxy If Specified
        self.lout = path.join(self.out, 'List')                                #List Output Directory
        self.sout = path.join(self.out, 'Stories')                             #Stories Output Directory
        self.usf = path.join(self.lout, 'Authors_Found.txt')                   #Author Search Output File
        self.ssf = path.join(self.lout, 'Story_Found.txt')                     #Story Search Output File
        self.uurl = "https://literotica.com/api/3/users/%s"                    #Literotica Author/User Info API Endpoint Url
        self.aurl = "https://literotica.com/api/3/users/%s/stories"            #Literotica Author Stories API Endpoint Url
        self.iurl = "https://www.literotica.com/i/%s"                          #Literotica Illustration(Art) Story Url
        self.purl = "https://www.literotica.com/p/%s"                          #Literotica Poem Story Url
        self.hurl = "https://www.literotica.com/s/%s"                          #Literotica Story Url
        self.surl = "https://literotica.com/api/3/stories/%s"                  #Literotica Story API Endpoint Url
        self.ssrl = "https://literotica.com/api/3/search/members?params={%s}"  #Literotica Search Usernames API Endpoint Url
        self.csrl = 'https://literotica.com/api/3/search/stories?params={%s}'  #Literotica Category API Endpoint Url
        self.iprl = 'https://literotica.com/api/3/stories/new?params={%s}'     #Literotica Illustration & Poem Category API Endpoint Url
        [self.gdir(a) for a in [self.out, self.lout, self.sout]]              #Make Default List & Stories Directories If Not Created
        
        #UrlEncoded Search Usernames API Endpoint Url Parameters String
        self.sus = "%22q%22:%22{}%22,%22page%22:{},%22user_type%22:%22{}%22,%22languages%22:[1]"
        
        #UrlEncoded Illustrated/Poem Category API EndPoint Url Parameters String
        self.ipnt = "%22period%22:%22all%22,%22page%22:{},%22category%22:{},%22pageSize%22:50,%22type%22:%22{}%22,%22sort%22:%22date%20dsc%22,%22language%22:1"
        
        #UrlEncoded Illustrated/Poem Category API EndPoint Url With Tags Parameters String
        self.ipwt = "%22q%22:%22{}%22,%22period%22:%22all%22,%22page%22:{},%22category%22:{},%22pageSize%22:50,%22type%22:%22{}%22,%22sort%22:%22date%20dsc%22,%22where%22:%22tags%22,%22language%22:1"
        
        #UrlEncoded Story Category API EndPoint Url Parameters String
        self.cnt = "%22page%22:{},%22categories%22:[{}],%22period%22:%22all%22,%22sort%22:%22date%20dsc%22,%22languages%22:[1]"
        
        #UrlEncoded Story Category API EndPoint Url With Tags Parameters String
        self.cwt = "%22q%22:%22{}%22,%22page%22:{},%22categories%22:[{}],%22period%22:%22all%22,%22sort%22:%22date%20dsc%22,%22where%22:%22tags%22,%22languages%22:[1]"
        
        #Categories Which Won't Be Saved As Text Output
        self.nto = ['audio-sex-stories', 'illustrated-erotic-fiction', 'adult-comics', 
                    'erotic-art', 'illustrated-poetry', 'erotic-audio-poetry']
        
        #Html Tag To Replace With Downloaded Audio File In Audio Story Html Output
        self.atag = '<button aria-label="Play" class="rhap_button-clear rhap_main-controls-button rhap_play-pause-button" type="button">'
        
        #Re-compiled Regex To Retrieve Audio File Links In Audio Type Stories Html
        self.areg = re.compile(r'(/audio/.*?)"')
    
    def resp(self, u: str):
        """
        Returns Valid Requests Url Response Object Or None If Error Occurs.
        :param u: String Url To Request.
        """
        try:
            
            r = self.req.get(u)
            assert r.status_code == 200
            return r
        except:return None
    
    def dfile(self, u: str, fn: str):
        """
        Requests Url & Downloads Response As Specified Output File.
        :param u: String Url To Request
        :param fn: String Filepath To Save As File.
        """
        fr = self.resp(u)
        if fr and not path.exists(fn):
            with open(fn, 'wb') as wb:
                wb.write(fr.content)
    
    def illus(self, t: str, fn: str) -> str:
        """
        Parses & Downloads Image Urls In Story Html And Returns Edited Html With Local Files Linked.
        :param t: String Html Response.
        :param fn: String Directory Path To Save Downloaded Files To.
        """
        l = re.findall(r'<img src="(\S+)"', t)
        for i in l:
            a = i
            if '?' in i:i = i.split('?')[0]
            ir = (i.split('/')[-1])
            if 'literotica.com/' not in i:i = f'https://www.literotica.com{i}'
            self.dfile(i, path.join(fn, ir))
            t = t.replace(a, './'+ir)
        return t
    
    def gdir(self, d: str) -> str:
        """
        Creates (If Not Created) Directory & Returns Directory As String.
        :param d: String Directory To Create & Return.
        """
        try:
            if not path.exists(d):mkdir(d)
            return d
        except:return ''
    
    def read(self, fn: str) -> list:
        """
        Returns Specified File Contents As List.
        :param fn: String Filename To Open & Return As List.
        """
        return open(fn, 'r', encoding='ISO-8859-1').read().splitlines()
    
    def flist(self, o: str) -> list:
        """
        Returns Argument Or File Contents As List.
        :param o: Argument Or File Containing Data To Return As List.
        """
        a = [o]
        if path.isfile(o):
            a = [re.search(r'(\S+)', str(x)).group(1) for x in self.read(o)]
        return a
    
    def author(self, a: str) -> list:
        """
        Returns A List Containing A List Of Specified Author's Stories & Author Name.
        :param a: String Author Name.
        """
        id = ''
        sl = []
        if a.isdigit():id = a
        else:
            resp = self.resp(self.uurl %(a))
            if resp:
                #Get Author's UserId From Literotica API
                id = resp.json()['user']['userid']
        if id:
            url = self.aurl %(id)
            rb = self.resp(url)
            if rb:
                ai = rb.json()                   #Initial Page API Json Response Containing Author's Stories
                ic = int(ai['last_page'])        #Amount Of Pages (50 Stories Per Page) Containing All Author's Stories
                a = ai['data'][0]['authorname']
                with open(path.join(self.lout, f'{a}.txt'), 'w', encoding='utf-8') as fw:
                    #Iterate Total Pages Of Author Stories
                    for i in range(1, ic + 1):
                        if i > 1:
                            #Subsequent Paginated Author API Responses
                            ai = self.resp(url+"?params={%22page%22:%20"+str(i)+"}").json()
                        #Iterate API Json Response Containing Story Data Per Page
                        for n in range(len(ai['data'])):
                            self.gl += 1
                            t = ai['data'][n]['url']                       #Story Title
                            c = ai['data'][n]['category_info']['pageUrl']  #Story Category
                            sl.append(t)
                            #Write Story Titles & Matching Categories To Output File
                            fw.write(t+' '+'_'*(71-len(t))+c+'\n')
        return [sl,a]
    
    def category(self, c: str, t: str='', p: int=1, ps: int=1, tx: bool=False) -> list:
        """
        Returns A List Containing A List Of Specified Category Stories & Category Name.
        :param c: String Integer/Name Specifying Category (e.g 17 | erotic-poetry)..
        :param t: Optional String Specifying Tag.
        :param p: Optional Integer Amount Of Pages To Parse Category For Stories (Default=1).
        :param ps: Optional Integer Start Page To Parse Category Stories From (Default=1).
        :param tx: Optional Bool Specifying Text Output (Default=False).
        """
        sl = []
        sd = []
        jd = 'data'
        cd = {'17': 'poem', '36': 'poem', '46': 'poem', '47': 'poem', '55': 'illustra', '56': 'illustra'}
        if c.isdigit():vl = [i for i in self.dsl if i[0]==str(c)]
        else:vl = [i for i in self.dsl if i[1]==str(c)]
        if vl:
            c,cat = vl[0]
            #Iterate 1 Page Or Specified Amount Of Pages For Stories
            for i in range(ps, p + ps):
                if cd.get(c):
                    #Illustrated/Poem Stories Api Endpoint Urls With Tag If Specified
                    crl = self.iprl %(self.ipnt.format(i,c,cd[c]))
                    if t:crl = self.iprl %(self.ipwt.format(t,i,c,cd[c]))
                else:
                    #Typical Stories Api Endpoint Urls With Tag If Specified
                    crl = self.csrl %(self.cnt.format(i,c))
                    if t:crl = self.csrl %(self.cwt.format(t,i,c))
                js = self.resp(crl).json()
                if js.get('submissions'):jd = 'submissions'
                #Iterate Json Response For Stories & Matching Authors
                for n in range(len(js[jd])):
                    if t and len(js[jd][n]['tags']) == 0:break
                    sd.append((f"{js[jd][n]['authorname']}",f"{js[jd][n]['url']}"))
            if sd:
                nf = path.join(self.lout, f'{cat}.txt')
                if t:nf = path.join(self.lout, f'{cat}__{t}.txt')
                with open(nf, 'w', encoding='utf-8') as fw:
                    for a in sd:
                        self.gl += 1
                        sl.append(a[1])
                        fw.write(a[1]+' '+'_'*(72-len(a[1]))+a[0]+'\n')    #Write Story Titles & Matching Authors To Output File
                if tx and cat in self.nto:return
            return [sl,cat]
    
    def story(self, st: str, dr: str, tx: bool=False, cs: str=''):
        """
        Download Story Pages/Audio/Images & Save Output To Text Or Html.
        :param st: String Story Title To Download.
        :param dr: String Foldername To Save Downloaded Story & Media In Output Stories Directory.
        :param tx: Optional Bool Specifying Text Output (Default=False).
        :param cs: Optional String To Search Story Text For A Match (Default='').
        """
        ht = ''
        ft = ''
        surl = self.surl %(st)
        resp = self.resp(surl)
        if resp:
            js = resp.json()                                         #Story API Json Response
            pgs = int(js['meta']['pages_count'])                     #Story Pages
            dsc = js['submission']['description']                    #Story Description
            uid = js['submission']['author']['userid']               #Story Author UserId
            aut = js['submission']['authorname']                     #Story Author Name
            cat = js['submission']['category_info']['pageUrl']       #Story Category
            tit = js['submission']['title']                          #Story Title
            typ = js['submission']['type']                           #Story Type
            if cat in self.nto and tx:return                         
            if not cs:                                               
                self.gs += 1                                         
                #If Specified Directory Does Not Exist It Is Created In Stories Output Directory
                if not path.isdir(dr):
                    dr = self.gdir(path.join(self.sout, dr))                    
                dr = self.gdir(path.join(dr, st))                    
            for i in range(1, pgs+1):                                #Iterate Story Pages
                fn = path.join(dr, f'{st}__Page{i}.html')
                txt = ''
                if i > 1:
                    uri = surl+"?params={%22contentPage%22:%20"+str(i)+"}"
                    js = self.resp(uri).json()
                if tx or cs and js.get('pageText'):
                    fn = f'{fn[:-4]}txt'
                    tt = ' '.join(x.strip() for x in js['pageText'].split())
                    rem = re.compile('<.*?>')
                    tt = re.sub(rem, '', tt)
                    if cs:
                        rt="Title: %s\nAuthor: %s\nUser_Id: %s\nCategory: %s\nTotal_Pages: %s\nOn_Page: %s\nDescription: %s\nSearch_String: %s\n" %(st,aut,uid,cat,pgs,i,dsc,cs)
                        #Search Story For Matching String & Save Provided Info To Text File When Found
                        if self.find_story(cs, tt, rt):
                            #If Story Search Is Successful Kill The Program
                            kill(self.pid, SIGTERM)
                    else:
                        tt = self.text(tt)
                        txt = "Title: %s\nAuthor: %s\nUser_Id: %s\nCategory: %s\nDescription: %s\n\n%s" %(tit,aut,uid,cat,dsc,tt)
                else:
                    if typ == 'illustra':
                        #Story Title With Added Page Increment
                        pi = f'{st}?page={i}'
                        txt = self.art(pi, dr, js)
                    else:
                        url = self.hurl %(st)
                        if 'poetry' in cat:url = self.purl %(st)
                        if i > 1:url = f'{url}?page={i}'
                        txt = self.resp(url).text
                        if typ == 'audio' or cat in ['audio-sex-stories', 'erotic-audio-poetry']:
                            txt = self.audio(st, txt, fn.split('__')[0])
                        elif cat in ['illustrated-erotic-fiction', 'illustrated-poetry']:
                            txt = self.illus(txt, dr)
                    if txt and pgs > 1:
                        if not ht:
                            ht = re.search(r'href="(/\w/'+st+'\?page=)\d+"', txt).group(1)
                            ft = ht.split('?')[0]
                        # Link Locally Saved Html Pages For Easy Navigation
                        for n in range(2, pgs+1):
                            txt = txt.replace(f'{ht}{n}', f'./{st}__Page{n}.html')
                        txt = txt.replace(ft, f'./{st}__Page1.html')
                if txt:
                    with open(fn, 'w', encoding='utf-8') as fw:
                        fw.write(txt)
    
    def audio(self, st: str, txt: str, fn: str) -> str:
        """
        Downloads Audio Story With Media File(s) & Returns Locally Linked Html File.
        :param st: String Audio Story Title.
        :param txt: String Audio Story Html Requests Response.
        :param fn: String Filename To Save Media File(s).
        """
        c = 0
        ar = [x for x in re.findall(self.areg, txt) if '\\' not in x]  #Parse Audio Story Html For Audio Links
        for a in sorted(set(ar)):
            try:
                c += 1
                l = f'https://www.literotica.com{a}'
                if 'literotica-audio-' in a:l = f'https://uploads.literotica.com{a}'
                fe = path.basename(l).split('.')[1]
                afn = f'{fn}_{c}.{fe}'
                self.dfile(l,afn)
                if self.atag in txt:
                    txt = txt.replace(self.atag, '<audio controls><source src="%s" /></audio>' %(f'./{st}_{c}.{fe}'))
                else:
                    hf = f'./{st}_{c}.{fe}'
                    txt = txt.replace(l.replace('https','http'),hf)
                    txt = txt.replace(l,hf)
                    txt = txt.replace(a,hf)
            except:pass
        return txt
    
    def art(self, st: str, fn: str, js: dict) -> str:
        """
        Downloads Art Story With Media File(s) & Returns Locally Linked Html Output.
        :param st: String Illustration Art Story Title.
        :param fn: String Filename To Save Media File(s).
        :param js: Dictionary Literotica Api Illustration Story Response Data.
        """
        tt = self.resp(self.iurl %(st)).text
        pi = js['pageIllustrations']['illustrations']
        for i in range(len(pi)):
            irl = pi[i]['orig']                              #Art Story Full Image Url
            rrl = pi[i]['prev']                              #Art Story Preview Image Url
            ext = pi[i]['file'].split('.')[1]                #Art Story Image Extension
            tit = pi[i]['title']                             #Art Story Image Title
            ifn = path.join(fn, f'{tit}.{ext}')
            self.dfile(irl, ifn)
            #Replace Image Url(s) With Downloaded Image Path(s) In Story Html.
            tt = tt.replace('<img src="%s"' %(rrl), '</div><img src="%s"' %(f'./{tit}.{ext}'))
        
        #Return Edited Art Story Html Containing Image File(s) Linked Locally For Offline Viewing.
        return tt
    
    def find_story(self, cs: str, tt: str, rt: str):
        """
        Regex Search Story For String, Output Info To 'Story_Found.txt' In List Directory & Return Bool.
        :param cs: String To Re-Compile And Search Story For.
        :param tt: Story Text To Be Searched.
        :param rt: String To Output To Text File (Anything You Choose As Identifying).
        """
        try:
            s=re.compile(cs)
            re.search(s, tt).group()
            with open(self.ssf, 'w', encoding='utf-8') as fw:
                fw.write(rt)
            return True
        except:return False
    
    def find_user(self, usr: str, st: str='authors'):
        """
        Searches For Usernames Matching String & Outputs Names To 'Authors_Found.txt' In List Directory.
        :param usr: String User To Search For Matching Usernames.
        :param st: String User Type Of Usernames To Search e.g ('nonauthors | Default = authors').
        """
        i = 0
        t = 1
        while i < t:                                               #Iterate Json Response Pages For Usernames Found
            try:
                i += 1
                sl = self.ssrl %(self.sus.format(usr,i,st))
                js = self.resp(sl).json()
                tt = int(js['meta']['total'])                      #Total Usernames Found
                if tt % 50 != 0:t = (tt // 50) + 1                 #Calculate Amount Of Pages To Parse For Username Json Responses
                self.usl.extend(re.findall(r"'username': '(.*?)'",str(js)))
            except:break
    
    def text(self, fa: str, wv: int=128):
        """
        Returns TextWrap Formatted Story Text With Default Width (128 chars) Or Specified Width.
        :param fa: String Story Text To Be Formatted.
        :param wv: Integer Value Of Width To Format Text Default=128.
        """
        #Awesome Textwrap TextWrapper Class To Output Text 128 Characters Per Line
        wc = textwrap.TextWrapper(width=wv)
        return wc.fill(text=fa)
    
    def main(self, args):
        """
        Main Function To Execute Specified Arguments & Create Default Directories.
        :param args: Namespace Containing Argparse Arguments.
        """
        st = ""
        fl = []
        dl = []
        ml = []
        dr = self.sout
        print('\033[1;32;40m...Executing Selected Arguments Hold On...\n\033[0m')
        dl = self.flist(args.object)  #Store Argument Object As List (File Contents If File)
        if args.asearch:st = "authors"
        elif args.nsearch:st = "nonauthors"
        if dl:
            with ThreadPoolExecutor(args.threads) as ex:
                if st:
                    for usr in dl:
                        #Search For Usernames With Matching String Using Literotica Api
                        ex.submit(self.find_user, usr, st)
                    if self.usl:
                        #Write Usernames Found To 'Authors_Found.txt' In List Directory
                        with open(self.usf, 'a', encoding='utf-8') as fw:
                            [fw.write(f'{s}\n') for s in self.usl]
                else:
                    if args.author and dl:
                        #Retrieve & List Author Stories Using Threads
                        fl = [ex.submit(self.author,a) for a in dl]
                    elif args.category or args.tag:
                        #Retrieve & List Category Stories Using Threads
                        fl = [ex.submit(self.category,a,t=args.tag,p=args.pages,ps=args.pstart,tx=args.text) for a in dl]
                    elif args.story:ml = [[dl, 'Misc']]
                    if fl:
                        #Return List Of Completed Futures (Stories List).
                        ml = [i.result() for i in as_completed(fl) if type(i.result()) is list]
                    if args.download or args.csearch and ml:
                        #Iterate & Download Stories With Concurrent.Futures ThreadPoolExecutor Threads
                        for m in ml:
                            if not args.csearch:
                                #Only Create Story Output Directory If Necessary
                                dr = self.gdir(path.join(self.sout, m[1]))
                            for i in m[0]:
                                ex.submit(self.story, i, dr, tx=args.text, cs=args.csearch)
        clear_screen()
        print('\033[1;32;40m[*]OUTPUT:\033[0m')
        if self.gs > 0:print(f'\033[1;34;40m\n{self.gs} Stories Downloaded To Respective Folders In {self.sout}\033[0m')
        elif self.gl > 0:print(f'\033[1;34;40m\n{self.gl} Stories Listed In Text File(s) In {self.lout}\033[0m')
        elif len(self.usl) > 0:print(f'\033[1;34;40m\n{len(self.usl)} Usernames Found & Listed In {self.usf}\033[0m')
        else:print('\033[1;31;40m\nNo Stories/Usernames Found/Listed/Downloaded Enter Valid Arguments Or Check Internet Connection!!\033[0m')
    
def clear_screen():
    """Clear Command Line Screen."""
    if name=='nt':system('cls')
    else:system('clear')

def slow_print(doc: str, sp: float=0.0005):
    """
    Print String By Speed In Seconds Less Is Faster.
    :param doc: String To Be Printed
    :param sp:  Speed To Print String `e.g 0.0001 | Default = 0.0005`
    """
    for d in doc:
        sys.stdout.write(d)
        sleep(sp)

def cli_main():
    """
    Wuddz-Lit Entry Point Executing Specified Argparse NameSpace Arguments.
    """
    clear_screen()
    usage = ('[*]EXAMPLES:\n'
             '  wudz-lit -f "C:\\file.txt" -s -d -x 100       Download Stories In "C:\\file.txt" File As Html Using 100 Threads.\n'
             '  wudz-lit -f 2 -c -d -i                       Parse 1 Page Of Erotic-Couplings Category Stories & Download As Text.\n'
             '  wudz-lit -f 2 -c -p "socks5://localhost:80"  Parse 1 Page Of Stories & List To Text Using Specified Proxy.\n'
             '  wudz-lit -f author -a -x 120              Save All Specified Author(Uid/Name) Stories To Text File Using 120 Threads.\n'
             '  wudz-lit -f 26 -t milf -d -n 2 -ns 5      Parse 2 Pages Mature-Sex Stories "milf" Tag Start Page 5 & Download As Html.\n'
             '  wudz-lit -f mature-sex -c -t milf -d      Parse 1 Page Mature-Sex Category Stories With "milf" Tag & Download As Html.\n'
             '  wudz-lit -f Jay -as                       Search For Authors Matching "Jay" Who Have Story Submissions & Output To File.\n'
             '  wudz-lit -f Jen -an                       Search For Authors Matching "Jen" With No Stories & Output To File.\n'
             '  wudz-lit -f 6 -c -cs "Wowwwwwwwww"        Search Category For 1st Story Containing "Wowwwwwwwww" & Output To File.\n'
             '  wudz-lit -f story -s -d -o "C:\\Lit"       Download Specified Story As Html To "C:\\Lit" Output Folder.\n\n')
    slow_print(f'{__doc__}\n\033[1;34;40m{usage}\033[0m')
    parser = argparse.ArgumentParser(description="Wuddz-Lit An Efficient Literotica.com Author/Category/Audio/Illustration Stories Downloader & Search.")
    parser.add_argument('-f', '--object', required=True, type=str, default=None, help="Author/Story/Category Or File (e.g 2 | author(Uid/Name) | story | file.txt).")
    parser.add_argument('-a', '--author', action="store_true", help="Specify Author As Object Argument.")
    parser.add_argument('-s', '--story', action="store_true", help="Specify Story As Object Argument.")
    parser.add_argument('-c', '--category', action="store_true", help="Specify Category As Object Argument.")
    parser.add_argument('-d', '--download', action="store_true", help="Download Stories.")
    parser.add_argument('-i', '--text', action="store_true", help="Save Stories As Text Output (Html Is Default If Not Specified).")
    parser.add_argument('-as', '--asearch', action="store_true", help="Search For Users With Submitted Stories Matching String.")
    parser.add_argument('-an', '--nsearch', action="store_true", help="Search For Users With No Stories Matching String.")
    parser.add_argument('-cs', '--csearch', type=str, default='', help="Search Category For Story Containing String Specified.")
    parser.add_argument('-p', '--proxy', type=str, default='', help="Proxy Url (e.g socks5h://localhost:1080 | http://localhost:8080).")
    parser.add_argument('-t', '--tag', type=str, default='', help="Search For Tag (e.g wife | milf).")
    parser.add_argument('-o', '--output', type=str, default='', help="Output Directory (e.g C:\\Lit | Default = 'Lit' Folder In Current User's Desktop Directory).")
    parser.add_argument('-n', '--pages', type=int, default=1, help="Amount Of Category/Tag Pages To Parse For Stories (e.g 3 | Default = 1).")
    parser.add_argument('-ns', '--pstart', type=int, default=1, help="Page Number To Start Parsing Stories From. (e.g 10 | Default = 1).")
    parser.add_argument("-x", "--threads", type=int, default=64, help="Amount Of Threads (e.g 10 | 30 | Default = 64).")
    args=parser.parse_args()
    if len(sys.argv)>2:
        try:
            clear_screen()
            le=LitErotica(out=args.output,prx=args.proxy)
            le.main(args)
        except:sys.exit()
