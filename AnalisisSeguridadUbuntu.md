# Análisis de Ciberseguridad - Sistema Ubuntu

## Información General
- **Usuario analizado**: `basicftp`
- **Sistema**: Ubuntu (VirtualBox)
- **Contexto**: Trabajo académico de bootcamp en Ciberseguridad
- **Objetivo**: Análisis de configuración y búsqueda de vectores de escalada de privilegios

## 1. Análisis del archivo `/etc/adduser.conf`

### 1.1 Descripción
El archivo `/etc/adduser.conf` es el archivo de configuración para el comando `adduser` en sistemas Ubuntu/Debian. Define los valores predeterminados utilizados al crear nuevos usuarios.

### 1.2 Configuraciones principales identificadas

#### Configuraciones básicas
```bash
DSHELL=/bin/bash          # Shell predeterminado para nuevos usuarios
DHOME=/home               # Directorio base para homes de usuarios
SKEL=/etc/skel           # Directorio con archivos esqueleto
```

#### Rangos de IDs
- **Sistema**: UIDs/GIDs del 100 al 999 para cuentas del sistema
- **Usuarios normales**: UIDs/GIDs del 1000 al 59999 para usuarios regulares

#### Configuraciones de grupos
```bash
USERGROUPS=yes           # Cada usuario tiene su propio grupo personal
USERS_GID=100           # GID por defecto si USERGROUPS=no
```

#### Permisos y seguridad
```bash
DIR_MODE=0750           # Permisos de directorios home (rwxr-x---)
SETGID_HOME=no         # Bit setgid desactivado en directorios home
```

### 1.3 Configuraciones comentadas (análisis de riesgo)

Las siguientes líneas están deshabilitadas pero representan vectores potenciales:

```bash
#EXTRA_GROUPS="dialout cdrom floppy audio video plugdev users"
#ADD_EXTRA_GROUPS=1
#NAME_REGEX="^[a-z][-a-z0-9_]*\$"
#USE_EXTRAUSERS=1
```

#### Implicaciones si se descomentaran:
- **EXTRA_GROUPS**: Usuarios nuevos obtendrían permisos adicionales automáticamente
  - `dialout`: Acceso a modems y puertos serie
  - `cdrom`: Montar CDs/DVDs
  - `audio/video`: Dispositivos multimedia
  - `plugdev`: Montar dispositivos USB
  - `users`: Grupo general de usuarios

## 2. Intento de Modificación y Análisis de Privilegios

### 2.1 Resultado del intento de edición
```bash
basicftp@ubuntu-VirtualBox:/etc$ sudo nano /etc/adduser.conf
[sudo] contraseña para basicftp: 
basicftp no está en el archivo sudoers. Se informará de este incidente.
```

### 2.2 Hallazgos importantes
- ✅ **Seguridad correcta**: El usuario `basicftp` no tiene privilegios sudo
- ✅ **Protección de archivos**: Los archivos de configuración del sistema están protegidos
- ✅ **Principio de menor privilegio**: El sistema implementa correctamente la restricción de acceso

## 3. Vectores de Escalada de Privilegios Sugeridos

### 3.1 Enumeración de privilegios actuales
```bash
# Información del usuario actual
id
groups
whoami

# Verificar permisos del usuario
cat /etc/passwd | grep basicftp
```

### 3.2 Búsqueda de archivos con permisos especiales
```bash
# Buscar archivos SUID
find / -perm -4000 2>/dev/null

# Buscar archivos SGID
find / -perm -2000 2>/dev/null

# Archivos escribibles por el usuario
find / -writable -type f 2>/dev/null | grep -v proc | grep -v sys
```

### 3.3 Análisis de servicios y procesos
```bash
# Procesos del usuario
ps aux | grep basicftp

# Puertos y servicios activos
netstat -tulpn
```

## 4. Evaluación de Seguridad

### 4.1 Aspectos positivos identificados
- **Separación de privilegios**: Usuario sin acceso sudo
- **Protección de archivos críticos**: Configuración del sistema protegida
- **Configuración segura**: `DIR_MODE=0750` proporciona permisos restrictivos
- **Grupos personales**: `USERGROUPS=yes` mejora el aislamiento entre usuarios

### 4.2 Áreas de mejora potencial
- **Auditoría de grupos**: Verificar necesidad real de grupos adicionales
- **Monitoreo**: Implementar alertas para intentos de sudo fallidos
- **Validación**: Considerar activar `NAME_REGEX` para nombres de usuario más restrictivos

## 5. Conclusiones del Análisis

### 5.1 Estado de seguridad general
El sistema presenta una configuración de seguridad **adecuada** con:
- Implementación correcta del principio de menor privilegio
- Protección efectiva de archivos de configuración críticos
- Separación apropiada entre usuarios del sistema y usuarios normales

### 5.2 Recomendaciones para análisis adicional
1. **Enumeración completa del sistema**: Continuar con la búsqueda de vectores alternativos
2. **Análisis de servicios**: Examinar servicios ejecutándose con el usuario `basicftp`
3. **Revisión de archivos de configuración**: Buscar otros archivos accesibles para lectura
4. **Análisis de red**: Verificar servicios de red y posibles vulnerabilidades

### 5.3 Valor educativo
Este ejercicio demuestra la importancia de:
- Configuraciones de seguridad por defecto bien implementadas
- La efectividad de las restricciones de privilegios
- La necesidad de múltiples vectores de ataque en pentesting real

---

**Nota**: Este análisis se realizó en un entorno controlado para fines educativos como parte de un Bootcamp en Ciberseguridad.