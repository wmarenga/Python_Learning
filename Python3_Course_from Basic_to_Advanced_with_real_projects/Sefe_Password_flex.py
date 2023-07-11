# pip install flet

import flet as ft
import secrets
import string


def main(page):

    page.title = "Safe Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def btn_click(e):
        safe_password = str()
        if not characters.value:
            characters.error_text = "Please enter How many characters do you need."
        else:
            char = characters.value

            for i in range(int(char)):
                safe_password += secrets.choice(str(secrets.token_bytes(128)) + string.ascii_letters + str(
                    secrets.token_urlsafe(128)) + string.digits + str(secrets.token_hex(128)) + string.punctuation)
        page.add(ft.Text(f"You safe code is:"))
        page.add(ft.Text(f"{safe_password}", size=20, color=ft.colors.WHITE,
                 bgcolor=ft.colors.RED_500, weight=ft.FontWeight.W_100, selectable=True))
        page.release()

    characters = ft.TextField(
        label="How many characters do you want to generate?")

    page.add(characters, ft.ElevatedButton(
        "Password Generate", on_click=btn_click))


ft.app(target=main)
