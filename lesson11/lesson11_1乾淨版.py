import streamlit as st
import datasource  #複製lesson10的資料來用，重新命名為datasource

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人口數")
st.subheader("進出站人數顯示區")


#增加抓取資料的效能
@st.cache_data
def get_stations():
    """取得車站資料"""
    return datasource.get_stations_names() #從這裡知道若沒有資料會傳出none

stations = get_stations()
#所以到這裡設定若無資料時(AI寫))
if stations is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()

common_stations = ['臺北','桃園','新竹','台中','臺南','高雄','其他']
choice = st.sidebar.radio("快速選擇常用車站", common_stations)

if choice == "其他":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

st.write("您選擇的車站:", station)