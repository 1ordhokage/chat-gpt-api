from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    RDBMS: str
    DRIVER: str
    HOST: str
    PORT: str
    USER: str
    PASS: str
    NAME: str

    @property
    def connection_string(self) -> str:
        connector = f"{self.RDBMS}+{self.DRIVER}://"
        credentials = f"{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"
        return connector + credentials
    
    model_config = SettingsConfigDict(
        env_prefix="DB_",
        env_file=".env"
    )


db_settings = DBSettings()
