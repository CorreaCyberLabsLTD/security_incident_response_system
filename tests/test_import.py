"""Test Security Incident Response System."""

import security_incident_response_system


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(security_incident_response_system.__name__, str)
