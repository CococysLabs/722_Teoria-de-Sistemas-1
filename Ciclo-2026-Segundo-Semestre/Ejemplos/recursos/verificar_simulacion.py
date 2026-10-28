"""Comprobaciones numéricas del ejemplo. Ejecutar junto a simulacion.py."""
import math
from simulacion import simular,lookup

filas,m=simular()
assert math.isclose(m['pendientes_finales'],80,abs_tol=1e-8)
assert math.isclose(m['area_tickets_dia'],1500,abs_tol=1e-7)
for l,c,q in [(0,10,20),(12,0,20),(12,10,0),(0,0,0)]:
    rows,med=simular(llegadas=l,capacidad=c,q0=q)
    assert all(r['pendientes']>=0 for r in rows)
    assert abs(med['residual_balance'])<1e-7
assert math.isclose(simular(llegadas=12,capacidad=0)[1]['pendientes_finales'],380)
assert math.isclose(simular(capacidad=16)[1]['pendientes_finales'],12,abs_tol=1e-6)
assert math.isclose(simular(llegadas=8)[1]['pendientes_finales'],8,abs_tol=1e-6)
assert lookup(-1)==1 and lookup(3)==.4 and math.isclose(lookup(1.25),.75)
for orden in (1,3):
    for tau in (1,3,6):
        coarse,mc=simular(orden=orden,tau=tau,dias=60,dt=.0125)
        medium,mm=simular(orden=orden,tau=tau,dias=60,dt=.00625)
        fine,mf=simular(orden=orden,tau=tau,dias=60,dt=.003125)
        # En la oscilación con tau=6 los pasos .1 y .05 no bastan.
        error1=abs(mc['pendientes_finales']-mm['pendientes_finales'])
        error2=abs(mm['pendientes_finales']-mf['pendientes_finales'])
        assert error2<=error1+1e-8
        assert error2/max(1,abs(mf['pendientes_finales']))<.01
        assert all(x['pendientes']>=0 for x in fine)
try: simular(dt=2)
except ValueError: pass
else: raise AssertionError('Debe rechazar paso excesivo')
print('Correcto: balance, extremos, equilibrio, Lookup y convergencia del ejemplo.')
