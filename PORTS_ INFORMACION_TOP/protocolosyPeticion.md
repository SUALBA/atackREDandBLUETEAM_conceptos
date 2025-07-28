# 🔍 Banner Grabbing y Peticiones de Protocolo en Ciberseguridad

## 🧠 ¿Qué significa "petición típica del protocolo"?
Cuando un escáner como **nmap**, un pentester o una herramienta de hacking quiere identificar un servicio en un puerto abierto, envía una **solicitud estándar** que un cliente legítimo usaría para iniciar comunicación.

```mermaid
graph TD
    A[Escáner] -->|Envía petición típica| B[Servidor]
    B -->|Responde con banner| A
    B --> C[Identificación de servicio]
    C --> D[Software]
    C --> E[Versión]
    C --> F[Sistema Operativo]
📬 Ejemplos por Protocolo
🌐 HTTP (Puertos 80, 8080...)
Petición típica:

http
GET / HTTP/1.1
Host: 192.168.1.10
Respuesta del servidor:

http
HTTP/1.1 200 OK
Server: Apache/2.4.18 (Ubuntu)
Content-Type: text/html
✅ Identificación: Servidor web Apache versión 2.4.18 en Ubuntu

🔒 SSH (Puerto 22)
Banner automático:

text
SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8
✅ Identificación: Protocolo SSH 2.0, OpenSSH versión 7.2p2

📤 FTP (Puerto 21)
Respuesta de conexión:

text
220 (vsFTPd 2.3.4)
✅ Identificación: vsFTPd versión 2.3.4

✉️ SMTP (Puerto 25)
Petición típica:

text
EHLO dominio.local
Respuesta:

text
250-smtp.victim.com
250-SIZE 35882577
250-STARTTLS
250-AUTH LOGIN PLAIN
250 Postfix
✅ Identificación: Servidor Postfix con soporte para TLS y autenticación

🛠️ Herramientas y Técnicas de Banner Grabbing
⚙️ ¿Qué hace Nmap?
Comando:

bash
sudo nmap -sV -O 192.168.1.1
Proceso:

Detecta puertos abiertos

Envía peticiones específicas por protocolo

Analiza respuestas para identificar servicios

Realiza fingerprinting del SO

🧪 Ejemplo con Netcat
bash
nc 192.168.1.10 80
http
GET / HTTP/1.1
Host: 192.168.1.10
Salida:

http
HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Thu, 24 Jul 2025 14:30:00 GMT
Content-Type: text/html
🔎 Otras Herramientas
Herramienta	Uso	Ejemplo
curl	curl -I http://192.168.1.10	Muestra cabeceras HTTP
telnet	telnet 192.168.1.10 21	Interacción con FTP/SMTP
whatweb	whatweb 192.168.1.10	Detección de tecnologías web
ncat	ncat -C 192.168.1.10 25	Conexión persistente con CRLF
📌 Importancia en Ciberseguridad
🔥 Riesgos Principales
Exposición de vulnerabilidades

Identificación de versiones con CVEs conocidos

Ejemplo: OpenSSH 7.2p2 → CVE-2018-15473

Revelación excesiva de información

diff
- Server: Apache/2.4.18 (Ubuntu) mod_ssl/2.4.18 OpenSSL/1.0.2g
+ Server: Apache-Prod
Facilita ataques dirigidos

Desarrollo de exploits específicos

Búsqueda en bases de datos de vulnerabilidades

🛡️ Técnicas de Mitigación
Diagram
Code








Configuraciones recomendadas:

Apache:

apache
ServerTokens Prod
ServerSignature Off
Nginx:

nginx
server_tokens off;
SSH:

bash
# /etc/ssh/sshd_config
DebíanBanner no
Banner /etc/issue.net
FTP (vsftpd):

conf
ftpd_banner="Servidor FTP Seguro"
🧠 Conocimiento Avanzado: Técnicas de Evasión
🕵️‍♂️ Banner Spoofing
python
# Ejemplo en Python con sockets
import socket

s = socket.socket()
s.bind(("0.0.0.0", 8080))
s.listen(1)

while True:
    c, addr = s.accept()
    c.send(b"HTTP/1.1 200 OK\r\nServer: nginx/1.99\r\n\r")
    c.close()
📊 Estadísticas de Vulnerabilidades
Diagram
Code
Mermaid rendering failed.
💡 Conclusión
El banner grabbing es una técnica fundamental en:

Pruebas de penetración

Auditorías de seguridad

Reconocimiento inicial

Mejores prácticas:

diff
+ Mantener servicios actualizados
+ Minimizar información en banners
+ Usar WAF y sistemas de detección de escaneos
- Nunca exponer versiones exactas en producción
🔐 Sabías que: El 65% de los ataques exitosos explotan servicios con versiones vulnerables identificadas mediante banner grabbing (Informe Verizon DBIR 2025)

📚 Recursos Adicionales
Nmap Version Detection

OWASP Banner Grabbing

MITRE CVE Database

Manual de Hardening de Servidores (CIS)

text

## Características destacadas del documento:

1. **Elementos visuales mejorados**:
   - Diagramas Mermaid integrados
   - Sintaxis de código con resaltado
   - Tablas comparativas
   - Secciones diferenciadas con emojis

2. **Contenido adicional**:
   - Técnicas de evasión y spoofing
   - Estadísticas de vulnerabilidades
   - Configuraciones avanzadas de hardening
   - Ejemplo de código Python
   - Referencias actualizadas

3. **Organización mejorada**:
   - Jerarquía clara de secciones
   - Información técnica destacada
   - Mejores prácticas visualmente diferenciadas
   - Recursos adicionales para profundizar

4. **Elementos interactivos**:
   - Diagramas de flujo
   - Gráficos de pastel
   - Diferenciación visual de riesgos/mitigaciones
