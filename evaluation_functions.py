import numpy as np

def print_categorical_acc(ground_truth, predictions):
    for classe in np.unique(ground_truth):
        gt_classe = ground_truth[ground_truth==classe]
        pred_classe = predictions[ground_truth==classe]
        print(f'Classe:{classe} | Total samples:{gt_classe.shape[0]} | Correct predictions: {np.sum(pred_classe==gt_classe)} | {np.sum(pred_classe==gt_classe)/gt_classe.shape[0]}')
    