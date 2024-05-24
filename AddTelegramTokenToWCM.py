from CredentialsVault import CredentialsVault

"""Adds Telegram bot token to Windows Credential Manager via Keyring"""


def add_token_to_wcm():
    cred_vault = CredentialsVault()
    telegram_token = 'ADD_HERE'  # Add your Telegram token from BotFather here
    cred_reference = cred_vault.app_name
    cred_vault.save_credential(cred_reference, telegram_token)
    retrived_telegram_token = cred_vault.retrive_credential(cred_reference)

    print(f"SAVED TELEGRAM TOKEN:       {telegram_token}")
    print(f"RETRIVED TELEGRAM TOKEN:    {retrived_telegram_token}")
    print("If both the saved and retrieved Telegram tokens are exactly the same as from BotFather, you are good to go.")


add_token_to_wcm()
