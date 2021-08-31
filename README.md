# Machine Learning - kNN
 Implementando um algoritmo simples para aprendizado de máquina. Sim, implementando do zero mesmo porque como bom nerd, gosto do método e da matemática, e não me satisfaçõ em apenas obter um resultado sem saber como chegar nele. Existem bibliotecas muito boas para ML em Python - particularmente gosto muito da scikit learn) mas como kNN é relativamente simples, podemos aproveitar a disposição e construí-lo na mão. 

O conjunto de dados escolhido foi um clássico de qualquer aspirante ao campo de IA / ML / afins, a base de dados das flores do gênero Iris (que você pode conferir aqui neste link: https://archive.ics.uci.edu/ml/datasets/iris)

![iris-machinelearning](https://user-images.githubusercontent.com/62081666/131419211-05a5843e-e2fb-4b6a-89b1-9ceb5ed22392.png) Coisas lindas, né?


kNN é uma técnica de aprendizado baseado em instâncias que assume que todos os elementos de um conjunto são pontos em um espaço de N dimensões, sendo N o número de atributos que descreve um elemento. O algoritmo funciona agrupando os dados próximos neste espaço teórico como similares e é bastante efetivo para conjunto de dados que são linearmente separáveis.

![linha](https://user-images.githubusercontent.com/62081666/131420612-ddfa8c64-2530-4630-9729-fc00df1f60fb.png)

A imagem acima já mostra graficamente uma falha da técnica kNN. o algoritmo sofre de algo chamado _maldição da dimensionalidade_ que implica em dois problemas práticos: 

1) pode ser bastante custoso avaliar um novo ponto e classificá-lo. 

2) diferentemente de outros métodos, como árvores de decisão, que avaliam a classificação a partir de diferentes passos usando um subconjunto dos atributos em cada passo, o kNN usa todos os atributos de uma vez só. Esse fato pode causar uma má representação do conjunto de dados em que, digamos, apenas uma parcela dos atributos é relevante para a classificação. Assim, os outros atributos são apenas ruído, deslocando o ponto no espaço N-dimensional -  oque pode causar gráficos feito o segundo na imagem acima.

Como toda técnica, o kNN tem seus prós e contras. Cabe ao programador colocar a ferramenta certa no lugar certo :)

Todas as fotos cortesia do google imagens :)

 
