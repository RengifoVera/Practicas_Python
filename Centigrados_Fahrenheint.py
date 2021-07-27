from numpy.core.arrayprint import DatetimeFormat
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


celsius = np.array([-40,-10,0,8,15,22,38],dtype=float)
fahrenheint = np.array([-40,14,32,46,59,72,100],dtype=float)


capa=tf.keras.layers.Dense(units=1,input_shape=[1])
modelo =tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Entrenando Modelo ........")
historial=modelo.fit(celsius,fahrenheint,epochs=1000,verbose=False)
print("Modelo Entrenado.")


plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])


print("Hagamos Una prueba")

resultado=modelo.predict([100.0])
print("El Resultado es: " + str(resultado) + " Fahrenheint")

print("Variables internas del modelo")
print(capa.get_weights())