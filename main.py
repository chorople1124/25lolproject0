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
matches = {
    ('T1', 'Gen.G'): 3,
    ('T1', 'DRX'): 4,
    ('Gen.G', 'DK'): 2,
    ('DRX', 'Fredit BRION'): 1,
    ('DK', 'NS'): 3,
    ('KZ', 'Hanwha Life'): 2,
    ('Sandbox Gaming', 'Afreeca Freecs'): 1,
    ('T1', 'DK'): 1,
}

# 스트림릿 배경 어둡게 설정 (스타일 적용)
st.markdown(
    """
    <style>
    .main {
        background-color: #0a0a23;
        color: #39ff14;
        font-family: 'Courier New', Courier, monospace;
    }
    .neon-text {
        font-size: 3rem;
        font-weight: 900;
        color: #39ff14;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow:
            0 0 8px #39ff14,
            0 0 15px #39ff14,
            0 0 25px #39ff14,
            0 0 50px #0ff,
            0 0 80px #0ff,
            0 0 100px #0ff;
    }
    .neon-subheader {
        font-size: 1.75rem;
        font-weight: 700;
        color: #0ff;
        margin-top: 2rem;
        margin-bottom: 1rem;
        text-shadow:
            0 0 5px #0ff,
            0 0 10px #0ff,
            0 0 20px #0ff,
            0 0 40px #39ff14,
            0 0 60px #39ff14;
    }
    .match-record {
        font-size: 1.1rem;
        font-weight: 600;
        color: #0ff;
        margin-bottom: 0.6rem;
        text-shadow:
            0 0 4px #0ff,
            0 0 8px #0ff;
    }
    /* 플로틀리 차트 주변 여백 좀 더 넉넉히 */
    .css-1d391kg {
        padding: 1rem 1rem 2rem 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="neon-text">프로게이머 팀 우승 전적 TOP 10</h1>', unsafe_allow_html=True)

# Plotly bar chart - 네온 블루 스타일
fig = px.bar(
    df,
    x='팀명',
    y='우승 횟수',
    text='우승 횟수',
    color='우승 횟수',
    color_continuous_scale=px.colors.sequential.Blues,
    template='plotly_dark',
    title='프로게이머 팀 우승 전적 순위',
)

fig.update_traces(
    textposition='outside',
    marker_line_width=2.5,
    marker_line_color='cyan',
    marker_color='deepskyblue',
    textfont=dict(color='cyan', family='Courier New', size=16, weight='bold')
)

fig.update_layout(
    xaxis_tickangle=-45,
    coloraxis_showscale=False,
    uniformtext_minsize=16,
    uniformtext_mode='hide',
    plot_bgcolor='#0a0a23',
    paper_bgcolor='#0a0a23',
    font=dict(color='cyan', family='Courier New', size=14),
    margin=dict(l=50, r=50, t=90, b=50),
    title_font=dict(size=26, color='cyan', family='Courier New', weight='bold'),
)

st.plotly_chart(fig, use_container_width=True)

st.markdown('<h3 class="neon-subheader">주요 승패 기록</h3>', unsafe_allow_html=True)

for (winner, loser), count in matches.items():
    st.markdown(f'<p class="match-record">{winner} 팀이 {loser} 팀을 {count}회 이겼습니다.</p>', unsafe_allow_html=True)
