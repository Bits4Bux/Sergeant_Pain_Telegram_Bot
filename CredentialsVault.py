import keyring
import os


class CredentialsVault:
    _instance = None
    _initialized = False

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(CredentialsVault, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self.app_name = "Sergeant Pain Telegram Bot"  # Name as you like (optional)
        self.username = os.getlogin()  # Retrives your username from the system

        self._initialized = True

    # Save data in Windows Credential Manager
    def save_credential(self, cred_reference, credential):
        keyring.set_password(cred_reference, self.username, credential)

    # Retrives data from Windows Credential Manager
    def retrive_credential(self, cred_reference):
        retrived_credential = keyring.get_password(cred_reference, self.username)
        return retrived_credential


if __name__ == '__main__':
    pass
