
from flask import Flask, render_template, request, jsonify, send_file
# import boto3
import json
# # import L4Emodule as L4E
# import re
from flask_cors import CORS
import config
# import awswrangler as wr
import pandas as pd
import joblib
import numpy as np


invalid_method_call_message = {'message': 'Invalid method called'}
success_message = config.success_message
failed_message = config.failed_message


# current_user = boto3.client('sts').get_caller_identity().get('Account')

app = Flask(__name__)
CORS(app)

app.secret_key = "super secret key"

model_training_success_message = "Training of the model started. Please wait while the model is training."

glue_database = config.glue_database
property_data_glue_table = config.property_data_glue_table
property_data_glue_table_for_inference = config.property_data_glue_table_for_inference
meta_data_glue_table = config.meta_data_glue_table

@app.route('/api/detectAnomalies', methods=['POST'])
def detectAnomalies():
    try: 
        json_data = json.dumps(request.json['data']) 
        # Convert JSON to DataFrame
        df_new = pd.read_json(json_data)
        df_new = df_new.set_index('Time')
        # Print the DataFrame
        print(df_new)
        #Load the saved model
        loaded_model = joblib.load('isolation_forest_model.joblib')
        # Predict on new data
        new_results = loaded_model.predict(df_new)
        print(new_results)
        new_anomalies = np.where(new_results == -1)[0]
        print("Number of anomalies detected in data:", len(new_anomalies))
        dictToReturn = {'status': 'SUCCESS',
                            'data': len(new_anomalies), 'message': ''}
        return jsonify(dictToReturn)
    except Exception as error:
        print('An exception occurred', str(error))
        dictToReturn = {'status': 'FAILED', 'message': str(error)}
        return jsonify(dictToReturn)


    
    
@app.route('/')
def home():
    return render_template('LforE.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('LforE.html')


if __name__ == '__main__':
    # app.run(host ='0.0.0.0', port = 5001, debug = True)
    app.run(host='0.0.0.0', port=5001, debug=False)
    # http_server = WSGIServer(("localhost", 5001), app)
    # http_server.serve_forever()
