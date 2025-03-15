from rest_framework.authentication import BasicAuthentication

class CsrfExemptSessionAuthentication(BasicAuthentication):
    def enforce_csrf(self, request):
        return  # Просто пропускає перевірку CSRF
