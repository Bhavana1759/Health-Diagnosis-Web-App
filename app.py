import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image + dark overlay
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.55);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

better_visibility = """
<style>
/* Lighten overlay for better contrast */
[data-testid="stAppViewContainer"]::before {
    background-color: rgba(0, 0, 0, 0.4);
}

/* Headings / titles */
h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: #ffffff;
    font-size: 1.3rem;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.7);
    font-weight: 700;
}

/* Dropdown labels */
.stSelectbox label {
    color: black !important;
    font-size: 1.1rem;
    font-weight: 600;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
}

/* st.write text */
.stMarkdown, p, div {
    color: #ffffff !important;
    font-size: 1.05rem;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
}

/* Input labels */
.stTextInput label, .stNumberInput label {
    color: #ffffff !important;
    font-size: 1.1rem;
    font-weight: 600;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
}

/* Input fields */
.stTextInput input, .stNumberInput input {
    background-color: rgba(255,255,255,0.9);
    color: #000;
    border-radius: 6px;
    border: 1px solid #ccc;
}
</style>
"""
st.markdown(better_visibility, unsafe_allow_html=True)

# 🔽 FIX: Make selectbox options BLACK
selectbox_fix = """
<style>
/* Selected value inside selectbox */
.stSelectbox div[data-baseweb="select"] > div {
    color: black !important;
    background-color: white !important;
}

/* Dropdown options text */
div[data-baseweb="popover"] span {
    color: black !important;
}

/* Dropdown background */
div[data-baseweb="popover"] {
    background-color: white !important;
}
</style>
"""
st.markdown(selectbox_fix, unsafe_allow_html=True)


# Load the saved models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    [
        "🟦 Diabetes Prediction",
        "❤️ Heart Disease Prediction",
        "🟪 Parkinsons Prediction",
        "🟩 Lung Cancer Prediction",
        "🟨 Hypo-Thyroid Prediction"
    ]
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# ----------------- Diabetes Prediction Page -----------------
if selected == '🟦 Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level(Ranges from 80-130 mg/dL)', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value(Normal-Less than 130/80)(Prehypertension (At Risk)-130-139)(Hypertension (High BP, Requires Treatment)-140/90)(Severe Hypertension (Emergency Level)-180/120)', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value(10mm-30mm)', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level(Normal to High (>10-25 µU/mL))', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value(Ranges from 18.5 – 24.9 kg/m²)', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value(Ranges from 0.1 to 2.5)', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic.Please regulate his/her Sugar intake and Check for Insulin Levels on Timely Basis' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# ----------------- Heart Disease Prediction Page -----------------
if selected == '❤️ Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure(Ideal->below 120/80 mmHg)(Hypertension (140/90 or higher) needs medical attention)', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl(Total Cholesterol->Below 200)(LDL (Bad Cholesterol)-100 - 160)(HDL (Good Cholesterol-40 - 60))', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved(Ranges from 90 to 190 BPM)', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise(Ranges from 0mm to 2mm)', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease . treatment-> Coronary Artery Bypass Surgery (CABG),Heart Transplant, Control Blood Sugar, Blood Pressure & Cholesterol,Stress Management, Regular Exercise & Healthy Diet' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)

# ----------------- Parkinson's Prediction Page -----------------
if selected == "🟪 Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP:Fo(Hz)(Average vocal fundamental frequency)(Ranges from 85Hz to 165hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)(Maximum vocal fundamental frequency)(Ranges from 165Hz to 350Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)( Minimum vocal fundamental frequency)(Ranges from 60Hz to 165Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('(MDVP:Jitter(%)(Measures of variation in fundamental frequency)(Ranges from 0.2% to 3.5%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)(absolute value of the variation in fundamental frequency (pitch) of the voice)(Ranges from 0.01Hz to 0.1Hz)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP(Relative and Absolute Perturbation)(Ranges from 0.5% to 2.5%)', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ(Percent of Period Perturbation)(Ranges from 0.5% to 2.5%)', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP(Jitter: Difference of Differences)(Ranges from 0.6% to 7.5%)', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer(Measures of variation in amplitude)(Ranges from 1% to 7%)', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)(Measures of variation in decibals)(Ranges from 0.1dB to 1.5dB) ', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3(three-point Amplitude Perturbation Quotient)(Ranges from 0.5% to 5%)', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5(five-point Amplitude Perturbation Quotient)(Ranges from 1% to 6%)', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ(Amplitude Perturbation Quotient)(Ranges from 1.5% to 7%)', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA(Difference of Differences of Amplitude)(Ranges from 1% to 9%))', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR((Noise-to-Harmonics Ratio)(Ranges from 0.11 to 0.35))', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR(Harmonics-to-Noise Ratio)(Ranges from 10 to 25 db)', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE(Recurrence Period Density Entropy)(ranges from 0.3 to 0.6)', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA(Detrended Fluctuation Analysis)(Ranges from 0.5 to 1.0)', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1(Ranges from 0.8 to 1.7)', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2(Ranges from 0 to 4)', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2(Dopamine Receptor)', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE (Pitch Period Entropy)(Ranges from 0.1 to 0.3 )', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease. Treatment -> Medications are Dopamine Promoter,Antidepressant,Anti-Tremor and Physical Exercise" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# ----------------- Lung Cancer Prediction Page -----------------
if selected == "🟩 Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")

    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing(a high-pitched whistling sound made while breathing) (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease. Treatment->Surgery,Chemotherapy,Immunotherapy,Radiation and Targeted drugs." if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)

# ----------------- Hypo-Thyroid Prediction Page -----------------
# ----------------- Hypo-Thyroid Prediction Page -----------------
if selected == "🟨 Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    st.write("Enter the following details to predict hypo-thyroid disease:")

    age = display_input('Age', 'Enter age of the person', 'thy_age', 'number')
    sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'thy_sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Is the person on thyroxine?', 'on_thyroxine', 'number')
    tsh = display_input('TSH Level (Normal: 0.4 – 4.0 mIU/L)', 'Enter TSH value', 'tsh', 'number')
    t3 = display_input('T3 Level (Normal: 80 – 200 ng/dL)', 'Enter T3 value', 't3', 'number')
    t4 = display_input('T4 Level (Normal: 5 – 12 µg/dL)', 'Enter T4 value', 't4', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3, t4]])
        thyroid_diagnosis = (
            "The person has Hypo-Thyroid disease. Treatment → Thyroxine hormone therapy, regular monitoring."
            if thyroid_prediction[0] == 1
            else "The person does not have Hypo-Thyroid disease"
        )
        st.success(thyroid_diagnosis)
