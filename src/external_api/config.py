from pydantic_settings import BaseSettings, SettingsConfigDict


class ExternalAPISettings(BaseSettings):
    KEY: str
    MODEL: str
    ROLE: str
    URL: str
    PROXY: str
    
    model_config = SettingsConfigDict(
        env_prefix="EXTERNAL_API_",
        env_file=".env"
    )


external_api_settings = ExternalAPISettings()
