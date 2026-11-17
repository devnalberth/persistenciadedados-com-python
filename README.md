# Colocando tudo em ordem e guardando

Trabalho prático da disciplina **DGT2819 — Persistência de dados com Python**.

O programa lê um arquivo TXT linha a linha, separa as palavras com `split()`,
compara três formas de ordenação e grava as palavras ordenadas em outro TXT.
O projeto usa programação estruturada e somente a biblioteca padrão do Python.

## Executar no VS Code

1. Abra a pasta do projeto em **File > Open Folder**. Se recebeu um ZIP,
   extraia-o primeiro.
2. Abra um terminal nessa pasta em **Terminal > New Terminal**.
3. Confira o interpretador:

```bash
python3 --version
```

No Windows, use `py` no lugar de `python3` se esse for o comando disponível.
O projeto foi executado com Python 3.9.6. Não é necessário instalar pacotes.
Se utilizar a extensão Python da Microsoft no VS Code, selecione seu
interpretador em **Python: Select Interpreter**, na paleta de comandos.

Execute a comparação antes do programa final:

```bash
python3 kdd_comparacao.py
python3 kdd.py
```

O primeiro comando imprime os resultados dos três métodos, mede cinco
execuções de cada um e salva `resultados_comparacao.json`.
O segundo gera `palavras_ordenadas.txt`, com uma palavra por linha.

Para usar seu próprio texto UTF-8, substitua o conteúdo de `entrada.txt` ou execute:

```bash
python3 kdd_comparacao.py meu_texto.txt --repeticoes 10
python3 kdd.py meu_texto.txt --saida meu_glossario.txt
```

Os caminhos informados no terminal são relativos à pasta atual. Os caminhos
padrão são relativos à pasta dos scripts. A saída indicada será sobrescrita
a cada execução; o programa impede que a entrada seja usada como saída.

## Organização e relação com o enunciado

| Arquivo | Finalidade |
| --- | --- |
| `array.sort.py` | Microatividade 1: inteiros e strings em ordem crescente e decrescente |
| `bubble.sort.py` | Microatividade 2: demonstração de Bubble Sort com 15 inteiros |
| `selection.sort.py` | Microatividade 3: demonstração de Selection Sort com 15 inteiros |
| `algoritmos.py` | Implementações dos dois algoritmos, reutilizadas nos exemplos e na comparação |
| `ler.txt.py` | Microatividade 4: leitura completa, primeira linha, três caracteres e `with` |
| `loremipsum.txt` | Texto usado na microatividade de leitura |
| `escrever.txt.py` | Microatividade 5: lista criada com `list()`, frases com `append()` e escrita |
| `texto.txt` | Arquivo gerado pela microatividade de escrita |
| `entrada.txt` | Texto de exemplo com termos jurídicos, sem dados pessoais |
| `kdd_comparacao.py` | Etapa experimental: Bubble Sort, Selection Sort e `list.sort()` |
| `resultados_comparacao.json` | Tempos reais da comparação, repetição por repetição |
| `kdd.py` | Entrega final: leitura, ordenação com o método escolhido e persistência |
| `palavras_ordenadas.txt` | Resultado do programa final |
| `test_projeto.py` | Verificações automatizadas de ordenação e persistência |
| `verificacao_execucao.txt` | Registro da execução dos exemplos, comparação, programa final e testes |
| `ENUNCIADO.md` | Cópia do enunciado fornecido |
| `CONTINUAR_NO_VSCODE.md` | Contexto para continuar com Codex ou Claude no editor |

O enunciado pede remover os outros métodos do script final após a escolha.
Por isso, `kdd.py` contém apenas `sort()`. A etapa experimental permanece
em um arquivo separado para permitir a conferência dos resultados.
As microatividades são material de apoio; a entrega solicitada é o trabalho
prático por meio do link do repositório Git.

## Comparação registrada

Execução local de **17/11/2026**, com **89 palavras**, **5 repetições**,
Python **3.9.6** e macOS. Os valores abaixo correspondem ao JSON e à etapa
de comparação do registro de execução atualizados nessa data.

| Método | Mediana da ordenação |
| --- | ---: |
| Bubble Sort | 0,256375 ms |
| Selection Sort | 0,120667 ms |
| `list.sort()` | 0,003250 ms |

Cada método recebe uma cópia dos mesmos dados originais, ainda não ordenados.
A cópia, a leitura, a impressão, a escrita e a verificação ficam fora do
intervalo medido com `perf_counter()`. Os três resultados foram conferidos
contra `sorted()` fora da medição.

Foi escolhido `list.sort()` porque teve a menor mediana neste experimento.
Os tempos são curtos e variam conforme a máquina e a carga do sistema;
essa medição pequena não constitui um benchmark geral. Execute novamente
no seu computador para obter suas próprias evidências. O JSON é atualizado
ao rodar novamente a comparação; a tabela e o registro de execução não são
atualizados automaticamente.

## Como explicar o código

1. `palavras = list()` cria a lista inicialmente vazia.
2. `with open(..., encoding="utf-8")` abre o TXT e garante o fechamento.
3. `for linha in arquivo` percorre o arquivo linha a linha.
4. `linha.split()` divide a linha por espaços, tabulações e quebras de linha.
5. `palavras.extend(...)` acrescenta cada palavra à lista, sem listas aninhadas.
6. Bubble Sort compara vizinhos e troca os que estão fora de ordem.
7. Selection Sort encontra o menor elemento restante e o coloca na posição atual.
8. `perf_counter()` mede o tempo decorrido de cada ordenação.
9. `palavras.sort()` ordena a própria lista na versão final.
10. `arquivo.write(palavra + "\n")` persiste uma palavra por linha.

O comportamento segue o `split()` e a comparação padrão de strings do Python.
Repetições, maiúsculas, minúsculas, acentos e pontuação são preservados.
A ordenação é lexicográfica pela ordem dos caracteres Unicode; não é uma
ordenação linguística específica do português. Não há remoção de palavras
repetidas ou normalização porque essas etapas não são exigidas no roteiro.
O MVP lista termos; não atribui definições jurídicas a eles.

Os algoritmos didáticos apresentados percorrem dois laços e fazem um número
quadrático de comparações. Por isso, use arquivos pequenos na comparação.
O programa final mantém a leitura das palavras em memória, como pede o roteiro.

## Roteiro para apresentar o trabalho

### 1. Problema e organização

"O objetivo é ler palavras de um arquivo de texto, comparar três métodos de
ordenação e salvar o resultado em outro arquivo. Separei a experiência de
comparação do programa final, conforme o enunciado."

Mostre `entrada.txt`, depois `kdd_comparacao.py` e por último `kdd.py`.
As funções organizam a solução em programação estruturada. A classe usada
em `test_projeto.py` é parte do funcionamento do `unittest`; o MVP não usa
classes próprias nem banco de dados.

### 2. Leitura e formação da lista — `kdd.py`

```python
palavras = list()
with open(entrada, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())
```

`list()` cria a lista vazia. `"r"` abre para leitura e `encoding="utf-8"`
permite ler acentos nesse formato. `with` fecha o arquivo mesmo se ocorrer
um erro dentro do bloco. O `for` percorre uma linha por vez.

`split()` transforma `"lei contrato lei"` em `["lei", "contrato", "lei"]`.
`extend()` adiciona os três elementos à lista principal. Usar
`append(linha.split())` adicionaria uma lista dentro da outra; `append()`
seria adequado para adicionar uma palavra individual por vez.

### 3. Algoritmos didáticos — `algoritmos.py`

No Bubble Sort, `i` conta as passagens e `j` indica o primeiro elemento de
cada par vizinho. Se `array[j] > array[j + 1]`, os valores trocam de lugar,
usando `temporario` para não perder nenhum deles. Ao final de cada passagem,
o maior elemento da parte restante está no fim. Por isso o segundo laço
termina em `len(array) - i - 1`.

Exemplo: `[3, 1, 2]` passa por `[1, 3, 2]` e chega a `[1, 2, 3]`.

No Selection Sort, `i` marca a posição que será preenchida. `indice_menor`
começa em `i`, e `j` procura um valor menor no restante da lista. Depois
da busca, a troca coloca esse menor valor na posição `i`:

```python
array[i], array[indice_menor] = array[indice_menor], array[i]
```

O Python avalia o lado direito antes de atribuir ao esquerdo. Assim, a troca
simultânea preserva os dois valores, sem variável temporária explícita.
Em `[3, 1, 2]`, a primeira seleção produz `[1, 3, 2]`; a segunda, `[1, 2, 3]`.

As duas implementações fazem `n * (n - 1) / 2` comparações de elementos,
portanto têm quantidade de comparações O(n²), inclusive em listas já ordenadas.

### 4. Comparação justa — `kdd_comparacao.py`

Cada método recebe `originais.copy()` antes de cada uma das cinco medições.
Assim, nenhum aproveita o trabalho do método anterior. O intervalo medido é:

```python
inicio = perf_counter()
ordenar(copia)
tempos.append(perf_counter() - inicio)
```

`perf_counter()` fornece uma referência de tempo apropriada para medir
intervalos curtos; a diferença é expressa em segundos. A leitura, a cópia,
a impressão, a gravação e a conferência com `sorted()` ficam fora desse
intervalo. `sorted()` cria uma nova lista e serve como referência de correção.

A mediana é o valor central dos cinco tempos colocados em ordem. O relatório
JSON guarda todos os tempos, as medianas e o método com a menor mediana.
Nesta execução, o escolhido foi `list.sort()`. O experimento é pequeno e
seus tempos variam; ele não demonstra uma vantagem universal em toda entrada.

### 5. Escolha e persistência — `kdd.py`

`palavras.sort()` altera a própria lista e retorna `None`. Por isso o código
não faz `palavras = palavras.sort()`. O script final mantém somente esse
método, e os outros ficam no experimento e nas microatividades.

```python
with open(saida, "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")
```

`"w"` cria o arquivo ou sobrescreve seu conteúdo. `"\n"` separa as palavras
em linhas. A persistência consiste em guardar o resultado no disco para
continuar disponível depois que o programa encerrar. O retorno da função
permite conferir também a lista em memória nos testes.

### 6. Execução e cuidados

`main()` usa `argparse` para receber os caminhos pelo terminal. `Path` trata
os caminhos; `PASTA` usa a localização do próprio script como base dos padrões.
`if __name__ == "__main__"` executa `main()` ao rodar o arquivo diretamente,
sem executá-la quando os testes importam a função.

A função recusa caminhos resolvidos iguais para entrada e saída antes de
abrir a saída para escrita. O bloco `try/except` apresenta erros de arquivo,
codificação ou caminho iguais sem um traceback no uso normal pelo terminal.

Preservar repetições é intencional: `lei lei` gera duas linhas com `lei`.
`split()` também mantém a pontuação: `lei` e `lei,` são termos distintos.
A ordem Unicode pode colocar `Acordo` antes de `acao` e `ação` depois de
palavras iniciadas por `z`; não é uma ordenação linguística do português.

### 7. Demonstração ao vivo

```bash
python3 -m unittest -v
python3 kdd_comparacao.py
python3 kdd.py
```

Mostre os cinco testes passando, as três listas iguais e os tempos impressos.
Abra `palavras_ordenadas.txt`: a entrada de exemplo produz 89 linhas, mantendo
todas as ocorrências. Explique que o tempo do `kdd.py` é uma medição separada
e não precisa coincidir com a mediana registrada na comparação.

## Microatividades e testes

```bash
python3 array.sort.py
python3 bubble.sort.py
python3 selection.sort.py
python3 ler.txt.py
python3 escrever.txt.py
python3 -m unittest -v
```

Os cinco testes cobrem os algoritmos, incluindo listas vazias, negativas,
repetidas e 100 listas pseudoaleatórias, além da persistência UTF-8,
arquivo vazio, proteção da entrada e arquivo inexistente.
O registro incluído mostra os scripts executados com código de saída zero.
Na revisão local de 17/11/2026, também foram conferidos a igualdade da saída
com `sorted(entrada)`, as frequências de todas as palavras, as medianas do
JSON, os caminhos personalizados com espaços, a execução a partir de outra
pasta e os erros de entrada inexistente, saída igual à entrada e zero repetições.

## Publicar e entregar

Revise o código, execute no seu computador e confira o prazo na sala virtual.
Se a instituição exigir identificação, acrescente seu nome e matrícula antes
de publicar. O enunciado fornecido não informa esses dados nem uma data limite.

Crie um repositório vazio no GitHub, com o nome desejado. Para facilitar o
acesso do tutor, você pode escolher **Public**. Não marque a criação de README,
`.gitignore` ou licença nesse passo, pois a pasta local já tem arquivos.

Esta pasta já foi inicializada com Git na branch `main`. Depois de criar o
repositório remoto, use a URL real dele no lugar do exemplo:

```bash
git status
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

Confira `git remote -v` antes de configurar o remoto. Caso ainda não exista
um commit local (`git log -1`), execute `git add .` e
`git commit -m "Implementa trabalho de persistência de dados com Python"`
antes do envio. A autenticação deve ser feita pelo fluxo do GitHub ou por
uma chave SSH configurada. Não coloque tokens no código nem na URL do remoto.
Depois do envio, confira no GitHub se os arquivos estão na branch `main` e
se o tutor consegue acessar o repositório.

Envie o link do repositório na aba **Trabalhos** da Sala de Aula Virtual.
O projeto foi validado localmente e ainda não foi publicado no GitHub.
