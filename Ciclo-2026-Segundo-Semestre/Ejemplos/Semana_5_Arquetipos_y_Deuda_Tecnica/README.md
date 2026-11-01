# Semana 5 · Arquetipos y deuda técnica

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

Soluciones contraproducentes: una acción alivia un síntoma a corto plazo y activa una consecuencia que lo agrava después. Se documentan un bucle de alivio y otro de refuerzo con demora.

Desplazamiento de la carga: una respuesta sintomática reduce el uso o desarrollo de una solución fundamental. Debe explicarse el mecanismo de dependencia.

Límites al crecimiento combina un proceso de refuerzo con una restricción que activa un balance. Nombrar el arquetipo exige mostrar la estructura y no solo relatar una dificultad.

## Caso

Un equipo aplica parches para disminuir incidentes. Esto libera tiempo hoy, pero posterga pruebas automatizadas y documentación. Con el tiempo, comprender el código toma más horas y reaparecen incidentes.

## Ejemplo resuelto

1. Alivio B1: incidentes (+) parches (-) incidentes inmediatos. Efecto no deseado R1: parches (+) complejidad (+) incidentes (+) parches.

2. La solución fundamental es reducir defectos mediante pruebas y diseño. Si los parches consumen el tiempo destinado a esa capacidad, se sostiene la hipótesis de desplazamiento de la carga.

3. Política: reservar capacidad para prevención y medir incidentes reincidentes. Un parche sigue siendo válido en una emergencia si se registra su reparación posterior.

## Ejercicio propuesto

1. Dibuje el alivio de corto plazo y el efecto adverso con demora.
2. Distinga soluciones contraproducentes y desplazamiento de la carga en el caso.
3. Añada un caso de límites al crecimiento con una restricción concreta.
4. Diseñe una política y un riesgo de su aplicación. Entregue dos diagramas y su explicación.

## Error frecuente

Usar nombres de arquetipos como etiquetas sin bucles o afirmar que todo trabajo urgente constituye desplazamiento de la carga.

## Uso por el tutor

Explicación 20 min, microexplicación 5 min, demostración 25 min y aplicación 50 min. La guía local incluye reflexión y cierre. Las fechas y ponderaciones oficiales las comunica el docente.

## Fuentes

- Manual Vensim: https://vensim.com/documentation/22300.html
- Retardos materiales e informativos: https://www.vensim.com/documentation/mgu09_material_and_information_delays.html
- Escalera de inferencias: https://thesystemsthinker.com/the-ladder-of-inference/
- Intervención sistémica: https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/
