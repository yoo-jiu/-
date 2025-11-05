import streamlit as st
st.title('나의 첫 웹 사이트 만들기!')
a=st.text_input('안녕,니 이름이 뭐야?')
b=st.selectbox('좋아하는 음악 있어?',['K-pop','J-pop','rock','발라드'])
if st.button('인사말 생성'):
  st.info(a+' 그게 니 이름이구나! 만나서 반가워!')
  st.warning(b+'를 좋아하는구나! 나도 그거 좋아해!')
  st.error('반가워! 앞으로 잘부탁해!')
  st.cookies()
