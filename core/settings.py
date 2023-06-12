import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8080
    env: str = "prod"
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logging_dir = os.path.join(base_dir, "logs")
    logging_level = "INFO"
    secret_key = b"78f40f2cff929js24eee727a4b892dg36as"
    enable_requests_log = True
    bk_paas_host = os.getenv("BK_PAAS_HOST", "http://paas.example.com/")
    weops_app_id = os.getenv("WEOPS_APP_ID", "weops_saas")
    weops_app_token = os.getenv("WEOPS_APP_TOKEN", "kfsdifw82yu3sf4sf2gy2nv3mfeseaf")
    default_bk_api_ver = os.getenv("DEFAULT_BK_API_VER", "v2")
    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    max_thread_num: int = 16

    class Config:
        env_file = ".env"


settings = Settings()
