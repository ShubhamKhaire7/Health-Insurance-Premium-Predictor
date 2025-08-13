import pandas as pd
import joblib

model_young = joblib.load("model_young.joblib")
model_rest = joblib.load("model_rest.joblib")
scaler_young = joblib.load("scaler_young.joblib")
scaler_rest = joblib.load("scaler_rest.joblib")

def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    # Split the medical history into potential two parts and convert to lowercase
    diseases = medical_history.lower().split(" & ")

    # Calculate the total risk score by summing the risk scores for each part
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)  # Default to 0 if disease not found

    max_score = 14 # risk score for heart disease (8) + second max risk score (6) for diabetes or high blood pressure
    min_score = 0  # Since the minimum score is always 0

    # Normalize the total risk score
    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score

def preprocess_input(input_dict):
    # Define the expected columns and initialize the DataFrame with zeros
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}

    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Manually assign values for each categorical input based on input_dict
    for key, value in input_dict.items():
        if key == 'Gender' and value == 'Male':
            df['gender_Male'] = 1
        elif key == 'Region':
            if value == 'Northwest':
                df['region_Northwest'] = 1
            elif value == 'Southeast':
                df['region_Southeast'] = 1
            elif value == 'Southwest':
                df['region_Southwest'] = 1
        elif key == 'Marital Status' and value == 'Unmarried':
            df['marital_status_Unmarried'] = 1
        elif key == 'BMI Category':
            if value == 'Obesity':
                df['bmi_category_Obesity'] = 1
            elif value == 'Overweight':
                df['bmi_category_Overweight'] = 1
            elif value == 'Underweight':
                df['bmi_category_Underweight'] = 1
        elif key == 'Smoking Status':
            if value == 'Occasional':
                df['smoking_status_Occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_Regular'] = 1
        elif key == 'Employment Status':
            if value == 'Salaried':
                df['employment_status_Salaried'] = 1
            elif value == 'Self-Employed':
                df['employment_status_Self-Employed'] = 1
        elif key == 'Insurance Plan':  # Correct key usage with case sensitivity
            df['insurance_plan'] = insurance_plan_encoding.get(value, 1)
        elif key == 'Age':  # Correct key usage with case sensitivity
            df['age'] = value
        elif key == 'Number of Dependants':  # Correct key usage with case sensitivity
            df['number_of_dependants'] = value
        elif key == 'Income in Lakhs':  # Correct key usage with case sensitivity
            df['income_lakhs'] = value
        elif key == "Genetical Risk":
            df['genetical_risk'] = value

    # Assuming the 'normalized_risk_score' needs to be calculated based on the 'age'
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])
    df = handle_scaling(input_dict['Age'], df)

    return df

def handle_scaling(age, df):
    # scale age and income_lakhs column
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']
    
    # Handle column name mismatches between different scalers
    # Only add the column if it's needed and doesn't already exist
    if 'genitical_risk' in cols_to_scale and 'genitical_risk' not in df.columns:
        if 'genetical_risk' in df.columns:
            df['genitical_risk'] = df['genetical_risk'].copy()
    
    # Remove the original genetical_risk column if we created genitical_risk
    if 'genitical_risk' in df.columns and 'genitical_risk' in df.columns:
        df = df.drop('genetical_risk', axis=1)

    df['income_level'] = None # since scaler object expects income_level supply it. This will have no impact on anything
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    df.drop('income_level', axis='columns', inplace=True)
    
    # Determine which model will be used to set the correct column names
    if age <= 25:
        # Young model expects genetical_risk (correct spelling)
        expected_columns = [
            'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
            'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
            'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
            'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
        ]
    else:
        # Older model expects genitical_risk (with typo)
        expected_columns = [
            'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genitical_risk', 'normalized_risk_score',
            'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
            'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
            'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
        ]
        
        # Rename genetical_risk to genitical_risk to match what the older model expects
        if 'genetical_risk' in df.columns:
            df = df.rename(columns={'genetical_risk': 'genitical_risk'})
    
    # Keep only the expected columns in the correct order
    df = df[expected_columns]

    return df

def predict(input_dict):
    try:
        input_df = preprocess_input(input_dict)

        if input_dict['Age'] <= 25:
            prediction = model_young.predict(input_df)
        else:
            prediction = model_rest.predict(input_df)
        
        return int(prediction[0])
        
    except Exception as e:
        raise e
