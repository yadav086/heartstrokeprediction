import streamlit as st
import joblib

model_lr = joblib.load('stroke_lr.pkl')
model_dc = joblib.load('stroke_dc.pkl')
model_ct = joblib.load('stroke_ct.pkl')
model_ada= joblib.load('stroke_ada.pkl')
model_kn = joblib.load('stroke_kn.pkl')
model_sv = joblib.load('stroke_svm.pkl')
model_lt = joblib.load('stroke_lt.pkl')

st.title('Welcome to stroke predication Page!')
activities=['Decison Tree','Ada boost','Cat boost','Light gbm','Logistic regression','Knearest','Support vector machine']
option=st.sidebar.selectbox('Select the model for prediction',activities)

gender =st.selectbox('Select the gender',('Male','Female'))

if gender =='Male':
	gender=0
else:
	gender=1
ever_married = st.selectbox('Are you married',('Yes','No'))
if ever_married == 'Yes':
	ever_married=0
else:
	ever_married=1

work_type = st.radio('select the work type',('Private','Self-employed','Govt job','children','Never worked'))
if work_type=='Never worked':
	work_type=0
elif work_type=='children':
	work_type=1
elif work_type=='Self-employed':
	work_type=2
elif work_type=='Private':
	work_type=3
else:
	work_type=4

Residence_type=st.selectbox('where do you live',('Urban','Rural'))

if	Residence_type=='Urban':
	Residence_type=0
else:
	Residence_type=1

smoking_status = st.radio("How frequent you smoke ?",('FormerlySmoked','NeverSmoked','Smokes','Unknown'))

if smoking_status == 'Unknown':
	smoking_status=0
elif smoking_status == 'NeverSmoked':
	smoking_status=1
elif smoking_status == 'FormerlySmoked':
	smoking_status=2
else:	
	smoking_status=3

age = st.slider('Enter your age',0,100)

hypertension=st.radio('Do you hacv hypertension?',('Yes','No'))
if hypertension== 'Yes':
	hypertension=0
else:
	hypertension=1

heart_disease =st.radio('Do you have Heart Disease?',('Yes','No'))
if heart_disease== 'Yes':
	heart_disease=0
else:
	heart_disease=1

avg_glucose_level =st.slider('Enter your Average Glucose Level',0,100)

bmi =st.slider('Enter the bmi',0,500)

inputs =[[gender,ever_married,work_type,Residence_type,smoking_status,age,hypertension,heart_disease,avg_glucose_level,bmi]]

if option== 'Logistic regression':
	model_lr.predict(inputs)
elif option== 'Ada boost':
	model_ada.predict(inputs)
elif option== 'Light gbm':
	model_lt.predict(inputs)
elif option== 'Decison Tree':
	model_dc.predict(inputs)
elif option== 'Knearest':
	model_kn.predict(inputs)
elif option== 'Cat boost':
	model_ct.predict(inputs)			
else:
	model_sv.predict(inputs)

if st.button('Predict'):
	if model_lr.predict(inputs)[0]==0 or model_ada.predict(inputs)[0]==0 or model_lt.predict(inputs)[0]==0 or model_dc.predict(inputs)[0]==0 or model_kn.predict(inputs)[0]==0 or model_ct.predict(inputs)[0]==0 or model_sv.predict(inputs)[0]==0:
		st.success('There is possibility that you may get stroke .Kindly visit nearest hospital for checkup')
	else:
		st.success('Your health is fit and fine')


