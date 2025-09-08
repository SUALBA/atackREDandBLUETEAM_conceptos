# 🛡️ Reglas Locales de Snort: Defensa con Estilo 🚀

Este documento recoge **5 reglas clave de Snort** creadas para detectar ataques comunes.  
No solo veremos **qué hacen**, sino también **qué implican**, **qué consecuencias tienen**  
y cómo podemos **sacar conclusiones prácticas** al aplicarlas.  

---

## 🔍 Regla 1: Detectar escaneo Nmap 🕵️

```snort
alert tcp any any -> $HOME_NET any \
(msg: "NMAP Scan Detected"; sid:1000001; flags:S; \
threshold:type threshold, track by_dst, count 5, seconds 60)
📖 Explicación
Vigila intentos de conexiones SYN (inicio de sesión TCP).

Si un mismo host recibe 5 SYN en 60 segundos, se dispara la alerta.

Detecta escaneos de puertos Nmap en modo SYN.

⚡ Consecuencias
Un atacante probablemente está mapeando tus servicios.

Aunque el escaneo no cause daño directo, es el primer paso de un ataque.

🎯 Conclusión práctica: Si esta alerta suena, revisa qué servicios tienes expuestos y aplica hardening (firewall, IDS/IPS).

📁 Regla 2: Acceso a .git expuesto 🔑
snort
alert tcp any any -> $HOME_NET 80 \
(msg:"Access to hidden folder"; sid:1000002; \
content:"/.git/"; http_uri; classtype:web-application-attack;)

📖 Explicación
Busca accesos a la carpeta oculta .git/ en servidores web.

Los repositorios .git a veces quedan expuestos accidentalmente.

⚡ Consecuencias
Un atacante podría descargar tu código fuente, incluyendo:

Contraseñas

Llaves API

Configuraciones críticas

🎯 Conclusión práctica: ¡Nunca expongas .git! Usa .htaccess o configuraciones Nginx/Apache para bloquearlo.

🔑 Regla 3: Login FTP anónimo 🚨
snort
alert tcp any any -> $HOME_NET 21 \
(msg:"Anonymous FTP access"; content:"USER anonymous"; \
classtype:suspicious-login; sid:10000003; rev:1;)

📖 Explicación
Detecta intentos de login FTP con el usuario anonymous.

Es una táctica común para entrar en servidores mal configurados.

⚡ Consecuencias
Si está habilitado, los atacantes pueden descargar o subir archivos.

Puede usarse para exfiltración o malware.

🎯 Conclusión práctica:
Bloquea el FTP anónimo ❌.
Si necesitas compartir archivos, usa SFTP o servicios autenticados.

📂 Regla 3b: Intento de subir archivos por FTP 💾
snort
alert tcp any any -> $HOME_NET 21 \
(msg:"Try to upload a file"; content:"STOR"; sid:1000006;)

📖 Explicación
Detecta el comando STOR de FTP → subir archivos.

⚡ Consecuencias
Riesgo de que el atacante suba un webshell o malware.

Puede ser el paso final tras un acceso anónimo exitoso.

🎯 Conclusión práctica:
Monitorea el uso de STOR y considera deshabilitar la subida de archivos si no es esencial.

🔒 Regla 4: Fuerza Bruta SSH 🔐
snort
alert tcp any any -> $HOME_NET 22 \
(msg:"Potential SSH Brute Force"; sid:1000004; flow:to_server; flags:S; \
detection_filter:track by_src, count 2, seconds 60; classtype:attempted-dos;)

📖 Explicación
Analiza intentos de conexión SSH.

Si una IP intenta conectarse 2 veces en 60 segundos, lanza alerta.

⚡ Consecuencias
Indica ataque de fuerza bruta contra SSH.

Riesgo de que el atacante adivine credenciales débiles.

🎯 Conclusión práctica:
Implementa fail2ban o iptables para bloquear IPs que fallen muchas veces.

🧨 Regla 5: Inyección de comandos en puerto 5011 ⚔️
snort
alert tcp any any -> any 5011 \
(msg:"Posible inyección de comandos por el puerto 5011"; content:"|3B|"; sid:1000008;)

📖 Explicación
Busca el carácter ; (0x3B en hex).

Común en inyecciones de comandos → ls; cat /etc/passwd.

⚡ Consecuencias
Si tu aplicación en el puerto 5011 ejecuta comandos,
un atacante puede ejecutar múltiples órdenes en el servidor.

🎯 Conclusión práctica:
Valida y escapa todas las entradas de usuario.
Considera este puerto crítico en tus revisiones de seguridad.

🌈 Reflexiones Finales
Con estas reglas:

Regla 1 → Detectamos al que curiosea con Nmap.

Regla 2 → Bloqueamos el robo de código fuente oculto.

Reglas 3 y 3b → Cerramos puertas a FTP mal configurados.

Regla 4 → Evitamos ataques persistentes a SSH.

Regla 5 → Vigilamos posibles inyecciones de comandos.

💡 Conclusión general:
Estas reglas convierten tu IDS en un perro guardián digital 🐕‍🦺.
Te avisan de exploradores sospechosos y te dan tiempo de reaccionar antes del daño real.

🖥️ Interfaces Gráficas Recomendadas para Snort
Aunque Snort funciona en consola, hay herramientas GUI que lo hacen más intuitivo:

BASE (Basic Analysis and Security Engine)

Antigua pero útil. Muestra alertas en una interfaz web.

Snorby

Muy visual y organizada. (Aunque está descontinuada, sigue siendo usada en labs).

Sguil + Squert

Interfaz moderna usada en entornos de SOC.

Permite correlacionar eventos y visualizar tendencias.

ELK Stack (Elasticsearch + Logstash + Kibana)

La más profesional.

Permite dashboards interactivos con alertas en tiempo real.

Security Onion 🧅

Distro de Linux orientada a SOC que ya trae Snort/Suricata + GUI.

Perfecta si quieres un entorno todo en uno.

🎯 Recomendación personal:
Si buscas algo fácil y rápido → Snorby o BASE.
Si quieres nivel profesional → monta Security Onion con ELK.


*********************************************
>© 2025 [sualba.dev] Todos los derechos reservados
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.