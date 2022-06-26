from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os

class GoogleAuth():
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.filename = "coc-dice-bot"

        self.variables_keys = {
            "type": os.environ.get("SHEET_TYPE"),
            "project_id": os.environ.get("SHEET_PROJECT_ID"),
            "private_key_id": os.environ.get("SHEET_PRIVATE_KEY_ID"),
            "private_key": os.environ.get("SHEET_PRIVATE_KEY"),
            "client_email": os.environ.get("SHEET_CLIENT_EMAIL"),
            "client_id": os.environ.get("SHEET_CLIENT_ID"),
            "auth_uri": os.environ.get("SHEET_AUTH_URI"),
            "token_uri": os.environ.get("SHEET_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.environ.get("SHEET_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.environ.get("SHEET_CLIENT_X509_CERT_URL")
        }


    def get_auth(self):
        credit = gspread.service_account_from_dict(self.variables_keys)
        gc = credit.open(self.filename)
        return gc
