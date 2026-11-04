import streamlit as st
import time
from ai_helper import ask_ai
import random

# 페이지 설정
st.set_page_config(page_title="영어 단어 외우기", layout="wide")

# 단어 데이터셋
WORD_DATABASE = [
    {"eng": "apple", "kor": "사과", "loan": "애플"},
    {"eng": "cat", "kor": "고양이", "loan": "캣"},
    {"eng": "dog", "kor": "개"},
    {"eng": "tree", "kor": "나무", "loan": "트리"},
    {"eng": "water", "kor": "물", "loan": "워터"},
    {"eng": "fire", "kor": "불"},
    {"eng": "house", "kor": "집", "loan": "하우스"},
    {"eng": "book", "kor": "책"},
    {"eng": "computer", "kor": "컴퓨터"},
    {"eng": "phone", "kor": "휴대폰", "loan": "폰"},
    {"eng": "table", "kor": "테이블"},
    {"eng": "chair", "kor": "의자"},
    {"eng": "window", "kor": "창문", "loan": "윈도우"},
    {"eng": "door", "kor": "문", "loan": "도어"},
    {"eng": "light", "kor": "빛", "loan": "라이트"},
]

# 중학교 1학년 수준 단어 데이터셋
MIDDLE1_WORD_DATABASE = [
    {"eng": "able", "kor": "할 수 있는"},
    {"eng": "alone", "kor": "혼자인"},
    {"eng": "angry", "kor": "화난"},
    {"eng": "bake", "kor": "굽다"},
    {"eng": "birthday", "kor": "생일"},
    {"eng": "bottle", "kor": "병"},
    {"eng": "busy", "kor": "바쁜"},
    {"eng": "candy", "kor": "사탕"},
    {"eng": "carry", "kor": "나르다"},
    {"eng": "catch", "kor": "잡다"},
    {"eng": "clean", "kor": "깨끗한"},
    {"eng": "cloud", "kor": "구름"},
    {"eng": "cold", "kor": "추운, 감기"},
    {"eng": "cook", "kor": "요리하다"},
    {"eng": "cousin", "kor": "사촌"},
    {"eng": "cry", "kor": "울다"},
    {"eng": "dance", "kor": "춤추다"},
    {"eng": "dark", "kor": "어두운"},
    {"eng": "daughter", "kor": "딸"},
    {"eng": "dream", "kor": "꿈"},
    {"eng": "dry", "kor": "마른"},
    {"eng": "early", "kor": "이른"},
    {"eng": "easy", "kor": "쉬운"},
    {"eng": "enjoy", "kor": "즐기다"},
    {"eng": "exam", "kor": "시험"},
    {"eng": "fast", "kor": "빠른"},
    {"eng": "finish", "kor": "끝내다"},
    {"eng": "floor", "kor": "바닥, 층"},
    {"eng": "flower", "kor": "꽃"},
    {"eng": "forget", "kor": "잊다"},
    {"eng": "fresh", "kor": "신선한"},
    {"eng": "glass", "kor": "유리잔, 유리"},
    {"eng": "glove", "kor": "장갑"},
    {"eng": "grow", "kor": "자라다"},
    {"eng": "happy", "kor": "행복한"},
    {"eng": "heavy", "kor": "무거운"},
    {"eng": "hobby", "kor": "취미"},
    {"eng": "hurry", "kor": "서두르다"},
    {"eng": "invite", "kor": "초대하다"},
    {"eng": "kitchen", "kor": "부엌"},
    {"eng": "lazy", "kor": "게으른"},
    {"eng": "lesson", "kor": "수업, 교훈"},
    {"eng": "lonely", "kor": "외로운"},
    {"eng": "market", "kor": "시장"},
    {"eng": "meal", "kor": "식사"},
    {"eng": "medicine", "kor": "약"},
    {"eng": "morning", "kor": "아침"},
    {"eng": "mountain", "kor": "산"},
    {"eng": "museum", "kor": "박물관"},
    {"eng": "neighbor", "kor": "이웃"},
    {"eng": "noise", "kor": "소음"},
    {"eng": "ocean", "kor": "바다"},
    {"eng": "painting", "kor": "그림"},
    {"eng": "pencil", "kor": "연필"},
    {"eng": "pocket", "kor": "주머니"},
    {"eng": "quiet", "kor": "조용한"},
    {"eng": "remember", "kor": "기억하다"},
    {"eng": "rich", "kor": "부유한"},
    {"eng": "sad", "kor": "슬픈"},
    {"eng": "salt", "kor": "소금"},
    {"eng": "sauce", "kor": "소스"},
    {"eng": "shoe", "kor": "신발"},
    {"eng": "sick", "kor": "아픈"},
    {"eng": "sleep", "kor": "자다"},
    {"eng": "soap", "kor": "비누"},
    {"eng": "sometimes", "kor": "가끔"},
    {"eng": "spoon", "kor": "숟가락"},
    {"eng": "stairs", "kor": "계단"},
    {"eng": "sweet", "kor": "달콤한"},
    {"eng": "thirsty", "kor": "목마른"},
    {"eng": "tired", "kor": "피곤한"},
    {"eng": "towel", "kor": "수건"},
    {"eng": "wallet", "kor": "지갑"},
    {"eng": "weather", "kor": "날씨"},
    {"eng": "wet", "kor": "젖은"},
]

# 중학교 2학년 수준 단어 데이터셋
MIDDLE2_WORD_DATABASE = [
    {"eng": "ability", "kor": "능력"},
    {"eng": "accident", "kor": "사고"},
    {"eng": "action", "kor": "행동"},
    {"eng": "advantage", "kor": "장점, 이점"},
    {"eng": "afraid", "kor": "두려워하는"},
    {"eng": "allergy", "kor": "알레르기"},
    {"eng": "amazing", "kor": "놀라운"},
    {"eng": "anger", "kor": "분노"},
    {"eng": "apologize", "kor": "사과하다"},
    {"eng": "attention", "kor": "주의, 관심"},
    {"eng": "award", "kor": "상"},
    {"eng": "awkward", "kor": "어색한"},
    {"eng": "basic", "kor": "기본의"},
    {"eng": "battery", "kor": "건전지"},
    {"eng": "belief", "kor": "믿음"},
    {"eng": "capable", "kor": "유능한"},
    {"eng": "castle", "kor": "성"},
    {"eng": "cause", "kor": "원인, 야기하다"},
    {"eng": "chew", "kor": "씹다"},
    {"eng": "cliff", "kor": "절벽"},
    {"eng": "competition", "kor": "대회, 경쟁"},
    {"eng": "confident", "kor": "자신감 있는"},
    {"eng": "crack", "kor": "금, 갈라지다"},
    {"eng": "damage", "kor": "손상(시키다)"},
    {"eng": "deliver", "kor": "배달하다"},
    {"eng": "depend", "kor": "의존하다"},
    {"eng": "desert", "kor": "사막"},
    {"eng": "diet", "kor": "식단, 다이어트"},
    {"eng": "disaster", "kor": "재난"},
    {"eng": "drought", "kor": "가뭄"},
    {"eng": "economy", "kor": "경제"},
    {"eng": "effort", "kor": "노력"},
    {"eng": "emergency", "kor": "비상사태"},
    {"eng": "equal", "kor": "같은, 동등한"},
    {"eng": "error", "kor": "실수"},
    {"eng": "expand", "kor": "확장하다"},
    {"eng": "factory", "kor": "공장"},
    {"eng": "fault", "kor": "잘못, 탓"},
    {"eng": "feature", "kor": "특징"},
    {"eng": "foreign", "kor": "외국의"},
    {"eng": "fuel", "kor": "연료"},
    {"eng": "habit", "kor": "습관"},
    {"eng": "hero", "kor": "영웅"},
    {"eng": "hesitate", "kor": "망설이다"},
    {"eng": "honor", "kor": "명예"},
    {"eng": "ignore", "kor": "무시하다"},
    {"eng": "income", "kor": "수입"},
    {"eng": "independent", "kor": "독립적인"},
    {"eng": "industry", "kor": "산업"},
    {"eng": "insect", "kor": "곤충"},
    {"eng": "interest", "kor": "흥미, 관심"},
    {"eng": "island", "kor": "섬"},
    {"eng": "judge", "kor": "판단하다, 판사"},
    {"eng": "labor", "kor": "노동"},
    {"eng": "layer", "kor": "층"},
    {"eng": "leisure", "kor": "여가"},
    {"eng": "mirror", "kor": "거울"},
    {"eng": "negative", "kor": "부정적인"},
    {"eng": "obvious", "kor": "분명한"},
    {"eng": "occur", "kor": "일어나다"},
    {"eng": "organ", "kor": "장기, 기관"},
    {"eng": "pattern", "kor": "무늬, 패턴"},
    {"eng": "peaceful", "kor": "평화로운"},
    {"eng": "permit", "kor": "허락하다"},
    {"eng": "pleasure", "kor": "기쁨"},
    {"eng": "pretend", "kor": "가장하다"},
    {"eng": "profit", "kor": "이익"},
    {"eng": "quality", "kor": "품질"},
    {"eng": "region", "kor": "지역"},
    {"eng": "religion", "kor": "종교"},
    {"eng": "rescue", "kor": "구조하다"},
    {"eng": "resource", "kor": "자원"},
    {"eng": "routine", "kor": "일상, 틀에 박힌"},
    {"eng": "sculpture", "kor": "조각"},
    {"eng": "security", "kor": "보안"},
    {"eng": "shadow", "kor": "그림자"},
    {"eng": "sincere", "kor": "진심 어린"},
    {"eng": "spacious", "kor": "넓은"},
    {"eng": "statue", "kor": "동상"},
    {"eng": "strategy", "kor": "전략"},
    {"eng": "structure", "kor": "구조"},
    {"eng": "surface", "kor": "표면"},
    {"eng": "tension", "kor": "긴장"},
    {"eng": "vehicle", "kor": "차량"},
    {"eng": "verify", "kor": "확인하다"},
    {"eng": "vital", "kor": "필수적인"},
    {"eng": "weapon", "kor": "무기"},
    {"eng": "witness", "kor": "목격자"},
]

# 중학교 3학년 수준 단어 데이터셋
MIDDLE3_WORD_DATABASE = [
    {"eng": "admire", "kor": "존경하다, 감탄하다"},
    {"eng": "advice", "kor": "조언"},
    {"eng": "allow", "kor": "허락하다"},
    {"eng": "ancient", "kor": "고대의"},
    {"eng": "argue", "kor": "논쟁하다"},
    {"eng": "arrive", "kor": "도착하다"},
    {"eng": "avoid", "kor": "피하다"},
    {"eng": "beauty", "kor": "아름다움"},
    {"eng": "breath", "kor": "숨, 호흡"},
    {"eng": "careless", "kor": "부주의한"},
    {"eng": "celebrate", "kor": "축하하다"},
    {"eng": "century", "kor": "세기, 100년"},
    {"eng": "certain", "kor": "확실한"},
    {"eng": "character", "kor": "성격, 등장인물"},
    {"eng": "climate", "kor": "기후"},
    {"eng": "collect", "kor": "모으다"},
    {"eng": "common", "kor": "흔한, 공통의"},
    {"eng": "compare", "kor": "비교하다"},
    {"eng": "complete", "kor": "완료하다, 완전한"},
    {"eng": "confuse", "kor": "혼란스럽게 하다"},
    {"eng": "custom", "kor": "관습"},
    {"eng": "danger", "kor": "위험"},
    {"eng": "define", "kor": "정의하다"},
    {"eng": "delicious", "kor": "맛있는"},
    {"eng": "describe", "kor": "묘사하다"},
    {"eng": "develop", "kor": "발달하다, 개발하다"},
    {"eng": "disappear", "kor": "사라지다"},
    {"eng": "discover", "kor": "발견하다"},
    {"eng": "education", "kor": "교육"},
    {"eng": "effect", "kor": "영향, 결과"},
    {"eng": "emotion", "kor": "감정"},
    {"eng": "encourage", "kor": "격려하다"},
    {"eng": "environment", "kor": "환경"},
    {"eng": "excellent", "kor": "훌륭한"},
    {"eng": "experience", "kor": "경험"},
    {"eng": "explain", "kor": "설명하다"},
    {"eng": "express", "kor": "표현하다"},
    {"eng": "familiar", "kor": "익숙한"},
    {"eng": "freedom", "kor": "자유"},
    {"eng": "gather", "kor": "모이다, 모으다"},
    {"eng": "generous", "kor": "관대한"},
    {"eng": "honest", "kor": "정직한"},
    {"eng": "imagine", "kor": "상상하다"},
    {"eng": "improve", "kor": "향상시키다"},
    {"eng": "include", "kor": "포함하다"},
    {"eng": "increase", "kor": "증가하다"},
    {"eng": "injure", "kor": "다치게 하다"},
    {"eng": "instead", "kor": "대신에"},
    {"eng": "introduce", "kor": "소개하다"},
    {"eng": "invent", "kor": "발명하다"},
    {"eng": "journey", "kor": "여행"},
    {"eng": "knowledge", "kor": "지식"},
    {"eng": "lecture", "kor": "강의"},
    {"eng": "manage", "kor": "관리하다, 해내다"},
    {"eng": "memory", "kor": "기억"},
    {"eng": "mention", "kor": "언급하다"},
    {"eng": "nervous", "kor": "긴장한"},
    {"eng": "obey", "kor": "복종하다"},
    {"eng": "opportunity", "kor": "기회"},
    {"eng": "passenger", "kor": "승객"},
    {"eng": "pollution", "kor": "오염"},
    {"eng": "polite", "kor": "예의 바른"},
    {"eng": "possible", "kor": "가능한"},
    {"eng": "prepare", "kor": "준비하다"},
    {"eng": "prevent", "kor": "막다, 예방하다"},
    {"eng": "protect", "kor": "보호하다"},
    {"eng": "provide", "kor": "제공하다"},
    {"eng": "purpose", "kor": "목적"},
    {"eng": "realize", "kor": "깨닫다"},
    {"eng": "recycle", "kor": "재활용하다"},
    {"eng": "reduce", "kor": "줄이다"},
    {"eng": "reject", "kor": "거절하다"},
    {"eng": "remove", "kor": "제거하다"},
    {"eng": "repair", "kor": "수리하다"},
    {"eng": "respect", "kor": "존경(하다)"},
    {"eng": "responsible", "kor": "책임이 있는"},
    {"eng": "reveal", "kor": "드러내다"},
    {"eng": "secret", "kor": "비밀"},
    {"eng": "signal", "kor": "신호"},
    {"eng": "suggest", "kor": "제안하다"},
    {"eng": "suspect", "kor": "의심하다"},
    {"eng": "thorough", "kor": "철저한"},
    {"eng": "tradition", "kor": "전통"},
    {"eng": "trust", "kor": "신뢰(하다)"},
    {"eng": "unique", "kor": "독특한"},
    {"eng": "valuable", "kor": "귀중한"},
    {"eng": "wisdom", "kor": "지혜"},
]

# 이 레벨부터 시간 제한 없음 (단어 수준은 get_level_tier 참고)
ADVANCED_LEVEL = 10
TIME_LIMIT_SEC = 20
MAX_HINTS = 5
LOAN_HINT_CHANCE = 1 / 3

def get_level_tier(level):
    """레벨에 맞는 (학년 라벨, 단어 데이터셋) 반환. 라벨이 None이면 초급"""
    if level >= 20:
        return "중학교 3학년", MIDDLE3_WORD_DATABASE
    if level >= 15:
        return "중학교 2학년", MIDDLE2_WORD_DATABASE
    if level >= ADVANCED_LEVEL:
        return "중학교 1학년", MIDDLE1_WORD_DATABASE
    return None, WORD_DATABASE

# 세션 상태 초기화
def init_session():
    if "stage" not in st.session_state:
        st.session_state.stage = "start"  # start, learning, quiz, result
    if "words" not in st.session_state:
        st.session_state.words = []
    if "current_quiz_idx" not in st.session_state:
        st.session_state.current_quiz_idx = 0
    if "answers" not in st.session_state:
        st.session_state.answers = []
    if "quiz_words" not in st.session_state:
        st.session_state.quiz_words = []
    if "level" not in st.session_state:
        st.session_state.level = 1
    if "timer_started" not in st.session_state:
        st.session_state.timer_started = False
    if "quiz_start_time" not in st.session_state:
        st.session_state.quiz_start_time = None
    if "current_question_start_time" not in st.session_state:
        st.session_state.current_question_start_time = None
    if "question_types" not in st.session_state:
        st.session_state.question_types = []
    if "problem_data" not in st.session_state:
        st.session_state.problem_data = {}

init_session()

def set_background_color(success, level):
    """성공 여부와 레벨에 따라 배경색 설정"""
    if success:
        # 성공: 초록색
        bg_color = "#2ECC71"
        text_color = "white"
    else:
        if level < 5:
            # 레벨 5 미만 실패: 지옥 배경 (어두운 빨강)
            bg_color = "#8B0000"
            text_color = "white"
        else:
            # 레벨 5 이상 실패: 정상 배경
            bg_color = "#F0F0F0"
            text_color = "black"

    st.markdown(f"""
    <style>
        .stApp {{
            background-color: {bg_color};
        }}
        .result-text {{
            color: {text_color};
        }}
    </style>
    """, unsafe_allow_html=True)

def start_page():
    """시작 페이지"""
    st.title("📚 영어 단어 외우기")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("난이도 설정")
        level = st.slider("레벨을 선택하세요 (1-20)", 1, 20, 1)
        st.session_state.level = level

        # 난이도에 따라 단어 개수 결정
        num_words = min(5 + level, 15)
        st.info(f"📝 총 {num_words}개의 단어를 학습하게 됩니다.")
        label, _ = get_level_tier(level)
        if label:
            st.caption(f"{label} 수준 단어 · 시간 제한 없음")

    with col2:
        st.subheader("📊 게임 규칙")
        if level < ADVANCED_LEVEL:
            time_rule = f"4. **{TIME_LIMIT_SEC}초 내에 영어 단어 입력**"
        else:
            time_rule = "4. **시간 제한 없이 영어 단어 입력**"
        st.markdown(f"""
        1. 단어 외우기 버튼을 클릭
        2. 화면에 표시된 단어들을 외우기
        3. AI가 낸 문제 맞추기
        {time_rule}
        5. **80% 이상 정답하면 성공!**

        **문제 유형:**
        - 🔤 한글 뜻을 보고 영어 단어 맞추기
        - 📝 예문의 빈칸 채우기
        """)

    if st.button("🎯 단어 외우기 시작", use_container_width=True, key="start_btn"):
        num_words = min(5 + st.session_state.level, 15)
        _, pool = get_level_tier(st.session_state.level)
        st.session_state.words = random.sample(pool, min(num_words, len(pool)))
        st.session_state.stage = "learning"
        st.rerun()

def learning_page():
    """단어 학습 페이지"""
    st.title("📖 단어 학습하기")
    st.subheader(f"난이도: {st.session_state.level} | 단어 개수: {len(st.session_state.words)}")

    if st.session_state.level < ADVANCED_LEVEL:
        st.info(f"⏱️ 이 단어들을 잘 외우세요. 다음 화면에서 {TIME_LIMIT_SEC}초 안에 문제를 풀어야 합니다!")
    else:
        st.info("⏱️ 이 단어들을 잘 외우세요. 다음 화면에서는 시간 제한 없이 문제를 풀 수 있습니다.")

    # 단어 표시
    cols = st.columns(2)
    for idx, word in enumerate(st.session_state.words):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style='border: 2px solid #3498DB; padding: 15px; margin: 10px 0; border-radius: 10px;'>
                <h3 style='color: #3498DB; margin: 0;'>{word["eng"].upper()}</h3>
                <p style='color: #555; margin: 5px 0;'>{word["kor"]}</p>
            </div>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ 외웠습니다 - 문제 풀기", use_container_width=True):
            st.session_state.quiz_words = st.session_state.words.copy()
            random.shuffle(st.session_state.quiz_words)
            st.session_state.current_quiz_idx = 0
            st.session_state.answers = []

            # 복불복으로 문제 유형 결정 (뜻 맞추기 vs 예문 채우기)
            num_words = len(st.session_state.quiz_words)
            st.session_state.question_types = random.choices([0, 1], k=num_words)
            st.session_state.problem_data = {}
            st.session_state.hints_left = MAX_HINTS
            st.session_state.hint_positions = {}
            st.session_state.hint_loans = {}

            st.session_state.stage = "quiz"
            st.session_state.quiz_start_time = time.time()
            st.session_state.current_question_start_time = time.time()
            st.rerun()

    with col2:
        if st.button("🔄 다시 보기", use_container_width=True):
            st.session_state.stage = "start"
            st.rerun()

def generate_sentence_problem(word_eng, word_kor):
    """영어 예문과 한국어 해석 생성"""
    prompt = f"""Create one simple English sentence that uses the word "{word_eng}" ({word_kor} in Korean).
Use the word exactly as written, without changing its form.
The Korean translation must include the Korean word "{word_kor}".

Output exactly two lines and nothing else:
English: [the English sentence]
Korean: [the natural Korean translation]"""

    return ask_ai(prompt)

def quiz_page():
    """문제 풀이 페이지"""
    st.title("🧠 문제 풀기")

    if st.session_state.current_quiz_idx < len(st.session_state.quiz_words):
        current_word = st.session_state.quiz_words[st.session_state.current_quiz_idx]
        total = len(st.session_state.quiz_words)
        current = st.session_state.current_quiz_idx + 1
        question_type = st.session_state.question_types[st.session_state.current_quiz_idx]

        # 진행 상황 표시
        progress = current / total
        st.progress(progress)
        st.markdown(f"<h3>문제 {current}/{total}</h3>", unsafe_allow_html=True)

        timed = st.session_state.level < ADVANCED_LEVEL
        if timed:
            # 각 문제마다 별도의 타이머
            current_elapsed = time.time() - st.session_state.current_question_start_time
            time_left = max(0, TIME_LIMIT_SEC - current_elapsed)

            # 시간이 지나면 자동으로 다음 문제로
            if time_left <= 0:
                st.session_state.answers.append({
                    "correct": False,
                    "user_answer": "시간초과",
                    "correct_answer": current_word["eng"],
                    "question_type": question_type
                })
                st.session_state.current_quiz_idx += 1
                st.session_state.current_question_start_time = time.time()
                st.rerun()

            st.markdown(f"⏱️ **남은 시간: {time_left:.1f}초**")

        # 문제 생성 및 표시
        if question_type == 0:
            # 유형 0: 한글 뜻을 보고 영어 단어 맞추기
            st.markdown(f"""
            <div style='background-color: #E8F4F8; padding: 20px; border-radius: 10px; margin: 20px 0;'>
                <h4>📚 한글 뜻 보고 영어 단어 맞추기:</h4>
                <p style='font-size: 16px;'>뜻: <strong>{current_word["kor"]}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            prompt_text = "👇 영어 단어를 입력하세요:"
        else:
            # 유형 1: 영어 예문과 해석을 보여주고 뜻에 맞는 영어 단어 맞추기 (예문은 한 번만 생성해서 재사용)
            problem_key = f"problem_{current_word['eng']}_{question_type}"
            target_kor = current_word["kor"].split(",")[0].strip()
            if problem_key not in st.session_state.problem_data:
                st.session_state.problem_data[problem_key] = generate_sentence_problem(current_word["eng"], target_kor)
            st.markdown(f"""
            <div style='background-color: #FFF8E8; padding: 20px; border-radius: 10px; margin: 20px 0;'>
                <h4>📝 예문 보고 영어 단어 맞추기:</h4>
                <p style='font-size: 16px; white-space: pre-wrap;'>{st.session_state.problem_data[problem_key]}</p>
            </div>
            """, unsafe_allow_html=True)
            prompt_text = f"👇 해석의 '{target_kor}'에 해당하는 영어 단어를 입력하세요:"

        # 힌트로 공개된 철자와 외래어 표시
        revealed = st.session_state.hint_positions.get(st.session_state.current_quiz_idx, [])
        if revealed:
            masked = " ".join(c.upper() if i in revealed else "_" for i, c in enumerate(current_word["eng"]))
            st.markdown(f"💡 **철자 힌트:** `{masked}`")
        loan_hint = st.session_state.hint_loans.get(st.session_state.current_quiz_idx)
        if loan_hint:
            st.markdown(f"💡 **외래어 힌트:** {loan_hint}")

        # 답변 입력
        user_answer = st.text_input(prompt_text, key=f"answer_{current}")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("✅ 제출", use_container_width=True):
                is_correct = user_answer.lower().strip() == current_word["eng"].lower()
                st.session_state.answers.append({
                    "correct": is_correct,
                    "user_answer": user_answer,
                    "correct_answer": current_word["eng"],
                    "question_type": question_type
                })
                st.session_state.current_quiz_idx += 1
                st.session_state.current_question_start_time = time.time()
                st.rerun()

        with col2:
            if st.button("⏭️ 건너뛰기", use_container_width=True):
                st.session_state.answers.append({
                    "correct": False,
                    "user_answer": "건너뜀",
                    "correct_answer": current_word["eng"],
                    "question_type": question_type
                })
                st.session_state.current_quiz_idx += 1
                st.session_state.current_question_start_time = time.time()
                st.rerun()

        with col3:
            idx = st.session_state.current_quiz_idx
            hints_left = st.session_state.hints_left
            revealed = st.session_state.hint_positions.get(idx, [])
            letters_left = len(revealed) < len(current_word["eng"])
            loan = current_word.get("loan")
            loan_available = loan is not None and idx not in st.session_state.hint_loans
            can_hint = hints_left > 0 and (letters_left or loan_available)
            if st.button(f"💡 힌트 ({hints_left}/{MAX_HINTS})", use_container_width=True, disabled=not can_hint):
                if loan_available and (not letters_left or random.random() < LOAN_HINT_CHANCE):
                    st.session_state.hint_loans[idx] = loan
                else:
                    hidden = [i for i in range(len(current_word["eng"])) if i not in revealed]
                    st.session_state.hint_positions[idx] = revealed + [random.choice(hidden)]
                st.session_state.hints_left -= 1
                st.rerun()

        # 타이머 자동 업데이트 (0.5초마다)
        if timed:
            time.sleep(0.5)
            st.rerun()
    else:
        st.session_state.stage = "result"
        st.rerun()

def result_page():
    """결과 페이지"""
    # 점수 계산
    correct_count = sum(1 for a in st.session_state.answers if a["correct"])
    total_count = len(st.session_state.answers)
    score_percentage = (correct_count / total_count * 100) if total_count > 0 else 0
    success = score_percentage >= 80

    # 배경색 설정
    set_background_color(success, st.session_state.level)

    st.title("📊 결과")

    # 점수 표시
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("맞은 개수", f"{correct_count}/{total_count}")
    with col2:
        st.metric("정답률", f"{score_percentage:.1f}%")
    with col3:
        st.metric("현재 레벨", st.session_state.level)

    st.markdown("---")

    # 결과에 따른 메시지
    if success:
        st.success("🎉 축하합니다! 성공했습니다!")

        # AI가 수준을 파악하고 다음 레벨 추천
        feedback_prompt = f"""학생이 영어 단어 학습 테스트를 했습니다.
- 현재 레벨: {st.session_state.level}
- 정답률: {score_percentage:.1f}%
- 맞은 개수: {correct_count}/{total_count}

학생의 수준을 파악하고, 다음 레벨을 추천해주세요.
- 추천 이유를 간단히 설명하세요 (한국어)
- 격려의 한마디를 해주세요"""

        recommendation = ask_ai(feedback_prompt)
        st.info(recommendation)
    else:
        st.error("😢 실패했습니다. 다시 도전해보세요!")

        if st.session_state.level < 5:
            st.markdown("""
            <div style='background-color: #FFD700; padding: 15px; border-radius: 10px; margin: 20px 0;'>
                <h4>💡 팁:</h4>
                <p>현재 난이도에서 더 연습하거나 낮은 레벨부터 시작해보세요!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            feedback_prompt = f"""학생이 영어 단어 학습 테스트에서 실패했습니다.
- 현재 레벨: {st.session_state.level}
- 정답률: {score_percentage:.1f}%
- 맞은 개수: {correct_count}/{total_count}

학생을 격려하고, 더 나은 성적을 위한 조언을 해주세요. (한국어)"""

            encouragement = ask_ai(feedback_prompt)
            st.info(encouragement)

    # 상세 결과
    st.subheader("📋 문제별 풀이 결과")
    for idx, answer in enumerate(st.session_state.answers):
        status = "✅" if answer["correct"] else "❌"
        color = "#90EE90" if answer["correct"] else "#FFB6C6"
        qtype = "🔤 뜻 맞추기" if answer.get("question_type", 0) == 0 else "📝 예문 채우기"

        st.markdown(f"""
        <div style='background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;'>
            <p><strong>{status} 문제 {idx+1} ({qtype})</strong></p>
            <p>정답: <strong>{answer["correct_answer"]}</strong></p>
            <p>당신의 답: <strong>{answer["user_answer"]}</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 다시 시작 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 다시 도전", use_container_width=True):
            st.session_state.stage = "start"
            st.rerun()

    with col2:
        if st.button("📊 대시보드로 돌아가기", use_container_width=True):
            st.session_state.stage = "start"
            st.rerun()

# 메인 실행
if __name__ == "__main__":
    if st.session_state.stage != "start":
        if st.button("🏠 홈으로", key="home_btn"):
            st.session_state.stage = "start"
            st.rerun()

    if st.session_state.stage == "start":
        start_page()
    elif st.session_state.stage == "learning":
        learning_page()
    elif st.session_state.stage == "quiz":
        quiz_page()
    elif st.session_state.stage == "result":
        result_page()
