import streamlit as st
import random
import time

st.set_page_config(page_title="Car Racing Game", page_icon="🚗")

# Initialize game state
if "position" not in st.session_state:
    st.session_state.position = 0
    st.session_state.score = 0
    st.session_state.game_over = False

st.title("🚗 Simple Car Racing Game")

# Road display
road = ["⬜"] * 10
car_index = min(st.session_state.position, 9)
road[car_index] = "🚗"

st.write("### Road")
st.write(" ".join(road))

# Obstacle
obstacle_pos = random.randint(4, 9)
st.write(f"🚧 Obstacle at position {obstacle_pos}")

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("⬆️ Accelerate") and not st.session_state.game_over:
        st.session_state.position += 1
        st.session_state.score += 10

        if st.session_state.position == obstacle_pos:
            st.session_state.game_over = True

with col2:
    if st.button("🔄 Restart"):
        st.session_state.position = 0
        st.session_state.score = 0
        st.session_state.game_over = False

# Game status
st.write("### Score:", st.session_state.score)

if st.session_state.game_over:
    st.error("💥 Crash! Game Over")

