import numpy as np
import pandas as pd


def from_dict(report):
    accuracy = report["accuracy"]
    precision = report['classification_report']['weighted avg']['precision']
    recall = report['classification_report']['weighted avg']['recall']
    f1 = report['classification_report']['weighted avg']['f1-score']
    return accuracy, precision, recall, f1


def from_list(reports):
    accuracies = []
    precisions = []
    recalls = []
    f1s = []

    for report in reports:
        accuracies.append(report['accuracy'])
        precisions.append(report['classification_report']['weighted avg']['precision'])
        recalls.append(report['classification_report']['weighted avg']['recall'])
        f1s.append(report['classification_report']['weighted avg']['f1-score'])

    return np.mean(accuracies), np.mean(precisions), np.mean(recalls), np.mean(f1s)


def extract_metrics(report):
    return from_dict(report) if isinstance(report, dict) else from_list(report)


def metrics_summary(reports, labels):
    summary = {
        'accuracy': [],
        'precision': [],
        'recall': [],
        'f1-score': []
    }
    
    for report in reports:
        accuracy, precision, recall, f1 = extract_metrics(report)
        summary['accuracy'].append(accuracy)
        summary['precision'].append(precision)
        summary['recall'].append(recall)
        summary['f1-score'].append(f1)
    
    df = pd.DataFrame(summary, index=labels)
    return df

        
def metric_increment(report_a, report_b):
    def compute_increment(old, new):
        return (new - old) / (old) * 100
    
    accuracy_a, precision_a, recall_a, f1_a = extract_metrics(report_a)
    accuracy_b, precision_b, recall_b, f1_b = extract_metrics(report_b)
    return compute_increment(accuracy_a, accuracy_b), compute_increment(precision_a, precision_b), compute_increment(recall_a, recall_b), compute_increment(f1_a, f1_b)


def metric_increment_summary(comparisons):
    increments = {
        'accuracy': [],
        'precision': [],
        'recall': [],
        'f1-score': []
    }
    
    for (report_a, report_b) in comparisons.values():
        acc_inc, prec_inc, rec_inc, f1_inc = metric_increment(report_a, report_b)
        increments['accuracy'].append(acc_inc)
        increments['precision'].append(prec_inc)
        increments['recall'].append(rec_inc)
        increments['f1-score'].append(f1_inc)
        
    df = pd.DataFrame(increments, index=list(comparisons.keys()))
    return df