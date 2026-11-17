# AxoBackup · Sistema de Respaldo Multiplataforma

Herramienta de software libre ligera y portátil con interfaz gráfica (GUI) orientada a la protección de datos, código fuente y documentos críticos en entornos de desarrollo y sistemas de escritorio (Windows y Linux).

---

## Características Principales

- **Multiplataforma:** Compatible con sistemas Windows y distribuciones GNU/Linux (Ubuntu).
- **Interfaz Gráfica Intuitiva:** Desarrollada con cuadros de diálogo nativos (`tkinter`) para seleccionar fácilmente carpetas de origen y destino sin depender de comandos complejos.
- **Compresión Automática:** Opción integrada para empaquetar los respaldos directamente en formato `.zip` con marcas de tiempo (`YYYY-MM-DD_HH-MM-SS`).
- **Portabilidad Absoluta:** Compilado como ejecutable independiente para que funcione de inmediato con un solo clic, sin instalaciones previas.

---

## Tecnologías y Stack

- **Lenguaje:** Python 3
- **Librerías GUI:** `tkinter`, `shutil`, `datetime`
- **Empaquetado:** PyInstaller / Pipx

---

## Uso del Ejecutable 

1. Descarga el ejecutable desde la carpeta `dist/` o los releases del repositorio.
2. Haz doble clic sobre el archivo `axobackup` (Linux) o `axobackup.exe` (Windows).
3. Selecciona la carpeta que deseas respaldar haciendo clic en **Examinar**.
4. Selecciona el destino del respaldo.
5. Haz clic en **INICIAR RESPALDO** y verifica el registro de éxito en tiempo real.

---

## Autor / Desarrollador

* **Desarrollador:** **@AxoD** (Adderly Xavier Orozco de la Hoz)
* **GitHub:** [@AxoD33](https://github.com/AxoD33)
