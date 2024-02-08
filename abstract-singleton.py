from abc import ABC, abstractmethod

class Textura(ABC):
    @abstractmethod
    def desenhar(self, msg: str):
        pass

class Sombra(ABC):
    @abstractmethod
    def sombrear(self, msg: str):
        pass

class Modelo(ABC):
    @abstractmethod
    def carregar_modelo(self, msg: str):
        pass

class FabricaRenderizacao(ABC):
    @abstractmethod
    def criar_textura(self) -> Textura:
        pass

    @abstractmethod
    def criar_sombra(self) -> Sombra:
        pass

    @abstractmethod
    def criar_modelo(self) -> Modelo:
        pass

#OpenGL

class OpenGLTextura(Textura):
    def desenhar(self, msg: str):
        print(f'Desenhando textura OpenGl {msg}')

class OpenGLSombra(Sombra):
    def sombrear(self, msg: str):
        print(f'Aplicando sombra OpenGl {msg}')

class OpenGLModelo(Modelo):
    def carregar_modelo(self, msg: str):
        print(f'Carregando modelo OpenGl {msg}')

class OpenGL(FabricaRenderizacao):
    _instance = None

    def criar_textura(self) -> Textura:
        return OpenGLTextura()

    def criar_sombra(self) -> Sombra:
        return OpenGLSombra()

    def criar_modelo(self) -> Modelo:
        return OpenGLModelo()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
      
#DirectX

class DirectXTextura(Textura):
    def desenhar(self, msg: str):
        print(f'\nDesenhando textura DirectX {msg}')

class DirectXSombra(Sombra):
    def sombrear(self, msg: str):
        print(f'Aplicando sombra DirectX {msg}')

class DirectXModelo(Modelo):
    def carregar_modelo(self, msg: str):
        print(f'Carregando modelo DirectX {msg}')

class DirectX(FabricaRenderizacao):
    _instance = None

    def criar_textura(self) -> Textura:
        return DirectXTextura()

    def criar_sombra(self) -> Sombra:
        return DirectXSombra()

    def criar_modelo(self) -> Modelo:
        return DirectXModelo()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def usar_framework_renderizacao(fabrica: FabricaRenderizacao):
    textura = fabrica.criar_textura()
    sombra = fabrica.criar_sombra()
    modelo = fabrica.criar_modelo()

    textura.desenhar('textura')
    sombra.sombrear('sombra')
    modelo.carregar_modelo('modelo')

if __name__ == "__main__":
    fabrica_opengl = OpenGL.instance()
    usar_framework_renderizacao(fabrica_opengl)
    
    fabrica_directx = DirectX.instance()
    usar_framework_renderizacao(fabrica_directx)
