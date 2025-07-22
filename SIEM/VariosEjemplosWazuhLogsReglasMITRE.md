# 🛡️ Ejercicios Básicos Wazuh - Logs + Reglas MITRE

Este archivo contiene ejemplos basicos prácticos de logs con sus respectivas reglas y explicaciones.

---

## 🔁 Ejemplo 1 - 🌐 Tráfico HTTP no crítico

**Log:**
```text
ownapp:WARNING,192.168.1.10,192.168.1.20,3333,80,tcp,111001,2
```

**Explicación:**  
Se trata de un tráfico hacia puerto 80 (HTTP) clasificado como WARNING con severidad baja.

**Regla Wazuh:**
```xml
<rule id="100101" level="2">
  <if_sid>100003</if_sid>
  <match>WARNING</match>
  <field name="estado">2</field>
  <description>Tráfico HTTP no crítico - Nivel 2</description>
  <mitre>
    <id>T1071.001</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 2 - 🔐 Acceso SSH sospechoso

**Log:**
```text
ownapp:DANGER,10.0.0.4,10.0.0.5,40222,22,tcp,222002,5
```

**Explicación:**  
Conexión a puerto SSH (22) desde puerto elevado, severidad 5.

**Regla Wazuh:**
```xml
<rule id="100102" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">22</field>
  <field name="estado">5</field>
  <description>Posible ataque SSH detectado</description>
  <mitre>
    <id>T1021.004</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 3 - 🚨 Alerta sobre SSH

**Log:**
```text
ownapp:ALERT,10.10.10.10,10.10.10.11,5050,22,tcp,555005,4
```

**Explicación:**  
El sistema lanza alerta de nivel medio por conexión SSH (puerto 22) con severidad 4.

**Regla Wazuh:**
```xml
<rule id="100103" level="6">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">22</field>
  <description>Alerta potencial sobre acceso SSH</description>
  <mitre>
    <id>T1566</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 4 - 🔄 Acceso entre MySQL y SSH

**Log:**
```text
ownapp:DANGER,192.168.2.3,192.168.2.4,3306,22,tcp,666006,5
```

**Explicación:**  
Tráfico desde un origen típico de MySQL hacia SSH. Severidad 5 y mensaje DANGER.

**Regla Wazuh:**
```xml
<rule id="100104" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertoorigen">3306</field>
  <field name="puertodestino">22</field>
  <description>Acceso crítico desde servidor MySQL a SSH</description>
  <mitre>
    <id>T1046</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 5 - ℹ️ Evento informativo por UDP

**Log:**
```text
ownapp:INFO,172.16.0.1,172.16.0.100,12000,443,udp,333003,1
```

**Explicación:**  
Actividad informativa sin severidad crítica. Tráfico a HTTPS sobre UDP.

**Regla Wazuh:**
```xml
<rule id="100105" level="1">
  <if_sid>100003</if_sid>
  <match>INFO</match>
  <description>Evento informativo no relevante</description>
</rule>
```

---

## ✅ Recomendaciones

- Repasa el uso de `<field>` y `<if_sid>`.
- Fíjate bien en los puertos destino y la severidad.
- Memoriza los niveles de alerta y relaciónalos con MITRE.




# 🛡️ Ejercicios Avanzados Wazuh - Logs + Reglas MITRE

Esta colección incluye logs realistas para detección de amenazas y las reglas Wazuh correspondientes con explicaciones claras.

---

## 🔁 Ejemplo 6 - 🧪 Escaneo de red sospechoso (SYN scan)

**Log:**
```text
ownapp:DANGER,10.0.0.100,10.0.0.1,4444,135,tcp,606001,5
```

**Explicación:**  
Actividad en puerto RPC (135) desde origen no habitual. Podría indicar un escaneo SYN o descubrimiento lateral.

**Regla Wazuh:**
```xml
<rule id="100106" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">135</field>
  <description>Posible escaneo RPC detectado</description>
  <mitre>
    <id>T1046</id> <!-- Network Service Scanning -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 7 - 🛰️ Transferencia FTP no autorizada

**Log:**
```text
ownapp:ALERT,192.168.1.5,192.168.1.10,54321,21,tcp,707002,4
```

**Explicación:**  
Puerto FTP (21) activo con severidad 4. Puede ser una transferencia sin control.

**Regla Wazuh:**
```xml
<rule id="100107" level="7">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">21</field>
  <description>Posible intento de transferencia por FTP</description>
  <mitre>
    <id>T1105</id> <!-- Ingress Tool Transfer -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 8 - 💻 Uso de RDP sin autorización

**Log:**
```text
ownapp:DANGER,172.16.2.5,172.16.2.10,5555,3389,tcp,808003,5
```

**Explicación:**  
Intento de conexión al puerto RDP (3389) con severidad crítica.

**Regla Wazuh:**
```xml
<rule id="100108" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">3389</field>
  <description>Intento de acceso remoto vía RDP</description>
  <mitre>
    <id>T1021.001</id> <!-- Remote Desktop Protocol -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 9 - 📡 Exfiltración DNS sospechosa

**Log:**
```text
ownapp:WARNING,10.1.1.10,8.8.8.8,40000,53,udp,909004,3
```

**Explicación:**  
Tráfico DNS a un servidor externo (Google) con severidad moderada.

**Regla Wazuh:**
```xml
<rule id="100109" level="5">
  <if_sid>100003</if_sid>
  <match>WARNING</match>
  <field name="puertodestino">53</field>
  <description>Tráfico DNS potencialmente anómalo</description>
  <mitre>
    <id>T1048.003</id> <!-- Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 10 - 🧷 Comunicación SMB interna sospechosa

**Log:**
```text
ownapp:ALERT,192.168.0.50,192.168.0.55,45000,445,tcp,101010,4
```

**Explicación:**  
Puerto 445 (SMB) usado en entorno interno sin justificación clara.

**Regla Wazuh:**
```xml
<rule id="100110" level="6">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">445</field>
  <description>Acceso sospechoso a SMB</description>
  <mitre>
    <id>T1021.002</id> <!-- SMB/Windows Admin Shares -->
  </mitre>
</rule>
```

---

## ✅ Recomendaciones para examen

- Practica escribir logs tú mismo y diseña reglas para ellos.
- Recuerda qué protocolos comunes corresponden a qué puertos:
  - `21` → FTP
  - `22` → SSH
  - `53` → DNS
  - `135` → RPC
  - `445` → SMB
  - `3389` → RDP
- Asócialos a técnicas MITRE relevantes para subir nivel profesional de tus reglas.



# 🧪 Ejercicios Avanzados Wazuh - Nivel Experto (Ejemplos 11 al 15)

Cinco escenarios complejos con logs y reglas avanzadas basadas en puertos, protocolos y contexto de MITRE ATT&CK.

---

## 🔁 Ejemplo 11 - 🔓 Intento de explotación por WinRM (puerto 5985)

**Log:**
```text
ownapp:DANGER,10.2.3.4,10.2.3.5,50000,5985,tcp,111111,5
```

**Explicación:**  
El puerto 5985 (Windows Remote Management) es usado en automatización. Intento de acceso con severidad crítica.

**Regla Wazuh:**
```xml
<rule id="100111" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">5985</field>
  <description>Intento de acceso vía WinRM detectado</description>
  <mitre>
    <id>T1021.006</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 12 - ⚠️ Proxy malicioso (puerto 8081 externo)

**Log:**
```text
ownapp:ALERT,192.168.1.90,172.217.0.1,44321,8081,tcp,222222,4
```

**Explicación:**  
Puerto 8081 expuesto a red externa puede ser indicio de uso de proxy no autorizado.

**Regla Wazuh:**
```xml
<rule id="100112" level="6">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">8081</field>
  <description>Posible uso de proxy malicioso</description>
  <mitre>
    <id>T1090.002</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 13 - 📥 Acceso anómalo a API web (puerto 8443)

**Log:**
```text
ownapp:WARNING,10.10.10.10,10.10.10.20,60001,8443,tcp,333333,3
```

**Explicación:**  
Puerto alternativo seguro (HTTPS/8443), posible API privada expuesta.

**Regla Wazuh:**
```xml
<rule id="100113" level="4">
  <if_sid>100003</if_sid>
  <match>WARNING</match>
  <field name="puertodestino">8443</field>
  <description>Acceso anómalo a API sobre HTTPS alternativo</description>
  <mitre>
    <id>T1190</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 14 - 🧨 Ataque por SMBv1 (puerto 137)

**Log:**
```text
ownapp:DANGER,172.20.1.1,172.20.1.2,4040,137,udp,444444,5
```

**Explicación:**  
Uso de NetBIOS/SMBv1 vulnerable por UDP. Riesgo crítico si está habilitado.

**Regla Wazuh:**
```xml
<rule id="100114" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">137</field>
  <description>Intento de explotación por SMBv1/NetBIOS</description>
  <mitre>
    <id>T1210</id>
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 15 - 📤 Comando a través de HTTPS sospechoso

**Log:**
```text
ownapp:ALERT,192.168.100.10,192.168.100.20,30000,443,tcp,555555,4
```

**Explicación:**  
HTTPS legítimo pero desde puerto de origen inusual puede encubrir shell o C2.

**Regla Wazuh:**
```xml
<rule id="100115" level="7">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">443</field>
  <field name="puertoorigen">30000</field>
  <description>Posible tráfico C2 encubierto sobre HTTPS</description>
  <mitre>
    <id>T1071.001</id>
  </mitre>
</rule>
```

---

## 📌 Recomendaciones

- Identifica puertos alternativos y protocolos inusuales.
- Aplica lógica condicional múltiple en las reglas.
- Justifica tu nivel de alerta con técnicas MITRE ATT&CK.
