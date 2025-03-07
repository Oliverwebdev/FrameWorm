"""
Simulierte Keylogger-Funktionalität
"""
import os
import random
import threading
import time
from datetime import datetime

from ..core.logger import logger
from ..core.config import SIMULATION_MODE

class KeyloggerPayload:
    """Simulierter Keylogger"""
    
    def __init__(self):
        self.captured_keys = []
        self.running = False
        self.capture_thread = None
        self.screenshots = []
        logger.info("[+] KeyloggerPayload initialisiert")
    
    def execute(self):
        """Simuliert einen Keylogger"""
        if not SIMULATION_MODE:
            logger.warning("[!] Keylogger-Ausführung im Nicht-Simulationsmodus deaktiviert")
            return False
        
        logger.info("[+] Keylogger gestartet (simuliert)")
        self.running = True
        
        # Starte den Erfassungs-Thread
        self.capture_thread = threading.Thread(target=self._simulate_key_capture)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        
        return True
    
    def _simulate_key_capture(self):
        """Simuliert das Erfassen von Tastenanschlägen in einem Thread"""
        sample_keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        special_sequences = ["[ENTER]", "[TAB]", "[CTRL+C]", "[CTRL+V]", "[BACKSPACE]"]
        
        # Simuliere einige häufig eingegebene Wörter
        common_words = ["password", "login", "username", "email", "secret", "admin", "user", 
                        "bank", "account", "credit", "card", "transfer", "money", "private"]
        
        # Simuliere typische Sätze
        common_phrases = [
            "my password is ",
            "login credentials: ",
            "username: ",
            "email: ",
            "credit card number: ",
            "the transaction id is ",
            "please transfer to account "
        ]
        
        while self.running:
            # Manchmal vollständige Wörter/Phrasen simulieren
            if random.random() > 0.7:  # 30% Chance auf ein komplettes Wort/Phrase
                if random.random() > 0.5:  # 50% Chance auf Phrase vs. Wort
                    phrase = random.choice(common_phrases)
                    for char in phrase:
                        self.captured_keys.append(char)
                        time.sleep(random.uniform(0.05, 0.15))
                    
                    # Manchmal ein Wort an die Phrase anhängen
                    if "password" in phrase or "username" in phrase:
                        word = random.choice(common_words)
                        for char in word:
                            self.captured_keys.append(char)
                            time.sleep(random.uniform(0.05, 0.15))
                else:
                    word = random.choice(common_words)
                    for char in word:
                        self.captured_keys.append(char)
                        time.sleep(random.uniform(0.05, 0.15))
                    
                # Füge manchmal ein Leerzeichen oder Sonderzeichen hinzu
                if random.random() > 0.3:
                    self.captured_keys.append(" ")
            else:
                # Simuliere einen einzelnen Tastenanschlag
                if random.random() > 0.9:  # 10% Chance auf spezielle Taste
                    key = random.choice(special_sequences)
                else:
                    key = random.choice(sample_keys)
                
                self.captured_keys.append(key)
            
            # Simuliere gelegentliche Screenshots
            if random.random() > 0.95:  # 5% Chance pro Tastendruck
                self._take_simulated_screenshot()
            
            # Simuliertes Senden der gesammelten Daten, wenn genügend vorhanden sind
            if len(self.captured_keys) >= 100:
                self._send_captured_data()
            
            # Zufällige Verzögerung zwischen Tastendrücken
            time.sleep(random.uniform(0.1, 0.5))
    
    def _take_simulated_screenshot(self):
        """Simuliert das Erstellen eines Screenshots"""
        timestamp = datetime.now().isoformat()
        screenshot_info = {
            "timestamp": timestamp,
            "resolution": f"{random.choice([1920, 2560, 3440, 1280])}x{random.choice([1080, 1440, 1200, 720])}",
            "size_kb": random.randint(100, 5000),
            "active_window": random.choice([
                "Google Chrome", "Microsoft Outlook", "Microsoft Word",
                "Slack", "Terminal", "File Explorer", "Internet Banking", "Password Manager"
            ])
        }
        
        self.screenshots.append(screenshot_info)
        logger.info(f"[+] Screenshot erstellt: {screenshot_info['active_window']} ({screenshot_info['resolution']}) (simuliert)")
    
    def _send_captured_data(self):
        """Simuliert das Senden der gesammelten Daten"""
        data = ''.join(self.captured_keys)
        logger.info(f"[+] Keylogger-Daten gesendet: {data[:50]}... (simuliert)")
        self.captured_keys = []  # Leere den Puffer nach dem Senden
        
        # Sende auch Screenshots, wenn vorhanden
        if self.screenshots:
            logger.info(f"[+] {len(self.screenshots)} Screenshots gesendet (simuliert)")
            self.screenshots = []
    
    def get_captured_data(self):
        """Gibt die aktuell erfassten Daten zurück"""
        return {
            "keystrokes": ''.join(self.captured_keys),
            "keystroke_count": len(self.captured_keys),
            "screenshots": len(self.screenshots),
            "running_since": datetime.now().isoformat() if self.running else None
        }
    
    def stop(self):
        """Stoppt den Keylogger"""
        logger.info("[+] Keylogger gestoppt (simuliert)")
        self.running = False
        if self.capture_thread and self.capture_thread.is_alive():
            self.capture_thread.join(timeout=1.0)
        return True