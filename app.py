import streamlit as st

st.title("🏋️ BMI Calculator")
st.write("Calculate your BMI and healthy weight.")

#Functions

def BMI_calculate(Height,Weight):
    return round((Weight)/(Height**2),2)

def category(BMI):
    if BMI<18.5:
        return "You are Underweight"
    elif BMI>=18.5 and BMI<=24.9:
        return "You have a Normal weight"
    elif BMI>25.0 and BMI<=29.9:
        return "You are Over weight"
    elif BMI>30.0 and BMI<=34.9:
        return "You have Obseity Class I"
    elif BMI>35.0 and BMI<=39.9:
        return "You have Obseity Class II"
    else:
        return "You have Obesity Class III"
    
def healthy_weight(Gender):
    if Gender == "Male":
        return 50 + 2.3*((Height*39.3701)-60)
    else:
        return 45.5 + 2.3*((Height*39.3701)-60)
    
# -------------------------
# User Inputs
# -------------------------

Weight = st.number_input("Enter your weight in kgs", min_value=1.0)
Height = st.number_input("Enter your height in m",min_value=0.5)
Gender = st.selectbox("Select your gender",["Male","Female"])

# -------------------------
# Button
# -------------------------

if st.button("Calculate BMI"):

    BMI = BMI_calculate(Height,Weight)
    st.subheader(f"Your BMI is **{BMI}**")

    Category = category(BMI)
    st.info(Category)

    HW =  round(healthy_weight(Gender),2)
    st.info(f"Your healthy weight is **{HW}** Kgs")

    
    if Weight > HW:
        st.warning(f"You need to cut {round (Weight - HW,2)} kgs")
    elif Weight == HW:
        st.success(f"No bulking or cutting needed")
    else:
        st.warning(f"You need to add {round (HW - Weight ,2)} kgs")


