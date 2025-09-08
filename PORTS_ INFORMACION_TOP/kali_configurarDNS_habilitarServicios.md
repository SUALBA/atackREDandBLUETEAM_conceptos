# 📘 Chuleta Kali Linux - Redes y Servicios Básicos

Este documento es una guía rápida para cuando instales **Kali Linux mínimo**  
y la red no funcione al inicio. Incluye cómo **levantar una interfaz muerta**,  
**configurar DNS manualmente** y **habilitar servicios** para que se inicien solos.

---

## 🔹 1. Verificar interfaces de red

Ver todas las interfaces:

ip a
Si solo aparece lo → no hay adaptador configurado en VirtualBox/VMware.

Si aparece eth0 o enp0s3 con state DOWN → hay que levantarla.

🔹 2. Levantar una interfaz de red muerta

sudo ip link set eth0 up
(sustituir eth0 por el nombre real de la interfaz)

🔹 3. Configurar DNS manualmente
Si tienes conexión IP pero no puedes resolver nombres de dominio:

    1.Editar el archivo de configuración DNS:

    sudo nano /etc/resolv.conf

    2.Añadir servidores públicos:

    nameserver 8.8.8.8
    nameserver 1.1.1.1

    3.Guardar (CTRL + O, ENTER) y salir (CTRL + X).

    4.Probar:
    ping -c 4 google.com

🔹 4. Instalar y habilitar NetworkManager
    Para que la red se configure sola al arrancar:

    sudo apt update
    sudo apt install -y network-manager
    sudo systemctl enable NetworkManager
    sudo systemctl start NetworkManager

    Verificar estado:

    nmcli device status

    Debe aparecer eth0 en estado connected.

🔹 5. Comprobar conectividad básica
    Ping a Google por IP:

    ping -c 4 8.8.8.8
    
    Ping a Google por nombre (requiere DNS):

    ping -c 4 google.com

🔹 6. (Opcional) Instalar el escritorio XFCE + LightDM
Si solo tienes modo terminal y quieres entorno gráfico:

    sudo apt install -y kali-desktop-xfce lightdm

    Seleccionar lightdm como gestor de login cuando lo pida.
    Después reiniciar:
            sudo reboot


🔹 7. (Opcional) Instalar las herramientas principales de Kali
Para tener el pack estándar de herramientas:

sudo apt install -y kali-linux-default

----------------------------------------------------------
🔍 Qué vemos en tu home
Ahora tu directorio personal (~) ya no es tan vacío como al principio, porque XFCE creó carpetas y archivos de configuración.

Algunos destacados:

✅Carpetas estándar

    Descargas, Documentos, Escritorio, Imágenes, Música, Plantillas, Público, Vídeos
    Son directorios de usuario que XFCE crea para organizar tus archivos.

✅Archivos de sesión y configuración gráfica

    .ICEauthority, .Xauthority → controlan las sesiones gráficas de X11.

    .xsession-errors → registro de errores del entorno gráfico.

✅Configuraciones personales

    .config/ → configuración de aplicaciones (por ejemplo, Firefox, Thunar).

    .cache/ → cachés de aplicaciones gráficas.

    .dmrc → recuerda tu entorno de escritorio por defecto.

✅Otros útiles

    .bashrc, .zshrc → personalización de tus shells.

    .hushlogin → ya lo tienes, oculta el mensaje inicial de login.

    .sudo_as_admin_successful → marca que ya usaste sudo con éxito una vez.



****
sualba.dev © 2025 - Todos los derechos reservados