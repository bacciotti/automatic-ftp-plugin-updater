from main import WordPressPluginManager

plugin_name = 'Akismet'
plugin_manager = WordPressPluginManager()
plugin_manager.delete_plugin(name=plugin_name)
plugin_manager.check_plugin(name=plugin_name)

# Fazendo o upload de um novo arquivo zip com a versão atualizada do plugin
# plugin_manager.upload_new_version("caminho_para_o_arquivo_zip")

# Ativando o plugin Akismet
# plugin_manager.activate_akismet_plugin()
