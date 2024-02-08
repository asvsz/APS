from abc import ABC, abstractmethod


class ILog(ABC):

    @abstractmethod
    def registrar(self, msg: str):
        pass

class LogArquivo(ILog):
  
    def registrar(self, msg:str):
      with open('log.txt', 'a') as file:
        file.write(f'Arquivo {msg}\n')


class LogConsole(ILog):
  
    def registrar(self, msg:str):
      print(f'Console {msg}')


class LogBancoDeDados(ILog):
  
    def registrar(self, msg:str):
      print(f'[Banco de Dados] Registrando "{msg}" no banco de dados')

def criar_log(tipo):
  if tipo == 'arquivo':
    return LogArquivo()
  elif tipo == 'console':
    return LogConsole()
  elif tipo == 'banco_de_dados':
    return LogBancoDeDados()
  else: 
    raise ValueError('Tipo de log desconhecido: {tipo}'.format(tipo))


if __name__ == "__main__":
    log_arquivo = criar_log('arquivo')
    log_console = criar_log('console')
    log_bd = criar_log('banco_de_dados')
    
    log_arquivo.registrar('Mensagem de log no arquivo')
    log_console.registrar('Mensagem de log no console')
    log_bd.registrar('Mensagem de log no banco de dados')
    
    