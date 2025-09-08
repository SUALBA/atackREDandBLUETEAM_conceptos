#  Gestión de Ciberincidentes en España

España dispone de un sistema estructurado de **respuesta a ciberincidentes** apoyado en organismos públicos y normativas que buscan garantizar la **continuidad del negocio**, la **protección de infraestructuras críticas** y la **seguridad ciudadana**.

---

## 🏛️ Organismos de Referencia (CSIRT Nacionales)

### 🔐 CCN-CERT
- **Centro Criptológico Nacional del CNI**  
- Competencias:  
  - Sector Público general, autonómico y local.  
  - Sistemas que gestionan **información clasificada**.  
- Rol clave en la protección de la Defensa Nacional y administraciones públicas.

### 🛡️ INCIBE-CERT
- **Instituto Nacional de Ciberseguridad de España**  
- Competencias:  
  - Ciudadanía y sector privado.  
  - Instituciones académicas y de investigación (RedIRIS).  
- Funciones:  
  - Respuesta a incidentes de usuarios y empresas.  
  - Coordinación con CCN-CERT en casos de organismos públicos.  
  - Soporte especializado para Operadores de Servicios Esenciales (OSE).

### 🏗️ CNPIC
- **Centro Nacional de Protección de Infraestructuras y Ciberseguridad**  
- Competencias:  
  - Infraestructuras críticas y operadores estratégicos.  
  - Materialización de la respuesta técnica a través de CSIRT de referencia.  
- Funciones:  
  - Coordinación con operadores estratégicos.  
  - Oficina de Coordinación Cibernética (OCC) para gestión de incidentes según la Ley PIC 8/2011.

### ⚔️ ESP-DEF-CERT
- **Ministerio de Defensa (MDE)**  
- Competencias:  
  - Soporte a Defensa Nacional y operadores de servicios esenciales con incidencia en defensa.  
- Comunicación mediante correo cifrado PGP y enlaces oficiales:  
  - [Portal de Ciberdefensa](http://www.emad.mde.es/CIBERDEFENSA/ESPDEF-CERT/)

---

## 📩 Procedimiento de Reporte de Incidentes

1. **Notificación inicial del afectado**
   - El sujeto afectado envía un **ticket o correo** a su **CSIRT de referencia** (CCN-CERT o INCIBE-CERT).  
   
2. **Clasificación y derivación**
   - El CSIRT determina el organismo competente:  
     - Defensa Nacional → ESP-DEF-CERT  
     - Infraestructura Crítica → CNPIC  
     - RGPD → AEPD  
     - ENS (peligrosidad ALTA/CRÍTICA) → CCN-CERT  
     - Incidentes con reporte obligatorio (RD 12/2018) → Autoridad Nacional correspondiente  

3. **Notificación a la Autoridad Nacional**
   - Ejemplos según normativa:  
     - RGPD → Portal AEPD  
     - BDE → Plantilla .XLS Banco de España  
     - PIC → Plantilla .XLS CNPIC  
     - ENS → Plantilla .DOC CCN-CERT  
     - NIS → Plantilla de notificación de la Autoridad Nacional  

4. **Comunicación con el afectado**
   - La Autoridad Nacional se pone en contacto para recabar información adicional.  

---

## 📧 Canales de Reporte

### 🔹 Reporte a CCN-CERT
- Preferentemente vía aplicación **LUCIA**.  
- Alternativamente mediante correo:  
  - 📧 [incidentes@ccn-cert.cni.es](mailto:incidentes@ccn-cert.cni.es)  
- Se recomienda el uso de **PGP cifrado**.

### 🔹 Reporte a INCIBE-CERT
- Correo: 📧 [incidencias@incibe-cert.es](mailto:incidencias@incibe-cert.es)  
- Para Red Académica y de Investigación: 📧 [iris@incibe-cert.es](mailto:iris@incibe-cert.es)  
- Para Operadores de Servicios Esenciales: 📧 [pic@incibe-cert.es](mailto:pic@incibe-cert.es)  
- Información cifrada mediante PGP.

### 🔹 Reporte a ESP-DEF-CERT
- Canal oficial con el Ministerio de Defensa mediante correo cifrado PGP.  
- Enlace oficial: [ESP-DEF-CERT](http://www.emad.mde.es/CIBERDEFENSA/ESPDEF-CERT/)

---

## ⚠️ Clasificación de Incidentes por Nivel de Peligrosidad

| Nivel | Clasificación | Tipos de Incidente |
|-------|--------------|--------------------|
| 🔴 **Crítico** | APT | Amenazas Persistentes Avanzadas, distribución de malware, C&C Servers |
| 🟠 **Muy Alto** | Intrusión / Disponibilidad | Robo de información, sabotaje, interrupciones graves |
| 🟡 **Alto** | Contenido Abusivo / Código Dañino / Intrusión | Pornografía infantil, servidores infectados, compromisos de cuentas privilegiadas |
| 🟢 **Medio** | Fraude / Intento de Intrusión | Phishing, ataques desconocidos, accesos no autorizados |
| ⚪ **Bajo** | Impacto mínimo | Incidentes sin repercusión significativa |

---

## 📆 Plazos de Notificación

| Nivel de Impacto | Notificación Inicial | Notificación Intermedia | Notificación Final |
|------------------|----------------------|-------------------------|-------------------|
| 🔴 Crítico | Inmediata | 24-48 horas | 20 días |
| 🟠 Muy Alto | Inmediata | 72 horas | 40 días |
| 🟡 Alto | Inmediata | - | - |
| 🟢 Medio | - | - | - |
| ⚪ Bajo | - | - | - |

> 📌 Las notificaciones deben ser **escritas y cifradas** mediante los canales oficiales.

---

## ✅ Conclusión

El modelo español de gestión de ciberincidentes se basa en la **colaboración entre organismos nacionales especializados (CCN-CERT, INCIBE-CERT, ESP-DEF-CERT, CNPIC)** y en un **procedimiento de reporte estructurado** que asegura la correcta **clasificación, priorización y notificación** de incidentes.  
Gracias a este sistema, España puede responder de manera **coordinada, legal y técnica** a ciberamenazas que impactan tanto en el sector público como privado.

> 🔐 *“Un reporte a tiempo puede marcar la diferencia entre un incidente controlado y una crisis nacional.”*


#  Flujo de Reporte de Ciberincidentes en España

## 📌 Esquema General de Actuación

```ascii
┌────────────────────┐
│   Sujeto Afectado  │
│ (empresa, entidad) │
└─────────┬──────────┘
          │ Notificación inicial
          ▼
 ┌────────────────────┐
 │  CSIRT de Referencia│
 │ (CCN-CERT / INCIBE) │
 └─────────┬──────────┘
           │ Clasificación y derivación
           ▼
 ┌─────────────────────────────┐
 │   Autoridad Nacional        │
 │ (CNPIC, AEPD, BDE, ENS, NIS)│
 └─────────┬──────────────────┘
           │ Comunicación y coordinación
           ▼
 ┌────────────────────┐
 │   Comité Táctico   │
 │ (si procede)       │
 └─────────┬──────────┘
           │ Acciones de respuesta
           ▼
 ┌────────────────────┐
 │  Resolución/Informe│
 └────────────────────┘

****
sualba.dev © 2025 - Todos los derechos reservados