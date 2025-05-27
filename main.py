import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    "player_id": [1,1,2,2,3,3,4,4,5,5],
    "game_id": [101,102,101,103,102,104,103,105,104,105],
    "champion": ["아리", "리 신", "아리", "징크스", "리 신",
                 "아리", "가렌", "징크스", "리 신", "가렌"]
}

df = pd.DataFrame(data)

# 한국 플레이어 id 리스트 (예시)
korean_players = [1, 2, 3]

# 한국 플레이어 데이터만 필터링
korean_df = df[df['player_id'].isin(korean_players)]

# 챔피언별 사용 횟수 집계
usage_counts = korean_df['champion'].value_counts().head(10).reset_index()
usage_counts.columns = ['챔피언', '사용 횟수']

st.title("한국 플레이어 챔피언 사용 빈도 TOP 10")

fig = px.bar(usage_counts, x='챔피언', y='사용 횟수',
             title='한국 플레이어 챔피언 사용 빈도 TOP 10',
             text='사용 횟수',
             labels={'챔피언':'챔피언', '사용 횟수':'사용 횟수'})

fig.update_traces(textposition='outside')
fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)
