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

korean_players = [1, 2, 3]

korean_df = df[df['player_id'].isin(korean_players)]

usage_counts = korean_df['champion'].value_counts().head(10).reset_index()
usage_counts.columns = ['챔피언', '사용 횟수']

st.title("한국 플레이어 챔피언 사용 빈도 TOP 10")

fig = px.bar(
    usage_counts,
    x='챔피언',
    y='사용 횟수',
    text='사용 횟수',
    labels={'챔피언': '챔피언', '사용 횟수': '사용 횟수'},
    color='사용 횟수',
    color_continuous_scale='Viridis',
    template='plotly_dark',
    title='한국 플레이어 챔피언 사용 빈도 TOP 10'
)

fig.update_traces(
    textposition='outside',
    marker_line_width=1.5,
    marker_line_color='rgba(255,255,255,0.7)'
)

fig.update_layout(
    xaxis_tickangle=-45,
    coloraxis_showscale=False,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    margin=dict(l=40, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True)
