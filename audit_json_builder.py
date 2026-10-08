"""
tests/test_sections/conftest.py
─────────────────────────────────────────────────────────────────────────────
Fixtures communes à tous les tests de sections.
Pas de dépendances réseau ni LLM — 100% mockées.
"""
import pytest

# ── Valeurs partagées (définies une seule fois) ─────────────────────────────
AUDIT_ID = "audit_test_001"
START_DATE = "2026-01-10"
END_DATE = "2026-01-24"
AUDIT_TYPE = "Pentest externe"
TARGET_SCOPE = "Application web + API"
TARGET_HOST = "api.acme.fr"

# ── Fabriques de données ────────────────────────────────────────────────────
def make_stakeholder(**overrides):
    """Interlocuteur côté client."""
    return {
        "name": "Alice Martin",
        "role": "RSSI",
        "email": "a.martin@acme.fr",
        "interview_date": "2026-01-11",
        **overrides,
    }
 
 
def make_client(**overrides):
    """Client audité."""
    return {
        "name": "ACME Corp",
        "sector": "Finance",
        "stakeholders": [make_stakeholder()],
        **overrides,
    }
 
 
def make_mission(**overrides):
    """Cadre de la mission d'audit."""
    return {
        "qualified": True,
        "audit_type": AUDIT_TYPE,
        "activities": ["Reconnaissance", "Exploitation"],
        "classification": "CONFIDENTIEL",
        "recipients": ["RSSI", "DSI"],
        "scope": TARGET_HOST,
        "objectives": ["Identifier les vulnérabilités critiques"],
        "scope_reservations": ["Aucun accès physique"],
        "start_date": START_DATE,
        "end_date": END_DATE,
        **overrides,
    }
 
 
def make_team_member(**overrides):
    """Membre de l'équipe d'audit."""
    return {
        "name": "Bob Dupont",
        "role": "Lead pentester",
        "email": "b.dupont@cs.fr",
        "phone": "06xxxxxxxx",
        **overrides,
    }
 
 
def make_reference_doc(**overrides):
    """Document de référence cité dans le rapport."""
    return {
        "title": "Guide PASSI",
        "author": "ANSSI",
        "date": "2022-01-01",
        "type": "Référentiel",
        "version": "2.0",
        **overrides,
    }
 
 
def make_finding(**overrides):
    """Vulnérabilité relevée pendant l'audit."""
    return {
        "id": "F-001",
        "titre": "Injection SQL",
        "criticite": "Critique",
        "asset": f"{TARGET_HOST}/login",
        "source_outil": "ZAP",
        "statut": "brouillon",
        "cvss_score": 9.8,
        "en_exploitation_active": True,
        "attck_tactic": "Initial Access",
        "attck_technique": "T1190",
        "effort_remediation": "Faible",
        "short_term_recommandation": "Utiliser des requêtes préparées",
        **overrides,
    }
 

# ── Fixtures ────────────────────────────────────────────────────────────────
@pytest.fixture
def base_context():
    """Contexte d'audit complet et valide, utilisé par défaut dans les tests."""
    return {
        "audit_id": AUDIT_ID,
        "start_date": START_DATE,
        "end_date": END_DATE,
        "audit_type": AUDIT_TYPE,
        "target_scope": TARGET_SCOPE,
        "client": make_client(),
        "mission": make_mission(),
        "team": [make_team_member()],
        "reference_docs": [make_reference_doc()],
    }
 
 
@pytest.fixture
def sample_findings():
    """Liste minimale contenant un finding critique."""
    return [make_finding()]
 
 
@pytest.fixture
def finding_factory():
    """Permet aux tests de créer des findings sur mesure.
 
    Exemple : def test_x(finding_factory): f = finding_factory(criticite="Faible")
    """
    return make_finding
