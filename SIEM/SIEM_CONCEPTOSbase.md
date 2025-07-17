# 🛡️ SIEM: Security Information and Event Management

## 1. Introducción

El crecimiento exponencial de los ciberataques y la complejidad de los entornos digitales actuales exige a las organizaciones adoptar soluciones capaces de proporcionar **visibilidad, trazabilidad y capacidad de respuesta** en materia de seguridad. Una de las herramientas fundamentales en este contexto son los sistemas **SIEM** (Security Information and Event Management), los cuales centralizan y correlacionan eventos de seguridad en tiempo real, permitiendo tanto su análisis inmediato como histórico.

---

## 2. ¿Qué es un SIEM?

Un SIEM es una plataforma que combina dos funcionalidades principales:

- **SIM (Security Information Management)**: gestión de información de seguridad histórica.
- **SEM (Security Event Management)**: gestión en tiempo real de eventos de seguridad.

Su objetivo es **recopilar, almacenar, correlacionar, analizar y visualizar** los datos generados por los sistemas y dispositivos de una red con el fin de:

- Identificar comportamientos anómalos.
- Detectar intrusiones o actividades maliciosas.
- Cumplir con regulaciones legales.
- Apoyar a equipos de respuesta ante incidentes (Blue Team / SOC).

---

## 3. Arquitectura general de un SIEM

```mermaid
graph TD
  A[Dispositivos de red / hosts / servidores] --> B[Agentes de recolección]
  B --> C[Normalización de logs]
  C --> D[Motor de correlación]
  D --> E[Base de datos de eventos]
  E --> F[Dashboard y análisis visual]
  D --> G[Generador de alertas]
  G --> H[Respuesta automatizada o manual]
