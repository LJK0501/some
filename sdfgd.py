from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수 읽기
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")
port = os.getenv("PORT")

print(api_key, debug_mode, port)