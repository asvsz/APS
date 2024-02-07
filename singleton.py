class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "dark"
            cls._instance.fontSize = 12
            cls._instance.language = "pt-br"
        return cls._instance


print("Tema: {}, Linguagem: {}, Tamanho da Fonte: {}".format(Configuration().theme, Configuration().language, Configuration().fontSize))
