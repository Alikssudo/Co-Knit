import streamlit as st


st.set_page_config(page_title="Co-knit", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    /* ---- Pure black background, white text ---- */
    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    [data-testid="stAppViewBlockContainer"] {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    /* Remove default padding / top margin */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;

    /* Text elements white */
    p, h1, h2, h3, span, label, div {
        color: #ffffff !important;
    }

    /* Buttons subtle white border, transparent fill */
    .stButton > button {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
    }
    .stButton > button:hover,
    .stButton > button:focus,
    .stButton > button:active {
        background-color: transparent !important;
        color: #ffffff !important;
        border-color: #ffffff !important;
        box-shadow: none !important;
        transform: none !important;
    }

    /* Text inputs */
    .stTextInput > div > div > input {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #888888 !important;
    }
    .stTextInput > label {
        color: #ffffff !important;
    }
    .stTextInput button {
        display: none !important;
    }

    /* Centered title */
    .centered-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        letter-spacing: -1px;
    }
    .centered-subtitle {
        text-align: center;
        font-size: 1.25rem;
        margin-bottom: 2.5rem;
        opacity: 0.85;
    }

    /* Footer banner */
    .footer-banner {
        background-color: #2b2b2b;
        color: #ffffff;
        text-align: center;
        padding: 1rem 0;
        margin-top: 2rem;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        font-size: 1rem;
        font-weight: 600;
    }

    /* Social link buttons */
    .social-links {
        display: flex;
        gap: 12px;
        justify-content: center;
        margin-top: 1rem;
    }
    .social-links a {
        flex: 1;
        text-align: center;
        text-decoration: none;
        padding: 12px 20px;
        border-radius: 8px;
        color: #ffffff;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid #444;
    }
    .social-links a:hover,
    .social-links a:focus,
    .social-links a:active {
        color: inherit !important;
        transform: none !important;
        box-shadow: none !important;
        filter: none !important;
    }
    .social-fb  { background-color: #1877F2; }
    .social-ig  { background-color: #E4405F; }
    .social-wa  { background-color: #25D366; color: #000000; }

    /* Mr.rick haha */
    .rickroll-wrapper {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: 99999;
        overflow: hidden;
    }
    .rickroll-wrapper iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Navigation

if "view" not in st.session_state:
    st.session_state.view = "landing"


# View 1 — Landing

def landing_view():
    st.markdown('<h1 class="centered-title">Co-knit</h1>', unsafe_allow_html=True)

    left_col, right_col = st.columns(2)

    with left_col:
        st.title("**What to expect?**")
        st.subheader(
            "*After ensuring the authorization of your creditionals, You shall rest "
            "knowing three of the most popular socials will be secured and more "
            "accessible in this website.*"
        )
        st.write("")
        st.markdown(
    "<span style='background-color: red; color: black; font-weight: border-radius: 4px;'>Co-knit aims to knit your socials with your cooperation.</span>", 
    unsafe_allow_html=True
)

        st.write("")
        st.write("")
        st.title("**Why us?**")
        st.subheader(
            "*It's been tested with beta testers before and no complaints has been "
            "received nor any detected data breach.*"
        )

    # Candidate image
    with right_col:
        st.image("7 PM.jpeg", use_container_width=True)
        st.subheader("One of the beta testers:", text_alignment="right")

    # Navigation button
    col_spacer_l, col_btn, col_spacer_r = st.columns([1.5, 1, 1.5])
    with col_btn:
        if st.button("Proceed to Login", use_container_width=True):
            st.session_state.view = "login"
            st.rerun()


    # Footer banner
    st.markdown(
        '<div class="footer-banner">Update to the more safer and niche option!</div>',
        unsafe_allow_html=True,
    )

# View 2 

def login_view():
    st.markdown('<h1 class="centered-title">Sign In</h1>', unsafe_allow_html=True)
    left_col, right_col = st.columns(2)

    with left_col:
        st.image("5 PM.jpeg", use_container_width=True)

    with right_col:
        email = st.text_input("* Email")
        password = st.text_input("* Password", type="password")

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Sign In", use_container_width=True):
                st.session_state.view = "dashboard"
                st.rerun()
        with col_b:
            if st.button("Create an account", use_container_width=True):
                st.session_state.view = "dashboard"
                st.rerun()

        st.markdown("<p style='text-align:center; margin-top:1.5rem;'>Or sign in / sign up with</p>",
                    unsafe_allow_html=True)

        st.markdown(
            """
            <div class="social-links">
                <a class="social-fb" href="https://www.facebook.com/login/" target="_blank">Facebook</a>
                <a class="social-ig" href="https://www.instagram.com/accounts/login/" target="_blank">Instagram</a>
                <a class="social-wa" href="https://web.whatsapp.com/" target="_blank">WhatsApp</a>
            </div>
            """,
            unsafe_allow_html=True,
        )



# View 3 

def dashboard_view():
    st.markdown(
        """
        <style>
        /* Hide ALL streamlit UI so only the embed(yt vid) is visible */
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stHeader"] { display: none !important; }
        [data-testid="stAppViewBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
        .block-container { padding: 0 !important; }
        #stDecoration, #MainMenu, footer { display: none !important; }
        .stApp { background: #000 !important; }
        </style>
        <div class="rickroll-wrapper">
            <iframe
                src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=0"
                title="Rick Astley - Never Gonna Give You Up"
                allow="autoplay; encrypted-media; fullscreen"
                allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Router

if st.session_state.view == "landing":
    landing_view()
elif st.session_state.view == "login":
    login_view()
elif st.session_state.view == "dashboard":
    dashboard_view()