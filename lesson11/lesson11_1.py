# 當輸出df變數時,st.write()會自動執行
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import datasource  #複製lesson10的資料來用，重新命名為datasource

#df = pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#})

#df

#st.write("**Hello World")

# st.title("台鐵車站資訊")
# st.header("2023年各站進出人口數")
#col1, col2 = st.columns(2)
#col1.subheader("站點")
#col2.subheader("進出站點人數")  #太佔空間，使用sidebar

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人口數")
st.subheader("進出站人數顯示區")
#stations = datasource.get_stations_names()
#station = st.sidebar.selectbox(
#"請選擇車站",
#("台北","台中","高雄")
#)

#st.write("您選擇的車站:", station)

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
#sidebar要先顯示常用的車站名稱
#使用者可以很快的選擇
#如果不常用的車站名稱,再使用selectbox

# 先取前五個站為常用站（可改為固定清單或從使用者設定讀取）
#common_stations = stations[:5] if len(stations) >= 5 else stations

# 在 sidebar 顯示常用站列表，並加上「其他」選項（當總站數大於常用站數時）

#quick_options = common_stations + (["其他"] if len(stations) > len(common_stations) else [])
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