import streamlit as st
st.title('나의 첫 웹 사이트 만들기!')
a=st.text_input('안녕,니 이름이 뭐야?')
st.selectbox('좋아하는 음악 있어?',['K-pop','J-pop','rock','발라드'])
if st.button('인사말 생성'):
  st.write(a+' 그게 니 이름이구나! 만나서 반가워!')
