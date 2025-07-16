# 🛡️ Comandos de Linux para Ciberseguridad - Guía Profesional

## 🔐 Introducción

En ciberseguridad, dominar la terminal de Linux es una habilidad esencial. Aquí encontrarás una lista ampliada y clasificada de comandos útiles para **monitorización**, **auditoría**, **respuesta ante incidentes**, **análisis forense**, y **pentesting ético**.

---

## 🧠 Índice de Categorías

- 🔍 Monitorización del sistema
- 🌐 Red y conexiones
- 👥 Gestión de usuarios y permisos
- 🔒 Auditoría y hardening
- 📂 Logs y análisis forense
- 🧪 Herramientas de pentesting
- 📌 Recomendaciones generales

---

## 🔍 Monitorización del sistema

| Comando     | Función | Ejemplo | 🛠️ Utilidad |
|-------------|--------|---------|--------------|
| `top` / `htop` | Ver uso de CPU, RAM y procesos activos. | `htop` | Detectar procesos sospechosos. |
| `df` | Uso de disco. | `df -h` | Control de espacio en particiones. |
| `free` | Uso de RAM y swap. | `free -m` | Diagnóstico de memoria. |
| `uptime` | Tiempo activo + carga promedio. | `uptime` | Detectar sobrecarga. |
| `vmstat` | Estadísticas de memoria, CPU, IO. | `vmstat 1` | Diagnóstico de rendimiento. |

---

## 🌐 Red y conexiones

| Comando     | Función | Ejemplo | 🌍 Utilidad |
|-------------|---------|---------|-------------|
| `ip a` / `ifconfig` | Ver IPs e interfaces. | `ip a` | Diagnóstico de red. |
| `ss` / `netstat` | Puertos abiertos y conexiones. | `ss -tuln` | Ver servicios activos. |
| `tcpdump` | Capturar tráfico de red. | `tcpdump -i eth0` | Análisis de red. |
| `nmap` | Escaneo de red/puertos. | `nmap -sS 192.168.1.0/24` | Descubrir hosts y servicios. |
| `ping`, `traceroute` | Ver latencia y rutas. | `traceroute google.com` | Diagnóstico de conectividad. |
| `dig`, `nslookup` | Consultas DNS. | `dig github.com` | Resolver problemas DNS. |
| `curl`, `wget` | Peticiones HTTP desde terminal. | `curl -I http://web.com` | Ver cabeceras de respuesta. |

---

## 👥 Usuarios y permisos

| Comando     | Función | Ejemplo | 🔐 Utilidad |
|-------------|---------|---------|--------------|
| `who`, `w`, `last` | Usuarios conectados y actividad. | `w` | Detección de accesos activos. |
| `id`, `groups`, `whoami` | Ver UID y grupos. | `id` | Revisión de permisos. |
| `chmod`, `chown`, `ls -l` | Permisos y propietarios. | `chmod 700 archivo` | Hardening de archivos. |
| `passwd`, `usermod`, `userdel` | Gestión de cuentas. | `usermod -L user` | Bloqueo de usuarios. |
| `sudo`, `visudo` | Privilegios administrativos. | `sudo su` | Control de acceso privilegiado. |

---

## 🔒 Auditoría y hardening

| Comando / Herramienta | Función | Ejemplo | 🧱 Utilidad |
|-----------------------|---------|---------|-------------|
| `auditctl`, `ausearch` | Auditoría de eventos (Auditd). | `ausearch -x /usr/bin/passwd` | Trazabilidad de acciones. |
| `chkrootkit`, `rkhunter` | Buscar rootkits. | `chkrootkit` | Detección de malware. |
| `lynis` | Auditoría automática del sistema. | `lynis audit system` | Informe de hardening. |
| `fail2ban-client` | Revisión de reglas Fail2ban. | `fail2ban-client status sshd` | Defensa contra fuerza bruta. |
| `iptables`, `ufw` | Configurar cortafuegos. | `iptables -L` | Control de tráfico. |
| `crontab`, `systemctl`, `ps aux` | Revisar tareas y servicios. | `crontab -l` | Buscar servicios sospechosos. |

---

## 📂 Logs y análisis forense

| Comando     | Función | Ejemplo | 🕵️ Utilidad |
|-------------|---------|---------|--------------|
| `journalctl` | Leer logs del sistema. | `journalctl -xe` | Investigar eventos críticos. |
| `dmesg` | Ver mensajes del kernel. | `dmesg | tail` | Errores de hardware. |
| `logrotate` | Gestión automática de logs. | - | Control del tamaño de logs. |
| `sha256sum`, `md5sum` | Verificar integridad. | `sha256sum archivo.iso` | Detección de alteraciones. |
| `stat`, `find`, `grep` | Buscar y analizar archivos. | `find / -perm 777` | Encontrar configuraciones peligrosas. |
| `strings`, `hexdump` | Ver contenido binario/texto oculto. | `strings malware.exe` | Análisis estático básico. |

---

## 🧪 Pentesting y análisis ofensivo (uso ético)

⚠️ **Advertencia**: estas herramientas deben utilizarse sólo en entornos autorizados (CTF, laboratorio, pruebas internas).

| Herramienta | Función | Comando básico | 🧨 Utilidad |
|-------------|---------|----------------|-------------|
| `nmap` | Escaneo de red. | `nmap -A IP` | Reconocimiento de servicios. |
| `hydra` | Fuerza bruta de credenciales. | `hydra -l admin -P pass.txt ssh://IP` | Test de contraseñas. |
| `nikto` | Escaneo de vulnerabilidades web. | `nikto -h http://IP` | Detectar fallos comunes. |
| `tcpdump`, `wireshark` | Captura de paquetes. | `tcpdump -i eth0` | Interceptar tráfico. |
| `hashcat`, `john` | Ataque de hashes. | `hashcat -m 0 hash.txt dict.txt` | Cracking de contraseñas. |

---

## 📌 Recomendaciones profesionales

✅ **Haz esto**:
- Automatiza alertas con scripts y herramientas como `auditd`, `logwatch`, `fail2ban`.
- Usa entornos aislados para practicar (`VirtualBox`, `Kali`, `Remnux`, etc.).
- Documenta cada hallazgo o intervención.
- Familiarízate con los logs del sistema (los logs te hablan 📢).

❌ **Evita esto**:
- Usar comandos peligrosos sin comprenderlos.
- Trabajar siempre como `root`.
- Ejecutar herramientas ofensivas fuera de un entorno de prueba.
- Ignorar actualizaciones de seguridad del sistema.

---

> 🧠 **Recuerda**: la terminal es tu mejor aliada en ciberseguridad. Dominar estos comandos no solo te ayuda a aprobar el examen, sino a **pensar como analista de seguridad**.
