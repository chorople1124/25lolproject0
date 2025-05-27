import streamlit as st
import pandas as pd
import plotly.express as px

# 우승 횟수 데이터
data = {
    '팀명': ['T1', 'Gen.G', 'DRX', 'DK', 'Fredit BRION', 'NS', 'KZ', 'Hanwha Life', 'Sandbox Gaming', 'Afreeca Freecs'],
    '우승 횟수': [10, 7, 4, 6, 2, 1, 3, 2, 1, 1]
}
df = pd.DataFrame(data).sort_values(by='우승 횟수', ascending=False)

# 임의의 승패 기록 (예시)
# 팀 A가 팀 B를 이긴 횟수
matches = {
    ('T1', 'Gen.G'): 3,
    ('T1', 'DRX'): 4,
    ('Gen.G', 'DK'): 2,
    ('DRX', 'Fredit BRION'): 1,
    ('DK', 'NS'): 3,
    ('KZ', 'Hanwha Life'): 2,
    ('Sandbox Gaming', 'Afreeca Freecs'): 1,
    ('T1', 'DK'): 1,
    # ... 추가 가능
}

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

# 승패 기록 텍스트 출력
st.subheader("주요 승패 기록")

for (winner, loser), count in matches.items():
    st.write(f"{winner} 팀이 {loser} 팀을 {count}회 이겼습니다.")
