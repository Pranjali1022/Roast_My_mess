"""
Roast My Mess — Prototype: IIT KGP Campus AI Companion
"""

import streamlit as st
import anthropic
import json
import random
from datetime import datetime
from data import COMMUNITY_POSTS, LEADERBOARD, COMPLAINT_DATA, SAMPLE_MENUS, HALLS, TONE_PROMPTS

# Page config (must be first Streamlit call) 
st.set_page_config(
    page_title="Roast My Mess — IIT KGP",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# custom CSS ─
st.markdown("""
<style>
/* Global dark theme */
[data-testid="stAppViewContainer"] {
    background-color: #0f0f0f;
    color: #f0f0f0;
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background-color: #181818; }

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Custom navbar */
.navbar {
    background: #181818;
    border-bottom: 1px solid #2a2a2a;
    padding: 12px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 10px;
    margin-bottom: 24px;
}
.nav-brand { font-size: 20px; font-weight: 800; color: #f0f0f0; }
.nav-brand span { color: #ff4500; }
.campus-badge {
    background: #222;
    border: 1px solid #2a2a2a;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 12px;
    color: #888;
}

/* Cards */
.card {
    background: #181818;
    border: 1px solid #2a2a2a;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 16px;
}
.card-title {
    font-size: 14px;
    font-weight: 600;
    color: #f0f0f0;
    margin-bottom: 6px;
}
.card-body { font-size: 13px; color: #888; line-height: 1.6; }

/* Roast result */
.roast-box {
    background: #181818;
    border: 1px solid #ff4500;
    border-radius: 14px;
    padding: 20px;
    margin: 16px 0;
}
.roast-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 14px;
    padding-bottom: 12px;
    border-bottom: 1px solid #2a2a2a;
}
.roast-text { font-size: 15px; line-height: 1.75; color: #f0f0f0; white-space: pre-wrap; }

/* Meme card */
.meme-card {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 14px;
    padding: 24px;
    text-align: center;
    position: relative;
    margin-top: 12px;
}
.meme-tag {
    display: inline-block;
    background: #ff4500;
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 10px;
    letter-spacing: 0.08em;
}
.meme-quote { font-size: 17px; font-weight: 700; color: #f0f0f0; line-height: 1.4; }
.meme-quote span { color: #ff4500; }
.meme-footer { font-size: 11px; color: #555; margin-top: 10px; }

/* Leaderboard */
.lb-row {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 0;
    border-bottom: 1px solid #2a2a2a;
}
.lb-rank { font-size: 18px; font-weight: 800; width: 28px; }
.lb-dish { flex: 1; }
.lb-dish-name { font-size: 13px; font-weight: 600; color: #f0f0f0; }
.lb-dish-meta { font-size: 11px; color: #888; }
.lb-count { font-size: 16px; font-weight: 700; color: #ff4500; }

/* Community posts */
.post {
    background: #181818;
    border: 1px solid #2a2a2a;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
}
.post-author { font-size: 13px; font-weight: 600; color: #f0f0f0; }
.post-time { font-size: 11px; color: #555; }
.post-content { font-size: 14px; line-height: 1.6; color: #ccc; margin: 10px 0; }
.tone-pill {
    display: inline-block;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 20px;
    margin-left: 8px;
}
.tp-savage { background: rgba(255,69,0,0.15); color: #ff4500; }
.tp-mild   { background: rgba(34,197,94,0.15);  color: #22c55e; }
.tp-poetic { background: rgba(245,158,11,0.15); color: #f59e0b; }

/* Stats */
.stat-num { font-size: 28px; font-weight: 800; }
.stat-lbl { font-size: 12px; color: #888; margin-top: 4px; }

/* Complaint bar */
.bar-wrap { margin: 8px 0; }
.bar-label { font-size: 13px; font-weight: 600; color: #f0f0f0; margin-bottom: 4px; }
.bar-bg { background: #222; border-radius: 4px; height: 8px; }
.bar-fill { height: 8px; border-radius: 4px; background: #ff4500; }

/* Authority */
.auth-banner {
    background: linear-gradient(135deg, #0a1628, #0f2040);
    border: 1px solid #1e3a5f;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 20px;
}
.auth-title { font-size: 18px; font-weight: 700; color: #f0f0f0; }
.auth-sub { font-size: 13px; color: #888; margin-top: 4px; }

/* Rating badge */
.rating-badge {
    background: #ff4500;
    color: white;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
}

/* Buttons */
.stButton > button {
    background: #ff4500 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: all 0.15s !important;
}
.stButton > button:hover {
    background: #ff6b35 !important;
    transform: translateY(-1px) !important;
}
</style>
""", unsafe_allow_html=True)

# Session state init 
if "posts" not in st.session_state:
    st.session_state.posts = list(COMMUNITY_POSTS)   
if "last_roast" not in st.session_state:
    st.session_state.last_roast = None               
if "likes" not in st.session_state:
    st.session_state.likes = {}                      

# Navbar 
st.markdown("""
<div class="navbar">
  <div class="nav-brand">🔥 <span>Roast</span> My Mess</div>
  <div class="campus-badge">IIT KGP · 2025</div>
</div>
""", unsafe_allow_html=True)

# Tab navigation
# st.tabs() creates clickable tabs — Streamlit handles state automatically
tab_roast, tab_feed, tab_authority = st.tabs(["🔥 Roast", "📢 Campus Feed", "📊 Authority Dashboard"])



# TAB 1:  ROAST ENGINE

with tab_roast:
    st.markdown("### Today's Mess Menu")
    st.markdown("<p style='color:#888;font-size:13px;margin-top:-8px'>Type the menu → get roasted → share with the world</p>", unsafe_allow_html=True)

    col_input, col_settings = st.columns([3, 2], gap="large")

    with col_input:
        # Text area for menu input
        menu_text = st.text_area(
            "Menu",
            placeholder="e.g. Monday lunch: Dal tadka, rice, roti, aloo gobhi, raita, boiled egg, banana...",
            height=160,
            label_visibility="collapsed",
        )

        # Sample menu button — st.button returns True only when clicked
        if st.button("🎲 Try a sample IIT KGP menu", use_container_width=True):
            # We use session_state to "remember" a sample was requested
            st.session_state.sample_menu = random.choice(SAMPLE_MENUS)
            st.rerun()  # rerun triggers re-render with the new sample

        # Fill input if sample was requested
        if "sample_menu" in st.session_state and not menu_text:
            menu_text = st.session_state.sample_menu

    with col_settings:
        # Selectbox for hall
        hall = st.selectbox("Your Hall / Mess", HALLS)

        # Radio for tone — maps to different system prompts
        tone = st.radio(
            "Roast Tone",
            options=["🔥 Savage", "😅 Mild", "🎭 Poetic Tragedy", "🧑‍🎓 IIT Jhola Guy"],
            index=0,
        )
        # Map display label back to key for TONE_PROMPTS dict
        tone_key = tone.split(" ", 1)[1].strip().lower().replace(" ", "_")

    # Generate roast
    st.markdown("---")
    generate = st.button("🔥 Roast This Menu", use_container_width=True, type="primary")

    if generate:
        if not menu_text.strip():
            st.warning("Please enter today's menu first!")
        else:
            loading_html = """
                        <div style="text-align:center;padding:30px 0">
                        <div class="loader-fire"></div>
                        <div style="margin-top:15px;font-size:16px;font-weight:600">
                            Cooking up a savage roast 🔥
                        </div>
                        <div style="font-size:12px;color:#888;margin-top:6px">
                            Analyzing mess trauma... please wait
                        </div>
                    </div>

                    <style>
                    .loader-fire {
                    width: 60px;
                    height: 60px;
                    border-radius: 50%;
                    background: radial-gradient(circle, #ff4500 40%, #ff6b35 60%, transparent 70%);
                    animation: pulse 1s infinite ease-in-out;
                    margin: auto;
                    }

                    @keyframes pulse {
                    0% { transform: scale(0.8); opacity: 0.6; }
                    50% { transform: scale(1.2); opacity: 1; }
                    100% { transform: scale(0.8); opacity: 0.6; }
                    }
                    </style>
                    """
            # st.spinner shows a loading indicator while the API call runs
            placeholder = st.empty()
            placeholder.markdown(loading_html, unsafe_allow_html=True)
            try:
                    #Anthropic API call 
                    client = anthropic.Anthropic()

                    system_prompt = TONE_PROMPTS.get(tone_key, TONE_PROMPTS["savage"])
                    user_prompt = f"Menu from {hall} Mess, IIT KGP:\n{menu_text}\n\nRoast this menu. Be funny and culturally specific to IIT KGP campus life."

                    message = client.messages.create(
                        model="claude-opus-4-6",          # strongest model for creative roasting
                        max_tokens=1024,
                        system=system_prompt,
                        messages=[{"role": "user", "content": user_prompt}],
                    )

                    roast = message.content[0].text

                    # Extract rating from the roast text (e.g. "2.5/10")
                    import re
                    rating_match = re.search(r"(\d[\d.]*)/10", roast)
                    rating = rating_match.group(0) if rating_match else "??/10"

                    # Store in session_state so result persists across reruns
                    st.session_state.last_roast = {
                        "text": roast,
                        "rating": rating,
                        "hall": hall,
                        "tone": tone,
                        "tone_key": tone_key,
                        "menu": menu_text,
                        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                    }

            except Exception as e:
                st.error(f"Roast failed: {e}")

    # Display result 
    if st.session_state.last_roast:
        r = st.session_state.last_roast
        tone_colors = {
            "savage": "#ff4500", "mild": "#22c55e",
            "poetic_tragedy": "#f59e0b", "iit_jhola_guy": "#a78bfa"
        }
        tc = tone_colors.get(r["tone_key"], "#ff4500")

        st.markdown(f"""
        <div class="roast-box">
            <div class="roast-header">
                <div>
                    <div style="font-size:14px;font-weight:600;color:#f0f0f0">{r['hall']} · IIT KGP</div>
                    <div style="font-size:11px;color:#888">{r['timestamp']}</div>
                </div>
                <div>
                    <span class="rating-badge">{r['rating']}</span>
                    <span style="background:rgba(255,69,0,0.1);color:{tc};font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px;margin-left:8px">{r['tone']}</span>
                </div>
            </div>
            <div class="roast-text">{r['text']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Meme card — shareable format
        first_line = r["text"].split(".")[0][:90]
        st.markdown(f"""
        <div class="meme-card">
            <div class="meme-tag">ROAST MY MESS</div>
            <div style="font-size:11px;color:#888;margin-bottom:10px;letter-spacing:0.08em">IIT KGP · {r['hall']}</div>
            <div class="meme-quote">"{first_line}..."</div>
            <div class="meme-footer">roastmymess.in · Share the suffering</div>
        </div>
        """, unsafe_allow_html=True)

        # Action buttons
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            # st.download_button lets users save the roast as a text file
            st.download_button(
                "📋 Save Roast",
                data=r["text"],
                file_name=f"mess_roast_{r['hall'].replace(' ','_')}.txt",
                mime="text/plain",
                use_container_width=True,
            )
        with col_b:
            # Copy-friendly display
            if st.button("📋 Copy Meme Text", use_container_width=True):
                st.code(f'"{first_line}..."\n\n{r["text"]}\n\n— roastmymess.in', language=None)
        with col_c:
            # Post to community feed
            if st.button("📢 Post to Campus Feed", use_container_width=True):
                new_post = {
                    "author": f"You · {r['hall']}",
                    "initials": random.choice(["YO", "ME", "US"]),
                    "time": "Just now",
                    "content": r["text"][:200] + ("..." if len(r["text"]) > 200 else ""),
                    "tone_key": r["tone_key"],
                    "likes": 0,
                    "comments": 0,
                }
                # Prepend to community feed (list stored in session_state)
                st.session_state.posts.insert(0, new_post)
                st.success("Posted to campus feed! Switch to the 📢 Campus Feed tab.")



# TAB 2: COMMUNITY FEED

with tab_feed:
    # Live indicator
    col_h, col_live = st.columns([3, 1])
    with col_h:
        st.markdown("### Campus Feed")
    with col_live:
        st.markdown("<div style='text-align:right;padding-top:10px;font-size:13px;color:#888'>🟢 Live · IIT KGP</div>", unsafe_allow_html=True)

    #Leaderboard
    st.markdown("#### 🏆 Mess of Shame — This Week")
    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)
    for i, item in enumerate(LEADERBOARD):
        rank_colors = ["#ff4500", "#f59e0b", "#22c55e"]
        rc = rank_colors[i] if i < 3 else "#888"
        st.markdown(f"""
        <div class="lb-row">
            <div class="lb-rank" style="color:{rc}">{i+1}</div>
            <div class="lb-dish">
                <div class="lb-dish-name">{item['dish']}</div>
                <div class="lb-dish-meta">{item['hall']} · {item['days']}</div>
            </div>
            <div class="lb-count">{item['roasts']:,}</div>
            <div style="font-size:11px;color:#888">roasts</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"#### Recent Posts ({len(st.session_state.posts)} total)")

    # Community posts 
    tone_pill_map = {
        "savage": '<span class="tone-pill tp-savage">savage</span>',
        "mild":   '<span class="tone-pill tp-mild">mild</span>',
        "poetic_tragedy": '<span class="tone-pill tp-poetic">poetic</span>',
        "iit_jhola_guy":  '<span class="tone-pill tp-poetic">jhola</span>',
    }
    avatar_colors = [
        ("#2a0f00", "#ff6b35"), ("#0a1a0a", "#22c55e"),
        ("#1a1000", "#f59e0b"), ("#1a0a1a", "#a78bfa"),
    ]

    for idx, post in enumerate(st.session_state.posts):
        bg, fg = avatar_colors[idx % len(avatar_colors)]
        pill = tone_pill_map.get(post.get("tone_key", "savage"), "")
        likes_key = f"likes_{idx}"
        current_likes = st.session_state.likes.get(likes_key, post.get("likes", 0))

        st.markdown(f"""
        <div class="post">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">
                <div style="width:34px;height:34px;border-radius:50%;background:{bg};color:{fg};display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0">{post['initials']}</div>
                <div>
                    <div class="post-author">{post['author']} {pill}</div>
                    <div class="post-time">{post['time']}</div>
                </div>
            </div>
            <div class="post-content">{post['content']}</div>
            <div style="display:flex;gap:16px;font-size:12px;color:#888">
                <span>👍 {current_likes}</span>
                <span>💬 {post.get('comments', 0)}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Like button per post (using unique key)
        if st.button(f"👍 Like", key=f"like_btn_{idx}"):
            st.session_state.likes[likes_key] = current_likes + 1
            st.rerun()


# TAB 3: AUTHORITY DASHBOARD
with tab_authority:
    st.markdown("""
    <div class="auth-banner">
        <div class="auth-title">📊 Mess Feedback Dashboard</div>
        <div class="auth-sub">Anonymized student sentiment · IIT KGP · Week of Jan 13–19, 2025</div>
    </div>
    """, unsafe_allow_html=True)

    # KPI metrics 
    # st.metric() is Streamlit's built-in KPI card with delta support
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Roasts", "2,841", "+340 vs last week")
    col2.metric("Avg. Satisfaction", "4.2/10", "-0.3")
    col3.metric("Positive Mentions", "23%", "+2%")
    col4.metric("Active Students", "1,204", "+89")

    st.markdown("---")

    # Complaint chart 
    col_chart, col_list = st.columns([2, 1], gap="large")

    with col_chart:
        st.markdown("#### Most Complained Items")
        # st.progress() renders a simple progress bar — repurposed as a complaint bar
        for item in COMPLAINT_DATA:
            pct = item["count"] / COMPLAINT_DATA[0]["count"]  # normalize to max
            st.markdown(f"**{item['name']}** — {item['count']} complaints")
            st.progress(pct)

    with col_list:
        st.markdown("#### Halls by Complaint Volume")
        hall_data = {
            "LBS Hall": 847, "MMM Hall": 612, "RP Hall": 389,
            "Nehru Hall": 341, "VS Hall": 214,
        }
        # st.bar_chart() is a quick built-in chart — no matplotlib needed
        st.bar_chart(hall_data, color="#ff4500")

    st.markdown("---")

    # Insight box 
    st.markdown("#### Key Insight for Mess Committee")
    st.info("""
    **Top complaint is texture, not taste.** Students are okay with the type of food — they're not okay with how it's cooked. Soya chunks appear 5× per week; reducing to 2× and adding one new sabzi variant on Mon/Thu is estimated to drop dissatisfaction by ~35%.

    The weekly "Mess of Shame" leaderboard shows which dishes are repeat offenders — this data can directly inform menu planning.
    """)

    # Export 
    # Build a simple text report
    report_lines = [
        "ROAST MY MESS — WEEKLY MESS REPORT",
        "IIT KGP | Week of Jan 13–19, 2025",
        "=" * 40,
        f"Total Roasts: 2,841",
        f"Avg Satisfaction: 4.2/10",
        f"Positive Mentions: 23%",
        "",
        "TOP COMPLAINTS:",
    ]
    for item in COMPLAINT_DATA:
        report_lines.append(f"  - {item['name']}: {item['count']} complaints")
    report_lines += [
        "",
        "KEY RECOMMENDATION:",
        "Reduce soya chunks from 5x/week to 2x/week.",
        "Add one new sabzi variant on Mon/Thu.",
        "",
        "Generated by Roast My Mess | roastmymess.in",
    ]

    st.download_button(
        label="📄 Download Weekly Report (.txt)",
        data="\n".join(report_lines),
        file_name="mess_report_jan_w3_2025.txt",
        mime="text/plain",
        use_container_width=True,
    )
