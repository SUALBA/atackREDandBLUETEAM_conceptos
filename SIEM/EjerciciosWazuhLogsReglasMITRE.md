


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
