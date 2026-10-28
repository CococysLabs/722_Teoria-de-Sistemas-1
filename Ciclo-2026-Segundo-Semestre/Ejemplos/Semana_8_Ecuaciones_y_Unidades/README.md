# Semana 8 · Ecuaciones y consistencia dimensional

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

La formulación continua dQ/dt = L - R corresponde a Q = INTEG(L - R, Q0). Cada ecuación debe declarar significado, unidad y supuesto.

Con R = MIN(C, Q/T), C se mide en tickets/día y T en días. Si L < C y el nivel no satura la capacidad, el equilibrio es Q* = L × T.

Calibrar es estimar parámetros con evidencia. Elegir números para que una gráfica se vea bien no demuestra validez. Compare condiciones iniciales y datos, y declare incertidumbre.

## Caso

Q0 = 20 tickets, L = 12 tickets/día, C = 10 tickets/día, T = 1 día. Se simulan 30 días con Euler y dt = 0.25 días.

## Ejemplo resuelto

1. Q = INTEG(llegadas - resoluciones, 20). Resoluciones = MIN(capacidad, Q/tiempo_atencion). Capacidad = 10; llegadas = 12; tiempo_atencion = 1.

2. Como Q/T >= C durante todo el caso base, R = 10 y Q(t) = 20 + 2t. Se espera Q(5) = 30, Q(10) = 40 y Q(30) = 80 tickets.

3. Unidades: tickets/día - tickets/día da tickets/día; su integral temporal da tickets. Es incorrecto restar tiempo_atencion de capacidad.

## Ejercicio propuesto

1. Escriba las ecuaciones de cada variable y su unidad.
2. Calcule una actualización Euler con dt = 0.25 días.
3. Proponga cómo estimar llegadas con un registro de cinco días.
4. Cambie C a 16 y razone el equilibrio antes de simular. Entregue diccionario y cálculo.

## Error frecuente

Confundir equilibrio con cero o declarar unidades correctas sin verificar cada término de las ecuaciones.

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
