import random
import streamlit as st
import yt_dlp

# 웹페이지 기본 설정
st.set_page_config(
    page_title="서양음악사 청음 테스트", page_icon="🎵", layout="centered"
)


# =========================================================================
# 58곡 전곡 데이터 리스트
# =========================================================================
@st.cache_data
def get_music_list():
    return [
        [
            "Schubert <Erlkönig> (마왕)",
            "https://youtu.be/JS91p-vmSf0?si=rrO4kgNvBSHCNcKM",
            0,
        ],
        [
            "Schumann <Widmung> (헌정)",
            "https://youtu.be/UXDz0aByZVc?si=lYV30_7MVEG84A5_",
            0,
        ],
        [
            "Schumann <Träumerei> (꿈)",
            "https://youtu.be/6z82w0l6kwE?si=8-w8t43qNT58pEx9",
            0,
        ],
        [
            "Mendelssohn ‘Songs without Words’",
            "https://youtu.be/Nuq_gGVTg2I?si=ALo_HsGlvupm6yUg",
            0,
        ],
        [
            "Mendelssohn Violin Concerto in E Minor, 1st Mvt.",
            "https://youtu.be/SDwKJ6bBXEA?si=sOn_Gf6DduE7_C9S",
            0,
        ],
        [
            "Paganini Caprice No. 24",
            "https://youtu.be/loOuh543gaY?si=vL_WNxEE7qS0YecM",
            0,
        ],
        [
            "Rossini opera <William Tell> overture finale",
            "https://youtu.be/c7O91GDWGPU?si=wwxoKehQDVZSwb0F",
            0,
        ],
        [
            "Chopin Nocturne Op. 9 No. 2 (23초부터)",
            "https://youtu.be/8YQJWHCenJU?si=8t5VMLCQyiSg3Yv8",
            23,
        ],
        [
            "Chopin Polonaise in A-flat Major, Op. 53 ‘Heroic’",
            "https://youtu.be/d3IKMiv8AHw?si=Mrix2Kd9r8pzTzN8",
            0,
        ],
        [
            "Liszt ‘La Campanella’ (Paganini Etude No. 3)",
            "https://youtu.be/M0U73NRSIkw?si=oR8XxjqGybk2YVXu",
            0,
        ],
        [
            "Liszt Transcendental Etude No. 4 ‘Mazeppa’",
            "https://youtu.be/Uk6qyGFYJ9M?si=v_Gw48RQ3V5ZRYQN",
            0,
        ],
        [
            "Liszt Paganini Etude No. 6",
            "https://youtu.be/rQndTrMpkz8?si=Uh5-ojY4NbAr1rNI",
            0,
        ],
        [
            "Berlioz <Symphonie Fantastique> 4th Mvt.",
            "https://youtu.be/roX70PAu3oA?si=iMRL0guNH2As9sFo",
            0,
        ],
        [
            "Brahms Symphony No 3, 3rd Mvt.",
            "https://youtu.be/2tB2SLLnPZg?si=ZCL0RPrhIysPY4ef",
            0,
        ],
        [
            "Brahms Hungarian Dance No. 5",
            "https://youtu.be/Nzo3atXtm54?si=l9aT001cU7CxTv6C",
            0,
        ],
        [
            "Saint-Saëns ‘Swan’ (from <The Carnival of the Animals>)",
            "https://youtu.be/Wpk7Kx4dt-U?si=SAVCziuzVfvxoC0c",
            0,
        ],
        [
            "Saint-Saëns ‘Tortoise’ (from <The Carnival of the Animals>)",
            "https://youtu.be/DfNgNTBDNUs?si=eIUTEpxaJeZnK6aU",
            0,
        ],
        [
            "Offenbach opera <Orpheus in the Underworld> overture (7분부터)",
            "https://youtu.be/vEnW5_GTooI?si=I8oZVyWc2UvIS5YV",
            420,
        ],
        [
            "Saint-Saëns ‘The Aquarium’ (from <The Carnival of the Animals>)",
            "https://youtu.be/a4lmvXYRfa4?si=Oe564Z2d07GYCXBU",
            0,
        ],
        [
            "Bizet opera <Carmen> ‘Toreador’ (투우사의 노래)",
            "https://youtu.be/CoV2YOjFowY?si=1hn9ZSaTF8FSEqpH",
            0,
        ],
        [
            "Bizet opera <Carmen> ‘Gypsy’",
            "https://youtu.be/JvjjoZFt26I?si=ctEsFvUoog-GVmJq",
            0,
        ],
        [
            "Leoncavallo opera <Pagliacci> ‘Vesti la giubba’ (의상을 입어라)",
            "https://youtu.be/Z0PMq4XGtZ4?si=aFEuc-piN-N1R0V7",
            0,
        ],
        [
            "Mascagni opera <Cavalleria Rusticana> intermezzo",
            "https://youtu.be/3N4uXfnH2aA?si=k7giCipOJcc4WQaM",
            0,
        ],
        [
            "Verdi <Requiem> ‘Dies Irae’",
            "https://youtu.be/ZcA-KuvHeVE?si=ugrD-QJ-ZwbaKbcc",
            0,
        ],
        [
            "Verdi opera <Rigoletto> ‘La Donna e mobile’ (여자의 마음)",
            "https://youtu.be/8A3zetSuYRg?si=DJw9514L78M1Manz",
            0,
        ],
        [
            "Puccini opera <Turandot> ‘Nessun dorma’ (아무도 잠들지 말라)",
            "https://youtu.be/M3ecaM3UjAA?si=RpRx03TwklH5_XkI",
            0,
        ],
        [
            "Puccini opera <Gianni Scchicci> ‘O mio babbino caro’ (사랑하는 나의 아버지)",
            "https://youtu.be/OrqYQoAIj_0?si=gxmQd9BmRw23uaI3",
            0,
        ],
        [
            "Dvorak Symphony No. 9 ‘From the New World’ 4th Mvt.",
            "https://youtu.be/89jOPAGJq-M?si=tiU5MUihec9TWaG5",
            0,
        ],
        [
            "Grieg Piano Concerto in A Minor, 1st Mvt.",
            "https://youtu.be/I1Yoyz6_Los?si=qJJ9Jr8GjuOwTPI_",
            0,
        ],
        [
            "Grieg <Peer Gynt> ‘Morning Mood’",
            "https://youtu.be/Gf39OSAa6xc?si=AMNQTjvhhn20RjzU",
            0,
        ],
        [
            "Sibelius Violin Concerto in D Minor, 3rd Mvt. (25분 10초부터)",
            "https://youtu.be/gpS_u5RvMpM?si=AtCbiggX7CRPMbfW",
            1510,
        ],
        [
            "Rimsky-Korsakov ‘The Flight of the Bumblebee’",
            "https://youtu.be/MW8asBxO4oI?si=Na6G0pe-RAugbdeQ",
            0,
        ],
        [
            "Mussorgsky <Pictures at an Exhibition> ‘Baba Yaga’, ‘Great Gate of Kiev’ (3분 20초부터)",
            "https://youtu.be/kZkoW1Ta3ew?si=BEmrf4cJaKh57MmA",
            200,
        ],
        [
            "Tchaikovsky Piano Concerto No. 1, 1st Mvt.",
            "https://youtu.be/ItSJ_woWnmk?si=fKRRMyIQkYO0oQA4",
            0,
        ],
        [
            "Tchaikovsky Symphony No. 6 ‘Pathetique’, 1st Mvt. (4분 50초부터)",
            "https://www.youtube.com/watch?v=oEW0cXVoGo0",
            290,
        ],
        [
            "Tchaikovsky <The Nutcracker> ‘Waltz of the Flowers’",
            "https://youtu.be/LKcZL8q1eBw?si=s15yZ_hlN5YlKi5x",
            0,
        ],
        [
            "Rachmaninoff Symphony No. 2, 3rd Mvt.",
            "https://youtu.be/21MHVIcg1HY?si=C8j_YwlyvjZMBL1_",
            0,
        ],
        [
            "Rachmaninoff Piano Concerto No. 3, 3rd Mvt. finale (39분부터)",
            "https://youtu.be/DPJL488cfRw?feature=shared",
            2340,
        ],
        [
            "Rachmaninoff <Rhapsody on a Theme of Paganini> 주제 + 제18변주 (16분 20초부터)",
            "https://youtu.be/3vaJ91DuDww?si=bKci5YQ-b0VdzW_-",
            980,
        ],
        [
            "Wagner <Die Walküre> ‘The Ride of the Valkyries’",
            "https://youtu.be/xeRwBiu4wfQ?si=w6HqqS9NQkiaLids",
            0,
        ],
        [
            "Wagner <Lohengrin> ‘Bridal Chorus’ (3분 20초부터)",
            "https://youtu.be/J2lX86w-pT4?si=M3Y8t_5-ACM_v63T",
            200,
        ],
        [
            "Mahler Symphony No. 5, 4th Mvt.",
            "https://youtu.be/Bj6KLv7kv2Q?si=O2OxPh6iMDGnY_zh",
            0,
        ],
        [
            "Richard Strauss <Also Sprach Zarathustra>",
            "https://youtu.be/GfwAPg4rQQE?feature=shared",
            0,
        ],
        [
            "Johann Strauss <Radetzky March>",
            "https://youtu.be/xhEGMSOIptw?si=cQ8yYVaOWTV7MxmR",
            0,
        ],
        [
            "Johann Strauss, Jr. <Frühlingsstimmen Waltz> (봄의 소리 왈츠)",
            "https://youtu.be/TF0XSkb7TyM?si=zkcbhGx8CPU13siI",
            0,
        ],
        [
            "Elgar <Salut d’amour> (사랑의 인사)",
            "https://youtu.be/ysG2AiEFeRw?si=YCKksDGuFiJ-Wb3C",
            0,
        ],
        [
            "Tarrega <Recuerdos de la Alhambra> (알람브라 궁전의 추억)",
            "https://youtu.be/EQGBbLBShzk?si=KFBsCP6JCQLzIgw_",
            0,
        ],
        [
            "Debussy ‘Clair de lune’ (달빛)",
            "https://youtu.be/U3u4pQ4WKOk?si=WK6Gcs5bG1UoRLW1",
            0,
        ],
        [
            "Debussy <Prelude to the Afternoon of a Faun> (목신의 오후 전주곡)",
            "https://youtu.be/9_7loz-HWUM?si=M0KRL-8uRxBWJxX4",
            0,
        ],
        ["Ravel <Bolero>", "https://youtu.be/dovA8PuWGLU?si=_FlYYQbSc-qKx4ck", 0],
        [
            "Ravel <Jeux d’eau> (물의 유희)",
            "https://youtu.be/C5kufJw5n3U?si=2nrob-3eaeQ8Aera",
            0,
        ],
        [
            "Stravinsky <The Rite of Spring>",
            "https://youtu.be/sPpq44uEyXo?feature=shared",
            0,
        ],
        [
            "Prokofiev <Romeo and Juliet>",
            "https://youtu.be/SyDo3h1Tu7c?si=9DBfUroIjznsXVI4",
            0,
        ],
        [
            "Bartõk <Romanian Folk Dances> (5분 40초부터)",
            "https://youtu.be/Z50Ooqv1GFg?si=fAPEXl4v9PYyj_LO",
            340,
        ],
        [
            "Gershwin <Rhapsody in Blue>",
            "https://youtu.be/cH2PH0auTUU?si=wM_K6FPtYzAgjQuR",
            0,
        ],
        [
            "Gershwin opera <Porgy and Bess> ‘Summertime’",
            "https://youtu.be/RyadsHUBpWc?si=xxKA09h413zwZQH1",
            0,
        ],
        [
            "Shostakovich Waltz No. 2",
            "https://youtu.be/mmCnQDUSO4I?si=dyNxSa4oa8OMel4p",
            0,
        ],
        [
            "Piazzolla <Libertango>",
            "https://youtu.be/t83XjF04r80?si=1_podGTr8-MIOQF-",
            0,
        ],
    ]


def get_audio_stream_url(youtube_url):
    """유튜브에서 실제 오디오 스트림 추출"""
    ydl_opts = {"format": "bestaudio/best", "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info["url"]


# 상태 초기화 함수
if "quiz_pool" not in st.session_state:
    pool = get_music_list().copy()
    random.shuffle(pool)
    st.session_state.quiz_pool = pool
    st.session_state.current_index = 0
    st.session_state.show_answer = False
    st.session_state.audio_url = None

# --- UI 그리기 ---
st.title("🎵 서양음악사 블라인드 청음 테스트")
st.write("유튜브 화면 없이 오직 소리로만 곡을 맞춰보세요! (총 58곡)")
st.markdown("---")

pool = st.session_state.quiz_pool
idx = st.session_state.current_index

if idx < len(pool):
    title, url, start_sec = pool[idx]

    st.subheader(f"📝 문제 {idx + 1} / {len(pool)}")

    # 실시간 스트리밍 URL 가져오기 (필요할 때만 실행)
    if st.session_state.audio_url is None:
        with st.spinner("유튜브 음원을 분석 중입니다... 잠시만 기다려주세요."):
            try:
                st.session_state.audio_url = get_audio_stream_url(url)
            except Exception as e:
                st.error(
                    "오디오를 불러오는 데 실패했습니다. 다음 곡으로 넘어가 주세요."
                )
                st.session_state.audio_url = "error"

    # 💡 [핵심 해결 포인트] 오디오 플레이어에 start_time 매개변수를 직접 세팅해 모바일 전 브라우저에서 확실하게 작동하도록 수정했습니다.
    if st.session_state.audio_url and st.session_state.audio_url != "error":
        st.audio(
            st.session_state.audio_url,
            format="audio/mp3",
            start_time=int(start_sec),
        )

        if start_sec > 0:
            st.info(
                f"💡 이 곡은 교수님 요청 구간인 **{start_sec//60}분 {start_sec%60}초** 지점부터 자동 재생됩니다."
            )

    st.write("")

    # 정답 확인 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👁️ 정답 확인하기", use_container_width=True):
            st.session_state.show_answer = True

    # 정답 표시
    if st.session_state.show_answer:
        st.success(f"📢 정답은 바로: **{title}** 입니다!")

    st.markdown("---")

    # 다음 문제 버튼
    with col2:
        if st.button("➡️ 다음 문제로 넘어가기", use_container_width=True):
            st.session_state.current_index += 1
            st.session_state.show_answer = False
            st.session_state.audio_url = None
            st.rerun()

else:
    st.balloons()
    st.success("🎉 축하합니다! 58곡의 모든 문제를 다 풀었습니다. 기말고사 만점 가자! 💯")
    if st.button("🔄 처음부터 다시 풀기"):
        del st.session_state.quiz_pool
        st.rerun()
