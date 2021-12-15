from re import S
import streamlit as st
import pickle
import sklearn
model = pickle.load(open('RF_price_predicting_model.pkl','rb'))

def main():
    string = "Car Price Predictior"
    st.set_page_config(page_title = string, page_icon= "🚗")
    st.title("Car Price Predictor 🚗")
    st.markdown("#### Are you planning to sell your car!! \n #### Here is Your Car Predictor App")
    # To add Image
    st.image("https://media.istockphoto.com/photos/illustration-of-generic-compact-car-perspective-view-picture-id1148853697",
    width=500)

    years = st.number_input("In which year Car was Purchased?",1990,2021,step=1,key='year')
    Year_old = 2021-years
    
    Present_price = st.number_input("What is the current Ex-Showroom Price of the car",0.00,50.00,step=0.5,key='present_year')

    Driven = st.number_input("How much the car is driven ('In KM')",0.00,500000.00,step=5000.00,key='driven')

    Owner = st.radio("The number of Owner car had previously?",(0,1,2,3),key='owner')

    Fuel_type = st.selectbox('What is the fuel type of the car?',( 'Petrol', 'Diesel', 'CNG'),key='fuel')
    if (Fuel_type =='Petrol'):
        Fuel_type_Petrol=1
        Fuel_type_Diesel = 0
    elif(Fuel_type=='Diesel'):
        Fuel_type_Petrol = 0
        Fuel_type_Diesel = 1
    else:
        Fuel_type_Petrol=0
        Fuel_type_Diesel=0

    seller_type_individual = st.selectbox("What is the Ownership Type?",('Individual','Dealership'),key='manual')
    if (seller_type_individual=='Individual'):
        seller_type_individual=1
    else:
        seller_type_individual=0

    Transmmision_Manual = st.selectbox("WHat is the Transmission Type?",('Manual','Automatic'),key='transmission_manual')
    if(Transmmision_Manual=='Manual'):
        Transmmision_Manual=1
    else:
        Transmmision_Manual=0

    if st.button("Estimate Price",key='predict'):
        try:
            prediction = model.predict([[Present_price, Driven, Owner, Year_old, Fuel_type_Diesel, Fuel_type_Petrol,seller_type_individual, Transmmision_Manual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will not be able to sell this car!!")
            else:
                st.success("You can sell the car for {} lakhs".format(output))
        except:
            st.warning("Opps Something went Wrong \n Try again")

if __name__ == '__main__':
    main()
    