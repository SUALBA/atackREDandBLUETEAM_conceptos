# 🚨 Path Traversal: Guía Completa de Seguridad Web

> **⚠️ Advertencia**: Esta información es para fines educativos y de seguridad defensiva únicamente.

---

## 🔍 ¿Qué es Path Traversal?

El **Path Traversal** (también conocido como *Directory Traversal* o *Dot-Dot-Slash Attack*) es una vulnerabilidad crítica de seguridad web que permite a atacantes acceder a archivos y directorios **fuera del directorio raíz** de la aplicación web.

### 🎯 Nombres Alternativos
- **Directory Traversal**
- **Dot-Dot-Slash Attack**
- **Backtracking Attack**
- **Path Climbing**

---

## ⚙️ ¿Cómo Funciona el Ataque?

### 🛠️ Secuencias de Ataque Comunes

| Sistema | Secuencia | Descripción |
|---------|-----------|-------------|
| 🐧 **Unix/Linux** | `../` | Navega hacia el directorio padre |
| 🪟 **Windows** | `..\` | Equivalente en Windows |
| 🌐 **URL Encoded** | `%2e%2e%2f` | Versión codificada para evadir filtros |
| 🔄 **Double Encoded** | `%252e%252e%252f` | Doble codificación |

### 📋 Ejemplo Práctico

#### ✅ Uso Legítimo
```http
https://ejemplo.com/download?file=documento.pdf
```

#### ❌ Ataque Path Traversal
```http
https://ejemplo.com/download?file=../../../etc/passwd
https://ejemplo.com/download?file=..\..\..\..\windows\system32\config\SAM
```

---

## 🎯 Objetivos Comunes de los Atacantes

### 📁 Archivos Críticos en Linux/Unix
- `/etc/passwd` - Lista de usuarios del sistema
- `/etc/shadow` - Contraseñas hasheadas
- `/etc/hosts` - Configuración de hosts
- `/var/log/auth.log` - Logs de autenticación
- `/home/user/.ssh/id_rsa` - Claves SSH privadas

### 📁 Archivos Críticos en Windows
- `C:\Windows\System32\config\SAM` - Base de datos de cuentas
- `C:\Windows\System32\drivers\etc\hosts` - Archivo hosts
- `C:\inetpub\wwwroot\web.config` - Configuración web
- `C:\Windows\win.ini` - Configuración del sistema

---

## 🛡️ Métodos de Prevención

### 1. 🔍 **Validación de Entrada**
```python
# Ejemplo en Python
import os

def validate_filename(filename):
    # Rechazar caracteres peligrosos
    dangerous_chars = ['..', '/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in dangerous_chars:
        if char in filename:
            return False
    return True
```

### 2. 📋 **Listas Blancas (Whitelist)**
```javascript
// Ejemplo en JavaScript
const allowedFiles = ['documento.pdf', 'imagen.jpg', 'reporte.docx'];

function isFileAllowed(filename) {
    return allowedFiles.includes(filename);
}
```

### 3. 🏠 **Sandboxing**
```php
<?php
// Ejemplo en PHP
$baseDir = '/var/www/uploads/';
$requestedFile = $_GET['file'];
$fullPath = realpath($baseDir . $requestedFile);

// Verificar que el archivo esté dentro del directorio permitido
if (strpos($fullPath, realpath($baseDir)) !== 0) {
    die('Acceso denegado');
}
?>
```

### 4. ✅ **Canonicalización**
```java
// Ejemplo en Java
import java.io.File;

public boolean isPathSafe(String userPath, String basePath) {
    try {
        File baseDir = new File(basePath).getCanonicalFile();
        File userFile = new File(baseDir, userPath).getCanonicalFile();
        return userFile.getCanonicalPath().startsWith(baseDir.getCanonicalPath());
    } catch (IOException e) {
        return false;
    }
}
```

---

## 📊 Niveles de Impacto

### 🔴 **Crítico**
- Acceso a archivos de configuración del sistema
- Lectura de credenciales y contraseñas
- Exposición de claves privadas

### 🟡 **Alto**
- Acceso a código fuente de la aplicación
- Lectura de logs del sistema
- Información sensible de usuarios

### 🟢 **Medio**
- Enumeración de estructura de directorios
- Acceso a archivos de configuración de aplicaciones

---

## 🔧 Configuración de Servidor Web

### 🌐 **Apache (.htaccess)**
```apache
# Bloquear acceso a directorios padre
<Files ~ "^\.">
    Order allow,deny
    Deny from all
</Files>

# Bloquear patrones peligrosos
RewriteEngine On
RewriteRule \.\. - [F]
```

### ⚡ **Nginx**
```nginx
# Bloquear path traversal
location ~ /\. {
    deny all;
}

location ~ \.\. {
    deny all;
}
```

---

## 🧪 Herramientas de Testing

### 🔍 **Herramientas Automatizadas**
- **Burp Suite** - Proxy y scanner web
- **OWASP ZAP** - Herramienta de testing gratuita
- **Nikto** - Scanner de vulnerabilidades web
- **DirBuster** - Enumeración de directorios

### 📝 **Payloads de Prueba**
```
../
..\/
..%2f
..%5c
%2e%2e%2f
%2e%2e%5c
..%252f
..%255c
```

---

## 📚 Referencias y Recursos

### 📖 **Documentación Oficial**
- [OWASP Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [CWE-22: Path Traversal](https://cwe.mitre.org/data/definitions/22.html)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

### 🎓 **Recursos de Aprendizaje**
- **OWASP WebGoat** - Aplicación vulnerable para práctica
- **Damn Vulnerable Web Application (DVWA)**
- **bWAPP** - Aplicación web vulnerable

---

## ✅ Checklist de Seguridad

- [ ] Implementar validación de entrada robusta
- [ ] Usar listas blancas para archivos permitidos
- [ ] Configurar sandboxing adecuado
- [ ] Implementar canonicalización de rutas
- [ ] Configurar restricciones a nivel de servidor
- [ ] Realizar testing de penetración regular
- [ ] Mantener logs de acceso detallados
- [ ] Capacitar al equipo de desarrollo

---

> 💡 **Recuerda**: La seguridad es un proceso continuo, no un destino. Mantén tus sistemas actualizados y revisa regularmente las configuraciones de seguridad.

---
*📅 Documento actualizado: Julio 2025*