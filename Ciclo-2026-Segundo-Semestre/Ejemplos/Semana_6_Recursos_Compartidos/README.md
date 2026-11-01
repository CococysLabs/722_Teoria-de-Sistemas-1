# Semana 6 · Recursos compartidos y arquetipos avanzados

Recursos elaborados en el cierre de 2S2026 para la actualización curricular con proyección a 1S2027. Propuesta de apoyo al curso sin laboratorio independiente.

## Lectura breve

La tragedia de los comunes aparece cuando beneficios individuales del uso de un recurso compartido no incorporan el costo agregado de degradarlo. La capacidad y las reglas de acceso son parte del modelo.

Éxito para quien tiene éxito describe una asignación de recursos que refuerza una ventaja inicial. Debe examinarse si el criterio de asignación crea el resultado que luego se usa para justificarlo.

En escalada, cada actor responde a la acción del otro incrementando su propia acción. El problema requiere describir la percepción de amenaza y la regla de respuesta.

## Caso

Tres servicios usan un servidor con capacidad de 120 solicitudes por minuto. Cada servicio demanda 50. Los equipos reintentan ante una respuesta lenta y elevan todavía más la carga.

## Ejemplo resuelto

1. Demanda total: 3 × 50 = 150 solicitudes/minuto. Exceso inicial: 30 solicitudes/minuto. Un reintento no elimina trabajo pendiente y puede agravar la congestión.

2. R1: carga (+) latencia (+) reintentos (+) carga. La capacidad compartida limita el rendimiento del conjunto.

3. Una cuota de 40 por servicio respeta 120, pero deja demanda sin atender. Debe acompañarse de priorización, espera o ampliación justificada; no se puede declarar resuelto el problema solo por limitar el ingreso.

## Ejercicio propuesto

1. Modele dos usuarios y la capacidad compartida con un DCC.
2. Compare cuotas, ampliación y reducción de reintentos usando un indicador de servicio.
3. Construya un ejemplo breve de éxito para quien tiene éxito y otro de escalada.
4. Explique a quién beneficia y perjudica cada política. Entregue una hoja de decisión.

## Error frecuente

Confundir cuota de admisión con capacidad de atención o asumir que un aumento individual mejora siempre el resultado agregado.

## Uso por el tutor

Explicación 20 min, microexplicación 5 min, demostración 25 min y aplicación 50 min. La guía local incluye reflexión y cierre. Las fechas y ponderaciones oficiales las comunica el docente.

## Fuentes

- Manual Vensim: https://vensim.com/documentation/22300.html
- Retardos materiales e informativos: https://www.vensim.com/documentation/mgu09_material_and_information_delays.html
- Escalera de inferencias: https://thesystemsthinker.com/the-ladder-of-inference/
- Intervención sistémica: https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/
