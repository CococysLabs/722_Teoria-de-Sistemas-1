# Semana 11 · Políticas y análisis de sensibilidad

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

Una política cambia una regla o estructura del sistema. Un escenario describe condiciones posibles. La sensibilidad varía parámetros para examinar cuánto depende la conclusión de los supuestos.

Los puntos de apalancamiento orientan la búsqueda de intervenciones. El efecto debe contrastarse y puede tener costos, demoras o consecuencias sobre otros actores.

Use el mismo horizonte, condiciones iniciales e indicadores al comparar. Con varios parámetros, empiece con una malla pequeña y documente cada combinación. La opción manual en Vensim PLE evita depender de funciones automáticas de otras ediciones.

## Caso

Compare Base: llegadas 12 y capacidad 10; política A: capacidad 16 desde el inicio; política B: llegadas 8 desde el inicio; Q0=20 y tiempo de atención=1. Horizonte 30 días.

## Ejemplo resuelto

1. Base termina en 80 tickets. A converge hacia 12 y B hacia 8; ambos reducen pendientes, pero B supone reducir demanda, lo cual puede significar prevención real o rechazo de solicitudes.

2. Indicadores: pendientes finales, máximo de pendientes y área bajo Q en tickets·día. El área aproxima carga acumulada y no equivale por sí sola al tiempo promedio de respuesta.

3. Pruebe llegadas 8,12,16 y capacidad 10,16,22. Registre nueve combinaciones y verifique si la recomendación cambia. Compare costos con un presupuesto explícito antes de declarar una política superior.

## Ejercicio propuesto

1. Ejecute los tres escenarios y documente los parámetros.
2. Construya una malla de nueve combinaciones.
3. Repita una corrida con la mitad del paso temporal y una condición extrema.
4. Recomiende una política con evidencia, costo supuesto y una consecuencia no deseada. Entregue una hoja de decisión.

## Error frecuente

Confundir sensibilidad con predicción probabilística o comparar políticas con horizontes y condiciones iniciales distintos.

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
python recursos/simulacion.py --caso sensibilidad --salida resultados/sensibilidad
```

[Variables, unidades, pruebas y límites numéricos](../recursos/README.md).
