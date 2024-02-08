class Configuration:
    _instance = None
        
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = (cls)
            cls._instance.theme = "dark"
            cls._instance.fontSize = 12
            cls._instance.language = "pt-br"
        return cls._instance


config_inst = Configuration.instance()

print("Tema: {}, Linguagem: {}, Tamanho da Fonte: {}".format(config_inst.theme, config_inst.language, config_inst.fontSize))
