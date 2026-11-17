import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class AxoBackupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AxoBackup — Sistema de Respaldo Multiplataforma")
        self.root.geometry("600x520")
        self.root.config(bg="#0f172a")

        # Título institucional / cabecera
        header = tk.Label(root, text="🛡️ AXOBACKUP · RESPALDO SEGURO", font=("Arial", 14, "bold"), bg="#0f172a", fg="#38bdf8")
        header.pack(pady=15)

        # Marco de Selección de Origen
        frame_src = tk.Frame(root, bg="#1e293b", padx=10, pady=10)
        frame_src.pack(fill="x", padx=20, pady=5)
        
        tk.Label(frame_src, text="Carpeta a Respaldar:", font=("Arial", 10), bg="#1e293b", fg="#e2e8f0").pack(anchor="w")
        self.txt_src = tk.Entry(frame_src, width=50)
        self.txt_src.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        tk.Button(frame_src, text="Examinar", command=self.select_source, bg="#334155", fg="white", cursor="hand2").pack(side="right", padx=5)

        # Marco de Selección de Destino
        frame_dst = tk.Frame(root, bg="#1e293b", padx=10, pady=10)
        frame_dst.pack(fill="x", padx=20, pady=5)
        
        tk.Label(frame_dst, text="Destino del Respaldo:", font=("Arial", 10), bg="#1e293b", fg="#e2e8f0").pack(anchor="w")
        self.txt_dst = tk.Entry(frame_dst, width=50)
        self.txt_dst.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        tk.Button(frame_dst, text="Examinar", command=self.select_destination, bg="#334155", fg="white", cursor="hand2").pack(side="right", padx=5)

        # Opciones de Compresión
        frame_opt = tk.Frame(root, bg="#0f172a", padx=10, pady=5)
        frame_opt.pack(fill="x", padx=20)
        
        self.zip_var = tk.BooleanVar(value=True)
        chk_zip = tk.Checkbutton(frame_opt, text="Comprimir en formato ZIP (.zip)", variable=self.zip_var, bg="#0f172a", fg="#e2e8f0", selectcolor="#1e293b", activebackground="#0f172a", activeforeground="white")
        chk_zip.pack(anchor="w")

        # Botón de Ejecución
        btn_run = tk.Button(root, text="INICIAR RESPALDO", command=self.run_backup, bg="#059669", fg="white", font=("Arial", 11, "bold"), padx=10, pady=8, cursor="hand2")
        btn_run.pack(pady=15)

        # Consola de Registros (Logs)
        self.log_area = scrolledtext.ScrolledText(root, width=70, height=10, bg="#020617", fg="#34d399", font=("Courier", 9))
        self.log_area.pack(padx=20, pady=5)
        self.log_area.insert(tk.END, "[Sistema] Listo para iniciar respaldo. Autor: @AxoD\n")

    def select_source(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.txt_src.delete(0, tk.END)
            self.txt_src.insert(0, dir_path)

    def select_destination(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.txt_dst.delete(0, tk.END)
            self.txt_dst.insert(0, dir_path)

    _log_area = property(lambda self: self.log_area)

    def log(self, message):
        self.log_area.insert(tk.END, f"{message}\n")
        self.log_area.see(tk.END)

    def run_backup(self):
        src = self.txt_src.get()
        dst = self.txt_dst.get()

        if not src or not dst:
            messagebox.showerror("Error", "Por favor selecciona la carpeta de origen y la de destino.")
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = os.path.basename(src)
        
        self.log(f"\n[Proceso] Iniciando respaldo de: {folder_name}...")

        try:
            if self.zip_var.get():
                # Modo Comprimido ZIP
                backup_filename = os.path.join(dst, f"Backup_{folder_name}_{timestamp}")
                shutil.make_archive(backup_filename, 'zip', src)
                self.log(f"[Éxito] Respaldo ZIP creado en: {backup_filename}.zip")
            else:
                # Modo Copia de Carpeta Directa
                dest_path = os.path.join(dst, f"Backup_{folder_name}_{timestamp}")
                shutil.copytree(src, dest_path)
                self.log(f"[Éxito] Carpeta copiada en: {dest_path}")

            messagebox.สำเร็จ("¡Completado!", "El respaldo se ha generado exitosamente.") if hasattr(messagebox, "สำเร็จ") else messagebox.showinfo("¡Completado!", "El respaldo se ha generado exitosamente.")
        
        except Exception as e:
            self.log(f"[Error] Falló el respaldo: {str(e)}")
            messagebox.showerror("Error", f"Ocurrió un error durante el respaldo:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AxoBackupApp(root)
    root.mainloop()