import pandas as pd
import fastparquet as fp
import requests, sys
from concurrent.futures import ThreadPoolExecutor, as_completed


class LitUsers:
    def __init__(self):
        hd={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.req=requests.Session()
        self.req.headers.update(hd)
        self.url="https://literotica.com/api/3/users/%s"
        self.fn="user_db.parquet"
        self.tx=200
        self.usl=[]
        self.idl=[]

    def upd_db(self):
        self.usl.append(max(self.idl)+1)
        df=pd.DataFrame({'name': self.usl})
        df.to_parquet(self.fn, engine='fastparquet', index=False, append=True)
    
    def get_user(self, i):
        try:
            r=self.req.get(self.url %(i)).json()
            u=r['user']['username']
            self.usl.append(u)
            self.idl.append(i)
        except:pass
    
    def get_id(self):
        df=fp.ParquetFile(self.fn).to_pandas()
        return df.iloc[-1]['name']
    
    def main(self):
        fl: Set[Future]=set()
        v=self.get_id()
        if v.isdigit():
            with ThreadPoolExecutor(self.tx) as exec:
                for i in range(int(v),int(v)+10000):
                    try:
                        fl.add(exec.submit(self.get_user, i))
                    except:pass
            if self.usl:self.upd_db()
    
if __name__=='__main__':
    LitUsers().main()