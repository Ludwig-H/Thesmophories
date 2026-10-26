#!/usr/bin/env python3
"""Interroge le catalogue collectif bavarois B3Kat (SRU, MARCXML) et imprime une notice résumée par ligne.
Usage : python3 b3kat_sru.py 'marcxml.title=Thesmophoriazusae' [max]
"""
import sys, urllib.parse, urllib.request
from lxml import etree
NS={'zs':'http://www.loc.gov/zing/srw/','m':'http://www.loc.gov/MARC21/slim'}
def sf(rec,tag,codes=None,sep=' '):
    out=[]
    for df in rec.findall(f'm:datafield[@tag="{tag}"]',NS):
        parts=[s.text or '' for s in df.findall('m:subfield',NS) if codes is None or s.get('code') in codes]
        out.append(sep.join(p.strip() for p in parts if p.strip()))
    return out
def main():
    q=sys.argv[1]; mx=int(sys.argv[2]) if len(sys.argv)>2 else 500
    start=1; n=0
    while True:
        url=('http://bvbr.bib-bvb.de:5661/bvb01sru?version=1.1&recordSchema=marcxml&operation=searchRetrieve'
             f'&maximumRecords=50&startRecord={start}&query='+urllib.parse.quote(q))
        x=etree.fromstring(urllib.request.urlopen(url,timeout=120).read())
        tot=int(x.findtext('zs:numberOfRecords',namespaces=NS) or 0)
        recs=x.findall('.//m:record',NS)
        if not recs: break
        for r in recs:
            n+=1
            idn=r.findtext('m:controlfield[@tag="001"]',namespaces=NS)
            t=' '.join(sf(r,'245',list('abnp')))
            ed=' '.join(sf(r,'250',['a']))
            pub=' ; '.join(sf(r,'264',list('abc')) or sf(r,'260',list('abc')))
            ext=' '.join(sf(r,'300',['a']))
            rel=' | '.join(sf(r,'490',['a','v'])+sf(r,'830',['a','v']))
            links=sorted(set(u for u in sf(r,'856',['u']) if u))
            print(f'{idn}\t{t}\t{ed}\t{pub}\t{ext}\t{rel}\t{" ".join(links)}')
        start+=len(recs)
        if start>tot or n>=mx: break
    print(f'# total={tot}',file=sys.stderr)
main()
