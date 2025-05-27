import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터: 게임별로 플레이된 챔피언 이름
data = {
    "game_id": [1,2,3,4,5,6,7,8,9,10],
    "champion": ["Ahri", "Lee Sin", "Ahri", "Jinx", "Lee Sin",
                 "Ahri", "Garen", "Jinx", "Lee Sin", "Garen"]
}

df = pd.DataFrame(data)

# 챔피언별 사용 횟수 집계
usage_counts = df['champion'].value_counts()

print("챔피언 사용 빈도:")
print(usage_counts)

# 시각화
usage_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('롤 챔피언 사용 빈도')
plt.xlabel('챔피언')
plt.ylabel('사용 횟수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
