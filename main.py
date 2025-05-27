import streamlit as st
import pandas as pd
import plotly.express as px

# 임의의 프로게이머 팀 우승 기록 데이터
data = {
    '팀명': ['T1', 'Gen.G', 'DRX', 'DK', 'Fredit BRION', 'NS', 'KZ', 'Hanwha Life', 'Sandbox Gaming', 'Afreeca Freecs'],
    '우승 횟수': [10, 7, 4, 6, 2, 1, 3, 2, 1, 1]
}

df = pd.DataFrame(data).sort_values(by='우승 횟수', ascending=False)

st.title("프로게이머 팀 우승 전적 TOP 10")

fig = px.bar(
    df,
    x='팀명',
    y='우승 횟수',
    text='우승 횟수',
    color='우승 횟수',
    color_continuous_scale='Blues',
    template='plotly_white',
    title='프로게이머 팀 우승 전적 순위',
)

fig.update_traces(
    textposition='outside',
    marker_line_width=1.5,
    marker_line_color='rgba(0,0,0,0.5)'
)

fig.update_layout(
    xaxis_tickangle=-45,
    coloraxis_showscale=False,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    margin=dict(l=40, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True)
