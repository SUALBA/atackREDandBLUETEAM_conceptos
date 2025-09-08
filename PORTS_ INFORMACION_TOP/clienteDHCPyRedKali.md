# 🌐 DHCP y Configuración de Red en Kali Linux

Este documento explica de manera sencilla cómo funciona **DHCP**,  
cómo interpretar la salida de `ip a` en Kali Linux, y cómo identificar tu IP  
y la puerta de enlace (gateway). Incluye un diagrama ASCII para visualizar la conexión.

---

## 🔹 1. ¿Qué es DHCP?

**DHCP (Dynamic Host Configuration Protocol)** es el protocolo que asigna automáticamente:

- Dirección IP
- Máscara de red
- Puerta de enlace (gateway)
- Servidores DNS

👉 El **cliente DHCP** (como `dhclient` o `dhcpcd`) es el programa que corre en tu sistema para **pedir esos datos** al servidor DHCP (normalmente, tu router o, en VirtualBox, el NAT interno).

Sin un cliente DHCP, tendrías que configurar todo esto manualmente.

---

## 🔹 2. Tu salida de `ip a`

Ejemplo real en Kali:


eth0: state UP
inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic eth0
default route via 10.0.2.2



### Desglose:

- **eth0: state UP**  
  La tarjeta de red está encendida y lista.

- **inet 10.0.2.15/24**  
  Tu **IP privada** dentro de la red virtual: `10.0.2.15`  
  - `/24` significa máscara `255.255.255.0`
  - Red local = `10.0.2.0/24`

- **brd 10.0.2.255**  
  Dirección de broadcast para mensajes a todos los hosts de la red.

- **scope global dynamic eth0**  
  “global” = válida en la red.  
  “dynamic” = asignada automáticamente por DHCP.

- **default route via 10.0.2.2**  
  La **puerta de enlace (gateway)** → el router virtual de VirtualBox.

---

## 🔹 3. Entonces, ¿cuál es tu IP?

- ✅ **Tu IP privada** = `10.0.2.15`  
- ✅ **Tu gateway (router virtual)** = `10.0.2.2`  
- El cliente DHCP fue quien te asignó estos valores.

---

## 🔹 4. Analogía sencilla

Imagina que tu red es una calle:

- **Tu casa (Kali)** → número **15** (`10.0.2.15`)  
- **El router (gateway)** → número **2** (`10.0.2.2`)  
- Cuando quieres salir de la calle (a Internet), pasas por la casa nº 2.

---

## 🔹 5. Diagrama ASCII de la conexión

```text
   ┌───────────┐
   │  Internet │
   └─────┬─────┘
         │
         ▼
   ┌─────────────┐
   │ Gateway NAT │  (10.0.2.2)
   │ VirtualBox  │
   └─────┬───────┘
         │
         ▼
   ┌─────────────┐
   │   Kali VM   │  (10.0.2.15)
   │   eth0 UP   │
   └─────────────┘


🔹 6. Comandos útiles
    Ver tu IP:
    ip a show eth0

    Ver tu puerta de enlace:
    ip route

    Ver tus servidores DNS:
    cat /etc/resolv.conf

✅ Resumen
Tu cliente DHCP (dhcpcd) te asignó la IP 10.0.2.15.

Tu gateway es 10.0.2.2 → VirtualBox NAT que conecta con Internet.

Gracias a esto, tu Kali VM puede comunicarse con el exterior automáticamente.

-----------------------------------------------------

# 🌐 Redes en VirtualBox: NAT vs Adaptador Puente

Cuando configuras una máquina virtual en VirtualBox, puedes elegir cómo se conectará a la red.  
Las dos opciones más comunes son **NAT** y **Adaptador Puente**.

---

## 🔹 NAT (Network Address Translation)

- La VM usa un **router virtual** interno de VirtualBox.
- Tu Kali recibe una IP privada (ejemplo `10.0.2.15`).
- El gateway es VirtualBox (ejemplo `10.0.2.2`).
- Desde dentro de la VM tienes acceso a Internet.
- Pero **otros dispositivos de tu red NO pueden ver tu Kali** directamente.

### Diagrama NAT

```text
   ┌───────────┐
   │  Internet │
   └─────┬─────┘
         │
   ┌─────────────┐
   │ VirtualBox  │  (Gateway: 10.0.2.2)
   └─────┬───────┘
         │ NAT
         ▼
   ┌─────────────┐
   │   Kali VM   │ (10.0.2.15)
   └─────────────┘


------------------------------------------------------


🔹 Adaptador Puente (Bridged)
La VM se conecta directamente a la red física como si fuera otro ordenador.

Tu Kali recibe una IP de tu router real (ejemplo 192.168.1.50).

Puede comunicarse directamente con otros dispositivos de tu red local.

Ideal para pentesting en LAN.

Pero depende de que tu router permita varias conexiones por tarjeta de red.

Diagrama Puente

   ┌───────────┐
   │  Internet │
   └─────┬─────┘
         │
   ┌─────────────┐
   │   Router    │  (192.168.1.1)
   └─────┬───────┘
         │
 ┌───────┼────────┐
 │       │        │
 ▼       ▼        ▼
PC Host  Kali VM  Otros Dispositivos
(192.168.1.10) (192.168.1.50)  ...


🔹 ¿Cuál elegir?
    NAT → más seguro y sencillo; recomendado para uso general y descargas.

    Puente → mejor para pruebas en red local (escaneo, pentesting), pero menos aislado.

🔹 Cambiar en VirtualBox
1.Apaga tu Kali VM.

2.Ve a Configuración → Red.

3.En Conectado a: selecciona:

    NAT (seguro y sencillo).

    Adaptador puente (para trabajar en la LAN real).

4.Activa Cable conectado.



****
sualba.dev © 2025 - Todos los derechos reservados

