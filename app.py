import streamlit as st
import pickle
# import 
model= pickle.load(open("spam.pkl",'rb'))
cv=pickle.load(open("vectorizer.pkl",'rb'))
st.title("Spam check")
# st.write("THis is ml")
user_input=st.text_area("mail desctiption",height=150,placeholder="Enter mail description")
if st.button("classify"):
    
    if user_input:
        data= [user_input]
        vect= cv.transform(data).toarray()
        pred= model.predict(vect)
        if pred[0]==0:
            # st.write("not spam")
            st.success("This mail is not spam")
        else:

            # st.write("spam")
            st.error("this is spam email")
    else:
        print("try agin")
    