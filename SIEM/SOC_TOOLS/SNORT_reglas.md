
# 🛡️ Guía para Crear Reglas Snort Personalizadas

Crear reglas en Snort te permite detectar patrones específicos de tráfico que podrían ser maliciosos o inusuales. Esta guía te orienta paso a paso para que puedas escribir tus propias reglas con confianza.

---

## 🧱 Estructura básica de una regla Snort

```snort
alert <protocolo> <IP_origen> <puerto_origen> -> <IP_destino> <puerto_destino> (opciones)
```

### Ejemplo:
```snort
alert tcp any any -> $HOME_NET 22 (msg:"SSH Connection Attempt"; sid:10000001;)
```

---

## 🔍 Campos clave

| Campo       | Descripción |
|-------------|-------------|
| `alert`     | Acción que tomará Snort: puede ser `alert`, `log`, `pass`, `drop`, etc. |
| `tcp/udp/icmp` | Protocolo a monitorear |
| `any`       | Cualquier IP o puerto (puedes poner IPs específicas) |
| `->`        | Dirección del tráfico |
| `msg`       | Mensaje que aparece cuando se activa la regla |
| `sid`       | Identificador único para cada regla |
| `rev`       | Revisión de la regla |
| `content`   | Texto específico que debe aparecer en el paquete |
| `flags`     | Flags TCP para detectar escaneos o conexiones |
| `flow`      | Sentido del tráfico (`to_server`, `from_server`, etc.) |
| `classtype` | Clasificación del ataque (por ejemplo: `attempted-recon`, `trojan-activity`) |
| `threshold` | Umbral para limitar la frecuencia de alertas |

---

## ✨ Tips para crear tus propias reglas

### 1. **Analiza el tráfico con Wireshark o tcpdump**
- Observa patrones sospechosos
- Anota puertos, protocolos, cadenas de texto y flags

### 2. **Empieza por lo simple**
- Crea reglas que detecten puertos o palabras clave
```snort
alert tcp any any -> $HOME_NET 21 (content:"USER anonymous"; msg:"FTP anonymous login"; sid:10000002;)
```

### 3. **Usa `content` e `http_uri` para tráfico web**
```snort
alert tcp any any -> $HOME_NET $HTTP_PORTS (content:"/login"; http_uri; msg:"Possible login page access"; sid:10000003;)
```

### 4. **Detecta escaneos con flags TCP**
```snort
alert tcp any any -> $HOME_NET any (flags:FPU; msg:"XMAS Scan Detected"; sid:10000004;)
```

### 5. **Combina con `threshold` para evitar spam de alertas**
```snort
threshold:type threshold, track by_src, count 5, seconds 60;
```

---

## 🧠 Patrones útiles para detectar ataques

| Técnica              | Patrón clave |
|----------------------|--------------|
| Escaneo SYN          | `flags:S;` |
| Escaneo NULL         | `flags:0;` |
| Escaneo XMAS         | `flags:FPU;` |
| SQLi con sqlmap      | `User-Agent: sqlmap` (en header HTTP) |
| Acceso anónimo FTP   | `content:"USER anonymous"` |
| Descarga de malware  | `content:".exe"` o `content:"/malware"` |

---

## 🛑 Consejos finales

- ✅ Usa `sid` únicos empezando desde 1000000 para tus reglas personalizadas
- ✅ Comenta tus reglas con `#` para pruebas
- ✅ Prueba una por una para evitar conflictos
- ✅ Guarda tus reglas en `local.rules` y asegúrate de que esté incluido en `snort.conf`

---

## 📚 Recursos útiles

- [Documentación oficial de Snort](https://www.snort.org/documents)
- [Snort Rules Cheat Sheet (PDF)](https://www.snort.org/assets/158/snort_rules_cheat_sheet.pdf)
- [Wireshark](https://www.wireshark.org/) para inspeccionar tráfico real

---

¡Con práctica y análisis, podrás crear reglas poderosas que protejan tu red como toda una experta! 🚀






# 📘 ejemplos de Reglas Snort - 

Este informe presenta varias  reglas configuradas (activas y comentadas), explicadas una por una de manera clara y profesional.

---

## 🔹 Regla 1

```snort
alert icmp any any -> any any (msg:"ICMP Traffic Detected"; sid:10000001; metadata:policy security-ips alert;)
```
🧠 **Explicación:** Detecta cualquier tráfico ICMP en la red (por ejemplo, ping). Es útil para controlar actividad de reconocimiento o test de conectividad.

---

## 🔹 Regla 2

```snort
alert tcp any any -> $HOME_NET any (msg:"Nmap SYN scan"; flags:S; threshold:type threshold, track by_dst, count 2, seconds 5; sid:10000002; rev:1;)
```
🧠 **Explicación:** Detecta escaneos SYN típicos de herramientas como Nmap. Dispara la alerta si se reciben múltiples paquetes SYN a un destino en poco tiempo.

---

## 🔹 Regla 3

```snort
alert tcp any any -> $HOME_NET any (msg:"Nmap XMAS Tree Scan"; flags:FPU; sid:10000003; rev:1;)
```
🧠 **Explicación:** Detecta escaneos tipo Xmas Tree, que activan las flags FIN, PUSH y URG en los paquetes TCP para evadir detección.

---

## 🔹 Regla 4

```snort
alert tcp any any -> $HOME_NET 21 (msg:"Anonymous FTP access"; content:"USER anonymous"; classtype:suspicious-login; sid:10000004; rev:1;)
```
🧠 **Explicación:** Detecta intentos de acceso FTP con el usuario 'anonymous', lo que puede indicar una mala configuración del servidor o un intento de abuso.

---

## 🔹 Regla 5

```snort
alert tcp any any -> $HOME_NET 22 (msg:"SSH Connection Attempt"; flow:to_server; flags:S; threshold:type threshold, track by_src, count 1, seconds 60; classtype:attempted-dos; sid:10000005; rev:4; resp:rst_all;)
```
🧠 **Explicación:** Genera una alerta si se detecta una conexión SSH (flag SYN) hacia un servidor, con respuesta RST para cortar la conexión. Detecta ataques DoS o fuerza bruta SSH.

---

## 🔹 Regla 6

```snort
alert tcp any any -> $HOME_NET $HTTP_PORTS (msg:"Test.html Accessed"; sid:10000006; content:"/test.html"; http_uri;)
```
🧠 **Explicación:** Detecta cuando un cliente accede a '/test.html' por HTTP. Útil para identificar pruebas o backdoors.

---

## 🔹 Regla 7

```snort
alert tcp any any -> $HOME_NET 22 (msg:"SSH Recon Attempt"; flow:to_server; flags:S; threshold:type threshold, track by_src, count 5, seconds 60; classtype:attempted-recon; sid:10000007;)
```
🧠 **Explicación:** Detecta varios intentos SYN al puerto 22 en 60 segundos. Puede ser un escaneo o intento de fuerza bruta SSH.

---

## 🔹 Regla 8

```snort
alert tcp any any -> $HOME_NET 21 (msg:"Anonymous FTP access v2"; content:"USER anonymous"; classtype:suspicious-login; sid:10000008; rev:1;)
```
🧠 **Explicación:** Versión duplicada para acceso FTP anónimo. Se recomienda evitar duplicación de SID o consolidar reglas similares.

---

## 🔹 Regla 9

```snort
alert tcp any any -> $HOME_NET $HTTP_PORTS (msg:"Index.html Accessed"; sid:10000009; content:"/index.html"; http_uri;)
```
🧠 **Explicación:** Genera alerta cuando se accede a '/index.html'. Útil para trazar navegación a recursos clave en servidores web internos.

---

## 🔹 Regla 10

```snort
alert udp any any -> $HOME_NET 161 (msg:"SNMP request detected"; content:"public"; sid:10000010;)
```
🧠 **Explicación:** Detecta solicitudes SNMP con la comunidad 'public'. Puede indicar barrido SNMP o configuraciones inseguras.

---

## 🔹 Regla 11

```snort
alert tcp $EXTERNAL_NET any -> $HOME_NET 3306 (msg:"MySQL Access Attempt"; sid:10000011; flow:to_server; flags:S;)
```
🧠 **Explicación:** Detecta intentos de acceso externo a un servidor MySQL (puerto 3306). Puede ser un ataque de reconocimiento o explotación.

---

## 🔹 Regla 12

```snort
alert tcp $EXTERNAL_NET any -> $HOME_NET 3389 (msg:"RDP Connection Attempt"; sid:10000012; flow:to_server; flags:S;)
```
🧠 **Explicación:** Detecta intentos de conexión RDP desde fuera hacia un host interno. Es común en ataques de fuerza bruta a escritorios remotos.

---

## 🔹 Regla 13

```snort
alert tcp any any -> $HOME_NET 80 (msg:"Suspicious HTTP User-Agent"; content:"User-Agent: sqlmap"; sid:10000013; http_header;)
```
🧠 **Explicación:** Detecta uso de la herramienta sqlmap enviando peticiones HTTP con su 'User-Agent'. Indica intento de inyección SQL.

---

## 🔹 Regla 14

```snort
alert tcp any any -> $HOME_NET 25 (msg:"SMTP Connection Detected"; content:"EHLO"; sid:10000014;)
```
🧠 **Explicación:** Detecta conexiones al puerto 25 (SMTP) con comando 'EHLO'. Útil para monitorear servidores de correo saliente en uso o potencial abuso para spam.

---
