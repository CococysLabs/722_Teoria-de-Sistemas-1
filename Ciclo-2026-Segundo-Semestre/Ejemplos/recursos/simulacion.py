"""Ejemplos didácticos de TS1. Python 3.10+; solo biblioteca estándar.

Los parámetros son sintéticos. Euler explícito, estados simultáneos.
No reproduce el motor de Vensim ni acredita validación externa.
"""
from __future__ import annotations
import argparse
import csv
import math
import random
from pathlib import Path

LOOKUP=((0,1),(.5,1),(1,.9),(1.5,.6),(2,.4))

def lookup(x):
    """Productividad relativa; x adimensional, acotado a [0,2]."""
    x=max(0,min(2,x))
    for (x0,y0),(x1,y1) in zip(LOOKUP,LOOKUP[1:]):
        if x<=x1: return y0+(y1-y0)*(x-x0)/(x1-x0)
    return LOOKUP[-1][1]

def simular(llegadas=12.,capacidad=10.,q0=20.,tiempo_atencion=1.,dias=30.,dt=.25,tau=3.,orden=0,usar_lookup=False):
    if min(llegadas,capacidad,q0)<0 or min(tiempo_atencion,dias,dt,tau)<=0:
        raise ValueError('Tasas y nivel no negativos; tiempos estrictamente positivos.')
    if orden not in (0,1,3): raise ValueError('Orden: 0, 1 o 3.')
    limite=min(tiempo_atencion,tau/orden) if orden else tiempo_atencion
    if dt>limite: raise ValueError('dt debe ser <= tiempo de atención y <= tau/orden.')
    pasos=round(dias/dt)
    if not math.isclose(pasos*dt,dias,abs_tol=1e-9): raise ValueError('El horizonte debe ser múltiplo de dt.')
    q=q0; etapas=[q0]*orden; entradas=salidas=area=0.;maximo=q
    filas=[]
    for i in range(pasos+1):
        percepcion=etapas[-1] if orden else q
        c=min(24.,max(0.,10.+.5*(percepcion-20.))) if orden else capacidad
        if usar_lookup: c*=lookup(q/20.)
        res=min(c,q/tiempo_atencion)
        filas.append(dict(dia=i*dt,pendientes=q,percibidos=percepcion,llegadas=llegadas,resoluciones=res,capacidad_efectiva=c))
        if i==pasos: break
        siguiente=q+(llegadas-res)*dt
        if siguiente < -1e-10: raise AssertionError('Nivel negativo: revise paso temporal.')
        if orden:
            fuentes=[q]+etapas[:-1]
            nuevas=[v+(fuente-v)*dt/(tau/orden) for v,fuente in zip(etapas,fuentes)]
            etapas=nuevas
        area+=(q+siguiente)*dt/2
        q=siguiente;maximo=max(maximo,q);entradas+=llegadas*dt;salidas+=res*dt
    residual=q-q0-entradas+salidas
    if abs(residual)>1e-7: raise AssertionError('No se conserva el balance.')
    return filas,dict(pendientes_finales=q,maximo=maximo,area_tickets_dia=area,residual_balance=residual)

def guardar_csv(path,filas):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(filas[0]));w.writeheader();w.writerows(filas)

def grafica(path,series,titulo):
    """Gráfico SVG con ejes y unidades, sin dependencias externas."""
    from html import escape
    ancho,alto=900,440;left,top=70,50;pw,ph=770,310
    xmax=max(rows[-1]['dia'] for _,rows in series)
    ymax=max(1,max(r['pendientes'] for _,rows in series for r in rows))*1.1
    colores=['#174E78','#B74B30','#297861','#86529A','#7B671E','#323C48']
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}"><rect width="100%" height="100%" fill="white"/><g font-family="Arial" font-size="13" fill="#172331">',f'<text x="70" y="25" font-size="19">{escape(titulo)}</text>']
    for i in range(6):
        x=left+i*pw/5;y=top+ph-i*ph/5
        svg += [f'<path d="M{left},{y}H{left+pw}" stroke="#E0E5EA"/><text x="12" y="{y+4}">{ymax*i/5:.1f}</text>',f'<text x="{x-10}" y="385">{xmax*i/5:.0f}</text>']
    svg += [f'<path d="M{left},{top}V{top+ph}H{left+pw}" fill="none" stroke="#152B40"/>','<text x="440" y="410">Tiempo en días</text>','<text x="12" y="45">Tickets</text>']
    for i,(name,rows) in enumerate(series):
        pts=' '.join(f"{left+r['dia']/xmax*pw:.2f},{top+ph-r['pendientes']/ymax*ph:.2f}" for r in rows)
        color=colores[i%len(colores)]
        svg += [f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.4"/>',f'<text x="{75+i*130}" y="435" fill="{color}">{escape(name)}</text>']
    svg.append('</g></svg>');path.write_text(''.join(svg),encoding='utf8')

def ejecutar(caso,output):
    output.mkdir(parents=True,exist_ok=True);series=[];resumen=[]
    if caso in ('base','politicas'):
        params=[('Base',12,10)] if caso=='base' else [('Base',12,10),('Politica_A',12,16),('Politica_B',8,10)]
        for nombre,l,c in params:
            filas,med=simular(llegadas=l,capacidad=c)
            guardar_csv(output/(nombre+'.csv'),filas);series.append((nombre,filas));resumen.append(dict(escenario=nombre,llegadas=l,capacidad=c,**med))
    elif caso=='sensibilidad':
        for l in (8,12,16):
            for c in (10,16,22):
                filas,med=simular(llegadas=l,capacidad=c)
                nombre=f'L{l}_C{c}';guardar_csv(output/(nombre+'.csv'),filas)
                resumen.append(dict(escenario=nombre,llegadas=l,capacidad=c,**med))
    elif caso=='retardos':
        for orden in (1,3):
            for tau in (1,3,6):
                filas,med=simular(dias=60,dt=.05,orden=orden,tau=tau)
                nombre=f'Orden{orden}_tau{tau}';guardar_csv(output/(nombre+'.csv'),filas);series.append((nombre,filas))
                resumen.append(dict(escenario=nombre,orden=orden,tau=tau,**med))
    elif caso=='lookup':
        for enabled in (False,True):
            filas,med=simular(capacidad=16,usar_lookup=enabled)
            nombre='Con_lookup' if enabled else 'Sin_lookup';guardar_csv(output/(nombre+'.csv'),filas);series.append((nombre,filas));resumen.append(dict(escenario=nombre,**med))
    elif caso=='montecarlo':
        rng=random.Random(722)
        for i in range(100):
            l=rng.uniform(8,16);c=rng.uniform(10,22);_,med=simular(llegadas=l,capacidad=c)
            resumen.append(dict(corrida=i+1,semilla=722,llegadas=l,capacidad=c,**med))
    guardar_csv(output/'resumen.csv',resumen)
    if series:grafica(output/'comparacion.svg',series,'Pendientes por escenario')
    return resumen

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--caso',choices=['base','politicas','sensibilidad','retardos','lookup','montecarlo'],default='base')
    parser.add_argument('--salida',type=Path,default=Path('resultados'))
    args=parser.parse_args()
    for row in ejecutar(args.caso,args.salida): print(row)
