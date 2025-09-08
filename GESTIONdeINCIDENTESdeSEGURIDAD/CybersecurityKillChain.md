
# 🔐 Cybersecurity Kill Chain

La **Cybersecurity Kill Chain**, desarrollada por Lockheed Martin, describe las fases que sigue un atacante para ejecutar con éxito un ciberataque.  
Es una herramienta clave tanto en **ciberseguridad ofensiva** como en **defensiva**, ya que permite:

- Comprender el ciclo de vida de un ataque.
- Detectar actividades maliciosas en cada fase.
- Implementar defensas adecuadas para interrumpir la cadena.

---

## 📊 Diagrama General

```text
[1] Reconocimiento → [2] Armamento → [3] Entrega → [4] Explotación 
       ↓                   ↓                ↓              ↓
[5] Instalación → [6] Comando & Control → [7] Acciones sobre los Objetivos






🔎 Las 7 Fases de la Kill Chain
1. Reconocimiento (Reconnaissance)
Objetivo: Recolectar información sobre la víctima.
Técnicas:

Escaneo de puertos (nmap, masscan).

Búsqueda en redes sociales y fuentes OSINT.

Uso de Shodan para localizar servicios expuestos.

Ejemplo ofensivo:
Un atacante descubre servidores RDP expuestos mediante Shodan.

Defensa:

Minimizar la huella digital (cerrar puertos innecesarios).

Monitorizar escaneos sospechosos.

Implementar threat intelligence.

2. Armamento (Weaponization)
Objetivo: Crear una carga útil (payload) adaptada al objetivo.
Técnicas:

Exploits con Metasploit.

Documentos maliciosos (PDF, Word con macros).

Malware polimórfico.

Ejemplo ofensivo:
Un atacante crea un PDF con exploit de Adobe Reader que abre una puerta trasera.

Defensa:

Mantener software actualizado.

Analizar adjuntos en sandbox.

Reglas YARA para detectar ofuscación.

3. Entrega (Delivery)
Objetivo: Hacer llegar el malware al sistema víctima.
Vectores comunes:

Phishing por correo electrónico.

Drive-by download (visitar un sitio web comprometido).

Dispositivos USB infectados.

Ejemplo ofensivo:
Correo con un Excel que contiene macros maliciosas.

Defensa:

Filtrado de correos y adjuntos.

Concienciación de usuarios.

Control de dispositivos externos.

4. Explotación (Exploitation)
Objetivo: Aprovechar una vulnerabilidad para ejecutar código malicioso.
Técnicas:

Explotar vulnerabilidades conocidas (ej. EternalBlue).

Uso de macros en documentos ofimáticos.

Ataques web (XSS, SQL Injection).

Ejemplo ofensivo:
Ataque con EternalBlue a un servidor SMB vulnerable.

Defensa:

Actualizaciones y parches frecuentes.

IDS/IPS para detectar intentos de explotación.

Configuración segura en aplicaciones web.

5. Instalación (Installation)
Objetivo: Establecer persistencia en el sistema comprometido.
Técnicas:

RATs (Remote Access Trojans).

Fileless malware (solo en memoria).

Claves en el registro o tareas programadas.

Ejemplo ofensivo:
Instalación de un troyano para mantener acceso remoto.

Defensa:

Monitorizar cambios en el registro.

EDR con análisis de comportamiento.

Control de integridad de archivos.

6. Comando y Control (C2)
Objetivo: Mantener comunicación con la infraestructura atacante.
Técnicas:

Túneles cifrados (HTTPS, DNS tunneling).

Uso de redes Tor o P2P.

Canales encubiertos en tráfico legítimo.

Ejemplo ofensivo:
El malware se comunica con un servidor C2 a través de HTTPS.

Defensa:

Analizar tráfico de red en busca de anomalías.

Bloquear dominios maliciosos conocidos.

Implementar Threat Feeds en firewalls y SIEM.

7. Acciones sobre los Objetivos (Actions on Objectives)
Objetivo: Alcanzar la meta final del atacante.
Posibles metas:

Robo de información sensible.

Despliegue de ransomware.

Movimiento lateral para comprometer más sistemas.

Ejemplo ofensivo:
Exfiltración de bases de datos con credenciales de clientes.

Defensa:

DLP (Data Loss Prevention).

Segmentación de red.

Monitorización continua con SIEM.

📌 Caso Real: WannaCry (2017)
Reconocimiento: Escaneo de sistemas Windows con SMB abierto.

Armamento: Exploit EternalBlue + ransomware.

Entrega: Propagación automática en red.

Explotación: Vulnerabilidad SMBv1.

Instalación: Copia de malware en los sistemas.

C2: Comunicación con servidores de activación.

Acción: Cifrado masivo de archivos y petición de rescate.

⚔️ Kill Chain vs MITRE ATT&CK
Modelo	Enfoque	Uso principal
Kill Chain	Lineal de 7 fases	Visión táctica para detectar y frenar ataques
MITRE ATT&CK	Matricial con tácticas y técnicas	Análisis granular y detallado de TTPs

👉 Lo ideal: usar Kill Chain + MITRE ATT&CK juntos para tener visión táctica y técnica.

🛡️ Recomendaciones Defensivas
Implementar Zero Trust y segmentación de red.

Usar EDR y SIEM con correlación de eventos.

Configurar reglas YARA/Sigma para detectar anomalías.

Realizar ejercicios Red Team / Purple Team.

Mantener un plan de respuesta a incidentes actualizado.

📌 Conclusión
La Cybersecurity Kill Chain no es solo un marco teórico, sino una guía práctica para la defensa proactiva.
Interrumpir la cadena en las primeras fases (Reconocimiento, Entrega o Explotación) puede prevenir que el ataque llegue a fases críticas como C2 o exfiltración.




****
sualba.dev © 2025 - Todos los derechos reservados