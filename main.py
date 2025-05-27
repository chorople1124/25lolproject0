import streamlit as st
import pandas as pd
import plotly.express as px

# 우승 횟수 데이터
data = {
    '팀명': ['T1', 'Gen.G', 'DRX', 'DK', 'Fredit BRION', 'NS', 'KZ', 'Hanwha Life', 'Sandbox Gaming', 'Afreeca Freecs'],
    '우승 횟수': [10, 7, 4, 6, 2, 1, 3, 2, 1, 1]
}
df = pd.DataFrame(data).sort_values(by='우승 횟수', ascending=False)

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

# 보노보노 캐릭터 이미지 URL (예시 - 무료 이미지나 GIF로 교체 가능)
bonobono_url = "https://upload.wikimedia.org/wikipedia/en/3/31/Bonobono_%28manga_character%29.png"

st.markdown(
    f"""
    <style>
    .main {{
        background: linear-gradient(270deg, 
            red, orange, yellow, green, blue, indigo, violet);
        background-size: 1400% 1400%;
        animation: rainbowBG 20s ease infinite;
        color: #222;
        font-family: 'Courier New', Courier, monospace;
        position: relative;
        min-height: 100vh;
        padding: 2rem;
        overflow-x: hidden;
    }}
    @keyframes rainbowBG {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    .neon-text {{
        font-size: 3rem;
        font-weight: 900;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow:
            0 0 8px white,
            0 0 15px white,
            0 0 25px white,
            0 0 50px cyan,
            0 0 80px cyan,
            0 0 100px cyan;
    }}
    .neon-subheader {{
        font-size: 1.75rem;
        font-weight: 700;
        color: white;
        margin-top: 2rem;
        margin-bottom: 1rem;
        text-shadow:
            0 0 5px cyan,
            0 0 10px cyan,
            0 0 20px cyan;
    }}
    .match-record {{
        font-size: 1.1rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.6rem;
        text-shadow:
            0 0 4px cyan,
            0 0 8px cyan;
    }}

    /* 보노보노 이미지 스타일 */
    .bonobono-img {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 150px;
        opacity: 0.85;
        z-index: 10;
        user-select: none;
        pointer-events: none;
        filter: drop-shadow(0 0 5px white);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="neon-text">프로게이머 팀 우승 전적 TOP 10</h1>', unsafe_allow_html=True)

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
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='cyan', family='Courier New', size=14),
    margin=dict(l=50, r=50, t=90, b=50),
    title_font=dict(size=26, color='cyan', family='Courier New', weight='bold'),
)

st.plotly_chart(fig, use_container_width=True)

st.markdown('<h3 class="neon-subheader">주요 승패 기록</h3>', unsafe_allow_html=True)

for (winner, loser), count in matches.items():
    st.markdown(f'<p class="match-record">{winner} 팀이 {loser} 팀을 {count}회 이겼습니다.</p>', unsafe_allow_html=True)

# 보노보노 캐릭터 이미지 추가
st.markdown(f'<img src="{bonobono_url}" class="bonobono-img" alt="Bonobono 캐릭터">', unsafe_allow_html=True)
