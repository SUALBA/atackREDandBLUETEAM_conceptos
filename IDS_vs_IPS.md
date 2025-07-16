# 🛡️ IDS vs IPS – Sistemas de Detección y Prevención de Intrusos

---

## 📘 ¿Qué son?

Los sistemas IDS (Intrusion Detection System) e IPS (Intrusion Prevention System) son tecnologías clave en la defensa de redes. Ambos **monitorean el tráfico**, detectan amenazas, y **se integran con firewalls, switches, routers y herramientas SIEM** para proteger entornos corporativos, industriales y gubernamentales.

---

## 🔍 Diferencias Fundamentales

| Característica         | 🕵️ IDS (Detección)             | 🛡️ IPS (Prevención)               |
|------------------------|-------------------------------|----------------------------------|
| Tipo de acción         | Reactiva (alerta)              | Proactiva (bloquea)              |
| Ubicación en la red    | Paralela al tráfico            | En línea con el tráfico          |
| Latencia               | Nula o mínima                  | Puede añadir latencia            |
| Control de tráfico     | ❌ No lo controla              | ✅ Sí, puede rechazar tráfico     |
| Registro de eventos    | ✅ Sí                          | ✅ Sí                            |
| Uso típico             | Monitoreo y auditoría          | Protección automática            |

---

## 🧪 Métodos de Detección

### 🔹 1. Detección basada en firmas (Signature-based)

- Compara el tráfico con una base de datos de patrones conocidos.
- Muy efectiva para amenazas conocidas.
- **Limitación**: no detecta ataques nuevos (zero-day).

📌 *Ejemplo:*
```plaintext
Detectar un patrón típico de un ataque SQL Injection como:
  SELECT * FROM users WHERE username = 'admin' --'
```

---

### 🔹 2. Detección basada en comportamiento (Anomaly-based)

- Analiza el tráfico y detecta anomalías respecto al comportamiento "normal".
- Detecta ataques nuevos (zero-day).
- **Limitación**: puede generar muchos falsos positivos.

📌 *Ejemplo:*
```plaintext
Un empleado que normalmente trabaja de 9 a 17h, comienza a transferir datos a las 3 a.m. a una IP externa.
```

---

## 🛠️ Herramientas IDS/IPS Reales

| Herramienta      | Tipo       | Descripción breve                                     |
|------------------|------------|--------------------------------------------------------|
| **Snort**        | IDS/IPS    | Muy popular, basado en reglas. Open Source.           |
| **Suricata**     | IDS/IPS    | Multithread, DPI y soporte para múltiples protocolos. |
| **Zeek (Bro)**   | IDS        | IDS con enfoque en análisis y scripting.              |
| **OSSEC**        | IDS (HIDS) | Host-based, monitoriza integridad de archivos.        |
| **Cisco Firepower** | IPS     | Solución empresarial con integración avanzada.        |
| **Wazuh**        | HIDS       | Detección, respuesta y SIEM.                          |

---

## 🧱 Tipos de IDS/IPS

### 🔸 Network-based (NIDS/NIPS)
- Monitorean todo el tráfico de red.
- Se colocan en puntos estratégicos (como switches o gateways).

### 🔸 Host-based (HIDS/HIPS)
- Instalan agentes en dispositivos individuales (servidores, endpoints).
- Protegen contra amenazas locales, cambios sospechosos de archivos, registros del sistema.

---

## ⚙️ Casos de uso habituales

✅ Empresas que monitorean tráfico en tiempo real.  
✅ Entornos industriales (ICS/SCADA) donde la latencia es crítica → IDS preferido.  
✅ Infraestructuras críticas, bancos, y gobiernos usan IPS para protección activa.  
✅ Implementaciones híbridas: IDS + IPS + SIEM para correlación de eventos.

---

## ❗ Excepciones y consideraciones

- 🔄 Un IPS mal configurado puede generar **falsos positivos que bloqueen tráfico legítimo**, afectando la productividad.
- 🔍 Un IDS mal supervisado puede generar **alertas que nadie revisa**, haciendo que el sistema sea inútil.
- 🧩 Muchos sistemas modernos combinan ambas funciones (**IDS/IPS híbridos**) y se integran con soluciones de orquestación de seguridad.

---

## 🎯 Ejemplo de arquitectura moderna

```plaintext
[ Internet ]
     ↓
[ Firewall ]
     ↓
[ IPS en línea ]
     ↓
[ Switch ]
     ├── IDS (recibe copia del tráfico)
     ↓
[ Red interna ]
```

---

## 🧰 Ejemplo práctico con Snort como IPS en Kali Linux

```bash
# Ejecutar Snort en modo prevención (inline)
snort --daq afpacket -Q -c /etc/snort/snort.conf -i eth0:eth1
```

---

## 🧠 Buenas prácticas

- ✍️ Mantén las reglas de detección actualizadas.
- 📊 Usa SIEM para correlacionar alertas de IDS/IPS.
- 🧪 Haz pruebas de penetración (pentest) para validar detección.
- 🧹 Revisa y ajusta falsos positivos regularmente.
- 🧵 Documenta excepciones críticas (como escáneres internos).

---

## 🧾 Conclusión

IDS e IPS son piezas clave de una defensa en profundidad. Usados correctamente, **detectan y neutralizan amenazas antes de causar daño**. Su valor real no está solo en la tecnología, sino en cómo se integran en una estrategia de seguridad bien diseñada.

🔐 **El verdadero poder está en la combinación: visibilidad + respuesta automatizada + análisis humano.**