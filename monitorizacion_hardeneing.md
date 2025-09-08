# 🛡️ Monitorización y Hardening - Guía de Estudio

## 🔐 Introducción a la protección de activos

La protección de activos consiste en aplicar medidas de seguridad para garantizar la integridad, disponibilidad y confidencialidad de los sistemas, redes y datos ante amenazas internas o externas. Las dos estrategias clave son:

- **Monitorización**: observar el comportamiento y el estado del sistema en tiempo real.
- **Hardening**: reducir la superficie de ataque mediante configuraciones seguras.

---

## 📊 Monitorización

### ¿Qué es?

La **monitorización** es la supervisión continua del estado, rendimiento y seguridad de sistemas y servicios. Permite detectar fallos, anomalías y amenazas antes de que generen un impacto grave.

### Tipos

- **Activa**: envía peticiones o señales para comprobar el estado de un sistema.
- **Pasiva**: analiza registros y eventos ya producidos.
- **Centralizada**: datos recopilados desde varios dispositivos hacia un solo servidor.
- **Distribuida**: cada nodo realiza parte de la monitorización.

### Pasos básicos

1. Identificación de recursos críticos.
2. Definición de métricas y umbrales.
3. Instalación de herramientas de monitorización.
4. Recolección y análisis de datos.
5. Configuración de alertas y acciones automáticas.

### Herramientas comunes

- **Nagios**: robusto y muy configurable, ideal para infraestructura completa.
- **Prometheus**: orientado a métricas modernas y cloud-native, se combina con Grafana.

---

## 🧰 Comandos útiles en Linux para monitorización

| Comando     | Función principal                                           | Ejemplo             | ¿Para qué sirve?                                      |
|-------------|-------------------------------------------------------------|---------------------|--------------------------------------------------------|
| `top`       | Muestra uso de CPU, RAM, procesos activos.                  | `top`               | Ver procesos que consumen más recursos.               |
| `df`        | Muestra uso del disco.                                      | `df -h`             | Revisar espacio libre en particiones.                 |
| `tcpdump`   | Captura paquetes de red.                                    | `tcpdump -i eth0`   | Analizar tráfico y detectar conexiones sospechosas.   |
| `netstat`   | Muestra conexiones y puertos abiertos.                      | `netstat -tuln`     | Ver servicios activos y puertos escuchando.           |
| `htop`      | Interfaz mejorada de `top`.                                 | `htop`              | Monitorización más visual e interactiva.              |
| `iftop`     | Monitoriza ancho de banda por IP.                           | `iftop -i eth0`     | Ver qué IP consume más ancho de banda.                |
| `iptraf`    | Monitor de tráfico de red con interfaz de texto.            | `iptraf`            | Ver tráfico por protocolo y puerto.                   |
| `w`         | Muestra usuarios conectados y su actividad.                 | `w`                 | Detectar accesos sospechosos o usuarios conectados.   |

---

## 📌 ¿Qué recursos es interesante monitorizar?

| Categoría      | Qué se monitoriza                         | ¿Por qué es importante?                                |
|----------------|--------------------------------------------|---------------------------------------------------------|
| **CPU**        | Uso del procesador                         | Evitar sobrecarga o detectar malware.                   |
| **Memoria**    | RAM libre, uso de swap                     | Prevenir cuelgues por falta de memoria.                |
| **Disco**      | Espacio libre, salud de discos             | Evitar pérdida de datos y fallos por saturación.       |
| **Red**        | Latencia, tráfico de red                   | Detectar cuellos de botella o ataques DDoS.            |
| **Procesos**   | Número, estado, consumo                    | Supervisar procesos anómalos o colgados.               |
| **Usuarios**   | Usuarios conectados                        | Identificar accesos sospechosos o no autorizados.      |
| **Servicios**  | Estado de servicios clave (SSH, HTTP...)   | Asegurar disponibilidad de servicios esenciales.       |
| **Logs**       | Registros del sistema                      | Detectar errores o intentos de intrusión.              |
| **Temperatura**| Sensores de hardware                       | Prevenir daños por sobrecalentamiento.                 |
| **Backups**    | Estado de copias de seguridad              | Confirmar que hay respaldo funcional ante fallos.      |

---

## 🛡️ Hardening (Endurecimiento de sistemas)

### ¿Qué es?

El **hardening** consiste en aplicar configuraciones seguras a un sistema, desactivar servicios innecesarios y reforzar la seguridad para minimizar posibles puntos de ataque.

### Tipos

#### 🔧 Manual

- Revisar servicios y puertos abiertos.
- Desactivar funciones no utilizadas.
- Establecer contraseñas seguras y políticas de bloqueo.
- Configurar firewalls (iptables, ufw).
- Controlar permisos y usuarios.

#### ⚙️ Automático

Uso de herramientas que automatizan la revisión y aplicación de buenas prácticas:
- **Lynis**
- **OpenSCAP**
- **Ansible Roles de Hardening**
- **CIS-CAT**
- **Microsoft Security Compliance Toolkit**

### Ejemplos de acciones de hardening

- Cambiar puertos por defecto.
- Deshabilitar SSH root login.
- Activar autenticación multifactor.
- Cifrado de discos y datos sensibles.
- Monitorizar cambios en archivos críticos (ej. `/etc/passwd`).

---

## 🎯 Consejos finales para el examen

- Aprende al menos **3 comandos por categoría** (procesos, red, disco...).
- Recuerda qué herramientas son **activas vs pasivas**.
- Entiende bien qué se considera **recurso crítico** y cómo protegerlo.
- Practica con `htop`, `df`, `netstat`, `tcpdump`, `w` en una máquina Linux.
- Familiarízate con **Nagios** o **Prometheus** (aunque sea visualmente).
- Estudia la lógica del hardening: **menos servicios = menos riesgos**.

---

> ¡Ánimo! Con esta guía tienes una base sólida para monitorizar, proteger y endurecer sistemas como un profesional.

***
>© 2025 [sualba.dev] Todos los derechos reservados
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.