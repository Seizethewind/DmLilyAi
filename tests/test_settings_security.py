import pytest

from LilyAiCore.Config.settings import validate_security_settings


def test_production_api_requires_admin_token():
    with pytest.raises(RuntimeError, match="ADMIN_TOKEN"):
        validate_security_settings(enable_api=True, admin_token="", environment="production")


def test_non_production_api_can_run_without_admin_token():
    validate_security_settings(enable_api=True, admin_token="", environment="development")


def test_disabled_api_does_not_require_admin_token():
    validate_security_settings(enable_api=False, admin_token="", environment="production")
