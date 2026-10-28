# Semana 9 · Construcción y verificación en Vensim

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

Antes de simular, defina el horizonte, paso temporal y unidad de tiempo. Use nombres estables y documente todos los parámetros.

La comprobación de unidades detecta incompatibilidades dimensionales, pero no demuestra que el modelo represente el caso. También se requieren pruebas estructurales y de comportamiento.

Guarde una corrida base antes de cambiar parámetros. Identifique cada escenario por el cambio aplicado; un gráfico sin ejes, unidades o nombres de corrida no permite comparar.

## Caso

Implemente el modelo de tickets de la semana 8. Controles: INITIAL TIME = 0, FINAL TIME = 30, TIME STEP = 0.25 y SAVEPER = TIME STEP; unidad de tiempo Day.

## Ejemplo resuelto

1. Dibuje Pendientes con entrada Llegadas y salida Resoluciones. Cree Capacidad y Tiempo_atencion como auxiliares o constantes, y conecte los enlaces de información requeridos.

2. Ingrese Pendientes = INTEG(Llegadas-Resoluciones,20), Llegadas=12, Capacidad=10, Tiempo_atencion=1 y Resoluciones=MIN(Capacidad,Pendientes/Tiempo_atencion). Declare tickets, tickets/Day y Day.

3. Ejecute la comprobación de modelo y de unidades. Corra Base. En el caso base se esperan 20, 40 y 80 tickets en los días 0, 10 y 30. Si difiere, revise controles y ecuaciones.

## Ejercicio propuesto

1. Construya y guarde un archivo .mdl con todas las unidades.
2. Capture comprobación de unidades y gráfica con ejes.
3. Compare días 0, 10 y 30 contra la predicción manual.
4. Repita con TIME STEP=0.125; registre diferencias. Entregue .mdl, tabla y explicación.

## Error frecuente

Confundir verificación de software con validación del modelo, o cambiar varios parámetros sin registrar cuál produjo el efecto.

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
