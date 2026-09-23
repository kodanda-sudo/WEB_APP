import streamlit as st

st.set_page_config(page_title="Welcome Back", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .login-card {
            background: rgba(255, 255, 255, 0.96);
            padding: 2.
            2rem;
            border-radius: 18px;
            max-width: 420px;
            margin: 2rem auto;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
        }
        .welcome-title {
            font-size: 2rem;
            font-weight: 700;
            color: #242424;
            margin-bottom: 0.25rem;
        }
        .welcome-subtitle {
            font-size: 0.96rem;
            color: #626262;
            margin-bottom: 1.5rem;
        }
        .field-label {
            color: #444;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.45rem;
        }
        .submit-btn {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #5a6fd6 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 1rem;
            font-weight: 600;
            margin-top: 0.5rem;
        }
        .extra-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0.9rem 0 1.2rem;
            font-size: 0.85rem;
        }
        .remember {
            color: #555;
        }
        .forgot {
            color: #667eea;
            text-decoration: none;
        }
        .signup {
            text-align: center;
            font-size: 0.85rem;
            color: #666;
            margin-top: 1rem;
        }
        .signup a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="login-card">
        <div class="welcome-title">Welcome Back</div>
        <div class="welcome-subtitle">Please enter your details to sign in.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    email = st.text_input("Email Address", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    col1, col2 = st.columns([1.2, 1])
    with col1:
        remember = st.checkbox("Remember me")
    with col2:
        st.markdown('<div style="text-align:right; margin-top:0.4rem;"><a href="#" class="forgot">Forgot Password?</a></div>', unsafe_allow_html=True)

    if st.button("Sign In", use_container_width=True):
        if email and password:
            st.success(f"Welcome back, {email}!")
        else:
            st.warning("Please complete both fields before signing in.")

    st.markdown(
        '<div class="signup">Don\'t have an account? <a href="#">Sign up</a></div>',
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
