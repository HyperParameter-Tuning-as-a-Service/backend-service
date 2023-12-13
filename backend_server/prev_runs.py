from backend_server import app, session, mongo
from flask import redirect, url_for, jsonify

def best_runs_all(runs):
    best_runs = dict()
    for exp_name in runs:
        best_trial = best_run_exp(exp_name, runs.get(exp_name))
        best_runs[exp_name] = best_trial
    return best_runs

def best_run_exp(exp_name, runs):
    best_trial = f'exp_name_{0}'
    best_accuracy = runs[0].get('accuracy')
    for trial in runs:
        if trial.get('accuracy') > best_accuracy:
            best_trial = trial.get('exp_id')
            best_accuracy = trial.get('accuracy')
    return best_trial

@app.route('/prev-runs', defaults={'expname': None}, methods=['GET'])
@app.route('/prev-runs/<expname>', methods=['GET'])
def prev_runs(expname):
    if 'user-id' not in session:
        return redirect(url_for("index"))
    prev_runs = mongo.get_all_runs(session.get('user-id'))
    if len(prev_runs.keys()) == 0:
        data = {'message': 'No previous experiments were found'}
        return jsonify(data), 200
    elif expname is None:
        data = {
            'message': f'found {len(prev_runs.keys())} experiments',
            'runs': prev_runs,
            'best_runs': best_runs_all(prev_runs)
            }
        return jsonify(data), 200
    else:
        if expname not in prev_runs:
            data = {'message': 'given experiment name does not exist'}
            return jsonify(data), 200
        else:
            data = {
                'message': 'found exp',
                'runs': prev_runs.get(expname),
                'best_runs': {expname: best_run_exp(expname, prev_runs.get(expname))}
                }
            return jsonify(data), 200


