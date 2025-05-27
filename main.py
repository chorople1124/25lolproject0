import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터: player_id, game_id, champion
data = {
    "player_id": [1,1,2,2,3,3,4,4,5,5],
    "game_id": [101,102,101,103,102,104,103,105,104,105],
    "champion": ["Ahri", "Lee Sin", "Ahri", "Jinx", "Lee Sin",
                 "Ahri", "Garen", "Jinx", "Lee Sin", "Garen"]
}

df = pd.DataFrame(data)

st.title("모든 플레이어 챔피언 사용 빈도 분석")

# 챔피언 사용 횟수 집계 (플레이어 구분 없이 전체 합산)
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
