"""
Simulierte Ransomware-Funktionalität
"""
import os
import random
import threading
import time
from datetime import datetime

from ..core.logger import logger
from ..core.config import SIMULATION_MODE
from ..utils.crypto import EncryptionModule

class RansomwarePayload:
    """Simulierter Ransomware-Angriff"""
    
    def __init__(self):
        self.encryption_key = None
        self.encrypted_files = []
        self.payment_address = self._generate_fake_address()
        self.ransom_amount = random.uniform(0.5, 5.0)  # BTC
        self.deadline_hours = random.randint(48, 168)  # 2-7 Tage
        logger.info("[+] RansomwarePayload initialisiert")
    
    def execute(self):
        """Simuliert einen Ransomware-Angriff"""
        if not SIMULATION_MODE:
            logger.warning("[!] Ransomware-Ausführung im Nicht-Simulationsmodus deaktiviert")
            return False
        
        logger.info("[+] Ransomware-Payload wird ausgeführt (simuliert)")
        
        # Generiere Schlüssel
        self.encryption_key = EncryptionModule.generate_key()
        logger.info(f"[+] Verschlüsselungs-Schlüssel generiert: {self.encryption_key[:10]}... (simuliert)")
        
        # Simuliere das Verschlüsseln von Dateien
        self._simulate_encryption()
        
        # Simuliere das Anzeigen einer Ransomware-Nachricht
        self._show_ransom_note()
        
        return True
    
    def _simulate_encryption(self):
        """Simuliert das Verschlüsseln von Dateien"""
        # Simuliere Dateilisten für verschiedene Verzeichnisse
        directories = ["Dokumente", "Bilder", "Videos", "Desktop", "Downloads"]
        file_extensions = [
            ".doc", ".docx", ".pdf", ".xlsx", ".pptx", ".txt",  # Dokumente
            ".jpg", ".png", ".gif", ".bmp", ".tiff",            # Bilder
            ".mp4", ".avi", ".mov", ".mkv",                     # Videos
            ".zip", ".rar", ".7z",                              # Archive
            ".sql", ".db", ".accdb"                             # Datenbanken
        ]
        
        # Simuliere Verschlüsselung in jedem Verzeichnis
        encrypted_count = 0
        for directory in directories:
            # Simuliere 5-15 Dateien pro Verzeichnis
            num_files = random.randint(5, 15)
            
            for i in range(num_files):
                file_ext = random.choice(file_extensions)
                file_name = f"{directory}/datei_{i}{file_ext}"
                
                # Simuliere Dateigrößen für realistische Verschlüsselungszeiten
                file_size_mb = random.uniform(0.1, 50.0)  # 100KB bis 50MB
                
                logger.info(f"[+] Verschlüssele Datei: {file_name} ({file_size_mb:.2f} MB) (simuliert)")
                
                # Simuliere die Verschlüsselung
                encrypted_file = {
                    "path": file_name,
                    "size_mb": file_size_mb,
                    "original_extension": file_ext,
                    "encrypted_extension": ".encrypted",
                    "encryption_time": datetime.now().isoformat()
                }
                
                self.encrypted_files.append(encrypted_file)
                encrypted_count += 1
                
                # Kleine Pause, um die Simulation natürlicher zu machen
                time.sleep(0.05)
        
        logger.info(f"[+] Verschlüsselung abgeschlossen: {encrypted_count} Dateien verschlüsselt (simuliert)")
    
    def _show_ransom_note(self):
        """Simuliert das Anzeigen einer Ransomware-Nachricht"""
        ransom_note = f"""
        ACHTUNG! IHRE DATEIEN WURDEN VERSCHLÜSSELT!
        ----------------------------------------------
        Alle Ihre Dokumente, Fotos, Videos und anderen wichtigen Dateien wurden verschlüsselt.
        
        Um Ihre Dateien wiederherzustellen, müssen Sie einen Entschlüsselungs-Schlüssel erwerben.
        
        ANLEITUNG ZUR ZAHLUNG:
        1. Senden Sie {self.ransom_amount:.2f} BTC an die folgende Adresse:
           {self.payment_address}
        
        2. Senden Sie eine E-Mail an recover@example.com mit folgenden Informationen:
           - Ihrer persönlichen ID: {random.randint(10000, 99999)}
           - Der Transaktions-ID der Zahlung
        
        3. Sie erhalten den Entschlüsselungs-Schlüssel innerhalb von 24 Stunden nach Zahlungseingang.
        
        WICHTIGE HINWEISE:
        - Sie haben {self.deadline_hours} Stunden Zeit, um zu zahlen. Danach verdoppelt sich der Betrag.
        - Versuchen Sie nicht, die Dateien selbst zu entschlüsseln. Dies führt zu permanentem Datenverlust.
        - Versuchen Sie nicht, Ihr System neu zu installieren oder Ihre Festplatte zu formatieren.
        
        HINWEIS: Dies ist nur eine Simulation für Bildungszwecke!
        In einer echten Situation würde hier eine Anleitung zur Zahlung stehen.
        """
        
        logger.info("[+] Ransomware-Nachricht angezeigt (simuliert):")
        for line in ransom_note.strip().split('\n'):
            logger.info(f"    {line}")
        
        # Simuliere das Ändern des Desktop-Hintergrunds
        logger.info("[+] Desktop-Hintergrund mit Ransomware-Nachricht geändert (simuliert)")
        
        # Simuliere das Erstellen von Ransom-Notizen in jedem Verzeichnis
        directories = ["Dokumente", "Bilder", "Videos", "Desktop", "Downloads"]
        for directory in directories:
            logger.info(f"[+] Ransom-Notiz in {directory} erstellt: IHRE_DATEIEN_WURDEN_VERSCHLUESSELT.txt (simuliert)")
    
    def _generate_fake_address(self):
        """Generiert eine simulierte Bitcoin-Adresse"""
        return "bc1" + "".join(random.choice("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz") for _ in range(39))
    
    def decrypt_files(self):
        """Simuliert die Entschlüsselung aller Dateien"""
        logger.info("[+] Beginne Entschlüsselung aller Dateien (simuliert)")
        
        # Zähle die Gesamtgröße der zu entschlüsselnden Dateien
        total_size_mb = sum(file["size_mb"] for file in self.encrypted_files)
        logger.info(f"[+] Gesamtgröße zu entschlüsselnder Dateien: {total_size_mb:.2f} MB (simuliert)")
        
        # Simuliere den Entschlüsselungsprozess für jede Datei
        for i, file in enumerate(self.encrypted_files):
            progress = (i + 1) / len(self.encrypted_files) * 100
            logger.info(f"[+] Entschlüssele Datei: {file['path']} ({progress:.1f}%) (simuliert)")
            time.sleep(0.05)
        
        logger.info(f"[+] Alle {len(self.encrypted_files)} Dateien wurden entschlüsselt (simuliert)")
        
        # Simuliere das Entfernen der Ransom-Notizen
        logger.info("[+] Entferne Ransom-Notizen (simuliert)")
        
        # Simuliere das Wiederherstellen des Desktop-Hintergrunds
        logger.info("[+] Desktop-Hintergrund wiederhergestellt (simuliert)")
        
        # Leere die Liste der verschlüsselten Dateien
        self.encrypted_files = []
        
        return True
    
    def get_status(self):
        """Gibt den Status der Ransomware zurück"""
        return {
            "encrypted_files": len(self.encrypted_files),
            "total_size_mb": sum(file["size_mb"] for file in self.encrypted_files),
            "payment_address": self.payment_address,
            "ransom_amount": self.ransom_amount,
            "deadline_hours": self.deadline_hours,
            "encryption_key_available": self.encryption_key is not None
        }