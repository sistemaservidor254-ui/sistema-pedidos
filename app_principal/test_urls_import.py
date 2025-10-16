# salvar como test_urls_import.py (opcional) ou rodar inline
import os
import django
import importlib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

importlib.import_module("backend.urls")
print("✅ backend.urls importado com sucesso")
