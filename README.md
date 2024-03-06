ECG Heartbeat Categorization Dataset
===
##Dataset from Kaggle competition: 
####https://www.kaggle.com/datasets/shayanfazeli/heartbeat/data

This dataset is composed of two collections of heartbeat signals derived from two famous datasets in heartbeat classification, the MIT-BIH Arrhythmia Dataset and The PTB Diagnostic ECG Database.
The signals correspond to electrocardiogram (ECG) shapes of heartbeats for the normal case and the cases affected by different arrhythmias and myocardial infarction. These signals are preprocessed and segmented, with each segment corresponding to a heartbeat.

###Content
####Arrhythmia Dataset
 * Number of Samples: 109446
 * Number of Categories: 5
 * Sampling Frequency: 125Hz
 * Data Source: Physionet's MIT-BIH Arrhythmia Dataset
 * Classes: ['N': 0, 'S': 1, 'V': 2, 'F': 3, 'Q': 4]
####The PTB Diagnostic ECG Database
 * Number of Samples: 14552
 * Number of Categories: 2
 * Sampling Frequency: 125Hz
 * Data Source: Physionet's PTB Diagnostic Database
Remark: All the samples are cropped, downsampled and padded with zeroes if necessary to the fixed dimension of 188.

####Data Files
This dataset consists of a series of CSV files. Each of these CSV files contain a matrix, with each row representing an example in that portion of the dataset. The final element of each row denotes the class to which that example belongs.
