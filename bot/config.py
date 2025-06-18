from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()                                     # .env → окружение

BOT_TOKEN    = os.getenv("BOT_TOKEN", "")
ADMIN_ID     = int(os.getenv("ADMIN_ID", "0"))

DATABASE_URL = os.getenv(
    "DATABASE_URL", "sqlite+aiosqlite:///data.db"  # по умолчанию файл SQLite
)

# если SQLite — создаём пустой файл, чтобы драйвер не ругался
if DATABASE_URL.startswith("sqlite"):
    Path("data.db").touch(exist_ok=True)
