import streamlit as st
import pandas as pd

from database import (
    create_table,
    add_patient,
    get_patients
)

from validator import (
    validate_email,
    validate_dob,
    validate_numeric
)

from ai_helper import generate_health_remark


st.set_page_config(
    page_title="AI Health Prediction System",
    page_icon="🏥",
    layout="wide"
)


create_table()


st.markdown(
    """
    <style>

    .main {
        background:#f6f8fc;
    }

    .metric-card {
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    }

    .big-font {
        font-size:30px;
        font-weight:bold;
        color:#1f77b4;
    }

    .small-font {
        color:gray;
    }

    </style>
    """,
    unsafe_allow_html=True
)


with st.sidebar:

    st.title("🏥 AI Health")

    st.success("System Online")

    st.divider()

    st.write("### Features")

    st.write("✔ AI Prediction")
    st.write("✔ Patient Database")
    st.write("✔ SQLite Storage")
    st.write("✔ CSV Export")

    st.divider()

    st.caption(
        "Built using Streamlit + AI"
    )


st.title(
    "🏥 AI Health Prediction Dashboard"
)

st.write(
    "Predict patient health status using AI and store records securely."
)


patients = get_patients()

total_patients = len(patients)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="metric-card">

        <div class="big-font">
        {total_patients}
        </div>

        <div class="small-font">
        Total Patients
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="metric-card">

        <div class="big-font">
        🤖
        </div>

        <div class="small-font">
        AI Enabled
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="metric-card">

        <div class="big-font">
        SQLite
        </div>

        <div class="small-font">
        Database
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


st.subheader(
    "🩺 Patient Details"
)


with st.form("patient_form"):

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Patient Name"
        )

        dob = st.date_input(
            "Date of Birth"
        )

        email = st.text_input(
            "Email"
        )

    with col2:

        glucose = st.text_input(
            "Glucose (mg/dL)"
        )

        haemoglobin = st.text_input(
            "Haemoglobin (g/dL)"
        )

        cholesterol = st.text_input(
            "Cholesterol (mg/dL)"
        )

    submit = st.form_submit_button(
        "🚀 Predict & Save"
    )


if submit:

    if name.strip() == "":

        st.error(
            "Patient name is required."
        )

    elif not validate_email(email):

        st.error(
            "Invalid email address."
        )

    elif not validate_dob(str(dob)):

        st.error(
            "Invalid DOB."
        )

    elif not validate_numeric(glucose):

        st.error(
            "Glucose must be numeric."
        )

    elif not validate_numeric(haemoglobin):

        st.error(
            "Haemoglobin must be numeric."
        )

    elif not validate_numeric(cholesterol):

        st.error(
            "Cholesterol must be numeric."
        )

    else:

        with st.spinner(
            "Generating AI prediction..."
        ):

            remark = generate_health_remark(
                glucose,
                haemoglobin,
                cholesterol
            )

        add_patient(
            name,
            str(dob),
            email,
            float(glucose),
            float(haemoglobin),
            float(cholesterol),
            remark
        )

        st.success(
            "Patient saved successfully!"
        )

        st.info(
            remark
        )

        st.rerun()


st.divider()


st.subheader(
    "📋 Patient Records"
)


patients = get_patients()


if patients:

    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "AI Remark"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(
        index=False
    ).encode(
        "utf-8"
    )

    st.download_button(
        label="⬇ Download Records",
        data=csv,
        file_name="patients.csv",
        mime="text/csv"
    )


else:

    st.info(
        "No patient records available."
    )


st.divider()


st.caption(
    "© 2026 AI Health Prediction System"
)
