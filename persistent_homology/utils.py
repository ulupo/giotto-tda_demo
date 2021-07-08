from sklearn.metrics import accuracy_score, roc_auc_score

def print_scores(fitted_model, X_train, X_valid, y_train, y_valid,
                 show_auc=False):
    res = {
        "Accuracy on train:": accuracy_score(fitted_model.predict(X_train), y_train),
        "Accuracy on valid:": accuracy_score(fitted_model.predict(X_valid), y_valid)
    }
    if show_auc:
        res.update({
            "ROC AUC on train:": roc_auc_score(
                y_train, fitted_model.predict_proba(X_train)[:, 1]
            ),
            "ROC AUC on valid:": roc_auc_score(
                y_valid, fitted_model.predict_proba(X_valid)[:, 1]
            ),
        })

    for k, v in res.items():
        print(k, round(v, 3))
