import gc
import tensorflow as tf
import numpy as np

from alive_progress import alive_bar
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from .random import set_seed, RANDOM_SEED


def clear_backend_and_seeds():
    tf.keras.backend.clear_session()
    tf.compat.v1.reset_default_graph()
    gc.collect()
    set_seed()
    
    
def one_hot_encoding(y, mapping):
    return to_categorical(list(map(lambda i: mapping[i], y)), num_classes=len(mapping.keys()))    

    
def build_report(y_test, y_pred, labels):
    y_test = np.argmax(y_test, axis=1)
    y_pred = np.argmax(y_pred, axis=1)
    
    accuracy = accuracy_score(y_test, y_pred)
    cf_matrix = confusion_matrix(y_test, y_pred).tolist()
    class_report = classification_report(y_test, y_pred, target_names=labels, output_dict=True, zero_division=0)
    return {
        'accuracy': accuracy,
        'confusion_matrix': cf_matrix,
        'classification_report': class_report
    }


def evaluate_model(model, x_test, y_test, labels):
    y_pred = model.predict(x_test, verbose=0)
    return build_report(y_test, y_pred, labels)


def cross_validation(model_builder, x, y, folds, batch_size, epochs, labels=None):
    reports = []
    skfold = StratifiedKFold(n_splits=folds, shuffle=True, random_state=RANDOM_SEED)
    with alive_bar(folds, title=f'Training models', force_tty=True) as progress_bar:
        for i, (train_index, test_index) in enumerate(skfold.split(x, np.argmax(y, axis=1))):
            x_train = x[train_index]
            y_train = y[train_index]
            x_test = x[test_index]
            y_test = y[test_index]
            
            model = model_builder()
            model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=0)
            report = evaluate_model(model, x_test, y_test, labels)
            reports.append(report)
            progress_bar()
    return reports