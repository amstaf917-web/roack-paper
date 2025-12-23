import streamlit as st

# Page Title
st.title("🪨 📄 ✂️ Rock Paper Scissors")

# Sidebar for Player Names
st.sidebar.header("Player Settings")
player1 = st.sidebar.text_input("Enter Player 1 Name:", "Player 1")
player2 = st.sidebar.text_input("Enter Player 2 Name:", "Player 2")

choices = ["rock", "paper", "scissors"]

# UI for Game Choices
st.subheader(f"Game: {player1} vs {player2}")

col1, col2 = st.columns(2)

with col1:
    p1_choice = st.selectbox(f"{player1}'s turn:", choices, key="p1")

with col2:
    p2_choice = st.selectbox(f"{player2}'s turn:", choices, key="p2")

# Play Button
if st.button("Play Game"):
    st.write("---")
    st.info(f"**{player1}** chose: {p1_choice}")
    st.info(f"**{player2}** chose: {p2_choice}")

    # Game Logic
    if p1_choice == p2_choice:
        st.warning("It's a Draw! 🤝")
    elif (
        (p1_choice == "rock" and p2_choice == "scissors") or
        (p1_choice == "scissors" and p2_choice == "paper") or
        (p1_choice == "paper" and p2_choice == "rock")
    ):
        st.success(f"🏆 {player1} Wins!")
    else:
        st.success(f"🏆 {player2} Wins!")

# Reset/Clear instructions
st.write("---")
st.caption("Choices ko change karein aur 'Play Game' button dabayein.")