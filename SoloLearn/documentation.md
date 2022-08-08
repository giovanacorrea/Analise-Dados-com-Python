## Numpy
### **1. O que é a Numpy?**

<p>A Numpy é uma biblioteca que facilita a manipulação de dados, muito utilizada no meio científico. A Numpy é essencial para análise, extração e manipulação de dados estatísticos </p>

### **2. Funções Essenciais** 

<p>Principais funções para manipulação de dados em um array da Numpy</p>


  Função   | Como Funciona
  ---------| -------------------
  np.array | Cria um novo array
  append   | Adiciona um novo elemento no array
  reshape  | Altera a dimensão do array 
  dim      | Retorna o número de dimensões do array 
  size     | Retorna a quantidade de elementos do array
  shape    | Retorna as dimensões do array
  arange   | Permite criar um array a partir de intervalos 
  sort     | Ordena o array
  delete   | Deleta um elemento do array

### **3. Média, Mediana, Variância e Desvio Padrão**

<p>Existem algumas fórmulas essenciais para a análise de dados, que podem ser facilmente realizadas com funções disponibilizadas pela biblioteca Numpy:</p>

  Função   | Como Funciona
  -------- | -------------------
  mean     | Retorna a média
  median   | Retorna a mediana
  std      | Retorna o desvio padrão
  var      | Retorna a variância 

</br>

## Pandas 

### **1. O que é?**

<p> A Pandas é uma biblioteca criada a partir da Numpy, que tem por objetivo facilitar a manipulação de dados para análise. Mais específicamente, para lidar com tabelas e estruturas de dados mais complexas </p>


### **2. Sintax Básica**  

Para importar a biblioteca: </br>
   ```python
   import panda as pd
   ```
### **3. Séries e Dataframes**

<p>Séries e colunas são duas estruturas essenciais da pandas. Uma série é uma coluna de uma tabela e um dataframe é uma matriz de n dimensões criada a partir das séries.</p>

- **Dataframes** 

     Exemplo de criação de dataframe: </br>

    ```python
    import pandas as pd

    data = {'ages': [14, 18, 24, 42],
            'heights': [165, 180, 176, 184]
          }
    df = pd.DataFrame(data)
    print(df)
    ```
    ```
    Output: 
      ages  heights
    0    14      165
    1    18      180
    2    24      176
    3    42      184
    ```
