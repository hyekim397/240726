import steamlit as st
st.title('나의 첫 웹 서비스 만들기!')
name = st.text_input('이름을 입력해주세요 : ', '홍길동')
menu = st.selctbox('좋아하는 음식을 선택해주세요: ', ['마라탕', '화덕피자', '황금올리브치킨', '샐러드 파스타'])
if st.button('인사말 생성') :
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 저도 좋아요!!')
