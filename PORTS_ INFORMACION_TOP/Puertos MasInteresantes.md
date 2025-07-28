# Puertos comunes en ciberseguridad y pentesting
1. Puertos bien conocidos (Well-known ports)
Los primeros 1024 puertos (0–1023) están reservados para servicios estándar, definidos por la IANA (Internet Assigned Numbers Authority).
Por convención, cada uno se asocia a un protocolo o servicio concreto.
Aquí tienes algunos ejemplos comunes:

## 🧰 Servicios de administración remota

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 22     | SSH       | Acceso remoto seguro              |
| 23     | Telnet    | Acceso remoto inseguro            |
| 3389   | RDP       | Escritorio remoto (Windows)       |
| 5900   | VNC       | Escritorio remoto VNC             |

## 🌐 Servicios web

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 80     | HTTP      | Web sin cifrado                   |
| 443    | HTTPS     | Web con cifrado TLS               |
| 8080   | HTTP Alt  | Proxy web o apps web alternas     |
| 8443   | HTTPS Alt | Web segura alternativa            |

## 📤📥 Transferencia de archivos

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 20     | FTP-DATA  | Transferencia FTP                 |
| 21     | FTP       | Control de conexión FTP           |
| 69     | TFTP      | FTP trivial (sin autenticación)   |
| 989    | FTPS-DATA | FTP con SSL/TLS                   |
| 990    | FTPS      | FTP seguro                        |
| 115    | SFTP      | FTP sobre SSH (a veces confuso)   |

## 📧 Correo electrónico

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 25     | SMTP      | Envío de correo                   |
| 110    | POP3      | Recepción (descarga) de correos   |
| 143    | IMAP      | Acceso a correos en servidor      |
| 587    | SMTP      | Envío con autenticación (TLS)     |
| 993    | IMAPS     | IMAP con cifrado                  |
| 995    | POP3S     | POP3 con cifrado                  |

## 🧠 DNS y Resolución

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 53     | DNS       | Resolución de nombres             |

## 🛢️ Bases de datos

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 1433   | MSSQL     | SQL Server                        |
| 3306   | MySQL     | MySQL                             |
| 5432   | PostgreSQL| PostgreSQL                        |
| 27017  | MongoDB   | MongoDB                           |

## 📚 Otros servicios útiles

| Puerto | Protocolo | Descripción                       |
|--------|-----------|-----------------------------------|
| 161    | SNMP      | Monitorización de red             |
| 389    | LDAP      | Directorio abierto                 |
| 636    | LDAPS     | LDAP con SSL/TLS                  |
| 111    | RPCbind   | RPC en UNIX                       |
| 2049   | NFS       | Sistema de archivos en red        |
| 631    | IPP       | Protocolo de impresión            |
| 4444   | Metasploit| Reverse shell (por convención)    |
| 1337   | Custom    | Usado en CTFs y pruebas            |



A tener en cuenta: 
🔎 2. ¿Dónde se consulta esto?
En el archivo local: /etc/services

 "  cat /etc/services | grep 22/tcp  "
O desde la propia salida de herramientas como nmap.


✅ Por qué esto es importante en ciberseguridad
Te ayuda a reconocer la superficie de ataque rápidamente.

Si ves un puerto inusual (como un 5011 por ejemplo), sabes que no es un servicio estándar → puede ser vulnerable, personalizado o mal configurado.

Te permite asociar vulnerabilidades conocidas (CVE) a servicios concretos.