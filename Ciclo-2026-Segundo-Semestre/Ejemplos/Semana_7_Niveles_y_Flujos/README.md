# Semana 7 · Niveles y flujos

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

Un nivel acumula cantidades y conserva memoria. Un flujo cambia un nivel y se mide en cantidad por unidad de tiempo. Una auxiliar calcula información necesaria; una constante fija un supuesto.

El diagrama de Forrester separa flujos materiales y enlaces informativos. Una flecha causal no se transforma automáticamente en una tubería.

Balance: Q(t + dt) = Q(t) + (entrada - salida) × dt. Si Q se mide en tickets, entrada y salida se expresan en tickets/día.

## Caso

Una mesa de ayuda inicia con 20 tickets pendientes, recibe 12 tickets/día y resuelve 10 tickets/día mientras hay trabajo suficiente.

## Ejemplo resuelto

1. Nivel: pendientes Q, unidad tickets. Flujos: llegadas y resoluciones, unidad tickets/día. Capacidad es un límite de la tasa de resolución.

2. Con dt = 1 día: Q(1) = 20 + (12 - 10) × 1 = 22 tickets; Q(2) = 24 tickets. El cambio neto es 2 tickets/día.

3. En un modelo con salida limitada por disponibilidad: resoluciones = MIN(capacidad, Q/tiempo de atención). Para evitar vaciar más de lo disponible con Euler, se exige dt <= tiempo de atención.

## Ejercicio propuesto

1. Dibuje un nivel, dos flujos, capacidad y tiempo de atención.
2. Clasifique ocho términos del caso por su función y unidad.
3. Calcule manualmente los primeros tres días con los flujos constantes.
4. Explique qué falla si se suma capacidad directamente al nivel. Entregue diagrama y tabla.

## Error frecuente

Modelar la llegada acumulada como tasa o sumar magnitudes con unidades incompatibles.

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
python recursos/simulacion.py --caso base --salida resultados/base
```

[Variables, unidades, pruebas y límites numéricos](../recursos/README.md).
