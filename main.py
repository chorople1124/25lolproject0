import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터: 게임별 플레이 챔피언
data = {
    "game_id": [1,2,3,4,5,6,7,8,9,10],
    "champion": ["Ahri", "Lee Sin", "Ahri", "Jinx", "Lee Sin",
                 "Ahri", "Garen", "Jinx", "Lee Sin", "Garen"]
}
df = pd.DataFrame(data)

st.title("롤 챔피언 사용 빈도 분석")

usage_counts = df['champion'].value_counts()

st.write("챔피언별 사용 횟수:")
st.dataframe(usage_counts)

fig, ax = plt.subplots()
usage_counts.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
plt.xlabel("챔피언")
plt.ylabel("사용 횟수")
plt.title("롤 챔피언 사용 빈도")
plt.xticks(rotation=45)

st.pyplot(fig)
