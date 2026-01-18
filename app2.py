import streamlit as st
import random

# Word list
words = ["python", "apple", "computer", "game", "streamlit"]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.lives = 6

st.title("🎯 Simple Word Guessing Game")

# Display word
display_word = ""
for letter in st.session_state.word:
    if letter in st.session_state.guessed:
        display_word += letter + " "
    else:
        display_word += "_ "

st.subheader(display_word)
st.write("❤️ Lives left:", st.session_state.lives)

# Input
guess = st.text_input("Enter a letter", max_chars=1)

if st.button("Guess"):
    if guess:
        if guess in st.session_state.guessed:
            st.warning("Already guessed!")
        elif guess in st.session_state.word:
            st.success("Correct guess!")
            st.session_state.guessed.append(guess)
        else:
            st.error("Wrong guess!")
            st.session_state.guessed.append(guess)
            st.session_state.lives -= 1

# Win condition
if all(letter in st.session_state.guessed for letter in st.session_state.word):
    st.balloons()
    st.success(f"🎉 You won! Word was **{st.session_state.word}**")

# Lose condition
if st.session_state.lives == 0:
    st.error(f"💀 Game Over! Word was **{st.session_state.word}**")

# Restart button
if st.button("Restart Game"):
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.lives = 6
