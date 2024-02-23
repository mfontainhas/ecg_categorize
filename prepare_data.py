import pandas as pd
import matplotlib.pyplot as plt

# According to the dataset information, the MITBIH has 5 different classifications that have the following names
dictionary_value  =['Normal Beats', 'Unknown Beats', 'Ventricular ectopic beats', 'Supraventricular ectopic beats', 'Fusion Beats']

def load_images_ecg():
    mitbih_train = pd.read_csv('DATA/mitbih_train.csv', delimiter=',', header=None)
    mitbih_test = pd.read_csv('DATA/mitbih_test.csv', delimiter=',', header=None)
    ptbdb_abnormal = pd.read_csv('DATA/ptbdb_abnormal.csv', delimiter=',', header=None)
    ptbdb_normal = pd.read_csv('DATA/ptbdb_abnormal.csv', delimiter=',', header=None)
    ptbdb = pd.concat([ptbdb_abnormal, ptbdb_normal])
    return {'mitbih_train':mitbih_train, 'mitbih_test':mitbih_test, 'ptbdb': ptbdb}
    

#Visualize check one ecg sample
#plt.plot(df1.iloc[0].index, df1.iloc[0].values)

# Check the histogram of the different each number represents the dictionary_value
#df1.iloc[:,187].hist()


