# 📌 Elementos y conceptos: SIEM (Security Information and Event Management)

## 🛡️ ¿Qué es un SIEM?

Un SIEM es un sistema de seguridad que permite a las empresas **detectar amenazas rápidamente**, **interpretar registros en tiempo real** y **responder ante incidentes** en sus sistemas informáticos.

## ⚙️ ¿Cómo funciona un SIEM?

1. **Recopila eventos** desde múltiples sistemas y dispositivos.
2. **Correlaciona esos eventos** para detectar patrones o anomalías.
3. **Genera alertas** que permiten actuar de inmediato ante amenazas.

## 🧩 Fuentes de información típicas que analiza un SIEM

| Fuente | Ejemplo de evento detectado |
|--------|-----------------------------|
| 🔐 Dispositivos de seguridad | Intentos de acceso masivo desde una IP extranjera (ataque de fuerza bruta) |
| 💻 Servidores & Hosts | Inicios de sesión sospechosos a horas inusuales |
| 🌐 Red & Actividad virtual | Grandes volúmenes de datos saliendo a una IP desconocida |
| 📦 Base de datos | Consultas masivas a registros sensibles por parte de un usuario común |
| ⚙️ Aplicaciones | Errores constantes de autenticación que indican intentos maliciosos |
| 🛠️ Configuración | Cambios no autorizados en archivos de configuración críticos |
| 🕳️ Vulnerabilidades | Software desactualizado con vulnerabilidades conocidas (CVE) |
| 👤 Actividad de usuarios | Comportamiento atípico de un usuario fuera de su perfil de trabajo |

---

## ⭐ Características del SIEM

- ✅ Distingue amenazas reales de falsos positivos.
- 🎯 Monitoriza amenazas desde una única plataforma centralizada.
- 🧠 Redirige las alertas al personal cualificado.
- 📘 Documenta automáticamente la detección y actuación.
- ⚖️ Asegura el cumplimiento de normativas (RGPD, ISO 27001...).

---

## 🔁 ¿Qué hace internamente?

- **Correlación de eventos:**  
  Une diferentes señales para ver si forman parte de un ataque mayor.

- **Detección de anomalías:**  
  Compara la actividad con lo habitual y alerta si algo es raro.

- **Generación de alertas:**  
  Lanza una notificación práctica y precisa para que el equipo de seguridad actúe.

---

## 🧪 Mini caso práctico: Actúas como analista de seguridad

### 🕵️ Contexto

Eres un analista del Blue Team. El SIEM lanza una alerta con el siguiente resumen:

> 🚨 **Actividad anómala detectada en el servidor de finanzas**  
> - Usuario: jlopez  
> - Hora: 02:37 AM  
> - Acceso remoto desde IP no registrada (192.168.88.200)  
> - Extracción masiva de datos de clientes (2 GB en 10 minutos)  
> - Permisos de archivos críticos modificados

### 🧠 Paso a paso de tu intervención

1. **Corroboras la información:**  
   Revisas los logs de acceso, confirmas la hora y la IP no habitual.

2. **Detectas comportamiento anómalo:**  
   El usuario “jlopez” normalmente trabaja de 9:00 a 17:00. Nunca ha accedido de madrugada ni modificado archivos.

3. **Aislas el servidor:**  
   Para prevenir filtraciones mayores, pones el servidor en cuarentena de red.

4. **Contactas con el usuario:**  
   Confirmas que jlopez estaba dormido y no ha iniciado sesión. Es probable que su cuenta haya sido comprometida.

5. **Generas un informe forense preliminar:**  
   Incluyes logs del SIEM, comportamiento detectado, IP, hora, archivos accedidos.

6. **Escalas el incidente:**  
   Se considera una posible intrusión interna o externa. Lo reportas al CISO y al equipo de respuesta a incidentes.

7. **Revisas configuraciones del SIEM:**  
   Ajustas las reglas de detección para que la próxima vez esta combinación dispare una alerta aún más temprana.

---

## 🎯 Resultado final

El SIEM te permitió:

- Detectar un comportamiento **fuera de lo normal**.
- Actuar en **tiempo real**.
- Proteger datos críticos.
- Iniciar una investigación **documentada y estructurada**.

---

## 🧠 Conclusión

Un SIEM es **esencial en cualquier estrategia de ciberseguridad moderna**. Permite no solo detectar amenazas, sino también responder a tiempo, proteger activos críticos y cumplir con normativas legales y de seguridad.

> **🔐 SIEM = Visibilidad + Inteligencia + Respuesta inmediata**

***
sualba.dev © 2025 Todos los derechos reservados