import streamlit as st
import time


QUESTIONS = [
    {
        "q": "주말 아침, 눈을 뜬 당신!\n가장 먼저 드는 생각은?",
        "options": {
            "오늘은 또 뭘 하고 놀까? 약속 없나 찾아봐야지!호호호호": "E",
            "아늑한 침대 최고... 조용히 뒹굴뒹굴해야지~": "I",
        },
    },
    {
        "q": "산책 중 처음 보는 댕댕이를 만났다!\n당신의 반응은?",
        "options": {
            "와! 새 친구다! 킁킁 냄새부터 맡고 꼬리치기!": "E",
            "일단 거리를 두고 스캔... 안전한지 지켜본다.": "I",
        },
    },
    {
        "q": "맛있는 간식이 눈앞에 두 개 있다.\n하나는 익숙한 맛, 하나는 처음 보는 맛!",
        "options": {
            "음~ 실패 없는 아는 맛! 이걸 먹어야지.": "S",
            "이건 무슨 맛일까? 새로운 맛에 도전!": "N",
        },
    },
    {
        "q": "주인이 '산책 갈까?'라고 물었다.\n당신의 머릿속에 그려지는 것은?",
        "options": {
            "오늘따라 유난히 파란 하늘, 포근한 바람, 흙냄새...": "S",
            "혹시... 공원? 친구들? 아니면 새로운 장소?! 기대된다!": "N",
        },
    },
    {
        "q": "주인이 공을 던져주며 놀아주다가\n실수로 당신의 발을 밟았다.",
        "options": {
            "아야! 아픈 건 아픈 거지! 깽! 하고 소리를 낸다.": "T",
            "주인이 더 놀랐겠네... 괜찮다고 꼬리를 흔들어준다.": "F",
        },
    },
    {
        "q": "주인이 훌쩍이고 있다.\n당신은 어떻게 위로할까?",
        "options": {
            "왜 슬플까? 이유가 뭘까? 일단 차분하게 지켜본다.": "T",
            "무슨 일인지 몰라도 슬퍼 보인다... 곁에 가서 핥아준다.": "F",
        },
    },
    {
        "q": "내일은 주인과 함께\n애견 운동장에 놀러 가는 날!",
        "options": {
            "벌써 신나! 어떤 장난감부터 챙길지 미리 다 정해놓는다.": "J",
            "내일의 나는 내일 생각하자! 일단은 꿀잠 잘 시간~": "P",
        },
    },
    {
        "q": "장난감이 어질러져 있다.\n당신의 놀이 스타일은?",
        "options": {
            "하나씩 순서대로! 공 놀이가 끝나면 인형을 가지고 논다.": "J",
            "이거 갖고 놀다 저거 갖고 놀다~ 자유롭게 노는 게 최고!": "P",
        },
    },
    {
        "q": "새로운 '앉아!' 훈련을 시작했다.",
        "options": {
            "왜 앉아야 하지? 간식을 위해서라면... 일단 앉는다.": "T",
            "주인이 기뻐하니까! 나도 기뻐! 열심히 따라 한다.": "F",
        },
    },
    {
        "q": "낯선 소리가 들렸을 때,\n가장 먼저 드는 생각은?",
        "options": {
            "어? 방금 무슨 소리 났는데? 정확히 확인해봐야겠다.": "S",
            "혹시... 간식 배달? 아니면 나쁜 사람?! 온갖 상상을 한다.": "N",
        },
    },
    {
        "q": "친구가 내 최애 장난감을 빌려달라고 한다.",
        "options": {
            "지금 내가 안 갖고 노니까... 그래, 잠깐은 괜찮아.": "T",
            "소중한 거지만... 친구가 좋다니깐... 기꺼이 빌려준다.": "F",
        },
    },
    {
        "q": "피곤한 오후, 낮잠 잘 곳을 고른다면?",
        "options": {
            "항상 자던 나의 뽀송한 전용 쿠션이 최고지!": "J",
            "햇살 좋은 곳이라면 어디든 OK! 발길 닿는 대로 눕는다.": "P",
        },
    },
]

MBTI_DOGS = {
    "ENFP": {"emoji": "🐶", "dog_name": "에너자이저 비글", "desc": "세상에 나쁜 개는 없다! 모든 사람, 모든 댕댕이와 친구가 될 수 있는 핵인싸 댕댕이!\n호기심 많고 장난기 넘쳐서 지루할 틈을 주지 않아요.", "good_match": "인싸력 넘치는 '골든 리트리버'", "bad_match": "계획이 중요한 '보더콜리'"},
    "ENTP": {"emoji": "🦴", "dog_name": "천재 웰시코기", "desc": "짧은 다리로 세상을 지배하는 똑똑이 댕댕이!\n새로운 장난감의 작동 원리를 가장 먼저 파악하고, 주인을 골탕 먹이는 창의적인 방법을 늘 연구해요.", "good_match": "함께라면 뭐든 OK! '시베리안 허스키'", "bad_match": "조용한 게 최고 '차우차우'"},
    "ISFP": {"emoji": "🐾", "dog_name": "평화주의 시바견", "desc": "싫은 건 싫다고 확실히 표현하지만, 사실은 누구보다 따뜻한 마음을 가진 댕댕이.\n자신만의 공간에서 여유를 즐기는 걸 좋아해요.", "good_match": "다정한 '몰티즈'", "bad_match": "밀어붙이는 '불도그'"},
    "ISTJ": {"emoji": "🐕", "dog_name": "듬직한 셰퍼드", "desc": "주인의 말을 법처럼 여기는 충성심 강한 댕댕이!\n정해진 산책 시간, 정해진 밥 시간을 어기는 법이 없는 모범생이에요.", "good_match": "귀염둥이 '닥스훈트'", "bad_match": "자유로운 영혼 '비글'"},
    "INFP": {"emoji": "💖", "dog_name": "순둥이 골든 리트리버", "desc": "사람을 너무 좋아해서 '인절미'로 불리는 순둥이!\n주인의 감정을 잘 살피고, 슬플 땐 말없이 다가와 위로를 건네는 따뜻한 마음의 소유자예요.", "good_match": "에너자이저 '비글'", "bad_match": "냉철한 '셰퍼드'"},
    "INFJ": {"emoji": "✨", "dog_name": "사려 깊은 진돗개", "desc": "겉으로는 과묵해 보이지만, 속으로는 깊은 생각을 하는 댕댕이.\n주인의 감정을 섬세하게 읽고, 묵묵히 곁을 지켜주는 충실한 친구예요.", "good_match": "밝고 긍정적인 '푸들'", "bad_match": "다혈질 '치와와'"},
    "ENFJ": {"emoji": "🐩", "dog_name": "인기 만점 푸들", "desc": "모두의 사랑을 한몸에 받는 인기쟁이 댕댕이!\n사교성이 뛰어나 어떤 무리에서도 금방 친구를 만들고, 긍정적인 에너지로 주변을 환하게 밝혀줘요.", "good_match": "사려 깊은 '진돗개'", "bad_match": "독립적인 '아키타견'"},
    "ESTP": {"emoji": "🔥", "dog_name": "대담한 불독", "desc": "새로운 것을 보면 일단 들이받는(?) 대담한 댕댕이!\n넘치는 에너지로 항상 새로운 모험을 찾아 떠나며, 어떤 상황에서도 즐거움을 놓치지 않아요.", "good_match": "명랑한 '코카 스파니엘'", "bad_match": "신중한 '말티즈'"},
    "ESTJ": {"emoji": "🧐", "dog_name": "똑 부러지는 보더콜리", "desc": "주인의 명령을 완벽하게 수행하는 엘리트 댕댕이!\n규칙과 질서를 중요하게 생각하며, 주어진 임무를 충실하게 해내는 믿음직스러운 친구예요.", "good_match": "차분한 '도베르만'", "bad_match": "자유로운 '비글'"},
    "ESFP": {"emoji": "🌟", "dog_name": "발랄한 코카 스파니엘", "desc": "타고난 연예인 기질로 주변을 즐겁게 만드는 댕댕이!\n어디서든 주목받는 것을 좋아하고, 톡톡 튀는 매력으로 모두를 웃게 만들어요.", "good_match": "대담한 '불독'", "bad_match": "내향적인 '차우차우'"},
    "ESFJ": {"emoji": "🥰", "dog_name": "다정한 시츄", "desc": "주인 바라기, 친구 바라기! 주변 사람들을 끔찍이 아끼는 댕댕이.\n언제나 다정하게 곁을 지키며, 모두가 행복하길 바라요.", "good_match": "든든한 '리트리버'", "bad_match": "차가운 '시베리안 허스키'"},
    "INTP": {"emoji": "💡", "dog_name": "호기심 박사 닥스훈트", "desc": "온 세상이 궁금한 지식 탐험가 댕댕이!\n새로운 냄새, 새로운 소리, 새로운 장난감의 비밀을 파헤치는 것을 즐기는 똑똑한 친구예요.", "good_match": "차분한 '바셋 하운드'", "bad_match": "무계획적인 '비글'"},
    "INTJ": {"emoji": "♟️", "dog_name": "전략가 도베르만", "desc": "미래를 예측하고 계획하는 카리스마 넘치는 댕댕이!\n주인과의 놀이에서도 항상 최적의 전략을 구상하며, 빈틈없는 모습을 보여줘요.", "good_match": "듬직한 '셰퍼드'", "bad_match": "감정적인 '시츄'"},
    "ISFJ": {"emoji": "😇", "dog_name": "헌신적인 말티즈", "desc": "주인만을 위한 맞춤형 댕댕이!\n조용하지만 섬세하게 주인을 보살피고, 언제나 곁에서 든든한 버팀목이 되어주는 사랑스러운 친구예요.", "good_match": "평화주의 '시바견'", "bad_match": "제멋대로 '치와와'"},
    "ISTP": {"emoji": "😎", "dog_name": "쿨내 진동 시베리안 허스키", "desc": "독립적이고 쿨한 매력의 댕댕이!\n어떤 상황에서도 침착함을 잃지 않으며, 자신만의 방식으로 문제를 해결하는 능력자예요.", "good_match": "천재 '웰시코기'", "bad_match": "응석받이 '푸들'"},
    "DEFAULT": {"emoji": "💖", "dog_name": "궁금증 많은 믹스견", "desc": "하나로 정의할 수 없는 매력을 가진 세상에 단 하나뿐인 댕댕이!\n때로는 활발하고, 때로는 조용하며 예측할 수 없는 매력으로 모두를 사로잡아요.", "good_match": "모든 댕댕이", "bad_match": "없음"}
}

def init_session_state():
    """세션 상태 초기화"""
    if 'page' not in st.session_state:
        st.session_state.page = 'start'
    if 'scores' not in st.session_state:
        st.session_state.scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    if 'question_num' not in st.session_state:
        st.session_state.question_num = 0
    if 'participant_count' not in st.session_state:
        st.session_state.participant_count = 12345 # 시뮬레이션된 참여자 수

def go_to_next_page(answer_type):
    """답변을 기록하고 다음 페이지로 이동"""
    st.session_state.scores[answer_type] += 1
    if st.session_state.question_num < len(QUESTIONS) - 1:
        st.session_state.question_num += 1
    else:
        st.session_state.page = 'loading'
    st.session_state.participant_count += 1

def calculate_mbti_result(scores):
    """MBTI 결과 계산"""
    result = ""
    result += "E" if scores["E"] >= scores["I"] else "I"
    result += "S" if scores["S"] >= scores["N"] else "N"
    result += "T" if scores["T"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["P"] else "P"
    return result

def render_start_page():
    st.title("🐾 나는 어떤 댕댕이일까? 🐾")
    st.header("MBTI로 알아보는 나의 멍BTI! 🐶")
    st.write("---")
    st.markdown(f"**💖 지금까지 {st.session_state.participant_count:,}마리의 댕댕이가 참여했어요! 💖**")
    if st.button("테스트 시작! 멍!", type="primary", use_container_width=True):
        st.session_state.page = 'test'
        st.rerun()

def render_test_page():
    q_num = st.session_state.question_num
    q_data = QUESTIONS[q_num]

    st.progress((q_num + 1) / len(QUESTIONS), text=f"**{q_num + 1} / {len(QUESTIONS)} 🐾**")
    st.markdown("---")
    
    # 질문을 가운데 정렬하고, 줄바꿈을 <br> 태그로 변환
    st.markdown(f"<h2 style='text-align: center; color: #333;'>{q_data['q'].replace('\\n', '<br>')}</h2>", unsafe_allow_html=True)
    st.write("") # 여백

    # 버튼을 세로로 배치하기 위해 st.columns 제거
    for i, (option, answer_type) in enumerate(q_data["options"].items()):
        st.write("") # 버튼 사이 여백
        if st.button(option, key=f"q{q_num}_{i}", use_container_width=True):
            go_to_next_page(answer_type)
            st.rerun()

def render_loading_page():
    with st.spinner("두근두근... 🐾 당신은 어떤 댕댕이일까요? 결과를 분석 중이에요! 🐶"):
        time.sleep(2)
        st.session_state.mbti_result = calculate_mbti_result(st.session_state.scores)
        st.session_state.page = 'result'
        st.rerun()

def render_result_page():
    result_mbti = st.session_state.mbti_result
    result_dog = MBTI_DOGS.get(result_mbti, MBTI_DOGS["DEFAULT"])

    st.balloons()
    st.header("🎉 나의 멍BTI 결과는?! 🎉")
    st.markdown(f"# {result_dog['emoji']} MBTI 유형 '{result_mbti}'인 당신은 바로 **{result_dog['dog_name']}** 이에요!")
    
    st.markdown("---")
    st.markdown(f"### ✨ 특징 ✨")
    st.markdown(f"> _{result_dog['desc'].replace('\\n', '  \\n')}_")
    
    st.markdown("---")
    st.subheader("💖 댕댕이 궁합 💖")
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**💚 환상의 궁합:** {result_dog['good_match']}")
    with col2:
        st.error(f"**💔 안 맞는 궁합:** {result_dog['bad_match']}")

    st.markdown("---")
    if st.button("다시하기", type="primary", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def main():
    st.set_page_config(page_title="나는 어떤 댕댕이일까? 🐾", page_icon="🐾")
    init_session_state()
    if st.session_state.page == 'start':
        render_start_page()
    elif st.session_state.page == 'test':
        render_test_page()
    elif st.session_state.page == 'loading':
        render_loading_page()
    elif st.session_state.page == 'result':
        render_result_page()

if __name__ == "__main__":

    main()

