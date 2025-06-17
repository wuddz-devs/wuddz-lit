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
   (1) anal-sex-stories        (14) adult-humor                 (27) erotic-novels            
   (2) audio-sex-stories       (15) illustrated-erotic-fiction  (28) reviews-and-essays       
   (3) bdsm-stories            (16) taboo-sex-stories           (29) adult-romance            
   (4) celebrity-stories       (17) interracial-erotic-stories  (30) science-fiction-fantasy  
   (5) chain-stories           (18) lesbian-sex-stories         (31) masturbation-stories     
   (6) erotic-couplings        (19) erotic-letters              (32) transgender-crossdressers
   (7) erotic-horror           (20) loving-wives                (33) adult-comics
   (8) exhibitionist-voyeur    (21) mature-sex                  (34) erotic-art
   (9) fetish-stories          (22) mind-control                (35) erotic-poetry
  (10) first-time-sex-stories  (23) non-english-stories         (36) illustrated-poetry
  (11) gay-sex-stories         (24) non-erotic-stories          (37) non-erotic-poetry
  (12) group-sex-stories       (25) non-consent-stories         (38) erotic-audio-poetry
  (13) adult-how-to            (26) non-human-stories
\033[0m"""

import argparse, requests, re, sys, textwrap, fastparquet as fp
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
        self.dbu = "https://github.com/wuddz-devs/wuddz-lit/raw/refs/heads/main/user_db.parquet"  #User Database Url To Download
        self.gl = 0
        self.gs = 0
        self.pid = getpid()
        self.req = requests.Session()
        self.req.headers.update(hd)
        self.out = path.join(path.expanduser('~'), 'Desktop', 'Lit')           #Default Output Directory
        if out and path.isdir(path.dirname(path.abspath(out))):self.out = out  #Specified Output Directory
        if prx:self.req.proxies.update({'http': prx, 'https': prx})            #Update Requests Session With Proxy If Specified
        self.lout = path.join(self.out, 'List')                                #List Output Directory
        self.sout = path.join(self.out, 'Stories')                             #Stories Output Directory
        self.udb = path.join(self.lout, 'user_db.parquet')                     #User Database File
        self.usf = path.join(self.lout, 'Authors_Found.txt')                   #Author Search Output File
        self.ssf = path.join(self.lout, 'Story_Found.txt')                     #Story Search Output File
        self.uurl = "https://literotica.com/api/3/users/%s"                    #Literotica Author/User Info API Endpoint Url
        self.aurl = "https://literotica.com/api/3/users/%s/stories"            #Literotica Author Stories API Endpoint Url
        self.iurl = "https://www.literotica.com/i/%s"                          #Literotica Illustration(Art) Story Url
        self.purl = "https://www.literotica.com/p/%s"                          #Literotica Poem Story Url
        self.hurl = "https://www.literotica.com/s/%s"                          #Literotica Story Url
        self.surl = "https://literotica.com/api/3/stories/%s"                  #Literotica Story API Endpoint Url
        self.curl = 'https://www.literotica.com/c/%s'                          #Literotica Category Url
        self.turl = 'https://tags.literotica.com/%s'                           #Literotica Tag Url
        self.cturl = 'https://tags.literotica.com/%s/%s/'                      #Literotica Category & Tag Url
        [self.gdir(a) for a in [self.out, self.lout, self.sout]]              #Make Default List & Stories Directories If Not Created
        
        #Categories Which Won't Be Saved As Text Output
        self.nto = ['audio-sex-stories', 'illustrated-erotic-fiction', 'adult-comics', 
                    'erotic-art', 'illustrated-poetry', 'erotic-audio-poetry']
        
        #Dictionary Containing Category & Tag Url Structure For Parsing Categories For Stories With Matching Tag.
        #Categories 33-38 In Literotica Categories Menu Do Not Have Tags.
        self.ctag = {
                     "anal-sex-stories": "anal-category-tags",
                     "audio-sex-stories": "audio-category-tags",
                     "bdsm-stories": "bdsm-category-tags",
                     "celebrity-stories": "celebrities-fan-fiction-category-tags",
                     "chain-stories": "chain-stories-category-tags",
                     "erotic-couplings": "erotic-couplings-category-tags",
                     "erotic-horror": "erotic-horror-category-tags",
                     "exhibitionist-voyeur": "exhibitionist-voyeur-category-tags",
                     "fetish-stories": "fetish-category-tags",
                     "first-time-sex-stories": "first-time-category-tags",
                     "gay-sex-stories": "gay-male-category-tags",
                     "group-sex-stories": "group-sex-category-tags",
                     "adult-how-to": "how-to-category-tags",
                     "adult-humor": "humor-satire-category-tags",
                     "illustrated-erotic-fiction": "illustrated-category-tags",
                     "taboo-sex-stories": "incest-taboo-category-tags",
                     "interracial-erotic-stories": "interracial-love-category-tags",
                     "lesbian-sex-stories": "lesbian-sex-category-tags",
                     "erotic-letters": "letters-transcripts-category-tags",
                     "loving-wives": "loving-wives-category-tags",
                     "mature-sex": "mature-category-tags",
                     "mind-control": "mind-control-category-tags",
                     "non-english-stories": "non-english-category-tags",
                     "non-erotic-stories": "non-erotic-category-tags",
                     "non-consent-stories": "nonconsent-reluctance-category-tags",
                     "non-human-stories": "nonhuman-category-tags",
                     "erotic-novels": "novels-and-novellas-category-tags",
                     "reviews-and-essays": "reviews-essays-category-tags",
                     "adult-romance": "romance-category-tags",
                     "science-fiction-fantasy": "sci-fi-fantasy-category-tags",
                     "masturbation-stories": "toys-masturbation-category-tags",
                     "transgender-crossdressers": "transgender-crossdressers-category-tags"
                    }
        
        #Html Tag To Replace With Downloaded Audio File In Audio Story Html Output
        self.atag = '<button aria-label="Play" class="rhap_button-clear rhap_main-controls-button rhap_play-pause-button" type="button">'
        
        #Re-compiled Regex To Retrieve Audio File Links In Audio Type Stories Html
        self.areg = re.compile(r'(/audio/.*?)"')
        
        #Re-compiled Regex To Retrieve Story Title & Matching Author In Illustration Type Stories Html
        self.ireg = re.compile(r'"https://www.literotica.com/i/(\S+)".*?"https://www.literotica.com/authors/(\S+)/works"')
        
        #Re-compiled Regex To Retrieve Story Title & Matching Author In Typical Stories Html
        self.sreg = re.compile(r'"https://www.literotica.com/s/(\S+)".*?"https://www.literotica.com/authors/(\S+)/works"')
        
        #Re-compiled Regex To Retrieve Poem Title & Matching Author In Poem Html
        self.preg = re.compile(r'"https://www.literotica.com/p/(\S+)".*?"https://www.literotica.com/authors/(\S+)/works"')
    
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
    
    def flist(self, o: str, c: bool=False) -> list:
        """
        Returns Argument Or File Contents As List.
        :param o: Argument Or File Containing Data To Return As List.
        :param c: Optional Bool Specifying Category (Default=False).
        """
        a = []
        if path.isfile(o):
            a = [re.search(r'(\S+)', str(x)).group(1) for x in self.read(o)]
        elif o.isdigit() and c:
            if int(o) in range(1,39):
                a = [re.search(r'\('+o+r'\) (\S+)', str(__doc__)).group(1)]
        else:a = [o]
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
            if resp:id = resp.json()['user']['userid']               #Get Author's UserId From Literotica API
        if id:
            url = self.aurl %(id)
            rb = self.resp(url)
            if rb:
                ai = rb.json()                   #Initial Page API Json Response Containing Author's Stories
                ic = int(ai['last_page'])        #Amount Of Pages (50 Stories Per Page) Containing All Author's Stories
                a = ai['data'][0]['authorname']
                with open(path.join(self.lout, f'{a}.txt'), 'w', encoding='utf-8') as fw:
                    for i in range(1, ic + 1):                       #Iterate Total Pages Of Author Stories
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
    
    def category(self, c: str, u: str, t: str='', p: int=1, ps: int=1, tx: bool=False) -> list:
        """
        Returns A List Containing A List Of Specified Category Stories & Category Name.
        :param c: String Specifying Category.
        :param u: String Category Url.
        :param t: Optional String Specifying Tag.
        :param p: Optional Integer Amount Of Pages To Parse Category For Stories (Default=1).
        :param ps: Optional Integer Start Page To Parse Category Stories From (Default=1).
        :param tx: Optional Bool Specifying Text Output (Default=False).
        """
        url = u
        sl = []
        sd = []
        rg = self.sreg
        rt = p + 1
        if ps > 1:rt = p + ps
        if c in ['erotic-art', 'adult-comics']:rg = self.ireg
        elif 'poetry' in c:rg = self.preg
        for i in range(ps,rt):                                       #Iterate Specified Number Of Pages For Category
            if int(i) != 1:
                if t:url = f'{u}?page={i}'
                else:url = f'{u}?type=story&page={i}'
            fp = self.resp(url)
            if fp:sd.extend(re.findall(rg, fp.text))                 #Parse Category Html For All Stories & Matching Authors
        if sd:
            nf = path.join(self.lout, f'{c}.txt')
            if t:nf = path.join(self.lout, f'{c}__{t}.txt')
            with open(nf, 'w', encoding='utf-8') as fw:
                for a in sd:
                    self.gl += 1
                    sl.append(a[0])
                    fw.write(a[0]+' '+'_'*(72-len(a[0]))+a[1]+'\n')  #Write Story Titles & Matching Authors To Output File
            if tx and c in self.nto:return
        return [sl,c]
    
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
        :param st: String Art Story Title.
        :param fn: String Filename To Save Media File(s).
        :param js: Dictionary Literotica Api Story Response Data.
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
    
    def find_user(self, ul: list):
        """
        Returns Usernames Found In Database Matching String(s) & Outputs Names To 'Authors_Found.txt' In List Directory.
        :param usr: List Of Strings To Search User Database For Matching Usernames.
        """
        if not path.exists(self.udb):
            #Download User Database('user_db.parquet') To List Directory If Not Already On Device
            self.dfile(self.dbu, self.udb)
        df = fp.ParquetFile(self.udb).to_pandas()                            #Read Downloaded Database File Using Fastparquet Library
        c = 0
        for usr in ul:                                                   
            try:
                dff = df[df['name'].str.contains(usr, regex=True)]['name']   #Parse Database For Usernames With Matching String
                dff = dff.drop_duplicates()                                  #Remove Duplicates Before Writing To File
                c += len(dff)
                if c != 0:
                    #Append Found Usernames To 'Authors_Found.txt' In Output List Directory
                    dff.to_csv(self.usf, mode='a', index=False, header=False)
            except:break
        return c
    
    def text(self, fa: str, wv: int=128):
        """
        Returns TextWrap Formatted Story Text With Default Width (128 chars) Or Specified Width.
        :param fa: String Story Text To Be Formatted.
        :param wv: Integer Value Of Width To Format Text Default=128.
        """
        #Awesome Textwrap TextWrapper Class To Output Text 128 Characters Per Line
        wc = textwrap.TextWrapper(width=wv)
        return wc.fill(text=fa)
    
    def clist(self, c: bool=False, t: str='', l: list=[]) -> list:
        """
        Returns List Containing Tuple(s) Of Category/Tag & Url To Retrieve Stories From.
        :param c: Optional Bool Specifying Category (Default=False).
        :param t: Optional String Specifying Tag.
        :param l: Optional List Containing Categories (Required If Category Specified).
        """
        if c and t:
            #Return List Containing Category And Category + Tag Url
            return [(x, self.cturl %(self.ctag[x], t)) for x in l if self.ctag.get(x)]
        elif c:return [(x, self.curl %(x)) for x in l]        #Return List Containing Category And Category Url
        else:return [(tag, self.turl %(t))]                   #Return List Containing Tag And Tag Url
    
    def main(self, args):
        """
        Main Function To Execute Specified Arguments & Create Default Directories.
        """
        dr = self.sout
        us = 0
        fl = []
        dl = []
        ml = []
        print('\033[1;32;40m...Executing Selected Arguments Hold On...\n\033[0m')
        dl = self.flist(args.object, c=args.category)  #Store Argument Object As List (File Contents If File)
        if args.asearch:us = self.find_user(dl)        #Find Usernames With Matching String In Downloaded User Database
        else:
            with ThreadPoolExecutor(args.threads) as ex:
                if args.author and dl:
                    #Retrieve & List Author Stories Using Threads
                    fl = [ex.submit(self.author,a) for a in dl]
                elif args.category or args.tag:
                    dl = self.clist(c=args.category,t=args.tag, l=dl)
                    #Retrieve & List Category Stories Using Threads
                    fl = [ex.submit(self.category,a[0],a[1],t=args.tag,p=args.pages,ps=args.pstart,tx=args.text) for a in dl]
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
        elif self.gl > 0:print(f'\033[1;34;40m\n{self.gl} Stories Listed To Text File(s) In {self.lout}\033[0m')
        elif us > 0:print(f'\033[1;34;40m\n{us} Usernames Found & Listed To {self.usf}\033[0m')
        else:print('\033[1;31;40m\nNo Stories/Usernames Found/Listed/Downloaded Enter Valid Arguments Or Check Internet Connection!!\033[0m')
    
def clear_screen():
    """Clear Command Line Screen."""
    if name=='nt':system('cls')
    else:system('clear')

def slow_print(doc: str, sp: float=0.0005):
    """
    Print String By Speed In Seconds Less Is Faster.
    :param doc: String To Be Printed
    :param sp:  Speed To Print String `e.g 0.0001 or 0.0005 used`
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
             '  wudz-lit -f 6 -c -d -i                       Parse 1 Page Of Erotic-Couplings Category Stories & Download As Text.\n'
             '  wudz-lit -f 6 -c -p "socks5://localhost:80"  Parse 1 Page Of Stories & List To Text Using Specified Proxy.\n'
             '  wudz-lit -f author -a -x 120              Save All Specified Author(Uid/Name) Stories To Text File Using 120 Threads.\n'
             '  wudz-lit -f 20 -t milf -d -n 2 -ns 5      Parse 2 Pages "milf" Tag Start Page 5 & Download As Html.\n'
             '  wudz-lit -f mature-sex -c -t milf -d      Parse 1 Page Mature-Sex Category Stories With "milf" Tag & Download As Html.\n'
             '  wudz-lit -f Jay -as                       Search For Authors/Usernames Containing "Jay" & Output To File.\n'
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
    parser.add_argument('-as', '--asearch', action="store_true", help="Search For Usernames Containing String Specified In '-f' Argument.")
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
