# Ejemplo numérico reproducible

Todos los datos son sintéticos. Python 3.10 o posterior, sin paquetes adicionales.
El script usa Euler explícito y actualiza los estados a partir del mismo instante.

Desde la carpeta `Ejemplos`, ejecutar:

```console
python recursos/verificar_simulacion.py
python recursos/simulacion.py --caso base --salida resultados/base
python recursos/simulacion.py --caso politicas --salida resultados/politicas
python recursos/simulacion.py --caso sensibilidad --salida resultados/sensibilidad
python recursos/simulacion.py --caso retardos --salida resultados/retardos
python recursos/simulacion.py --caso lookup --salida resultados/lookup
python recursos/simulacion.py --caso montecarlo --salida resultados/montecarlo
```

Cada ejecución genera tablas CSV. Los casos con series comparables también generan un gráfico SVG con ejes y unidades. `resultados_referencia` conserva salidas de referencia para contrastar. Ningún dato procede de estudiantes.

## Modelo base y comprobaciones

Q representa tickets pendientes; L llegadas en tickets/día; C capacidad en tickets/día y T tiempo de atención en días.

`dQ/dt = L - MIN(C,Q/T)`; Q0=20, L=12, C=10, T=1, horizonte=30, dt=0.25.

Resultados: Q(10)=40, Q(30)=80 y área bajo Q=1500 tickets·día. El área es carga acumulada, no tiempo medio de respuesta. Con capacidad 16 se converge hacia 12 tickets. Con llegadas 8 y capacidad 10, hacia 8. El nivel puede ser positivo en equilibrio aunque exista capacidad suficiente.

La verificación comprueba conservación, no negatividad, extremos, equilibrio, interpolación Lookup y refinamiento del paso. `ecuaciones_vensim.txt` sirve para construir el modelo en Vensim; no se entrega como archivo .mdl ya diagramado. `forrester_tickets.svg` muestra la estructura.

## Retardos y límites numéricos

Los retardos son informativos, con uno o tres niveles de percepción. No modelan material en tránsito. El script compara tau=1,3,6 y usa dt=0.05 para las gráficas didácticas. En el caso de tercer orden con tau=6, comparar solo dt=0.1 y 0.05 es insuficiente para aceptar convergencia. Consulte `resultados_referencia/convergencia_tau6.csv`, que refina hasta 0.003125. Las pruebas usan los pasos más finos y exigen que la diferencia disminuya y sea menor de 1% en el valor final. No se extrapola esta comprobación a todos los modelos.

## Sensibilidad y Monte Carlo

La sensibilidad central usa nueve combinaciones de llegadas 8/12/16 y capacidad 10/16/22. Monte Carlo es una extensión separada de 100 corridas, semilla 722, llegadas uniformes [8,16] y capacidad uniforme [10,22], independientes. Son distribuciones ilustrativas, no estimaciones empíricas ni probabilidades de un sistema real.

No se necesita una función automática de sensibilidad de pago: se pueden realizar corridas manuales en Vensim PLE y registrar la misma matriz. Los resultados Python se han ejecutado; las ecuaciones deben comprobarse en la instalación de Vensim donde se construya el diagrama.

## Fuentes

- Manual de funciones: https://vensim.com/documentation/22300.html
- Retardos: https://www.vensim.com/documentation/mgu09_material_and_information_delays.html
