--

# 📌 Explicación: `sudo`, `root` y flags como `-y` y `-v`

### 🔹 `sudo`
- Significa **SuperUser DO** (haz esto como superusuario).
- Permite ejecutar un comando con privilegios de administrador.
- Ejemplo:
    sudo apt update
→ Actualiza la lista de paquetes, pero necesita permisos de root.

🔹 root
Es el usuario administrador en Linux.
Tiene control total sobre el sistema.

El usuario normal (kali) usa sudo para ejecutar acciones de root sin iniciar sesión como root directamente.

🔹 Opción -y
Se usa en muchos comandos (como apt) para responder “yes” automáticamente a las preguntas.

Ejemplo:

sudo apt install nmap -y
→ Instala nmap sin pedir confirmación.

🔹 Opción -v
    Generalmente significa verbose (detallado).

    Hace que el comando muestre más información en pantalla.

    Ejemplo:
    ping -v google.com
    → Muestra salida detallada.

🔹 Otras opciones comunes
    -h → help (ayuda).

    -u → especificar usuario.

    -f → forzar una acción.

✅ Resumen
    sudo → ejecutar comandos como root.

    root → usuario administrador del sistema.

    -y → responder automáticamente “sí” a confirmaciones.

    -v → mostrar salida detallada (verbose).


# 📘 Linux - Glosario de Flags Comunes en Comandos

Este documento resume los **flags (opciones cortas)** más usados en Linux,  
con ejemplos prácticos. Ideal como chuleta para trabajar en Kali u otras distros.

---

## 🔹 1. Confirmación y automatización

- **`-y`** → Aceptar automáticamente preguntas tipo “¿desea continuar?”
sudo apt install nmap -y

-f → Forzar una acción
    rm -f archivo.txt


🔹 2. Verbosidad y depuración
    -v → Verbose (mostrar más información)
    curl -v http://example.com  
    -vv o -vvv → Aún más detalle
    ssh -vv user@host
    
    -q → Quiet (silencioso, mostrar menos salida)
    apt update -q

🔹 3. Ayuda y manuales
    -h → Mostrar ayuda breve
    ls -h
    --help → Versión extendida de la ayuda

    grep --help
    man comando → Manual completo
    man ls

🔹 4. Listados y formato de salida
    -l → Formato largo en listados
    ls -l
    
    -a → Mostrar archivos ocultos
    ls -a

    -la → Combinación común (largo + ocultos)
    ls -la

    -h → Human readable (en ls o df, para tamaños legibles)
    ls -lh
    df -h

🔹 5. Usuario y permisos
    -u → Especificar usuario
    sudo -u www-data whoami

    -r → Recursivo (muy usado en permisos y copias)
    chmod -R 755 /var/www

🔹 6. Flags de red
    -c → Número de paquetes a enviar (ping)
    ping -c 4 google.com

    -p → Puerto (nc, nmap, etc.)
    nc -v 192.168.1.1 -p 22

    -s → Escaneo sigiloso (nmap)
    nmap -sS 192.168.1.0/24

🔹 7. Búsqueda y filtrado
    -i → Ignorar mayúsculas/minúsculas (grep)
    grep -i "error" /var/log/syslog
    
    -r → Búsqueda recursiva en directorios
    grep -r "clave" /etc/

✅ Resumen
    -y → Sí automático

    -v → Verbose (detallado)

    -h → Ayuda breve

    -l / -a / -la → Listados en ls

    -R → Recursivo

    -c / -p / -s → Muy usados en comandos de red

⚡ Consejo: Muchos comandos aceptan flags combinados,
ejemplo:


ls -lah
→ lista larga, incluye ocultos, con tamaños legibles.











