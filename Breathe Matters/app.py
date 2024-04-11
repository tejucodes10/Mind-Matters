import streamlit as st
from algorithm import execute_program
from algorithm import (
    CLEAR_MIND_BEGINNER, CLEAR_MIND_MEDIUM, CLEAR_MIND_ADVANCED,
    ANTI_STRESS_BEGINNER, ANTI_STRESS_MEDIUM, ANTI_STRESS_ADVANCED,
    ANTI_APPETITE_BEGINNER, ANTI_APPETITE_MEDIUM, ANTI_APPETITE_ADVANCED,
    DECISION_MAKING_BEGINNER, DECISION_MAKING_MEDIUM, DECISION_MAKING_ADVANCED
)

def main():
    st.set_page_config(page_title="Breathe Matters", page_icon=":)", layout="centered", initial_sidebar_state="expanded")
    
    # Pink and white color scheme
    pink_color = "#f63366"
    black_color = "#000000"
    white_color = "#FFFFFF"
    
    # Set page background color to white
    st.markdown(f"""
    <style>
    .reportview-container {{
        background-color: {white_color};
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Header with pink background and black text
    st.markdown(f"""
    <div style="background-color:{pink_color};padding:3px;border-radius:3px">
    <h1 style="color:{white_color};text-align:center;">BREATHE MATTERS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(" ")
    st.markdown(" ")
    # Text in pink color No need to walk away to take a break, just sit comfortably, run the application and let the journey begin
    st.markdown(f'<p style="color: {black_color}; ">Breathe Matters is your virtual breathing gymnastics assistant.</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: {black_color}; ">It helps you overcome anxiety, increases oxygen levels for a detoxified energetic day and concentration.</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: {black_color}; ">Sit back and relax, let Breathe Matters enhance your mental health.</p>', unsafe_allow_html=True)

    exercise_type = st.selectbox('Select Exercise Type', ['Clear Mind', 'Anti stress', 'Anti apetite', 'Decision Making'])
    difficulty_level = st.selectbox('Select Difficulty Level', ['Beginner', 'Familiar', 'Advanced'])

    if st.button('Run Algorithm'):
        if exercise_type == 'Clear Mind':
            if difficulty_level == 'Beginner':
                program_data = CLEAR_MIND_BEGINNER
            elif difficulty_level == 'Familiar':
                program_data = CLEAR_MIND_MEDIUM
            elif difficulty_level == 'Advanced':
                program_data = CLEAR_MIND_ADVANCED
        elif exercise_type == 'Anti stress':
            if difficulty_level == 'Beginner':
                program_data = ANTI_STRESS_BEGINNER
            elif difficulty_level == 'Familiar':
                program_data = ANTI_STRESS_MEDIUM
            elif difficulty_level == 'Advanced':
                program_data = ANTI_STRESS_ADVANCED
        elif exercise_type == 'Anti apetite':
            if difficulty_level == 'Beginner':
                program_data = ANTI_APPETITE_BEGINNER
            elif difficulty_level == 'Familiar':
                program_data = ANTI_APPETITE_MEDIUM
            elif difficulty_level == 'Advanced':
                program_data = ANTI_APPETITE_ADVANCED
        elif exercise_type == 'Decision Making':
            if difficulty_level == 'Beginner':
                program_data = DECISION_MAKING_BEGINNER
            elif difficulty_level == 'Familiar':
                program_data = DECISION_MAKING_MEDIUM
            elif difficulty_level == 'Advanced':
                program_data = DECISION_MAKING_ADVANCED

        st.markdown(f'<p style="color: {pink_color};">Running algorithm for {exercise_type} exercise at {difficulty_level} difficulty...</p>', unsafe_allow_html=True)
        execute_program(program_data)

if __name__ == '__main__':
    main()