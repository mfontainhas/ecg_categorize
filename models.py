from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


#Different models created for ecg classification

def model_dense_layers_v1():
    # Simple first approach classification
    model = Sequential()
    model.add(Dense(186,activation='relu', input_shape=(186,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(5,activation='softmax'))
    return model