import streamlit as st
from post_generator import generate_post, get_analytics, score_post

st.set_page_config(page_title="AI LinkedIn Post Generator", layout="wide")

st.title("🚀 AI LinkedIn Post Generator")

# ---------------- DEFAULT TOPICS ---------------- #

default_topics = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Career Growth",
    "Job Search",
    "Women in Tech",
    "Productivity",
    "Leadership",
    "Startups",
    "Self Improvement",
    "Entrepreneurship", 
    "Leadership", 
    "Mental Health",
    "Networking",
    "Personal Branding",
    "Remote Work", 
    "Software Engineering", 
    "Python", 
    "Generative AI",
    "LLMs", 
    "Interview Preparation",
    "Tech Trends", 
    "Upskilling", 
    "Freelancing", 
    "Corporate Life"
]

# ---------------- SIDEBAR SETTINGS ---------------- #

st.sidebar.header("⚙ Settings")

creativity_level = st.sidebar.select_slider(
    "Creativity Level",
    options=["Low", "Balanced", "High"],
    value="Balanced"
)

add_hook = st.sidebar.toggle("Generate Strong Hook", value=True)

post_format = st.sidebar.selectbox(
    "Post Format",
    ["Paragraph", "Bullet Points"]
)

# ---------------- INPUT SECTION ---------------- #
selected_topics = st.multiselect("Select Topic", default_topics)
custom_topic = st.text_input("Or Enter Custom Topic")

length = st.selectbox("Length", ["Short", "Medium", "Long"])
language = st.selectbox("Language", ["English", "Hinglish"])
tone = st.selectbox("Tone", ["Professional", "Motivational","Story Telling","Bold", "Casual"])
emoji_style = st.selectbox("Emoji Style", ["No Emojis", "Few Emojis", "Emoji Rich"])
cta = st.selectbox("Call To Action", ["No CTA", "Ask Question", "Encourage Comment","Invite DM"])


# Combine topics
final_topics = selected_topics.copy()

if custom_topic.strip() != "":
    final_topics.append(custom_topic.strip())

final_topic_string = ", ".join(final_topics)

# ---------------- SESSION STATE ---------------- #

if "generated_post" not in st.session_state:
    st.session_state.generated_post = ""

# ---------------- BUTTONS ---------------- #

col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Generate Post"):
        if final_topic_string == "":
            st.warning("Please select or enter at least one topic.")
        else:
            post = generate_post(
                length,
                language,
                final_topic_string,
                tone,
                emoji_style,
                cta,
                creativity_level,
                add_hook,
                post_format
            )
            st.session_state.generated_post = post

with col2:
    if st.button("🔁 Regenerate"):
        if final_topic_string != "":
            post = generate_post(
                length,
                language,
                final_topic_string,
                tone,
                emoji_style,
                cta,
                creativity_level,
                add_hook,
                post_format
            )
            st.session_state.generated_post = post

# ---------------- DISPLAY OUTPUT ---------------- #

if st.session_state.generated_post:

    st.markdown("## 📄 Generated Post")
    st.write(st.session_state.generated_post)

    # ---------------- ANALYTICS ---------------- #

    st.markdown("## 📊 Analytics / Insights")
    analytics = get_analytics(st.session_state.generated_post)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Words", analytics["Word Count"])
    col2.metric("Characters", analytics["Character Count"])
    col3.metric("Reading Time (min)", analytics["Estimated Reading Time (mins)"])
    col4.metric("Hashtags", analytics["Hashtag Count"])

    # ---------------- SCORING ---------------- #

    st.markdown("## 🧠 AI Post Scoring")

    scores = score_post(st.session_state.generated_post)

    if "Error" not in scores:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Engagement", f"{scores['Engagement']}/10")
        col2.metric("Clarity", f"{scores['Clarity']}/10")
        col3.metric("Hook Strength", f"{scores['Hook Strength']}/10")
        col4.metric("CTA Strength", f"{scores['CTA Strength']}/10")
    else:
        st.write("Scoring unavailable.")

    st.download_button(
        "⬇ Download Post",
        st.session_state.generated_post,
        file_name="linkedin_post.txt"
    )
