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
        ("Pregnancies (No. of times pregnant)", "preg"),
        ("Glucose Level (80–130 mg/dL)", "glucose"),
        ("Blood Pressure (Normal <130/80)", "bp"),
        ("Skin Thickness (10–30 mm)", "skin"),
    ]

    right = [
        ("Insulin Level (10–25 µU/mL)", "insulin"),
        ("BMI (18.5–24.9 kg/m²)", "bmi"),
        ("Diabetes Pedigree Function (0.1–2.5)", "dpf"),
        ("Age (Years)", "age"),
    ]

    Pregnancies, Glucose, BP, Skin, Insulin, BMI, DPF, Age = two_columns(left, right)

    if st.button("Predict Diabetes"):
        result = models['diabetes'].predict([[Pregnancies, Glucose, BP, Skin, Insulin, BMI, DPF, Age]])
        st.success("Diabetic" if result[0] == 1 else "Not Diabetic")

# ================= Heart =================
elif selected == "❤️ Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    left = [
        ("Age (Years)", "h_age"),
        ("Sex (1 = Male, 0 = Female)", "h_sex"),
        ("Chest Pain Type (0–3)", "cp"),
        ("Resting BP (Ideal <120/80)", "trestbps"),
        ("Cholesterol (Total <200 mg/dL)", "chol"),
        ("Fasting Blood Sugar (>120 = 1)", "fbs"),
        ("Thal (0=Normal,1=Fixed,2=Reversible)", "thal")
    ]

    right = [
        ("Rest ECG (0–2)", "restecg"),
        ("Max Heart Rate (90–190 BPM)", "thalach"),
        ("Exercise Angina (1=Yes,0=No)", "exang"),
        ("Oldpeak (0–2 mm)", "oldpeak"),
        ("Slope (0–2)", "slope"),
        ("Major Vessels (0–3)", "ca"),
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Heart Disease"):
        result = models['heart'].predict([inputs])
        st.success("Heart Disease Detected" if result[0] == 1 else "No Heart Disease")

# ================= Parkinsons =================
elif selected == "🟪 Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction")

    left = [
        ("Fo (85–165 Hz)", "fo"),
        ("Fhi (165–350 Hz)", "fhi"),
        ("Flo (60–165 Hz)", "flo"),
        ("Jitter % (0.2–3.5%)", "jitterp"),
        ("Jitter Abs (0.01–0.1)", "jittera"),
        ("RAP (0.5–2.5%)", "rap"),
        ("PPQ (0.5–2.5%)", "ppq"),
        ("DDP (0.6–7.5%)", "ddp"),
        ("Shimmer (1–7%)", "shim"),
        ("Shimmer dB (0.1–1.5)", "shimdb"),
        ("APQ3 (0.5–5%)", "apq3")
    ]

    right = [
        ("APQ5 (1–6%)", "apq5"),
        ("APQ (1.5–7%)", "apq"),
        ("DDA (1–9%)", "dda"),
        ("NHR (0.11–0.35)", "nhr"),
        ("HNR (10–25 dB)", "hnr"),
        ("RPDE (0.3–0.6)", "rpde"),
        ("DFA (0.5–1.0)", "dfa"),
        ("Spread1 (0.8–1.7)", "s1"),
        ("Spread2 (0–4)", "s2"),
        ("D2 (Dopamine Receptor)", "d2"),
        ("PPE (0.1–0.3)", "ppe")
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Parkinson's"):
        result = models['parkinsons'].predict([inputs])
        st.success("Parkinson's Detected" if result[0] == 1 else "No Parkinson's")

# ================= Lung Cancer =================
elif selected == "🟩 Lung Cancer Prediction":
    st.title("Lung Cancer Prediction")

    left = [
        ("Gender (1=Male,0=Female)", "g"),
        ("Age (Years)", "la"),
        ("Smoking (1=Yes,0=No)", "sm"),
        ("Yellow Fingers (1=Yes,0=No)", "yf"),
        ("Anxiety (1=Yes,0=No)", "an"),
        ("Peer Pressure (1=Yes,0=No)", "pp"),
        ("Chronic Disease (1=Yes,0=No)", "cd"),
        ("Fatigue (1=Yes,0=No)", "ft"),
    ]

    right = [
        ("Allergy (1=Yes,0=No)", "al"),
        ("Wheezing (1=Yes,0=No)", "wh"),
        ("Alcohol (1=Yes,0=No)", "alc"),
        ("Coughing (1=Yes,0=No)", "cg"),
        ("Shortness of Breath (1=Yes,0=No)", "sb"),
        ("Swallowing Difficulty (1=Yes,0=No)", "sd"),
        ("Chest Pain (1=Yes,0=No)", "cp2"),
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Lung Cancer"):
        result = models['lung'].predict([inputs])
        st.success("Lung Cancer Detected" if result[0] == 1 else "No Lung Cancer")

# ================= Thyroid =================
elif selected == "🟨 Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid Prediction")

    left = [
        ("Age (Years)", "t_age"),
        ("Sex (1=Male,0=Female)", "t_sex"),
        ("On Thyroxine (1=Yes,0=No)", "thy"),
    ]

    right = [
        ("TSH (0.4–4.0 mIU/L)", "tsh"),
        ("T3 (80–200 ng/dL)", "t3"),
        ("T4 (5–12 µg/dL)", "t4"),
    ]

    inputs = two_columns(left, right)

    if st.button("Predict Thyroid"):
        result = models['thyroid'].predict([inputs])
        st.success("Hypo-Thyroid Detected" if result[0] == 1 else "No Hypo-Thyroid")
