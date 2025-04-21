from sklearn.neural_network import MLPClassifier
from pandas import read_excel as rx
from matplotlib import pyplot
import numpy as np

#Loading the data
dataset_init=rx('iris_data.xlsx',names=['Setal_length','Setal_width','Petal_length','Petal_width','Class'])
dataset=dataset_init.values
values=dataset[:,0:4] #Values
classes=dataset[:,4]   #Classes
mlp=MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='sgd', alpha=0.00001, max_iter=3000)
mlp_with_separation_data=MLPClassifier(hidden_layer_sizes=(100,), early_stopping=True, validation_fraction=0.1, activation='logistic', solver='sgd', alpha=0.00001, max_iter=3000)

#Training
mlp.fit(values,classes)
mlp_with_separation_data.fit(values,classes)
print("Acerto do MLP sem separação da base de dados dos testes: ",mlp.score(values,classes))
print("Acerto do MLP com separação da base de dados dos testes: ",mlp_with_separation_data.score(values,classes))

#Plotting
pyplot.figure()
pyplot.plot(mlp.loss_curve_)
pyplot.plot(mlp_with_separation_data.loss_curve_)
pyplot.savefig('mlp_loss.png')


#Guessing
setal_length = float(input("Digite o valor do comprimento da petala "))
setal_width =  float(input("Digite o valor da largura da petala "))
petal_length = float(input("Digite o valor do comprimento da petala "))
petal_width = float(input("Digite o valor da largura da petala "))
new_flower = np.array([setal_length,setal_width,petal_length,petal_width]).reshape(1,-1)

pred_mlp = mlp.predict(new_flower)
pred_mlp_with_separation_data = mlp_with_separation_data.predict(new_flower)

print("Previsão do MLP sem separação dos dados: ",pred_mlp[0])
print("Previsão do MLP com separação dos dados: ",pred_mlp_with_separation_data[0])