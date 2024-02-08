from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def desenhar(self):
        pass

class Janela(ABC):
    @abstractmethod
    def abrir(self):
        pass

class Cursor(ABC):
    @abstractmethod
    def clicar(self):
        pass

class Select(ABC):
    @abstractmethod
    def selecionar(self):
        pass

class Input(ABC):
    @abstractmethod
    def receber_input(self):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

    @abstractmethod
    def criar_cursor(self) -> Cursor:
        pass

    @abstractmethod
    def criar_select(self) -> Select:
        pass

    @abstractmethod
    def criar_input(self) -> Input:
        pass


class WindowsFactory(AbstractFactory):
    def criar_botao(self) -> Botao:
        return WindowsBotao()

    def criar_janela(self) -> Janela:
        return WindowsJanela()

    def criar_cursor(self) -> Cursor:
        return WindowsCursor()

    def criar_select(self) -> Select:
        return WindowsSelect()

    def criar_input(self) -> Input:
        return WindowsInput()


class MacOSFactory(AbstractFactory):
    def criar_botao(self) -> Botao:
        return MacOSBotao()

    def criar_janela(self) -> Janela:
        return MacOSJanela()

    def criar_cursor(self) -> Cursor:
        return MacOSCursor()

    def criar_select(self) -> Select:
        return MacOSSelect()

    def criar_input(self) -> Input:
        return MacOSInput()


class WindowsBotao(Botao):
    def desenhar(self):
        print("Botão do Windows")

class WindowsJanela(Janela):
    def abrir(self):
        print("Janela do Windows")

class WindowsCursor(Cursor):
    def clicar(self):
        print("Cursor do Windows")

class WindowsSelect(Select):
    def selecionar(self):
        print("Select do Windows")

class WindowsInput(Input):
    def receber_input(self):
        print("Input do Windows")


class MacOSBotao(Botao):
    def desenhar(self):
        print("Botão do macOS")

class MacOSJanela(Janela):
    def abrir(self):
        print("Janela do macOS")

class MacOSCursor(Cursor):
    def clicar(self):
        print("Cursor do macOS")

class MacOSSelect(Select):
    def selecionar(self):
        print("Select do macOS")

class MacOSInput(Input):
    def receber_input(self):
        print("Input do macOS")

def criar_interface(factory: AbstractFactory):
    botao = factory.criar_botao()
    janela = factory.criar_janela()
    cursor = factory.criar_cursor()
    select = factory.criar_select()
    input_obj = factory.criar_input()

    botao.desenhar()
    janela.abrir()
    cursor.clicar()
    select.selecionar()
    input_obj.receber_input()


print("Criando interface para Windows:")
criar_interface(WindowsFactory())


print("\nCriando interface para macOS:")
criar_interface(MacOSFactory())
