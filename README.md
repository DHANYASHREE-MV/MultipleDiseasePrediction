# Multiple Disease Prediction System

A web-based system for predicting Diabetes, Heart Disease, and Parkinson’s Disease using machine learning.  
Built with Streamlit, scikit-learn, MLflow, and Docker.

---

🚀 Features

- Predicts Diabetes, Heart Disease, and Parkinson’s Disease from user input.
- Interactive web UI built with Streamlit.
- ML pipelines for training, evaluation, and automated reporting.
- Experiment tracking and artifact logging with MLflow.
- Dockerized for easy deployment.
- Contact form with SMTP email notifications.

---

## 📁 Project Structure

```
.
├── datasets/                # CSV files for each disease
├── saved models/            # Trained model files (.sav)
├── pipeline_diabetes.py     # Diabetes ML pipeline
├── pipeline_heart.py        # Heart Disease ML pipeline
├── pipeline_parkinsons.py   # Parkinson's ML pipeline
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker setup
├── mdp.py                   # Streamlit web app
├── pipeline.yaml            # (Optional) Pipeline config
├── mlruns/                  # MLflow experiment tracking
└── README.md
```

---

## ⚙️ Setup

1. Clone the repository
    ```bash
    git clone https://github.com/DHANYASHREE-MV/MultipleDiseasePrediction.git
    cd MultipleDiseasePrediction
    ```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Run ML pipelines
    ```bash
    python pipeline_diabetes.py
    python pipeline_heart.py
    python pipeline_parkinsons.py
    ```

4. Start MLflow UI
    ```bash
    mlflow ui
    ```
    Visit [http://localhost:5000](http://localhost:5000) to view experiments and artifacts.

5. Run the Streamlit app
    ```bash
    streamlit run mdp.py
    ```
    or (if `streamlit` command not found):
    ```bash
    python -m streamlit run mdp.py
    ```

6. Run with Docker
    ```bash
    docker build -t disease-prediction-app .
    docker run -p 8501:8501 disease-prediction-app
    ```

---

📝 Usage

- Use the Streamlit app to make predictions.
- Use the ML pipeline scripts to retrain models and log results.
- View detailed reports and confusion matrices in the MLflow UI (Artifacts section).
- Use the contact form to send feedback or queries (sent via SMTP email).

---

📊 MLflow Artifacts

- **classification_report.txt**: Detailed classification metrics.
- **confusion_matrix.png**: Visual confusion matrix for each model.

---

🔒 Privacy Policy

- **Data Usage:**  
  This application processes user input data solely for the purpose of disease prediction. No personal or sensitive information is stored, shared, or used for any purpose other than generating predictions.
- **Data Storage:**  
  Uploaded or entered data is not retained on the server or shared with third parties.
- **Contact Form:**  
  If you use the contact form, your message is sent via email using SMTP. Your email address and message are used only to respond to your inquiry and are not shared with third parties.
- **User Responsibility:**  
  Users should avoid entering personally identifiable information (PII) into the application.

---

📬 Contact

For questions, feedback, or support, please contact:

- **Email:** [your-email@example.com]
- **GitHub Issues:** [GitHub Issues Page](https://github.com/DHANYASHREE-MV/MultipleDiseasePrediction/issues)

---

📄 Terms of Service

- **No Medical Advice:**  
  This tool is for educational and informational purposes only and does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.
- **No Warranty:**  
  The application is provided "as is" without warranty of any kind. The authors are not responsible for any decisions made based on the predictions.
- **User Agreement:**  
  By using this application, you agree to use it responsibly and acknowledge the limitations of machine learning predictions in healthcare.
- **Contact Form Consent:**  
  By using the contact form, you consent to your message being sent via email to the project maintainer for support or feedback purposes.

---

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

📄 License

This project is licensed under the MIT License.

---

**Developed by Dhanyashree M V**
