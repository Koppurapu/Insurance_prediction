import pickle
import numpy as np

class insurance_prediction:
    def __init__(self):
        # Load BOTH the scaler and the model
        with open('artifacts/scaler.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
        with open('artifacts/model.pkl', 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs):
        input_data = np.array([[Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs]])
        input_s = self.scaler.transform(input_data)
        
        # Use self.model.predict, NOT self.predict
        result = self.model.predict(input_s) 
        return result[0]