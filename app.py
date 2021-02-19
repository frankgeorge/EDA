import streamlit as st
import pandas as pd 

#st.title('My first ')

def table():
    df= load_data(r'C:\Users\frank\Desktop\project\EDA\ecommerce.csv')
    tableshow=st.dataframe(df.head(100))
    return tableshow

def load_data(data):
    df=pd.read_csv(r'C:\Users\frank\Desktop\project\EDA\ecommerce.csv')
    return df

def main():
    st.title("Flipkart crawler data EDA")

    menu = ["EDA", "About"]
    choice = st.sidebar.selectbox("Menu",menu)

    df= load_data(r'C:\Users\frank\Desktop\project\EDA\ecommerce.csv')
    
    if choice =="EDA":
        #st.subheader("EDA")
        #st.dataframe(df.head(100))
        
        #st.dataframe((df['product_name'].unique())
        if st.button("Show df"):
            st.dataframe(df)
            #st.text("Showing the widget") 

        
        
        #st.button("number of unique products in df")
        #st.button("number of brands in df")
        #st.button("number of categories in df")
                

        status = st.radio('Select your question: ', 
                  ('number of unique products in df', 'number of brands in df'))
            
        if (status == 'number of unique products in df'): 
            st.success("Success") 
        elif (status == 'number of brands in df'):
            st.warning("Success") 

         
         #   st.text("number of unique products in df {}.".format(bmi)) 


    else:
        st.subheader("About")
        st.text("lalala")



if __name__=='__main__':
    main()