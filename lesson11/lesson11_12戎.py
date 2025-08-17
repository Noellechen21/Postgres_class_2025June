#下午 練習使用者選取日期區間後可以顯示其選擇的日期區間_戎版
import streamlit as st
import datasource

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

@st.cache_data
def get_stations():
    """取得車站資料"""
    return datasource.get_stations_names()

@st.cache_data
def get_date_range():
    """取得日期範圍"""
    return datasource.get_min_and_max_date()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()


common_stations = ['臺北','桃園','新竹','台中','臺南','高雄','其它']
choice = st.sidebar.radio("快速選擇常用車站", common_stations)

if choice == "其它":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

date_range = get_date_range()
if date_range is None:
    st.error("無法取得日期範圍，請稍後再試。")
    st.stop()

# 假設 date_range = (min_date, max_date)
import datetime

start_date, end_date = date_range

# 確保 start_date 和 end_date 是 datetime.date 物件
if isinstance(start_date, str):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
if isinstance(end_date, str):
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

selected_dates = st.sidebar.date_input(
    "請選擇日期範圍",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date
)

st.write("您選擇的車站:", station)
st.write("日期範圍:", f"{start_date.strftime('%Y-%m-%d')} 至 {end_date.strftime('%Y-%m-%d')}")
if isinstance(selected_dates, tuple):
    st.write("您選擇的日期範圍:", f"{selected_dates[0].strftime('%Y-%m-%d')} 至 {selected_dates[1].strftime('%Y-%m-%d')}")
else:
    st.write("您選擇的日期範圍:", selected_dates.strftime('%Y-%m-%d'))
