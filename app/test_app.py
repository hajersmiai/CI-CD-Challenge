from app.main import get_env_config


def test_get_env_config_dev():
    title, bg = get_env_config("dev")
    assert "Dev" in title and bg.startswith("#")


def test_get_env_config_qa():
    title, _ = get_env_config("qa")
    assert "QA" in title


def test_get_env_config_prod():
    title, _ = get_env_config("prod")
    assert "Production" in title
    