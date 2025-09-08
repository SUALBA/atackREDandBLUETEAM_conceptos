# Funcionalidades de SIEM (SIM + SEM)

Un **SIEM** (Security Information and Event Management) es el resultado de combinar las capacidades de **SIM** (Security Information Management) y **SEM** (Security Event Management). Esta fusión proporciona una plataforma integral para la gestión de la seguridad de la información.

## 1. Recolección y Consolidación de Logs

### ¿Qué es?
Esta funcionalidad permite recopilar, almacenar y centralizar logs de múltiples fuentes de datos en toda la infraestructura de TI de una organización.

### Características principales:
- **Agregación centralizada**: Recopila logs de servidores, aplicaciones, bases de datos, dispositivos de red, sistemas operativos y dispositivos de seguridad
- **Normalización**: Convierte logs de diferentes formatos en un formato estándar para facilitar el análisis
- **Almacenamiento a largo plazo**: Mantiene históricos de logs para análisis forense y cumplimiento normativo

### Ejemplos:
- Logs de autenticación de Active Directory
- Logs de acceso de servidores web Apache/Nginx
- Logs de firewall mostrando conexiones bloqueadas/permitidas
- Logs de antivirus con detecciones de malware
- Logs de base de datos con intentos de acceso

---

## 2. Detección de Anomalías de Red

### ¿Qué es?
Capacidad para identificar patrones de tráfico de red inusuales o comportamientos que se desvían de la línea base normal de la organización.

### Métodos de detección:
- **Análisis de comportamiento**: Establece patrones normales de tráfico y detecta desviaciones
- **Detección basada en firmas**: Busca patrones conocidos de ataques
- **Machine Learning**: Utiliza algoritmos para identificar anomalías complejas

### Ejemplos:
- Detección de tráfico inusual hacia ubicaciones geográficas sospechosas
- Identificación de comunicaciones con dominios maliciosos conocidos
- Detección de transferencias de datos masivas fuera del horario laboral
- Identificación de patrones de escaneo de puertos
- Detección de protocolos no autorizados en la red

---

## 3. Análisis del Comportamiento de Usuarios

### ¿Qué es?
Monitoriza y analiza las actividades de los usuarios para detectar comportamientos anómalos que puedan indicar amenazas internas o cuentas comprometidas.

### Técnicas utilizadas:
- **UEBA** (User and Entity Behavior Analytics): Análisis avanzado de comportamiento
- **Perfilado de usuarios**: Creación de patrones de comportamiento normal
- **Análisis de privilegios**: Monitorización del uso de permisos elevados

### Ejemplos:
- Usuario accediendo a sistemas fuera de su horario habitual
- Empleado descargando grandes cantidades de datos confidenciales
- Cuenta de usuario iniciando sesión desde múltiples ubicaciones geográficas simultáneamente
- Uso inusual de comandos administrativos por parte de usuarios regulares
- Acceso a recursos que normalmente no utiliza un usuario específico

---

## 4. Análisis y Topología de Red

### ¿Qué es?
Proporciona visibilidad completa de la infraestructura de red, incluyendo dispositivos, conexiones y flujos de datos para identificar vulnerabilidades y puntos de control.

### Capacidades:
- **Mapeo de red**: Visualización de la topología completa de la red
- **Análisis de flujo**: Seguimiento de comunicaciones entre dispositivos
- **Segmentación de red**: Identificación de zonas de seguridad y DMZ

### Ejemplos:
- Identificación de dispositivos no autorizados conectados a la red
- Detección de comunicaciones laterales sospechosas entre servidores
- Análisis de rutas de red para identificar puntos de falla
- Monitorización de tráfico entre diferentes segmentos de red
- Identificación de dispositivos que actúan como puntos de pivote

---

## 5. Configuración de Dispositivos

### ¿Qué es?
Gestiona y monitoriza las configuraciones de seguridad de dispositivos de red y sistemas para asegurar el cumplimiento de políticas de seguridad.

### Funcionalidades:
- **Gestión de configuraciones**: Control centralizado de configuraciones de seguridad
- **Detección de cambios**: Alerta sobre modificaciones no autorizadas
- **Cumplimiento normativo**: Verificación de adherencia a estándares de seguridad

### Ejemplos:
- Detección de cambios en reglas de firewall sin autorización
- Monitorización de configuraciones de routers y switches
- Verificación de configuraciones de sistemas operativos según baseline de seguridad
- Alertas por deshabilitación de logs de auditoría
- Control de configuraciones de dispositivos IoT

---

## 6. Priorización de Vulnerabilidades

### ¿Qué es?
Evalúa y clasifica las vulnerabilidades detectadas según su criticidad, impacto potencial y contexto organizacional para optimizar los esfuerzos de remediación.

### Criterios de priorización:
- **Severidad técnica**: Puntuación CVSS de la vulnerabilidad
- **Contexto empresarial**: Importancia del activo afectado
- **Amenaza activa**: Existencia de exploits conocidos
- **Exposición**: Accesibilidad del sistema vulnerable

### Ejemplos:
- Vulnerabilidad crítica en servidor web público vs. servidor interno
- Priorización de parches para sistemas que manejan datos sensibles
- Vulnerabilidades con exploits públicos disponibles
- Sistemas sin segmentación de red adecuada
- Activos críticos para la continuidad del negocio

---

## 7. Análisis de Fallos y Simulación de Exploits

### ¿Qué es?
Realiza pruebas controladas de seguridad para identificar debilidades en los sistemas y validar la efectividad de las medidas de seguridad implementadas.

### Tipos de análisis:
- **Penetration Testing automatizado**: Pruebas de intrusión sistemáticas
- **Simulación de ataques**: Recreación de técnicas de atacantes reales
- **Análisis de superficie de ataque**: Evaluación de puntos de entrada potenciales

### Ejemplos:
- Simulación de ataques de phishing para evaluar la conciencia de seguridad
- Pruebas de escalación de privilegios en sistemas internos
- Simulación de ataques de ransomware para validar backups
- Pruebas de inyección SQL en aplicaciones web
- Evaluación de resistencia a ataques de ingeniería social

---

## 8. Correlación de Eventos (Event Correlation)

### ¿Qué es?
La **correlación de eventos** es el proceso de analizar eventos de seguridad aparentemente no relacionados para identificar patrones, conexiones y relaciones que puedan indicar ataques complejos, campañas de amenazas avanzadas o incidentes de seguridad coordinados.

### Tipos de Correlación en SIEM:

#### **Real-time Correlation** (Correlación en Tiempo Real)
- **Definición**: Análisis instantáneo de eventos mientras ocurren
- **Aplicación**: Detección inmediata de amenazas activas
- **Ejemplo**: Detección de múltiples intentos de login fallidos seguidos de acceso exitoso desde diferentes IPs

#### **Cross-correlation** (Correlación Cruzada)
- **Definición**: Análisis de eventos entre diferentes fuentes de datos y sistemas
- **Aplicación**: Identificación de ataques que abarcan múltiples vectores
- **Ejemplo**: Correlación entre alertas de firewall, logs de DNS y actividad de endpoints

#### **Pattern Correlation** (Correlación de Patrones)
- **Definición**: Identificación de secuencias específicas de eventos que indican amenazas conocidas
- **Aplicación**: Detección de TTPs (Tactics, Techniques, Procedures) de atacantes
- **Ejemplo**: Patrón de reconocimiento → explotación → escalación de privilegios → exfiltración

#### **Temporal Correlation** (Correlación Temporal)
- **Definición**: Análisis de eventos basado en ventanas de tiempo específicas
- **Aplicación**: Identificación de actividades sospechosas dentro de marcos temporales
- **Ejemplo**: Múltiples eventos de seguridad ocurriendo en una ventana de 5 minutos

### Técnicas Avanzadas de Correlación:

#### **Statistical Correlation**
- **Análisis de frecuencia**: Identificación de eventos que ocurren con mayor frecuencia de lo normal
- **Análisis de desviación**: Detección de comportamientos que se alejan de la línea base
- **Correlación de Pearson**: Medición de relaciones lineales entre variables

#### **Machine Learning Correlation**
- **Clustering**: Agrupación de eventos similares para identificar patrones
- **Anomaly Detection**: Identificación de eventos que no se ajustan a patrones normales
- **Behavioral Analytics**: Análisis del comportamiento de usuarios y entidades

#### **Rule-based Correlation**
- **Reglas simples**: IF-THEN básicas para correlaciones directas
- **Reglas complejas**: Lógica booleana avanzada con múltiples condiciones
- **Reglas adaptativas**: Reglas que se ajustan según el contexto organizacional

### Ejemplos Detallados por Tipo de Ataque:

#### **Ataque de Phishing Correlacionado**
1. **Email suspicious** → Usuario recibe email con link malicioso
2. **Web access** → Usuario accede a sitio de phishing
3. **Credential capture** → Captura de credenciales en sitio falso
4. **Login anomaly** → Intento de login desde IP sospechosa
5. **Data access** → Acceso inusual a datos sensibles

#### **Ataque APT (Advanced Persistent Threat)**
1. **Initial compromise** → Malware en endpoint via email
2. **C&C communication** → Comunicación con servidor de comando y control
3. **Lateral movement** → Movimiento lateral en la red
4. **Privilege escalation** → Escalación de privilegios
5. **Data exfiltration** → Exfiltración de datos sensibles

#### **Ataque DDoS Correlacionado**
1. **Network scanning** → Escaneo de puertos y servicios
2. **Botnet coordination** → Coordinación de bots atacantes
3. **Traffic spike** → Aumento súbito del tráfico
4. **Service degradation** → Degradación del rendimiento
5. **Application failure** → Falla de aplicaciones críticas

### Métricas de Correlación:

#### **Confidence Score** (Puntuación de Confianza)
- **Alto (90-100%)**: Correlación muy probable, requiere acción inmediata
- **Medio (70-89%)**: Correlación probable, requiere investigación
- **Bajo (50-69%)**: Correlación posible, monitoreo continuo

#### **Severity Level** (Nivel de Severidad)
- **Crítico**: Amenaza activa confirmada
- **Alto**: Indicadores fuertes de compromiso
- **Medio**: Actividad sospechosa que requiere análisis
- **Bajo**: Anomalías menores o falsos positivos potenciales

### Desafíos en la Correlación:

#### **Volume Challenge** (Desafío del Volumen)
- **Problema**: Procesamiento de millones de eventos por segundo
- **Solución**: Filtrado inteligente y priorización automática

#### **Velocity Challenge** (Desafío de Velocidad)
- **Problema**: Necesidad de análisis en tiempo real
- **Solución**: Algoritmos optimizados y procesamiento distribuido

#### **Variety Challenge** (Desafío de Variedad)
- **Problema**: Múltiples formatos y fuentes de datos
- **Solución**: Normalización y parsing avanzado

#### **False Positive Reduction**
- **Problema**: Alto número de alertas falsas
- **Solución**: Machine learning y refinamiento continuo de reglas

### Herramientas de Correlación:

#### **Correlation Engine**
- **CEP (Complex Event Processing)**: Procesamiento de eventos complejos
- **Stream Processing**: Análisis de flujos de datos en tiempo real
- **Graph Analytics**: Análisis de relaciones mediante grafos

#### **Correlation Rules**
```
EJEMPLO DE REGLA:
IF (failed_login_attempts > 5 AND time_window < 60_seconds AND source_ip = external)
AND (port_scan_detected = true AND target = same_network)
THEN alert_level = HIGH AND incident_type = "Brute Force + Reconnaissance"
```

### Casos de Uso Específicos:

#### **Insider Threat Detection**
- Correlación de acceso a datos + horarios inusuales + transferencias grandes
- Análisis de comportamiento vs. patrón histórico del usuario
- Detección de uso de privilegios elevados fuera de funciones normales

#### **Malware Campaign Detection**
- Correlación de indicators of compromise (IoCs) entre múltiples endpoints
- Análisis de comunicaciones con dominios maliciosos
- Detección de patrones de propagación lateral

#### **Compliance Monitoring**
- Correlación de eventos para cumplimiento PCI DSS, SOX, GDPR
- Análisis de acceso a datos regulados
- Detección de violaciones de políticas de seguridad

### Beneficios de la Correlación Efectiva:

1. **Reducción de False Positives**: Menor número de alertas falsas
2. **Faster Response Time**: Respuesta más rápida a amenazas reales
3. **Comprehensive Threat View**: Visión completa de amenazas complejas
4. **Automated Incident Response**: Respuesta automatizada basada en correlaciones
5. **Improved Security Posture**: Mejor postura de seguridad organizacional

---

## 9. Gestión de Incidentes/Alertas de Seguridad

### ¿Qué es?
Proporciona un flujo de trabajo estructurado para manejar incidentes de seguridad desde la detección inicial hasta la resolución y lecciones aprendidas.

### Componentes del proceso:
- **Detección y clasificación**: Identificación y categorización de incidentes
- **Investigación**: Análisis detallado del incidente
- **Contención**: Medidas para limitar el impacto
- **Remediación**: Acciones para resolver el incidente
- **Documentación**: Registro completo del proceso

### Ejemplos:
- Gestión de incidentes de malware con workflow automatizado
- Respuesta a brechas de datos con notificaciones automáticas
- Manejo de ataques DDoS con escalamiento automático
- Gestión de incidentes de phishing con análisis forense
- Respuesta a amenazas internas con investigación detallada

---

## 10. Generación de Informes

### ¿Qué es?
Produce informes comprensivos sobre el estado de seguridad, tendencias, cumplimiento normativo y métricas de rendimiento para diferentes audiencias organizacionales.

### Tipos de informes:
- **Ejecutivos**: Resúmenes de alto nivel con métricas de negocio
- **Técnicos**: Informes detallados para equipos de seguridad
- **Cumplimiento**: Informes específicos para auditorías y regulaciones
- **Operacionales**: Métricas de rendimiento y SLA

### Ejemplos:
- Informes de cumplimiento PCI DSS para industria de pagos
- Dashboards ejecutivos con KPIs de seguridad
- Informes técnicos sobre tendencias de amenazas
- Reportes de incidentes para seguros cibernéticos
- Análisis de efectividad de controles de seguridad

---

## Conclusión

La combinación de estas funcionalidades en un SIEM proporciona una plataforma integral para la gestión proactiva de la seguridad, permitiendo a las organizaciones detectar, analizar y responder a amenazas de manera más efectiva y eficiente.

***
© 2025 [sualba.dev] -Todos los derechos reservados
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.