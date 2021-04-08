#SMART BRAIN 

#Se debe instalar tensorflow e ImageAI.

from imageai.Prediction import ImagePrediction		#Usamos una librería ya existente.
import os

execution_path=os.getcwd()							#Devuelve el path de nuestra carpeta.

prediction = ImagePrediction()

prediction.setModelTypeAsSqueezeNet()			#Escogemos alguno de los módulos (squeeze para este)
												#Se descarga el módulo y se añade a esta carpeta.

prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

#result_count serán las predicciones que queremos devolver.
predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)