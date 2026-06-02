from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str = "postgresql://postgres:dreammarket_admin@localhost:5432/dreams_market"
    database_echo: bool = False

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 4
    api_reload: bool = False

    # Security
    secret_key: str = "your-super-secret-key-change-this-in-production-minimum-32-characters"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 480
    refresh_token_expire_days: int = 7
    password_min_length: int = 10

    # CORS
    cors_origins: List[str] = ["http://localhost", "http://localhost:8000", "http://localhost:3000"]

    # Application
    app_name: str = "Dreams Market AI Settlement Platform"
    app_version: str = "1.0.0"
    environment: str = "development"
    debug: bool = True

    # File Upload
    max_upload_size_mb: int = 100
    upload_dir: str = "./uploads"
    allowed_extensions: List[str] = ["pdf", "xlsx", "xls", "csv"]

    # Reconciliation
    reconciliation_tolerance_percent: float = 0.1
    reconciliation_date_tolerance_days: int = 3

    # Anomaly Detection
    anomaly_z_score_threshold: float = -2
    anomaly_moving_average_days: int = 14

    # Email
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_username: str = "your-email@gmail.com"
    smtp_password: str = "your-app-password"
    smtp_from_email: str = "noreply@dreammarket.com"
    smtp_from_name: str = "Dreams Market Platform"

    # Logging
    log_level: str = "INFO"
    log_file: str = "./logs/app.log"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Banks
    supported_banks: List[str] = ["banque_misr", "nbe", "aaib"]

    # Export
    export_pdf_margin: int = 20
    export_excel_max_rows: int = 100000

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
