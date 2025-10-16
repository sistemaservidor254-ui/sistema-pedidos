# backend/middleware.py
class SecurityHeadersMiddleware:
    """
    Aplica cabeçalhos de segurança básicos a cada resposta.
    Ajuste o CSP conforme recursos necessários (CDNs, domínios).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = (
            "geolocation=(), microphone=(), camera=()"
        )
        # CSP bem restrita; inclua domínios necessários (Bootstrap/HTMX CDNs)
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "img-src 'self' data:; "
            "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
            "script-src 'self' https://unpkg.com https://cdn.jsdelivr.net; "
            "connect-src 'self'; "
            "font-src 'self' https://cdn.jsdelivr.net; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        return response
