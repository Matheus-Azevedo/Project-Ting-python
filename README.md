# Ting
### Autor: Matheus Eduardo de Sousa Azevedo

Este projeto foi desenvolvido por mim e faz parte do acervo de atividades executadas na escola de programação Trybe. A formação ao longo de 1 ano em Desenvolvimento Web desta instituição  conta com mais de 1.500 horas de aulas e aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias ágeis e habilidades comportamentais. Tudo voltado totalmente para o mercado de trabalho com intuito de entregar um profissional adequado para a realidade atual. 

# Sobre o projeto

O projeto consiste em implementar um programa de indexação de documentos similar ao do Google, capaz de identificar ocorrências de termos em arquivos TXT. O programa terá dois módulos: gerenciamento de arquivos, que permitirá anexar arquivos de texto e o módulo de buscas, que permitirá realizar buscas nos arquivos anexados. O foco não será na análise de significados ou sinônimos. Serão exercitadas habilidades de manipulação de pilhas, deque, nó e listas ligadas, e listas duplamente ligadas.

# O que foi desenvolvido

Os requisitos solicitados no pacote ting_file_management são os seguintes:

1.  Implementar uma fila para armazenar os arquivos que serão lidos. A fila deve ser uma estrutura FIFO que implementa os métodos de inserção (enqueue), remoção (dequeue) e busca (search). Deve expor o tamanho da fila com o método **len** e lançar uma exceção do tipo IndexError com a mensagem "Índice Inválido ou Inexistente" caso um índice inválido seja passado.
    
2.  Implementar uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. Caso o arquivo TXT não exista, deve exibir a mensagem Arquivo {path_file} não encontrado na stderr, em que {path_file} é o caminho do arquivo. Caso a extensão do arquivo seja diferente de .txt, deve exibir a mensagem Formato inválido na stderr.
    
3.  Implementar a função process no módulo file_process. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue. A função irá receber como parâmetro um objeto instanciado da fila implementada no requisito 1 e o caminho para um arquivo. Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, arquivos com o mesmo nome e caminho (nome_do_arquivo) não devem ser readicionados a fila). Após cada nova inserção válida, a função deve mostrar via stdout os dados processados.
    
4.  Implementar uma função remove dentro do módulo file_process capaz de remover o primeiro arquivo processado. Caso não existam arquivos na fila, a função deve emitir a mensagem Não há elementos via stdout. Em caso de sucesso de remoção, deve ser emitida a mensagem Arquivo {path_file} removido com sucesso via stdout, em que {path_file} é o caminho do arquivo.
    

Esses são os 4 requisitos do pacote ting_file_management que serão avaliados. Cada um tem uma ou mais funções específicas a serem implementadas e requisitos de comportamento que devem ser satisfeitos.
