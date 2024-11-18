
#설치 명령어
#pip install streamlit

#실행 명령어
#streamlit run 파일이름

#스트림 릿 라이브러리
import streamlit as st
import pandas as pd

#타이틀과 헤더
# st.title("이것은 스트림릿 헤더입니다.")
# st.header("이것은 스트림릿 헤더입니다2222.")

# #텍스트 입력
# #Text / Write
# #단순한 텍스트 / 고정된 형식, 포맷팅 쓸 수 없음
# st.text("This is the articles.")

# #write
# #'변수' -> 문자열, 숫자, 리스트, 딕셔너리, 데이터프레임
# st.write("This is a writing!")
# st.write(pd.DataFrame({'first': [1,2,3,4],
# 						'second' : [4, 5, 6, 7]}))


# #markdown
# html_page = """
# <div style="background-color:blue;padding:50px">
# 	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
# </div>
# """

# #streamlit에서 html을 활용해서 페이지를 변경시킬 수 있음
# st.markdown(html_page, unsafe_allow_html=True) 


#팝업
#------------------------------------------
# st.success('Success!')
# st.info('information')
# st.warning('warn!')
# st.error('err!')

#이미지, 오디오, 비디오
#---------------------------------------
# from PIL import Image
# image = Image.open('./image.png')
# st.image(image, width=300, caption='~~이미지에요.')

#open('경로', 'wr') as f:
#	f.read()
# audio_file = open('경로', 'rb')
# audio_by = audio_file.read()
# st.audio(audio_by)

#유튜브 영상 넣기
# 로컬 영상 -> 리드 후 넣기
# 외부 영상 -> 링크 입력
# st.video("https://www.youtube.com/watch?v=JiBHjl2wgwE")

#---------------------------------------------------------
# 상호작용

# if st.button('눌러주세요'):
# 	st.text("버튼이 눌림")

# #checkbox
# if st.checkbox('check'):
# 	st.write('체크함')

# #radiobutton
# radio_button = st.radio('select', ['집에가기', '공부하기'])
# if radio_button == '집에가기':
# 	st.text('저도요...')

# else:
# 	st.text('힘들지만 좋은 선택...')

#셀렉트박스
# city = st.selectbox('Your city', ['Seoul', 'Busan', 'Incheon'])
# if city == 'Seoul':
# 	st.text('서울사람이구나')

# #멀티셀렉트
# job = st.multiselect('your futre job', ['programmer', 'data scientist', 'it consultant'])

#-----------------------------------------------
# 정보를 input
# name = st.text_input('이름을 기입하세요', "예) 홍길동...")

# #숫자 입력
# number = st.number_input('input number')

# #text area
# message = st.text_area('문자를 적어주세요', 'Write something....')

# #슬라이더
# #정수로 입력하면 1단위 상승, 소수로 입력하면 소수로 올라감
# select = st.slider('', 1.0, 10.00)

# if st.button('눌러보세요'):
# 	st.balloons()

#-------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv('./auto.csv')

# # st.area_chart(df[['mpg', 'cylinders']])
# # st.bar_chart(df[['mpg', 'cylinders']])
# # st.line_chart(df[['mpg', 'cylinders']])

# fig, ax = plt.subplots()
# corr_plot = sns.heatmap(df[['mpg', 'cylinders']].corr(), annot=True)
# st.pyplot(fig)

#-------------------------------------------------------------
# import datetime
# today = st.date_input('Today is', datetime.datetime.now())

# import time
# hour = st.time_input('the time is', datetime.time(12, 30))

# #json, code 블럭을 보여주기
# data = {"name":"John","surname":"Wick"}
# st.json(data)

# st.code("import pandas as pd")

# julia_code = """
# function doit(num::int)
# 	println(num)
# end
# """

# python_code = """

# def cutomizing(x, y):
# 	return x+y

# """

# st.code(python_code, language='python')


#---------------------------------------
#지연
import time

#프로그레스 바
# my_bar = st.progress(0)
# for v in range(100):
# 	time.sleep(1)
# 	my_bar.progress(v+1)

st.header("스트림릿 서빙 연습")

with st.spinner('Pleas wait....'):
	time.sleep(10)
st.success('Done!')