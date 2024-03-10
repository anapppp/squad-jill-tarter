#Etapa 1 – Adicionar um arquivo com testes para este exercício.
#Etapa 2 – Executar os testes e identificar a falha ( pytest test_exercise.py).
#Etapa 3 – Corrigir o bug e fazer com que os testes passem (linha 9, colocar return) e repetir com o comando pytest -v test_exercise.py
#Etapa 4.1 – Adicionar novo código com testes (importar pytest). Adicionar um novo teste à classe para verificar a exceção.
#      4.2- Execute os testes novamente com Pytest, todos eles devem ser aprovados.
#      4.3- Atualize a função para gerar explicitamente um TypeError.
#      4.4- Por fim, atualize o método test_non_list_commands() para verificar a mensagem de erro.

import pytest
def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects
    `command` to be a list.
    """
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")
    if sudo:
        return["sudo"] + command
    return command

class TestAdminCommand:

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected
    
   
    
    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"



