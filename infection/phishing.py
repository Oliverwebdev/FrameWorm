"""
Social Engineering und Phishing-Mechanismen
"""
import os
import random
import time
from datetime import datetime

from ..core.logger import logger
from ..core.config import SIMULATION_MODE

class PhishingAttack:
    """Klasse für simulierte Phishing-Angriffe"""
    
    def __init__(self, target_brand=None):
        self.target_brand = target_brand
        self.phishing_site = None
        self.email_templates = []
        self.credentials_stolen = []
        logger.info(f"[+] PhishingAttack initialisiert, Zielmarke: {target_brand or 'Nicht spezifiziert'}")
        self._initialize_templates()
    
    def _initialize_templates(self):
        """Initialisiert E-Mail-Templates für Phishing"""
        self.email_templates = [
            {
                "subject": "Dringende Sicherheitsbenachrichtigung für Ihr Konto",
                "body": "Sehr geehrter Kunde, wir haben verdächtige Aktivitäten auf Ihrem Konto festgestellt...",
                "type": "account_security"
            },
            {
                "subject": "Ihre Zahlung wurde abgelehnt",
                "body": "Ihre letzte Zahlung wurde abgelehnt. Bitte aktualisieren Sie Ihre Zahlungsinformationen...",
                "type": "payment_issue"
            },
            {
                "subject": "Ihr Paket wird bald geliefert",
                "body": "Ihr Paket ist unterwegs. Verfolgen Sie Ihr Paket durch Anmeldung bei Ihrem Konto...",
                "type": "delivery"
            }
        ]
        logger.info(f"[+] {len(self.email_templates)} E-Mail-Templates geladen")
    
    def execute(self):
        """Führt den simulierten Phishing-Angriff aus"""
        if not SIMULATION_MODE:
            logger.warning("[!] Phishing-Angriffe sind im Nicht-Simulationsmodus deaktiviert")
            return False
        
        # Zielmarke auswählen, falls nicht angegeben
        if not self.target_brand:
            popular_brands = ["Amazon", "PayPal", "Microsoft", "Apple", "Google", "Facebook", "Netflix"]
            self.target_brand = random.choice(popular_brands)
            logger.info(f"[+] Zufällige Marke für Phishing ausgewählt: {self.target_brand}")
        
        # Erstelle gefälschte Phishing-Website
        self.phishing_site = self._create_fake_website()
        
        # Wähle ein geeignetes E-Mail-Template
        template = random.choice(self.email_templates)
        
        # Simuliere Versand von Phishing-E-Mails
        num_emails = random.randint(10, 50)
        logger.info(f"[+] Simuliere Versand von {num_emails} Phishing-E-Mails mit Vorlage: {template['subject']}")
        
        # Simuliere Ergebnisse
        click_rate = random.uniform(0.05, 0.15)  # 5-15% Klickrate
        credential_rate = random.uniform(0.4, 0.7)  # 40-70% der Klicker geben Anmeldedaten ein
        
        clicks = int(num_emails * click_rate)
        creds = int(clicks * credential_rate)
        
        logger.info(f"[+] Simulierte Ergebnisse: {clicks} Klicks, {creds} gestohlene Anmeldeinformationen")
        
        # Simuliere gestohlene Anmeldeinformationen
        for i in range(creds):
            fake_cred = {
                "username": f"user{random.randint(100, 999)}@example.com",
                "password": f"Password{random.randint(100, 999)}!",
                "timestamp": datetime.now().isoformat()
            }
            self.credentials_stolen.append(fake_cred)
            logger.info(f"[+] Simulierte gestohlene Anmeldedaten: {fake_cred['username']}")
        
        return True
    
    def _create_fake_website(self):
        """Simuliert das Erstellen einer gefälschten Website für Phishing"""
        logger.info(f"[+] Erstelle gefälschte Website für {self.target_brand} (simuliert)")
        
        # Simuliere die Erstellung einer Phishing-Seite
        domain_variations = [
            f"{self.target_brand.lower()}-secure.com",
            f"{self.target_brand.lower()}-login.net",
            f"secure-{self.target_brand.lower()}.com",
            f"login-{self.target_brand.lower()}.org",
            f"{self.target_brand.lower()}.secure-site.com"
        ]
        
        domain = random.choice(domain_variations)
        
        # Simuliere die Entwicklung der gefälschten Website
        logger.info(f"[+] Registriere Domain {domain} (simuliert)")
        logger.info(f"[+] Kopiere Original-Website-Design von {self.target_brand} (simuliert)")
        logger.info(f"[+] Implementiere gefälschtes Login-Formular (simuliert)")
        logger.info(f"[+] Richte Datenerfassung für gestohlene Anmeldedaten ein (simuliert)")
        
        # Generiere eine Beschreibung der gefälschten Website
        fake_site = {
            "domain": domain,
            "target_brand": self.target_brand,
            "ssl_certificate": random.choice([True, False]),
            "creation_date": datetime.now().isoformat(),
            "status": "active"
        }
        
        logger.info(f"[+] Gefälschte Website für {self.target_brand} unter {domain} erstellt (simuliert)")
        return fake_site
    
    def get_results(self):
        """Gibt Ergebnisse des Phishing-Angriffs zurück"""
        return {
            "target_brand": self.target_brand,
            "phishing_site": self.phishing_site,
            "emails_sent": random.randint(10, 50),
            "credentials_stolen": self.credentials_stolen,
            "success_rate": len(self.credentials_stolen) / (random.randint(10, 50)) if self.credentials_stolen else 0
        }