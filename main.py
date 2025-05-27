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

st.title("모든 플레이어 챔피언 사용 빈도 분석")

usage_counts = df['champion'].value_counts().reset_index()
usage_counts.columns = ['챔피언', '사용 횟수']

fig = px.bar(usage_counts, x='챔피언', y='사용 횟수',
             title='롤 챔피언 사용 빈도 (전체 플레이어)',
             text='사용 횟수',
             labels={'챔피언':'챔피언', '사용 횟수':'사용 횟수'})

fig.update_traces(textposition='outside')
fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)
