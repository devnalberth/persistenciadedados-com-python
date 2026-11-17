# Contexto para Codex ou Claude no VS Code

Estou desenvolvendo o trabalho prático DGT2819 — Persistência de dados com
Python, da minha faculdade. Esta pasta já contém uma implementação funcional.

Leia primeiro `ENUNCIADO.md`, `README.md` e os arquivos Python. Explique o
fluxo antes de propor mudanças, pois preciso compreender e apresentar o código.

## Objetivo obrigatório

Ler um TXT com `with`, percorrer linha a linha, separar palavras com `split()`,
acrescentá-las a uma lista criada com `list()`, comparar Bubble Sort,
Selection Sort e `sort()` com medição de tempo e gerar um novo TXT ordenado.
Depois da comparação, o `kdd.py` final deve conservar somente o método escolhido.
A entrega é o link de um repositório Git na sala virtual.

## Estado atual

- As cinco microatividades estão implementadas.
- `kdd_comparacao.py` usa cópias da mesma lista original para cada método e
  repetição. Apenas a ordenação é cronometrada com `perf_counter()`.
- Os tempos reais ficam em `resultados_comparacao.json`.
- Na execução incluída, `sort()` teve a menor mediana e foi escolhido para `kdd.py`.
- `kdd.py` gera `palavras_ordenadas.txt` e não importa os algoritmos descartados.
- Os testes usam somente `unittest`, da biblioteca padrão.
- Nenhum pacote externo é necessário. A execução incluída usa Python 3.9.6.
- Revisão local em 17/11/2026: cinco testes passaram; as cinco microatividades,
  a comparação e o programa final executaram sem erro no Python 3.9.6.
- A saída foi conferida: 89 palavras ordenadas e todas as ocorrências preservadas.
- README, JSON e registro de execução foram atualizados com a mesma comparação.
- O README contém um roteiro por etapas para apresentar o código.
- Git foi inicializado na branch `main`. Confira `git status`, `git log -1`
  e `git remote -v` antes de continuar.
- O usuário informou que ainda não criou o repositório no GitHub.
  A publicação remota continua pendente da criação e da URL real.

## Próximas ações

1. Confira os requisitos contra a implementação e aponte eventuais lacunas concretas.
2. Verifique o interpretador disponível e execute `python3 -m unittest -v`.
   No Windows, adapte para `py` se necessário.
3. Execute as cinco microatividades, `kdd_comparacao.py` e `kdd.py`.
4. Confira se a saída está ordenada e preserva todas as ocorrências da entrada.
5. Explique `list()`, `with`, `split`, `extend`, os dois algoritmos, a troca
   simultânea, a medição e a escrita. Relacione cada conceito ao código.
6. Se houver correções necessárias, mantenha a solução simples e refaça
   somente as verificações afetadas.
7. Ajude a configurar o repositório e publicar quando eu informar a URL real.
   Não invente usuário, URL, nome completo, matrícula ou resultados de testes.

## Restrições de escopo

- Preserve programação estruturada e biblioteca padrão; não adicione frameworks,
  interface gráfica, servidor, banco de dados ou orientação a objetos ao MVP.
- Preserve os nomes das microatividades e `kdd.py`.
- A entrada usa UTF-8. Mantenha repetições e pontuação, conforme `split()`.
- Explique a comparação padrão Unicode e seus efeitos nas maiúsculas e acentos.
- Não normalize termos nem remova repetições sem um novo requisito.
- Se repetir a comparação, explique que a tabela do README registra a execução
  original; atualize-a apenas usando as novas medições reais.
- Não crie definições jurídicas ou alegue que o tutor já recebeu a entrega.
