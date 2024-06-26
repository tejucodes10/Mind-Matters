# Dictionary of questions
questions = {
    'Q1': "I do not tire quickly.",
    'Q2': "I am troubled by attacks of nausea.",
    'Q3': "I believe I am no more nervous than most others.",
    'Q4': "I have very few headaches.",
    'Q5': "I work under a great deal of tension.",
    'Q6': "I cannot keep my mind on one thing.",
    'Q7': "I worry over money and business.",
    'Q8': "I frequently notice my hand shakes when I try to do something.",
    'Q9': "I blush no more often than others.",
    'Q10': "I have diarrhea once a month or more.",
    'Q11': "I worry quite a bit over possible misfortunes.",
    'Q12': "I practically never blush.",
    'Q13': "I am often afraid that I am going to blush.",
    'Q14': "I have nightmares every few nights.",
    'Q15': "My hands and feet are usually warm.",
    'Q16': "I sweat very easily even on cool days.",
    'Q17': "Sometimes when embarrassed, I break out in a sweat.",
    'Q18': "I hardly ever notice my heart pounding and I am seldom short of breath.",
    'Q19': "I feel hungry almost all the time.",
    'Q20': "I am very seldom troubled by constipation.",
    'Q21': "I have a great deal of stomach trouble.",
    'Q22': "I have had periods in which I lost sleep over worry.",
    'Q23': "My sleep is fitful and disturbed.",
    'Q24': "I dream frequently about things that are best kept to myself.",
    'Q25': "I am easily embarrassed.",
    'Q26': "I am more sensitive than most other people.",
    'Q27': "I frequently find myself worrying about something.",
    'Q28': "I wish I could be as happy as others seem to be.",
    'Q29': "I am usually calm and not easily upset.",
    'Q30': "I cry easily.",
    'Q31': "I feel anxiety about something or someone almost all the time.",
    'Q32': "I am happy most of the time.",
    'Q33': "It makes me nervous to have to wait.",
    'Q34': "I have periods of such great restlessness that I cannot sit long I a chair.",
    'Q35': "Sometimes I become so excited that I find it hard to get to sleep.",
    'Q36': "I have sometimes felt that difficulties were piling up so high that I could not overcome them.",
    'Q37': "I must admit that I have at times been worried beyond reason over something that really did not matter.",
    'Q38': "I have very few fears compared to my friends.",
    'Q39': "I have been afraid of things or people that I know could not hurt me.",
    'Q40': "I certainly feel useless at times.",
    'Q41': "I find it hard to keep my mind on a task or job.",
    'Q42': "I am usually self-conscious.",
    'Q43': "I am inclined to take things hard.",
    'Q44': "I am a high-strung person.",
    'Q45': "Life is a trial for me much of the time.",
    'Q46': "At times I think I am no good at all.",
    'Q47': "I am certainly lacking in self-confidence.",
    'Q48': "I sometimes feel that I am about to go to pieces.",
    'Q49': "I shrink from facing crisis of difficulty.",
    'Q50': "I am entirely self-confident."
}



pink_color = "#f63366"
black_color = "#000000"
white_color = "#FFFFFF"
import streamlit as st
import pandas as pd


# Streamlit app
def main():
    st.markdown(f"""
    <div style="background-color:{pink_color};padding:3px;border-radius:3px">
    <h1 style="color:{white_color};text-align:center;">Taylor-Manifest Scale for anxiety diagnosis</h1>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")

    # Collect age and gender
    age = st.slider('Select your age:', min_value=18, max_value=100, value=30)
    gender = st.radio('Select your gender:', ['Male', 'Female'])

    # Display questionnaire
    st.header('Questionnaire')
    responses = {}
    for i, (key, question) in enumerate(questions.items(), start=1):
        responses[key] = st.radio(f'Q{i}: {question}', ['True', 'False'])

    # Submit button
    if st.button('Submit'):
        # Convert responses to dataframe
        responses_df = pd.DataFrame(responses, index=[0])
        
        # Calculate score
        score = responses_df.eq('True').sum(axis=1).values[0]

        # Determine anxiety level
        if score < 25:
            st.write("You don't have anxiety,your score is "+str(score))
        elif 26 <= score <= 39:
            st.write("You have mild anxiety, your score is "+str(score))
        elif 40 <= score <= 50:
            st.write("You have severe anxiety,your score is "+str(score))
        else:
            st.write("Invalid score.")

if __name__ == '__main__':
    main()
