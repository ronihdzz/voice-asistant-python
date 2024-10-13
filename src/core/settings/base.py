# Standard Library
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Third Party Stuff
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict
from loguru import logger

from core.utils.environment import EnvironmentsTypes

LIST_PATH_TO_ADD = []
if LIST_PATH_TO_ADD:
    sys.path.extend(LIST_PATH_TO_ADD)


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
logger.info(f"BASE_DIR: {BASE_DIR}")
ENVS_DIR = BASE_DIR / "envs"
logger.info(f"ENVS_DIR: {ENVS_DIR}")
ENV_BASE_FILE_PATH = ENVS_DIR / ".env.base"
logger.info(f"ENV_BASE_FILE_PATH: {ENV_BASE_FILE_PATH}")
load_dotenv(ENV_BASE_FILE_PATH)
logger.info("ENV_BASE_FILE_PATH loaded")
ENVIRONMENT = os.environ.get("ENVIRONMENT")
logger.info(f"ENVIRONMENT: {ENVIRONMENT}")
EnvironmentsTypes.check_env_value(ENVIRONMENT)
ENV_FILE_PATH = ENVS_DIR / EnvironmentsTypes.get_env_file_name(ENVIRONMENT)
logger.info(f"ENV_FILE_PATH: {ENV_FILE_PATH}")

class Settings(PydanticBaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="ignore", case_sensitive=True)
    ENVIRONMENT: str = ENVIRONMENT
    # Database settings
    # ----------------------------------------------------------------
    OPENAI_API_KEY: str
    PORT: int = 9000
    # Project Constants
    # ----------------------------------------------------------------
    PROJECT_NAME: str = "AsistentPython"
    PROJECT_ID: str = "A0002"
    TIME_ZONE: str = "utc"
    TIME_ZONE_UTC: str = "utc"
    DATE_FORMAT: str = "%Y-%m-%d"
    DATE_TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # OpenAI settings
    # ----------------------------------------------------------------
    VOICE: str = 'alloy'
    LOG_EVENT_TYPES: list[str] = [
        'response.content.done', 'rate_limits.updated', 'response.done',
        'input_audio_buffer.committed', 'input_audio_buffer.speech_stopped',
        'input_audio_buffer.speech_started', 'session.created'
    ]