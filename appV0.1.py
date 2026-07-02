import streamlit as st

st.title("🏥 Health Monitor")
st.write("Calculate your BMI and analyse your Blood Pressure.")

Report = st.selectbox("Enter what report you want",["BP","BMI"])

# ================= BMI =================

if Report == "BMI":
    st.header("BMI Calculator")

    def BMI_function():
        #Take input from the user

        Weight = st.number_input("Enter your weight in kgs", min_value=1.0)
        Height = st.number_input("Enter your height in m",min_value=0.5)
        Gender = st.selectbox("Select your gender",["Male","Female"])


        #defining a function to calculate the BMI
        
        
        if st.button("**Calculate BMI**"):

            def BMI_calculate(Height,Weight):
                return round((Weight)/(Height**2),2)

            BMI = BMI_calculate(Height,Weight)
            st.success(f"Your BMI is {BMI}")

        #Suggest weight category according to the BMI

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
                
            Category = category(BMI)
            st.info(Category)
                
            #Suggest healthy weight

            def healthy_weight(Gender):
                if Gender == "Male":
                    return 50 + 2.3*((Height*39.3701)-60)
                else:
                    return 45.5 + 2.3*((Height*39.3701)-60)
                
            HW =  round(healthy_weight(Gender),2)
            st.info(f"Your healthy weight is {HW} Kgs")

            #Suggest Weight to reduce or gain


            if Weight > HW:
                st.warning(f"You need to cut {round (Weight - HW,2)} kgs")
            elif Weight == HW:
                st.warning(f"No bulking or cutting needed")
            else:
                st.warning(f"You need to add {round (HW - Weight ,2)} kgs")

    BMI_function()

# ================= BP =================

else:

    st.header("Blood Pressure Calculator")
    


    def BP_function():

            #Take input from the user

            Systolic = st.number_input("Enter Systolic BP", min_value=50, max_value=250)
            Diastolic = st.number_input("Enter Diastolic BP", min_value=30, max_value=180)
            if st.button("**Analye BP**"):

                #Defining a function for MAP

                def Mean_Arterial_Pressure(Systolic,Diastolic):
                    return (Systolic+2*(Diastolic))/3
                
                M = Mean_Arterial_Pressure(Systolic,Diastolic)
                st.success(f"Your Mean Arterial Pressure is {round(M,2)} mmHg")

                #Also showing the pulse pressure(PP)
                st.success(f"Your Pulse pressure is {Systolic-Diastolic} mmHg")

                #Define BP category

                def BP_category(Systolic,Diastolic):
                      if Systolic >= 180 or Diastolic >= 120:
                        st.error("🚨 Hypertensive Crisis")
                        st.info("""
                            **Emergency:**
                            - Rest for 5 minutes and recheck your BP.
                            - If BP remains **≥180 and/or ≥120 mmHg**, seek immediate medical care.
                            - If you have chest pain, shortness of breath, severe headache,
                            confusion, weakness, or vision changes, call emergency services immediately.
                                    """)

                      elif Systolic >= 140 or Diastolic >= 90:
                        st.error("🔴 Hypertension Stage 2")
                        st.info("""
                            **Suggestions:**
                            - See a healthcare provider promptly.
                            - Lifestyle changes are essential.
                            - Take BP medication as prescribed.
                            - Monitor BP frequently.
                            - Follow your treatment plan.
                                    """)

                      elif Systolic >= 130 or Diastolic >= 80:
                        st.warning("🟠 Hypertension Stage 1")
                        st.info("""
                            **Suggestions:**
                            - Continue healthy lifestyle changes.
                            - Consult a healthcare provider.
                            - Take medication if prescribed.
                            - Monitor BP regularly.
                            - Reduce salt intake.
                            - Exercise regularly.
                                    """)

                      elif (120 <= Systolic <= 129) and Diastolic < 80:
                        st.warning("🟡 Elevated Blood Pressure")
                        st.info("""
                            **Suggestions:**
                            - Reduce sodium intake.
                            - Eat more fruits and vegetables.
                            - Exercise regularly.
                            - Maintain a healthy weight.
                            - Limit alcohol.
                            - Manage stress.
                            - Monitor BP regularly.
                                    """)

                      else:
                        st.success("🟢 Normal Blood Pressure")
                        st.info("""
                            **Maintain a healthy lifestyle:**
                            - Exercise regularly.
                            - Eat a balanced diet.
                            - Limit salt intake.
                            - Avoid smoking.
                            - Maintain a healthy weight.
                            - Check your blood pressure at least once a year.
                                    """)

                
                BP_category(Systolic,Diastolic)
                st.caption(
                            "⚠️ This tool is for educational purposes only and is not a substitute "
                            "for professional medical advice, diagnosis, or treatment. "
                            "Consult a healthcare provider for persistent high blood pressure or concerning symptoms."
                            )


    BP_function()
        




