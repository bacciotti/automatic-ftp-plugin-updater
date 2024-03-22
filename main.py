import requests
import os
from dotenv import load_dotenv


class WordPressPluginManager:
    def __init__(self):
        load_dotenv()
        self.url = "https://bacciotti.com/wp-json/wp/v2/plugins"
        self.username = os.getenv("WORDPRESS_USERNAME")
        self.password = os.getenv("WORDPRESS_PASSWORD")

    def check_plugin(self, name):
        try:
            response = requests.get(self.url, headers={"User-Agent": "XY"}, auth=(self.username, self.password))

            if not name:
                return None

            if response.status_code == 200:
                plugins = response.json()

                for plugin in plugins:
                    if name in plugin['name']:
                        return plugin
                return None
            else:
                print(f"Erro: Não foi possível obter a resposta da API. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print("Erro:", e)
            return None

    def delete_plugin(self, name):
        plugin = self.check_plugin(name)

        if plugin:
            self_link = plugin['_links']['self'][0]['href']
            print(self_link)
            print(plugin['name'])
            print(plugin['plugin'])
            plugin = plugin['plugin']
            try:
                response = requests.delete(self_link, auth=(self.username, self.password))

                if response.status_code == 200 or response.status_code == 204:
                    print(f"O plugin {name} foi excluído com sucesso.")
                else:
                    print(f"Erro: Não foi possível excluir o plugin {name}.")
            except requests.exceptions.RequestException as e:
                print("Erro:", e)
        else:
            print(f"O plugin {name} não está instalado.")

    def upload_new_version(self, file_path):
        # Implemente o método para fazer upload de um arquivo zip com a nova versão do plugin
        pass

    def activate_akismet_plugin(self):
        plugin = self.check_akismet_plugin()

        if plugin:
            plugin_slug = plugin['slug']
            activate_url = f"{self.url}/{plugin_slug}/activate"

            try:
                response = requests.post(activate_url, auth=(self.username, self.password))

                if response.status_code == 200 or response.status_code == 204:
                    print("O plugin Akismet foi ativado com sucesso.")
                else:
                    print("Erro: Não foi possível ativar o plugin Akismet.")
            except requests.exceptions.RequestException as e:
                print("Erro:", e)
        else:
            print("O plugin Akismet não está instalado.")
