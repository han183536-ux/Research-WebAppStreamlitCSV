import streamlit

# Page setting
streamlit.set_page_config(
    page_title="Streamlit Tutorial",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="auto"
)

# Task 01
streamlit.title("Task 01")

# Task 02
streamlit.title("Task 02")

# Task 03
streamlit.title("Task 03")
#============================================
#막대 그래프 생성
chart_data = pandas.DataFrame(
    {
        "X 축": list(range(20)) * 3,
        "Y 축": numpy.random.randn(60),
        "색": ["A"] * 20 + ["B"] * 20 + ["C"] * 20
    }
)
#막대 그래프 출력
streamlit.bar_chart(chart_data, x="X 축", y="Y 축", color = "색")
#============================================

#선 그래프 생성
line_data = pandas.DataFrame(
    numpy.random.randn(20, 3),
    columns=["A", "B", "C"]
)
#선 그래프 출력
streamlit.line_chart(line_data)

#============================================
#영역 그래프 생성
area_data = pandas.DataFrame(
    numpy.random.randn(20, 3),
    columns=["A", "B", "C"]
)
#영역 그래프 출력
streamlit.area_chart(area_data)

# Task 04
streamlit.title("Task 04")

# Task 05
streamlit.title("Task 05")

# Task 06
streamlit.title("Task 06")

# Task 07
streamlit.title("Task 07")
