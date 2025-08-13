
import streamlit as st
from prediction_helper import predict
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .prediction-result {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }
    
    .input-section {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏥 Health Insurance Cost Predictor</h1>
    <p style="font-size: 1.2rem; margin: 0;">AI-Powered Insurance Cost Estimation Tool</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for navigation and info
with st.sidebar:
    st.markdown("## 📊 App Information")
    st.markdown("""
    This application uses machine learning to predict health insurance costs based on various factors including:
    
    • **Personal Information**: Age, Gender, Marital Status
    • **Health Factors**: BMI, Medical History, Smoking Status
    • **Financial Details**: Income, Employment Status
    • **Coverage**: Insurance Plan Type, Region
    
    The model provides accurate predictions using advanced ML algorithms trained on comprehensive insurance data.
    """)
    
    st.markdown("---")
    st.markdown("## 🔍 How to Use")
    st.markdown("""
    1. Fill in your information in the form
    2. Click 'Predict Insurance Cost'
    3. View your personalized cost estimate
    4. Explore cost breakdown and insights
    """)
    
    st.markdown("---")
    st.markdown("## 📈 Model Accuracy")
    st.markdown("""
    Our machine learning models achieve high accuracy through:
    • Separate models for different age groups
    • Advanced feature engineering
    • Comprehensive data preprocessing
    • Regular model updates
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 📝 Enter Your Information")
    
    # Personal Information Section
    st.markdown("### 👤 Personal Information")
    personal_col1, personal_col2, personal_col3 = st.columns(3)
    
    with personal_col1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100, value=30)
        gender = st.selectbox('Gender', ['Male', 'Female'])
    
    with personal_col2:
        marital_status = st.selectbox('Marital Status', ['Unmarried', 'Married'])
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20, value=0)
    
    with personal_col3:
        income_lakhs = st.number_input('Income (Lakhs ₹)', step=1, min_value=0, max_value=200, value=10)
        genetical_risk = st.number_input('Genetic Risk Level', step=1, min_value=0, max_value=5, value=2)
    
    # Health Information Section
    st.markdown("### 🏥 Health Information")
    health_col1, health_col2, health_col3 = st.columns(3)
    
    with health_col1:
        bmi_category = st.selectbox('BMI Category', ['Normal', 'Obesity', 'Overweight', 'Underweight'])
        smoking_status = st.selectbox('Smoking Status', ['No Smoking', 'Regular', 'Occasional'])
    
    with health_col2:
        medical_history = st.selectbox('Medical History', [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ])
    
    with health_col3:
        employment_status = st.selectbox('Employment Status', ['Salaried', 'Self-Employed', 'Freelancer'])
    
    # Insurance Details Section
    st.markdown("### 🛡️ Insurance Details")
    insurance_col1, insurance_col2 = st.columns(2)
    
    with insurance_col1:
        insurance_plan = st.selectbox('Insurance Plan', ['Bronze', 'Silver', 'Gold'])
    
    with insurance_col2:
        region = st.selectbox('Region', ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

with col2:
    st.markdown("## 📊 Quick Insights")
    
    # Risk Assessment
    risk_score = 0
    if medical_history != 'No Disease':
        risk_score += 3
    if smoking_status != 'No Smoking':
        risk_score += 2
    if bmi_category in ['Obesity', 'Overweight']:
        risk_score += 2
    if age > 50:
        risk_score += 2
    
    risk_level = "Low" if risk_score <= 2 else "Medium" if risk_score <= 5 else "High"
    risk_color = "#28a745" if risk_level == "Low" else "#ffc107" if risk_level == "Medium" else "#dc3545"
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>Risk Assessment</h4>
        <p style="font-size: 2rem; color: {risk_color}; font-weight: bold; margin: 0;">{risk_level}</p>
        <p style="margin: 0; color: #6c757d;">Score: {risk_score}/10</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cost Range Estimate
    base_cost = income_lakhs * 0.1
    if insurance_plan == 'Gold':
        base_cost *= 1.5
    elif insurance_plan == 'Silver':
        base_cost *= 1.2
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>Estimated Cost Range</h4>
        <p style="font-size: 1.5rem; color: #667eea; font-weight: bold; margin: 0;">₹{int(base_cost*0.8):,} - ₹{int(base_cost*1.2):,}</p>
        <p style="margin: 0; color: #6c757d;">Annual Premium</p>
    </div>
    """, unsafe_allow_html=True)

# Prediction Button
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button('🚀 Predict Insurance Cost', use_container_width=True):
        # Validate inputs
        if age == 0 or income_lakhs == 0:
            st.error("❌ Please fill in all required fields (Age and Income cannot be 0)")
            st.stop()
        
        # Check if all fields have valid values
        required_fields = {
            'Age': age,
            'Income': income_lakhs,
            'Gender': gender,
            'Marital Status': marital_status,
            'BMI Category': bmi_category,
            'Smoking Status': smoking_status,
            'Employment Status': employment_status,
            'Region': region,
            'Medical History': medical_history,
            'Insurance Plan': insurance_plan
        }
        
        empty_fields = [field for field, value in required_fields.items() if not value or value == '']
        if empty_fields:
            st.error(f"❌ Please fill in all required fields: {', '.join(empty_fields)}")
            st.stop()
        # Create input dictionary
        input_dict = {
            'Age': age,
            'Number of Dependants': number_of_dependants,
            'Income in Lakhs': income_lakhs,
            'Genetical Risk': genetical_risk,
            'Insurance Plan': insurance_plan,
            'Employment Status': employment_status,
            'Gender': gender,
            'Marital Status': marital_status,
            'BMI Category': bmi_category,
            'Smoking Status': smoking_status,
            'Region': region,
            'Medical History': medical_history
        }
        
        # Make prediction
        try:
            with st.spinner('🤖 Analyzing your data and calculating insurance cost...'):
                prediction = predict(input_dict)
        except Exception as e:
            st.error(f"❌ Error during prediction: {str(e)}")
            st.info("Please check your input values and try again.")
            st.stop()
        
        # Display result
        st.markdown(f"""
        <div class="prediction-result">
            <h2>🎯 Your Insurance Cost Prediction</h2>
            <h1 style="font-size: 3rem; margin: 1rem 0;">₹{prediction:,}</h1>
            <p style="font-size: 1.2rem; margin: 0;">Annual Premium</p>
            <p style="font-size: 1rem; margin: 0.5rem 0;">Monthly: ₹{prediction//12:,} | Quarterly: ₹{prediction//4:,}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Cost breakdown and insights
        st.markdown("## 📊 Cost Analysis & Insights")
        
        # Create cost breakdown chart
        cost_breakdown = {
            'Base Premium': prediction * 0.6,
            'Risk Factor': prediction * 0.25,
            'Plan Benefits': prediction * 0.15
        }
        
        fig = go.Figure(data=[go.Pie(labels=list(cost_breakdown.keys()), 
                                   values=list(cost_breakdown.values()),
                                   hole=0.4,
                                   marker_colors=['#667eea', '#764ba2', '#f093fb'])])
        fig.update_layout(title="Cost Breakdown", height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Insights and recommendations
        col_ins1, col_ins2 = st.columns(2)
        
        with col_ins1:
            st.markdown("### 💡 Cost Optimization Tips")
            if insurance_plan == 'Gold':
                st.info("Consider Silver plan to reduce costs by ~20%")
            if smoking_status != 'No Smoking':
                st.info("Quitting smoking could reduce your premium by 15-25%")
            if bmi_category in ['Obesity', 'Overweight']:
                st.info("Healthy BMI could lower your premium by 10-20%")
            if age > 50:
                st.info("Early enrollment can lock in lower rates")
        
        with col_ins2:
            st.markdown("### 📈 Factors Affecting Your Cost")
            factors = []
            if age > 50:
                factors.append("Age (Higher risk category)")
            if medical_history != 'No Disease':
                factors.append("Medical History (Pre-existing conditions)")
            if smoking_status != 'No Smoking':
                factors.append("Smoking Status (Risk factor)")
            if bmi_category in ['Obesity', 'Overweight']:
                factors.append("BMI Category (Health risk)")
            if insurance_plan == 'Gold':
                factors.append("Premium Plan (Enhanced coverage)")
            
            for factor in factors:
                st.markdown(f"• {factor}")
        
        # Calculate risk level for this prediction
        prediction_risk_score = 0
        if medical_history != 'No Disease':
            prediction_risk_score += 3
        if smoking_status != 'No Smoking':
            prediction_risk_score += 2
        if bmi_category in ['Obesity', 'Overweight']:
            prediction_risk_score += 2
        if age > 50:
            prediction_risk_score += 2
        
        prediction_risk_level = "Low" if prediction_risk_score <= 2 else "Medium" if prediction_risk_score <= 5 else "High"
        
        # Save prediction history
        if 'prediction_history' not in st.session_state:
            st.session_state.prediction_history = []
        
        st.session_state.prediction_history.append({
            'timestamp': datetime.now(),
            'prediction': prediction,
            'age': age,
            'plan': insurance_plan,
            'risk_level': prediction_risk_level
        })

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; padding: 2rem;">
    <p>🔒 Your data is processed securely and never stored permanently</p>
    <p>📱 Built with Streamlit & Machine Learning</p>
    <p>© 2024 Health Insurance Cost Predictor</p>
</div>
""", unsafe_allow_html=True)
