import numpy as np

class Perceptron:
  def __init__(self, learning_rate = 0.01):
    self.lr = learning_rate
    self.weights = None
    self.bias = 0
    self.max_iterations = 1000


  #funcion de activacion para saber los resultados depues de aplicarle los pesos
  def activation_function(self, x_i):
    if x_i >= 0:
      return 1
    return 0
    
  def learn(self, x, d):
    #pesos para cada pixel, matriz 6x5
    self.weights = np.zeros((30,1))

    #valor despues de la funcion
    y = None

    #iteraciones para tener los pesos correctos
    for i in range(self.max_iterations):
      for idx, x_i in enumerate(x):
        #si el valor obtenido es igual al esperado
        if (y == d):
          break

        #producto punto (matriz de test, con los pesos) x0*w0 + x1*w1 + x2*w2
        output = np.dot(x_i.ravel(), self.weights) + self.bias
        #pasar el resulatdo por la funcino de activación
        y = self.activation_function(output)

        #actualizamos pesos: w0 = w0 + taza aprendizaje * x0 * (resultado del valor deseado - el obtenido)
        self.weights += self.lr * x_i.ravel().transpose() * (d[idx] - y)
        #self.bias += self.lr * (d[idx] - y)

  #funcion depues de que entrenamos los perceptrones, para hacer la prueba de que el entrenamiento es correcto
  def predict(self, x):
    #output = producto punto (matriz de test, con los pesos)
    output = np.dot(x.ravel(), self.weights) + self.bias
    return self.activation_function(output)
  

#cuando cambian tmbn cambia lo que reconoce y lo que no, hay que o hacer más entradas precisas, o controlar estas xd
ex_r1 = np.matrix(np.random.randint(2,size=(5,6)))
ex_r2 = np.matrix(np.random.randint(2,size=(5,6)))
ex_r3 = np.matrix(np.random.randint(2,size=(5,6)))
ex_r4 = np.matrix(np.random.randint(2,size=(5,6)))
ex_r5 = np.matrix(np.random.randint(2,size=(5,6)))
ex_r6 = np.matrix(np.random.randint(2,size=(5,6)))

'''
print(ex_r1)
print(ex_r2)
print(ex_r3)
print(ex_r4)
print(ex_r5)
print(ex_r6)
'''
#-------------------CERO--------------------------------#
ex0_00 = np.matrix([[1,1,1,1,1],
                   [1,0,0,0,1],
                   [1,0,0,0,1],
                   [1,0,0,0,1],
                   [1,0,0,0,1],
                   [1,1,1,1,1]])

ex0_01 = np.matrix([[0,1,1,1,0],
                   [0,1,0,1,0],
                   [0,1,0,1,0],
                   [0,1,0,1,0],
                   [0,1,1,1,0],
                   [0,0,0,0,0]])

ex0_02 = np.matrix([[0,0,0,0,0],
                   [0,1,1,1,0],
                   [0,1,0,1,0],
                   [0,1,0,1,0],
                   [0,1,1,1,0],
                   [0,0,0,0,0]])

ex0_03 = np.matrix([[0,0,0,0,0],
                   [0,1,1,1,0],
                   [0,1,0,1,0],
                   [0,1,0,1,0],
                   [0,1,0,1,0],
                   [0,1,1,1,0]])

ex0_04 = np.matrix([[0,0,0,0,0],
                   [0,0,1,1,1],
                   [0,0,1,0,1],
                   [0,0,1,0,1],
                   [0,0,1,0,1],
                   [0,0,1,1,1]])

ex0_05 = np.matrix([[0,0,0,0,0],
                   [1,1,1,0,0],
                   [1,0,1,0,0],
                   [1,0,1,0,0],
                   [1,0,1,0,0],
                   [1,1,1,0,0]])



#---------------CERO---------------------



#--------------UNO-----------------------


#-----------------------------------


# 1 triangular
ex1_01 =  np.matrix([[0,0,0,0,0],
                     [0,0,0,0,1],
                     [0,0,0,1,1],
                     [0,0,0,0,1],
                     [0,0,0,0,1],
                     [0,0,0,0,1]])

ex1_02 =  np.matrix([[0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,1,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0]])

ex1_03 =  np.matrix([[0,0,0,0,0],
                     [0,1,0,0,0],
                     [1,1,0,0,0],
                     [0,1,0,0,0],
                     [0,1,0,0,0],
                     [0,1,0,0,0]])

ex1_04 =  np.matrix([[0,0,1,0,0],
                     [0,1,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]])

ex1_05 =  np.matrix([[0,1,0,0,0],
                     [1,1,0,0,0],
                     [0,1,0,0,0],
                     [0,1,0,0,0],
                     [0,1,0,0,0],
                     [0,0,0,0,0]])

ex1_06 =  np.matrix([[0,0,0,1,0],
                     [0,0,1,1,0],
                     [0,0,0,1,0],
                     [0,0,0,1,0],
                     [0,0,0,1,0],
                     [0,0,0,0,0]])

ex1_07 =  np.matrix([[0,0,0,0,1],
                     [0,0,0,1,1],
                     [0,0,0,0,1],
                     [0,0,0,0,1],
                     [0,0,0,0,1],
                     [0,0,0,0,0]])




#--------------UNO-----------------------

#--------------DOS-----------------------

ex2_01 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1]])

ex2_02 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1]])


ex2_03 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,0]])

ex2_04 = np.matrix([[0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1]])




#-------------DOS---------------------------

#-------------TRES-------------------------

#para aprender 3

ex3_01 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])

ex3_02 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])


ex3_03 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,0]])

ex3_04 = np.matrix([[0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])

#---------------------------------------------------------
#misma arriba pero dif tamaños, linea horizontal del medio
ex3_05 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])

ex3_06 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])


ex3_07 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,0]])

ex3_08 = np.matrix([[0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])

#------------TRES----------------------------


#------------CUATRO--------------

ex4_00 = np.matrix([[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])

ex4_01 = np.matrix([[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])

ex4_02 = np.matrix([[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,0]])

ex4_03 = np.matrix([[0,0,0,0,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])

ex4_04 = np.matrix([[0,1,0,0,1],
                    [0,1,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,0]])

ex4_05 = np.matrix([[1,0,0,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,0],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,0,0,0]])

ex4_06 = np.matrix([[0,0,0,0,0],
                    [1,0,0,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,0],
                    [0,0,0,1,0],
                    [0,0,0,1,0]])

ex4_07 = np.matrix([[0,0,0,0,0],
                    [0,1,0,0,1],
                    [0,1,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])
#------------CUATRO-----------------


#------------CINCO----------------

ex5_01 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])

ex5_02 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])


ex5_03 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,0]])

ex5_04 = np.matrix([[0,0,0,0,0],
                    [1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])

#---------------------------------------------------------

ex5_05 = np.matrix([[0,1,1,1,1],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1]])


ex5_06 = np.matrix([[0,1,1,1,1],
                    [0,1,0,0,0],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1]])


ex5_07 = np.matrix([[0,1,1,1,1],
                    [0,1,0,0,0],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,0]])

ex5_08 = np.matrix([[0,0,0,0,0],
                    [0,1,1,1,1],
                    [0,1,0,0,0],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1]])

#----------CINCO------------------


#---------SEIS--------------------

ex6_01 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]])
					
ex6_02 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]])
					
ex6_03 = np.matrix([[1,1,1,1,1],
                    [1,1,0,0,0],
                    [1,1,1,1,1],
                    [1,1,0,0,1],
                    [1,1,0,0,1],
                    [1,1,1,1,1]])
					
ex6_04 = np.matrix([[1,1,1,1,1],
                    [1,1,0,0,0],
                    [1,1,0,0,0],
                    [1,1,1,1,1],
                    [1,1,0,0,1],
                    [1,1,1,1,1]])
					
ex6_05 = np.matrix([[1,1,1,1,1],
                    [1,1,0,0,0],
                    [1,1,0,0,0],
                    [1,1,1,1,1],
                    [1,1,0,0,1],
                    [1,1,1,1,1]])
					
ex6_06 = np.matrix([[1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,0]])

#--------SEIS-----------------------



#-------SIETE-----------------

ex7_01 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])
					
ex7_02 = np.matrix([[1,1,1,1,1],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]])
					
ex7_03 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]])
					
ex7_04 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0]])
					
ex7_05 = np.matrix([[1,1,1,1,1],
                    [0,0,0,1,0],
                    [1,1,1,1,1],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]])
					
ex7_06 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]])
					
ex7_07 = np.matrix([[1,1,1,1,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0]])
#-----------SIETE--------------


#-----------OCHO-----------------

ex8_01 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]])
					
ex8_02 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]])
					
ex8_03 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]])
					
ex8_04 = np.matrix([[0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,1,1,1,0]])
					
ex8_05 = np.matrix([[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,1,1,1,0]])
					
ex8_06 = np.matrix([[0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]])
					
ex8_07 = np.matrix([[0,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,0]])
					
ex8_08 = np.matrix([[0,0,0,0,0],
                    [0,1,1,1,1],
                    [0,1,0,0,1],
                    [0,1,1,1,1],
                    [0,1,0,0,1],
                    [0,1,1,1,1]])
#-------------OCHO------------------


#-------------NUEVE-----------------

ex9_01 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])
					
					
ex9_02 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,1]])
					
ex9_03 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1]])
					
ex9_04 = np.matrix([[1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,1,1,1]])
					
ex9_05 = np.matrix([[0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]])
					
					
ex9_06 = np.matrix([[0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,1,1,1,0]])
#------------NUEVE---------------------


#---------------ENTRENAMIENTO-------------
p0 = Perceptron(0.1)
p1 = Perceptron(0.1)
p2 = Perceptron(0.1)

p3 = Perceptron(0.1)
p4 = Perceptron(0.1)
p5 = Perceptron(0.1)

p6 = Perceptron(0.1)
p7 = Perceptron(0.1)

p8 = Perceptron(0.1)
p9 = Perceptron(0.1)

x0 = [ex0_00, ex0_01, ex0_02, ex0_03, ex0_04, ex0_05, ex1_01, ex1_02, ex1_03, ex1_04, ex1_05, ex1_06, ex1_07]

x1 = [ex1_01, ex1_02, ex1_03, ex1_04, ex1_05, ex1_06, ex1_07]

x2 = [ex2_01, ex2_02, ex2_03, ex2_04]

x3 = [ex3_01, ex3_02, ex3_03, ex3_04, ex3_05, ex3_06, ex3_07, ex3_08]

x4= [ex4_00, ex4_01, ex4_02, ex4_03, ex4_04, ex4_05, ex4_06, ex4_07]

x5 = [ex5_01, ex5_02, ex5_03, ex5_04, ex5_05, ex5_06, ex5_07, ex5_08]

x6 = [ex6_01, ex6_02, ex6_03, ex6_04, ex6_05, ex6_06]

x7 = [ex7_01, ex7_02, ex7_03, ex7_04, ex7_05, ex7_06, ex7_07]

x8 = [ex8_01, ex8_02, ex8_03, ex8_04, ex8_05, ex8_06, ex8_07, ex8_08]

x9 = [ex9_01, ex9_02, ex9_03, ex9_04, ex9_05, ex9_06]

d0 = [1]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d1 = [0]*len(x0) + [1]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d2 = [0]*len(x0) + [0]*len(x1) + [1]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d3 = [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [1]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d4 = [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [1]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d5 = [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [1]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d6 = [1]*len(x6) + [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x7) + [0]*len(x8) + [0]*len(x9)
d7 = [1]*len(x7) + [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x8) + [0]*len(x9)
d8 = [1]*len(x8) + [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x9)
d9 = [1]*len(x9) + [0]*len(x0) + [0]*len(x1) + [0]*len(x2) + [0]*len(x3) + [0]*len(x4) + [0]*len(x5) + [0]*len(x6) + [0]*len(x7) + [0]*len(x8)

p0.learn(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9, d0)
p1.learn(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9, d1)
p2.learn(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9, d2)
p3.learn(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9, d3)
p4.learn(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9, d4)
p5.learn(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9, d5)
p6.learn(x6+x0+x1+x2+x3+x4+x5+x7+x8+x9, d6)
p7.learn(x7+x0+x1+x2+x3+x4+x5+x6+x8+x9, d7)
p8.learn(x8+x0+x1+x2+x3+x4+x5+x6+x7+x9, d8)
p9.learn(x9+x0+x1+x2+x3+x4+x5+x6+x7+x8, d9)

#es un cero
test = np.loadtxt("test.txt")
print(test)
#es un 1
test1 =  np.loadtxt("test1.txt")
print(test1)
#es un 2
test2 =  np.loadtxt("test2.txt")
print(test2)
#Es un 3
test3 = np.loadtxt("test3.txt")
print(test3)

test4 = np.loadtxt("test4.txt")
print(test4)

test5 = np.loadtxt("test5.txt")
print(test5)

test6 = np.loadtxt("test6.txt")
print(test6)

test7 = np.loadtxt("test7.txt")
print(test7)

test8 = np.loadtxt("test8.txt")
print(test8)

test9 = np.loadtxt("test9.txt")
print(test9)

def Identify(test):
  recognition = []
  recognition.append(p0.predict(test))
  recognition.append(p1.predict(test))
  recognition.append(p2.predict(test))
  recognition.append(p3.predict(test))
  recognition.append(p4.predict(test))
  recognition.append(p5.predict(test))
  recognition.append(p6.predict(test))
  recognition.append(p7.predict(test))
  recognition.append(p8.predict(test))
  recognition.append(p9.predict(test))
  try:
    return (str)(recognition.index(1))
  except: return ("no se reconoció")

print ("test es " + Identify(test))
print ("test1 es " + Identify(test1))
print ("test2 es " + Identify(test2))
print ("test3 es " + Identify(test3))
print ("test4 es " + Identify(test4))
print ("test5 es " + Identify(test5))
print ("test6 es " + Identify(test6))
print ("test7 es " + Identify(test7))
print ("test8 es " + Identify(test8))
print ("test9 es " + Identify(test9))
