import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav','rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input tahun mobil')
mileage = st.number_input('Input Km mobil')
tax = st.number_input('Input pajak mobil')
mpg = st.number_input('Input konsumsi bbm')
engineSize = st.number_input('Input ukuran mesin')

predict = ''

if st.button('Estimasi harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )

    st.wtrite('Estimasi harga dalam EUR : ', predict)
    st.write('Estimasi harga dalam IDR : ', predict*20.188,37)