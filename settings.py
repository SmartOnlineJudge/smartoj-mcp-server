import os

import dotenv

# 是否是开发模式
# 该模式会影响配置文件的加载
DEV_ENV = True

# .env 文件路径
# 开发模式下使用 .env.local，生产模式下使用 .env
DOT_ENV_FILE = ".env.local" if DEV_ENV else ".env"

# 加载 .env 文件
dotenv.load_dotenv(DOT_ENV_FILE)

# 后端接口地址
BACKEDN_URL = os.getenv("BACKEND_URL")

# 后端 Session ID 在 HTTP Header 中的名称
BACKEND_SESSION_ID_NAME = os.getenv("BACKEND_SESSION_ID_NAME", "backend-session-id")
