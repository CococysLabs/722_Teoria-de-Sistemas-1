# Semana 10 · Comportamiento temporal y retardos

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

El crecimiento exponencial dP/dt=rP tiene tasa proporcional al nivel. El crecimiento logístico dP/dt=rP(1-P/K) incorpora una capacidad K. Un parecido visual no permite identificar por sí solo la estructura.

Un retardo informativo puede representarse con dS/dt=(Q-S)/tau. El retardo material debe conservar cantidades y contabilizar lo que está en tránsito; no es intercambiable con suavizar una observación.

Para respuesta informativa de tercer orden se usan tres niveles en cascada con tiempo tau/3 por nivel. Compare primer y tercer orden con la misma demora media; no atribuya oscilaciones a todo retardo automáticamente.

## Caso

La jefatura decide usando pendientes percibidos S, no Q. Capacidad = MIN(24, MAX(0, 10 + 0.5 × (S-20))). Q0=S0=20; llegadas=12; tau=3 días.

## Ejemplo resuelto

1. La percepción sigue dS/dt=(Q-S)/3. Si Q sube de 20 a 26 y se mantiene, la derivada inicial de S es (26-20)/3 = 2 tickets/día.

2. Con tres etapas inicializadas en 20: dS1/dt=(Q-S1)/(tau/3), dS2/dt=(S1-S2)/(tau/3), dS3/dt=(S2-S3)/(tau/3). La capacidad utiliza S3.

3. Una función Lookup puede relacionar carga normalizada x con productividad relativa: (0,1), (0.5,1), (1,0.9), (1.5,0.6), (2,0.4). Defina x como adimensional y documente interpolación y límites.

## Ejercicio propuesto

1. Compare tau=1, 3 y 6 con primer y tercer orden.
2. Grafique Q y percepción con los mismos ejes y horizonte de 60 días.
3. Compare dt=0.1 y 0.05; reporte máximo y valor final.
4. Implemente la Lookup acotada y explique un límite de la evidencia. Entregue tabla y dos conclusiones.

## Error frecuente

Usar el valor recién actualizado de una etapa para actualizar otra en el mismo paso, o llamar material a un retardo de percepción.

## Uso por el tutor

Explicación 20 min, microexplicación 5 min, demostración 25 min y aplicación 50 min. La guía local incluye reflexión y cierre. Las fechas y ponderaciones oficiales las comunica el docente.

## Fuentes

- Manual Vensim: https://vensim.com/documentation/22300.html
- Retardos materiales e informativos: https://www.vensim.com/documentation/mgu09_material_and_information_delays.html
- Escalera de inferencias: https://thesystemsthinker.com/the-ladder-of-inference/
- Intervención sistémica: https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/

## Reproducción

Desde `Ejemplos`:

```console
python recursos/simulacion.py --caso retardos --salida resultados/retardos
```

[Variables, unidades, pruebas y límites numéricos](../recursos/README.md).
