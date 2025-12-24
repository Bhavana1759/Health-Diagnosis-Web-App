import streamlit as st
import pickle

# ---------------- Page Config ----------------
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="wide")

# ---------------- Hide Streamlit UI ----------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- Background Image ----------------
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.45);
}}
h1,h2,h3,p,label {{
    color: white !important;
}}
.stNumberInput input {{
    background: white;
    color: black;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- Helper Functions ----------------
def display_input(label, key):
    return st.number_input(label, key=key, step=1)

def two_columns(left, right):
    col1, col2 = st.columns(2)
    values = []
    with col1:
        for label, key in left:
            values.append(display_input(label, key))
    with col2:
        for label, key in right:
            values.append(display_input(label, key))
    return values

# ---------------- Load Models ----------------
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# ---------------- Disease Selection ----------------
selected = st.selectbox("Select Disease", [
    "🟦 Diabetes Prediction",
    "❤️ Heart Disease Prediction",
    "🟪 Parkinsons Prediction",
    "🟩 Lung Cancer Prediction",
    "🟨 Hypo-Thyroid Prediction"
])

# ================= Diabetes =================
if selected == "🟦 Diabetes Prediction":
    st.title("Diabetes Prediction")

    left = [
        ("Pregnancies", "preg"),
        ("Glucose Level", "glucose"),
        ("Blood Pressure", "bp"),
        ("Skin Thickness", "skin"),
    ]

    right = [
        ("Insulin Level", "insulin"),
        ("BMI", "bmi"),
        ("Diabetes Pedigree Function", "dpf"),
        ("Age", "age"),
    ]

    Pregnancies, Glucose, BP, Skin, Insulin, BMI, DPF, Age = two_columns(left, right)

    if st.button("Predict Diabetes"):
        result = models['diabetes'].predict([[Pregnancies, Glucose, BP, Skin, Insulin, BMI, DPF, Age]])
        st.success("Diabetic" if result[0] == 1 else "Not Diabetic")

# ================= Heart =================
elif selected == "❤️ Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    left = [
        ("Age", "h_age"),
        ("Sex (1=Male,0=Female)", "h_sex"),
        ("Chest Pain Type", "cp"),
        ("Resting BP", "trestbps"),
        ("Cholesterol", "chol"),
        ("Fasting Blood Sugar", "fbs"),
         ("Thal", "thal")
    ]

    right = [
        ("Rest ECG", "restecg"),
        ("Max Heart Rate", "thalach"),
        ("Exercise Angina", "exang"),
        ("Oldpeak", "oldpeak"),
        ("Slope", "slope"),
        ("Major Vessels", "ca"),
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Heart Disease"):
        result = models['heart'].predict([inputs])
        st.success("Heart Disease Detected" if result[0] == 1 else "No Heart Disease")

# ================= Parkinsons =================
elif selected == "🟪 Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction")

    left = [
        ("Fo", "fo"), ("Fhi", "fhi"), ("Flo", "flo"),
        ("Jitter %", "jitterp"), ("Jitter Abs", "jittera"),
        ("RAP", "rap"), ("PPQ", "ppq"),
        ("DDP", "ddp"), ("Shimmer", "shim"),
        ("Shimmer dB", "shimdb"), ("APQ3", "apq3")
    ]

    right = [
        ("APQ5", "apq5"), ("APQ", "apq"),
        ("DDA", "dda"), ("NHR", "nhr"),
        ("HNR", "hnr"), ("RPDE", "rpde"),
        ("DFA", "dfa"), ("Spread1", "s1"),
        ("Spread2", "s2"), ("D2", "d2"),
        ("PPE", "ppe")
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Parkinson's"):
        result = models['parkinsons'].predict([inputs])
        st.success("Parkinson's Detected" if result[0] == 1 else "No Parkinson's")

# ================= Lung Cancer =================
elif selected == "🟩 Lung Cancer Prediction":
    st.title("Lung Cancer Prediction")

    left = [
        ("Gender", "g"), ("Age", "la"),
        ("Smoking", "sm"), ("Yellow Fingers", "yf"),
        ("Anxiety", "an"), ("Peer Pressure", "pp"),
        ("Chronic Disease", "cd"),
        ("Fatigue", "ft"),
    ]

    right = [
        ("Allergy", "al"), ("Wheezing", "wh"),
        ("Alcohol", "alc"), ("Coughing", "cg"),
        ("Shortness of Breath", "sb"),
        ("Swallowing Difficulty", "sd"),
        ("Chest Pain", "cp2"),
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Lung Cancer"):
        result = models['lung'].predict([inputs])
        st.success("Lung Cancer Detected" if result[0] == 1 else "No Lung Cancer")

# ================= Thyroid =================
elif selected == "🟨 Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid Prediction")

    left = [
        ("Age", "t_age"),
        ("Sex", "t_sex"),
        ("On Thyroxine", "thy"),
    ]

    right = [
        ("TSH", "tsh"),
        ("T3", "t3"),
        ("T4", "t4"),
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Thyroid"):
        result = models['thyroid'].predict([inputs])
        st.success("Hypo-Thyroid Detected" if result[0] == 1 else "No Hypo-Thyroid")

