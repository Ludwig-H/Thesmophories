#!/usr/bin/env python3
"""Mesure des encres des interventions (chapitre 4 de l'étude graphologique).

Principe : pixels de trait = (fond local - luminance) > seuil, sans condition de teinte
(pour ne pas exclure les encres neutres) ; absorbances relatives au fond local, canal par
canal ; comparaison à densité égale (classes d'absorbance rouge) avec le texte de T des
lignes voisines.

Usage :
  python3 encres_interventions.py f170r 780 822 1040 875   # mesure d'une zone
  python3 encres_interventions.py f170r 780 822 1040 875 --ref 240 600 1600 800
"""
"""(voir l'en-tête)
Mesure : pixels de trait = (fond local - luminance) > seuil, sans condition de teinte
(pour ne pas exclure les encres neutres) ; on garde le cœur (50 % les plus sombres) ;
absorbances relatives au fond local par canal, rapports A_G/A_R et A_B/A_R."""
import sys, os, json
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
RACINE='/workspaces/Thesmophories'
SRC=os.path.join(RACINE,'dossier_ravennas_thesmophories','folios_individuels_ff162v-177r')
PAGES={f.split('_')[1]:os.path.join(SRC,f) for f in os.listdir(SRC) if f.endswith('.jpg')}
OUT=os.path.join(RACINE,'.travail','chap4','verif')  # découpes de travail (non versionnées)
_c={}
def page(f):
    if f not in _c: _c[f]=Image.open(PAGES[f]).convert('RGB')
    return _c[f]
OBS=None
def obs(ref):
    global OBS
    if OBS is None:
        OBS={f"{o['_page']}#{o['_idx']}":o for o in json.load(open(os.path.join(RACINE,'.travail/chap4/toutes_obs.json')))}  # index des observations (fXXX.jsonl)
    return OBS[ref]
try: FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13)
except OSError: FONT=ImageFont.load_default()

def vue(f,box,ech=3,nom=None,mode='orig',regle=True):
    x0,y0,x1,y1=box
    im=page(f)
    if mode=='orig':
        c=im.crop(box)
    elif mode=='contraste':
        c=ImageOps.autocontrast(im.crop(box),cutoff=1)
    elif mode=='bleu':
        b=np.asarray(im.crop(box))[...,2]
        c=ImageOps.autocontrast(Image.fromarray(b),cutoff=1).convert('RGB')
    elif mode=='renfort':
        m=30
        cc=im.crop((x0-m,y0-m,x1+m,y1+m))
        L=np.asarray(cc.convert('L').filter(ImageFilter.GaussianBlur(1.0))).astype(float)
        bg=np.asarray(cc.convert('L').filter(ImageFilter.GaussianBlur(15))).astype(float)
        d=np.clip(255-(bg-L)*2.5,0,255).astype(np.uint8)[m:-m,m:-m]
        c=Image.fromarray(d).convert('RGB')
    elif mode=='ratio':  # carte B/R d'absorbance : orangé = rouge
        c=carte_ratio(f,box)
    w,h=c.size
    c=c.resize((int(w*ech),int(h*ech)),Image.LANCZOS)
    if regle:
        bt,bl=20,44
        o=Image.new('RGB',(c.size[0]+bl,c.size[1]+bt),'white'); o.paste(c,(bl,bt)); d=ImageDraw.Draw(o)
        pas=10 if (x1-x0)<=200 else (20 if (x1-x0)<=600 else 50)
        lab=pas*5 if pas<50 else pas*2
        for x in range((x0//pas+1)*pas,x1,pas):
            X=bl+(x-x0)*ech; L=8 if x%lab==0 else 4
            d.line([(X,bt-L),(X,bt-1)],fill=(200,0,0))
            if x%lab==0: d.text((X+2,1),str(x),fill=(200,0,0),font=FONT)
        for y in range((y0//pas+1)*pas,y1,pas):
            Y=bt+(y-y0)*ech; L=8 if y%lab==0 else 4
            d.line([(bl-L,Y),(bl-1,Y)],fill=(0,0,200))
            if y%lab==0: d.text((1,Y-7),str(y),fill=(0,0,200),font=FONT)
        c=o
    if nom is None: nom=f"{f}_{x0}_{y0}_{mode}.png"
    p=os.path.join(OUT,nom); c.save(p); return p

def absorb(f,box,seuil=22,coeur=0.5,marge=40):
    x0,y0,x1,y1=box
    im=page(f); W,H=im.size
    X0,Y0,X1,Y1=max(0,x0-marge),max(0,y0-marge),min(W,x1+marge),min(H,y1+marge)
    c=np.asarray(im.crop((X0,Y0,X1,Y1))).astype(float)
    L=c.mean(axis=2)
    Lb=np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(float)
    F=[np.asarray(Image.fromarray(c[...,i].astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(float) for i in range(3)]
    sl=(slice(y0-Y0,y1-Y0),slice(x0-X0,x1-X0))
    m=((Lb-L)>seuil)[sl]
    if m.sum()<4: return None
    Ls=L[sl]
    if coeur:
        t=np.percentile(Ls[m],coeur*100); m=m&(Ls<=t)
    A=[]
    for i in range(3):
        I=c[...,i][sl][m]; Fi=F[i][sl][m]
        A.append(float(np.mean(-np.log10(np.clip(I,1,255)/np.clip(Fi,1,255)))))
    return dict(n=int(m.sum()),A=[round(a,3) for a in A],GR=round(A[1]/A[0],2) if A[0]>0 else None,BR=round(A[2]/A[0],2) if A[0]>0 else None,
                contr=round(float((Lb[sl]-Ls)[m].mean()),1))
def fmt(d):
    if d is None: return 'aucun pixel'
    return f"n={d['n']:4d} A_R={d['A'][0]:.3f} G/R={d['GR']:.2f} B/R={d['BR']:.2f} contr={d['contr']}"

def carte_ratio(f,box,seuil=18):
    x0,y0,x1,y1=box; m=40
    im=page(f)
    c=np.asarray(im.crop((x0-m,y0-m,x1+m,y1+m))).astype(float)
    L=c.mean(axis=2)
    Lb=np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(float)
    F=[np.asarray(Image.fromarray(c[...,i].astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(float) for i in range(3)]
    A=[-np.log10(np.clip(c[...,i],1,255)/np.clip(F[i],1,255)) for i in range(3)]
    mask=(Lb-L)>seuil
    br=np.where(A[0]>0.02,A[2]/np.maximum(A[0],1e-3),0)
    out=np.full(L.shape+(3,),255,np.uint8)
    # échelle : B/R <1.6 gris ; 1.6-2.4 bleu (T/S2) ; 2.4-2.7 jaune ; >2.7 rouge (orangé)
    col=np.zeros(L.shape+(3,),np.uint8)
    col[...]=(150,150,150)
    col[(br>=1.6)&(br<2.45)]=(40,80,220)
    col[(br>=2.45)&(br<2.75)]=(230,190,0)
    col[br>=2.75]=(230,30,30)
    out[mask]=col[mask]
    return Image.fromarray(out[m:-m,m:-m])

def pixels(f,box,seuil=18,marge=40):
    """Absorbances par pixel (A_R, A_G, A_B) des pixels de trait d'une zone."""
    x0,y0,x1,y1=box
    im=page(f); W,H=im.size
    X0,Y0,X1,Y1=max(0,x0-marge),max(0,y0-marge),min(W,x1+marge),min(H,y1+marge)
    c=np.asarray(im.crop((X0,Y0,X1,Y1))).astype(float)
    L=c.mean(axis=2)
    Lb=np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(float)
    F=[np.asarray(Image.fromarray(c[...,i].astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(float) for i in range(3)]
    sl=(slice(y0-Y0,y1-Y0),slice(x0-X0,x1-X0))
    m=((Lb-L)>seuil)[sl]
    A=[(-np.log10(np.clip(c[...,i],1,255)/np.clip(F[i],1,255)))[sl][m] for i in range(3)]
    return np.stack(A,axis=1)

BINS=[(0.10,0.15),(0.15,0.20),(0.20,0.25),(0.25,0.32),(0.32,0.45)]
def par_densite(P):
    out=[]
    for a,b in BINS:
        s=P[(P[:,0]>=a)&(P[:,0]<b)]
        if len(s)<5: out.append(None); continue
        out.append((len(s),round(float(np.median(s[:,1]/s[:,0])),2),round(float(np.median(s[:,2]/s[:,0])),2)))
    return out
def fmtd(o):
    return ' | '.join('—' if x is None else f'n{x[0]} {x[1]:.2f}/{x[2]:.2f}' for x in o)


if __name__=='__main__':
    a=sys.argv[1:]
    f=a[0]; box=tuple(map(int,a[1:5]))
    P=pixels(f,box)
    print('zone :',fmt(absorb(f,box)))
    print('par densité :',fmtd(par_densite(P)))
    if '--ref' in a:
        k=a.index('--ref'); rb=tuple(map(int,a[k+1:k+5]))
        print('référence (T) :',fmtd(par_densite(pixels(f,rb))))
