import platform
import winreg
import os
import subprocess
from selenium import webdriver
        
class InfoBrowser(object):
    def __init__(self):
        self.__systemName = platform.system()

    def _get_default_browser_windows(self):
        try:
            # Caminho no registro onde o navegador padrão é configurado
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
                browser = winreg.QueryValueEx(key, "ProgId")[0]
            return browser
        except Exception as e:
            return None

    def _get_default_browser_linux(self):
        browser = os.environ.get("BROWSER")
        if browser:
            return browser
        else:
            # Tentativa de usar "xdg-settings" para obter o navegador padrão
            try:
                import subprocess
                browser = subprocess.check_output(["xdg-settings", "get", "default-web-browser"]).decode().strip()
                return browser
            except Exception:
                return None
        
    def _get_default_browser_mac(self):
        try:
            output = subprocess.check_output(
                ["defaults", "read", "com.apple.LaunchServices/com.apple.launchservices.secure", "LSHandlers"]
            ).decode("utf-8")
            return output
        except Exception:
            return None

    def _get_default_browser(self):
        if self.__systemName == "Windows":
            # search windows default browser
            return self._get_default_browser_windows()
        elif self.__systemName == "Linux":
            # search linux default browser
            return self._get_default_browser_linux()
        elif self.__systemName == "Darwin":
            return self._get_default_browser_mac()
        else:
            # Couldn't identify the system
            return None
    def start_browser_selenium(self):
        browser_name = self._get_default_browser().casefold()

        if not browser_name:
            return None
        
        chrome_str = "chrome"
        firefox_str = "firefox"
        edge_str = "edge"
        safari_str = "safari"
        explorer_str = "IE"

        if chrome_str.casefold() in browser_name:
            browser = webdriver.Chrome()
        elif firefox_str.casefold() in browser_name:
            browser = webdriver.Firefox()
        elif edge_str.casefold() in browser_name:
            browser = webdriver.Edge(options=webdriver.EdgeOptions())
        elif safari_str.casefold() in browser_name:
            browser = webdriver.Safari()
        elif explorer_str.casefold() in browser_name:
            browser = webdriver.Ie()
        else:
            browser = None

        return browser
        
        



