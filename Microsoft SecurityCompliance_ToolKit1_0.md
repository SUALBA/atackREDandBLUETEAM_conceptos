# Microsoft Security Compliance Toolkit (SCT) 1.0 - Guía Completa

## Introducción
El **Microsoft Security Compliance Toolkit 1.0** es un conjunto de herramientas diseñado para implementar, analizar y gestionar configuraciones de seguridad estandarizadas en entornos Windows. Forma parte del marco de seguridad de Microsoft y se alinea con el **Windows Security Configuration Framework**.

## Componentes Principales

| Herramienta | Descripción | Casos de Uso |
|-------------|-------------|--------------|
| **Policy Analyzer** | Compara múltiples GPOs y perfiles de seguridad | Auditorías, identificación de desviaciones |
| **LGPO.exe** | Versión local del procesador de GPO | Implementación en sistemas no unidos a dominio |
| **Baseline Files** | Plantillas de seguridad preconfiguradas | Hardening rápido según mejores prácticas |

## Versiones Compatibles
- ✅ Windows 10 (versiones 1607 en adelante)
- ✅ Windows 11 (todas versiones)
- ✅ Windows Server 2016/2019/2022
- ❌ Windows 7/8.1 (requiere versiones anteriores del toolkit)

## Flujo de Trabajo Recomendado

1. **Descarga de Baseline**
   ```powershell
   # Ejemplo de descarga desde Microsoft
   Invoke-WebRequest -Uri "https://aka.ms/securitybaseline" -OutFile "C:\baselines.zip"

***
>© 2025 [sualba.dev] Todos los derechos reservados
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.