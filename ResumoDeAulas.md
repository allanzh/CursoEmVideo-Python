# Resumo das aulas

## Aula 09 - Manipulando Texto
Considerando para exemplo uma variável chamada frase que recebe a string "Curso em vídeo Python" temos os seguintes modos de manipulação de string:
### Fatiamento
- Apenas uma letra
```py
    frase[9] ==> v
```
- Range de letras
Nesse caso é possível definir um índice inicial e final de letras 
```py
    frase[9:14] ==> vídeo
    frase[9:21] ==> vídeo python
    frase[9:30] ==> Erro, pois não existe índice 29
```
- Range de letras com salto
Funciona como o anterior, porém recebe um valor que indica os saltos dados no fatiamento
```py
    frase[9:21:2] ==> vdoPto
```
- Range de final definido
Apenas o final é definido e o inicial se considera o indice 0
```py
    frase[:5] ==> Curso
```
- Range de inicio definido
Apenas o inicio é definido e o final se considera o ultimo indice da string
```py
    frase[15:] ==> Python
```
- Range com saltos
É possivel fazer os ranges indefinidos com salto, p.ex:
```py
frase[9::3] ==> VeP
``` 
### Análise
- Tamanho da string:
```py
        len(frase) ==> 21
```
- Contar letras contidas na string:
```py
        frase.count('o') ==> 3    lembrando que é CASE SENSITIVE
        frase.count('o', 0, 13) ==> 1     count com fatiamento
```
- Contar fragmento de string:
```py
        frase.find("deo") ==> 11  procura na string se existe "deo" e retorna indice inicial
        frase.find("xxx")  ==> -1    se não existir retorna -1
```
- Operador In:
```py
        "Cur" in frase ==>   true
```
### Transformação
- Replace
```py
        frase.replace("Python", "Android")
```
- upper e lower
```py
        frase.upper()
        frase.lower()
```
- capitalize e title
```py
        frase.capitalize() ==> só primeira letra maiuscula
        frase.title() ==>  Todas as palavras com primeira letra maiuscula
```
- Strip
```py
        frase.strip() ==> remove espaços excedentes no começo e fim da string
        frase.rstrip() ==> remove apenas espaços do fim da string (right)
        frase.lstrip() ==> remove apenas espaços do começo da string (left)
```
### Divisão e Junção
- Split
```py
        frase.split() ==> divide considerando os espaços
```
- Join
```py
        "-".join(frase) ==> "Curso-em-video-Python"
        " ".join(frase) ==> "Curso em video Python"
```
