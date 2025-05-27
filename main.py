import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "player_id": [1,1,2,2,3,3,4,4,5,5],
    "game_id": [101,102,101,103,102,104,103,105,104,105],
    "champion": ["아리", "리 신", "아리", "징크스", "리 신",
                 "아리", "가렌", "징크스", "리 신", "가렌"]
}

df = pd.DataFrame(data)

st.title("모든 플레이어 챔피언 사용 빈도 분석")

usage_counts = df['champion'].value_counts()

st.write("챔피언별 사용 횟수 (모든 플레이어 합산):")
st.dataframe(usage_counts)

fig, ax = plt.subplots()
usage_counts.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
plt.xlabel("챔피언")
plt.ylabel("사용 횟수")
plt.title("롤 챔피언 사용 빈도 (전체 플레이어)")
plt.xticks(rotation=45)

st.pyplot(fig)
