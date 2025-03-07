"""
Code-Verschleierungstechniken
"""
import os
import random
import base64
import hashlib
import re
from datetime import datetime

from ..core.logger import logger

class CodeObfuscator:
    """Klasse für Code-Verschleierung und Anti-Analyse-Techniken"""
    
    def __init__(self):
        self.obfuscation_techniques = {
            "string_encoding": self._string_encoding,
            "control_flow_obfuscation": self._control_flow_obfuscation,
            "dead_code_insertion": self._dead_code_insertion,
            "variable_renaming": self._variable_renaming,
            "code_encryption": self._code_encryption
        }
        logger.info("[+] CodeObfuscator initialisiert")
    
    def execute(self):
        """Führt die Verschleierung aus"""
        logger.info("[+] Führe Code-Verschleierung aus")
        
        # In einer echten Anwendung würde hier der eigene Code verschleiert werden
        # In dieser Simulation führen wir nur eine Demo aus
        self._demonstrate_obfuscation()
        
        return True
    
    def _demonstrate_obfuscation(self):
        """Demonstriert verschiedene Verschleierungstechniken"""
        # Beispiel-Code
        sample_code = """
def check_system():
    import os
    import platform
    
    hostname = platform.node()
    os_info = platform.system() + " " + platform.release()
    
    if "Virtual" in os_info or "VM" in hostname:
        return False
    
    return True
    
def execute_payload():
    print("Executing payload...")
    # Payload execution would go here
    
if check_system():
    execute_payload()
"""
        
        logger.info("[+] Original-Code:")
        logger.info(sample_code)
        
        # Wende verschiedene Verschleierungstechniken an
        obfuscated_code = sample_code
        
        for technique_name, technique_func in self.obfuscation_techniques.items():
            logger.info(f"[+] Wende Verschleierungstechnik an: {technique_name}")
            try:
                obfuscated_code = technique_func(obfuscated_code)
            except Exception as e:
                logger.error(f"[-] Fehler bei Technik {technique_name}: {e}")
        
        logger.info("[+] Verschleierter Code:")
        logger.info(obfuscated_code)
    
    def _string_encoding(self, code):
        """Kodiert Strings im Code"""
        # Diese Implementation ist nur zur Demonstration, nicht für echte Verschleierung
        
        # Suche nach String-Literalen in Anführungszeichen
        pattern = r'("[^"\\]*(?:\\.[^"\\]*)*")|(' + r"'[^'\\]*(?:\\.[^'\\]*)*')"
        
        def encode_match(match):
            string = match.group(0)
            if not string:
                return string
            
            # Entferne Anführungszeichen
            content = string[1:-1]
            
            # Base64-Kodierung
            encoded = base64.b64encode(content.encode()).decode()
            
            # Ersetze den String durch eine Dekodierungsfunktion
            return f'base64.b64decode("{encoded}").decode()'
        
        # Ersetze Strings und füge Import hinzu
        modified_code = re.sub(pattern, encode_match, code)
        
        # Füge Import für base64 hinzu, falls noch nicht vorhanden
        if "import base64" not in modified_code:
            modified_code = "import base64\n" + modified_code
        
        return modified_code
    
    def _control_flow_obfuscation(self, code):
        """Verschleiert den Kontrollfluss im Code"""
        # Diese Implementation ist nur zur Demonstration, nicht für echte Verschleierung
        
        # Ersetze einfache if-Bedingungen durch komplexere Ausdrücke
        pattern = r'if\s+([^:]+):'
        
        def complex_condition(match):
            condition = match.group(1)
            # Erstelle komplexere Bedingung
            obfuscated = f"if (lambda x: x)({condition}):"
            return obfuscated
        
        return re.sub(pattern, complex_condition, code)
    
    def _dead_code_insertion(self, code):
        """Fügt toten Code hinzu, der nie ausgeführt wird"""
        # Diese Implementation ist nur zur Demonstration, nicht für echte Verschleierung
        
        # Liste von nutzlosen Funktionen
        dead_functions = [
            "\ndef _unused_function_1():\n    if False:\n        print('This will never execute')\n",
            "\ndef _calculate_unused():\n    result = []\n    for i in range(10):\n        result.append(i * i)\n    return sum(result) if False else None\n",
            "\ndef _dead_loop():\n    while False:\n        print('Dead loop')\n"
        ]
        
        # Wähle eine zufällige Funktion aus
        dead_function = random.choice(dead_functions)
        
        # Füge die Funktion zum Code hinzu
        return code + dead_function
    
    def _variable_renaming(self, code):
        """Benennt Variablen um, um den Code schwerer lesbar zu machen"""
        # Diese Implementation ist nur zur Demonstration, nicht für echte Verschleierung
        
        # Einfache Ersetzung von gängigen Variablennamen
        renames = {
            "hostname": "_a" + hashlib.md5(b"hostname").hexdigest()[:5],
            "os_info": "_b" + hashlib.md5(b"os_info").hexdigest()[:5],
            "check_system": "_c" + hashlib.md5(b"check_system").hexdigest()[:5],
            "execute_payload": "_d" + hashlib.md5(b"execute_payload").hexdigest()[:5]
        }
        
        result = code
        for original, new_name in renames.items():
            result = re.sub(r'\b' + re.escape(original) + r'\b', new_name, result)
        
        return result
    
    def _code_encryption(self, code):
        """Simuliert die Verschlüsselung von Code"""
        # Diese Implementation ist nur zur Demonstration, nicht für echte Verschleierung
        
        # Demonstriert einen einfachen XOR mit einem Schlüssel
        def xor_encrypt(text, key=42):
            return ''.join(chr(ord(c) ^ key) for c in text)
        
        # Verschlüssele den Code
        encrypted = xor_encrypt(code)
        encrypted_b64 = base64.b64encode(encrypted.encode()).decode()
        
        # Erstelle Code, der sich selbst entschlüsselt und ausführt
        decryption_code = f"""
# Selbstentschlüsselnder Code
import base64
import sys

def xor_decrypt(encrypted, key=42):
    return ''.join(chr(ord(c) ^ key) for c in encrypted)

# Verschlüsselter Code
encrypted_code = "{encrypted_b64}"

# Entschlüssele und führe den Code aus
decrypted = xor_decrypt(base64.b64decode(encrypted_code).decode())