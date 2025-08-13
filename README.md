# 🏥 Health Insurance Premium Predictor

Link - https://sk-health-insurance-premium-predictor.streamlit.app/

A professional, AI-powered web application that predicts health insurance costs using machine learning algorithms. Built with Streamlit and Python, this app provides accurate cost estimates based on comprehensive health and personal factors.

## ✨ Features

- **AI-Powered Predictions**: Uses advanced machine learning models for accurate cost estimation
- **Professional UI/UX**: Modern, responsive design with intuitive user interface
- **Comprehensive Analysis**: Considers multiple factors including health, financial, and personal details
- **Real-time Insights**: Provides cost breakdown, risk assessment, and optimization tips
- **Interactive Visualizations**: Beautiful charts and graphs using Plotly
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the project files**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser** and navigate to the displayed URL (usually `http://localhost:8501`)

## 📊 How It Works

The application uses two separate machine learning models:

1. **Young Age Model** (≤25 years): Specialized for younger demographics
2. **General Model** (>25 years): Optimized for adult populations

### Input Factors

- **Personal Information**: Age, Gender, Marital Status, Dependants
- **Health Factors**: BMI Category, Medical History, Smoking Status, Genetic Risk
- **Financial Details**: Income, Employment Status
- **Coverage Options**: Insurance Plan (Bronze/Silver/Gold), Region

### Output

- **Predicted Annual Premium**: Accurate cost estimation
- **Cost Breakdown**: Visual representation of premium components
- **Risk Assessment**: Personalized risk level evaluation
- **Optimization Tips**: Suggestions to reduce insurance costs

## 🏗️ Project Structure

```
App/
├── main.py                 # Main Streamlit application
├── prediction_helper.py    # ML prediction logic and preprocessing
├── model_young.joblib     # Young age group ML model
├── model_rest.joblib      # General population ML model
├── scaler_young.joblib    # Young age group data scaler
├── scaler_rest.joblib     # General population data scaler
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🎯 Key Features

### Professional UI Components
- **Gradient Headers**: Modern, eye-catching design elements
- **Metric Cards**: Clean, organized information display
- **Interactive Forms**: User-friendly input fields with validation
- **Responsive Layout**: Optimized for all screen sizes

### Advanced Functionality
- **Real-time Risk Assessment**: Instant evaluation of health risk factors
- **Cost Optimization Tips**: Personalized recommendations for cost reduction
- **Visual Analytics**: Interactive charts and graphs
- **Prediction History**: Track previous estimates (in session)

### Security & Privacy
- **Local Processing**: All data processed locally, no external API calls
- **Session-based Storage**: Temporary storage during app usage
- **No Data Persistence**: User information is not permanently stored

## 🔧 Technical Details

### Machine Learning Models
- **Algorithm**: Advanced regression models with feature engineering
- **Training Data**: Comprehensive insurance dataset with multiple variables
- **Accuracy**: High prediction accuracy through model specialization
- **Scalability**: Efficient preprocessing and prediction pipeline

### Frontend Technologies
- **Streamlit**: Modern web framework for data applications
- **Custom CSS**: Professional styling with gradients and animations
- **Plotly**: Interactive data visualizations
- **Responsive Design**: Mobile-first approach

## 📱 Usage Guide

1. **Fill Information**: Complete all required fields in the form
2. **Review Inputs**: Verify your information before prediction
3. **Get Prediction**: Click the prediction button for instant results
4. **Analyze Results**: Review cost breakdown and insights
5. **Optimize**: Use provided tips to potentially reduce costs

## 🎨 Customization

The app is highly customizable:

- **Color Schemes**: Modify CSS variables for different themes
- **Layout**: Adjust column arrangements and spacing
- **Features**: Add new input fields or output metrics
- **Styling**: Customize fonts, colors, and visual elements

## 🤝 Contributing

Feel free to contribute to improve the application:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📄 License

This project is open source and available under the Apache License.

## 🆘 Support

For questions or issues:
- Check the documentation above
- Review the code comments
- Ensure all dependencies are properly installed

## 🔮 Future Enhancements

- **User Accounts**: Save prediction history and preferences
- **Advanced Analytics**: More detailed cost analysis and trends
- **Comparison Tools**: Compare different insurance plans
- **Export Features**: Download reports and predictions
- **API Integration**: Connect with real insurance providers

---

**Built with ❤️ using Streamlit, Python, and Machine Learning**
