import source  #注意，老師的資料檔名是datasource
import streamlit as st #4點後介面

# def main():
#     results = source.get_stations_names()
#     if results:
#         for station in results:
#             print(station)
#     else:
#         print("無法取得車站資料")

# if __name__ == "__main__":
#     main()

    #介面 4點之後修改

def main():
    st.title("台鐵車站名稱列表")
    results = source.get_stations_names()
    if results:
        st.dataframe(results, width=400, height=600)
    else:
        st.error("無法取得車站資料")

if __name__ == "__main__":
    main()