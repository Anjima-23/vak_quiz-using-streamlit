# python -m streamlit run vak/vak.py
# '''from streanlit import * #import all function
#  title("VAK quiz) #we can directly call function but when there is some other module having same function it will be confusing'''

# '''import streamlit as st
# st.title("VAK quiz")
# v,a,k=0,0,0
# q1=st.radio("When you are trying to remember a phone number, what helps you must?",['Writing it down or picturing it in your head','Saying it softly to yourself a few times','Dialing it once so your fingers remember'])
# if q1=='Writing it down or picturing it in your head':
#     v+=1
# elif q1=='Saying it softly to yourself a few times':
#     a+=1
# else:
#     k+=1
# if(st.button("get result")):
#     st.write(f'visual : {v/30*100} %')#give the result in normal text
#     st.success(f'visual : {v/30*100} %')#give the result in a green box
#     st.success(f'Auditory : {a/30*100} %')
#     st.success(f'kinesthetic : {k/30*100} %')'''


import streamlit as st

st.title("VAK quiz")

v, a, k = 0, 0, 0

# Q1
q1 = st.radio(
    "When you are trying to remember a phone number, what helps you most?",
    ['Writing it down or picturing it in your head',
     'Saying it softly to yourself a few times',
     'Dialing it once so your fingers remember'],index=None
)
if q1 == 'Writing it down or picturing it in your head':
    v += 1
elif q1 == 'Saying it softly to yourself a few times':
    a += 1
else:
    k += 1

# Q2
q2 = st.radio(
    "You are learning a new topic for an exam. What do you do first?",
    ['Move around and try to apply it practically',
     'Listen to a video or explanation',
     'Look for diagrams or flowcharts'],index=None
)
if q2 == 'Move around and try to apply it practically':
    k += 1
elif q2 == 'Listen to a video or explanation':
    a += 1
else:
    v += 1

# Q3
q3 = st.radio(
    "While assembling a new gadget, you prefer to:",
    ['Read the instructions step by step',
     'Look at the pictures in the manual',
     'Start assembling and figure it out'],index=None
)
if q3 == 'Read the instructions step by step':
    a += 1
elif q3 == 'Look at the pictures in the manual':
    v += 1
else:
    k += 1

# Q4
q4 = st.radio(
    "In a classroom, you understand best when:",
    ['The teacher explains aloud clearly',
     'There are charts and slides',
     'You do an activity or experiment'],index=None
)
if q4 == 'The teacher explains aloud clearly':
    a += 1
elif q4 == 'There are charts and slides':
    v += 1
else:
    k += 1

# Q5
q5 = st.radio(
    "When giving directions to someone, you usually:",
    ['Describe landmarks they will see',
     'Tell them turn-by-turn verbally',
     'Walk them part of the way'],index=None
)
if q5 == 'Describe landmarks they will see':
    v += 1
elif q5 == 'Tell them turn-by-turn verbally':
    a += 1
else:
    k += 1

# Q6
q6 = st.radio(
    "To relax after a long day, you prefer:",
    ['Listening to music or a podcast',
     'Watching a movie or series',
     'Doing something physical'],index=None
)
if q6 == 'Listening to music or a podcast':
    a += 1
elif q6 == 'Watching a movie or series':
    v += 1
else:
    k += 1

# Q7
q7 = st.radio(
    "When recalling a past event, you remember mostly:",
    ['The conversations',
     'The actions you did',
     'The scenes and visuals'],index=None
)
if q7 == 'The conversations':
    a += 1
elif q7 == 'The actions you did':
    k += 1
else:
    v += 1

# Q8
q8 = st.radio(
    "While learning a new software, you like:",
    ['Watching a demo video',
     'Trying it yourself',
     'Listening to someone explain'],index=None
)
if q8 == 'Watching a demo video':
    v += 1
elif q8 == 'Trying it yourself':
    k += 1
else:
    a += 1

# Q9
q9 = st.radio(
    "When shopping online, you rely more on:",
    ['Reviews and ratings',
     'Product images and videos',
     'Trying a similar product in real life'],index=None
)
if q9 == 'Reviews and ratings':
    a += 1
elif q9 == 'Product images and videos':
    v += 1
else:
    k += 1

# Q10
q10 = st.radio(
    "In group discussions, you usually:",
    ['Prefer listening carefully',
     'Use hand gestures while talking',
     'Like writing or drawing points'],index=None
)
if q10 == 'Prefer listening carefully':
    a += 1
elif q10 == 'Use hand gestures while talking':
    k += 1
else:
    v += 1

# Q11
q11 = st.radio(
    "When studying late night, what helps you stay focused?",
    ['Reading notes with highlights',
     'Moving around or stretching',
     'Playing soft background audio'],index=None
)
if q11 == 'Reading notes with highlights':
    v += 1
elif q11 == 'Moving around or stretching':
    k += 1
else:
    a += 1

# Q12
q12 = st.radio(
    "When learning a dance step, you:",
    ['Watch someone perform it',
     'Practice the moves repeatedly',
     'Listen to instructions carefully'],index=None
)
if q12 == 'Watch someone perform it':
    v += 1
elif q12 == 'Practice the moves repeatedly':
    k += 1
else:
    a += 1

# Q13
q13 = st.radio(
    "You remember people best by:",
    ['Their voice or way of speaking',
     'Their face',
     'Interacting with them'],index=None
)
if q13 == 'Their voice or way of speaking':
    a += 1
elif q13 == 'Their face':
    v += 1
else:
    k += 1

# Q14
q14 = st.radio(
    "During online classes, you prefer:",
    ['Clear voice explanations',
     'Interactive tasks',
     'Slides with visuals'],index=None
)
if q14 == 'Clear voice explanations':
    a += 1
elif q14 == 'Interactive tasks':
    k += 1
else:
    v += 1

# Q15
q15 = st.radio(
    "When fixing a problem, you usually:",
    ['Talk it through',
     'Sketch or visualize it',
     'Try different actions'],index=None
)
if q15 == 'Talk it through':
    a += 1
elif q15 == 'Sketch or visualize it':
    v += 1
else:
    k += 1

# Q16
q16 = st.radio(
    "To understand a story, you focus more on:",
    ['The dialogue',
     'The imagery',
     'The events happening'],index=None
)
if q16 == 'The dialogue':
    a += 1
elif q16 == 'The imagery':
    v += 1
else:
    k += 1

# Q17
q17 = st.radio(
    "While learning a new language, you like:",
    ['Speaking and listening',
     'Acting out words',
     'Reading and seeing words'],index=None
)
if q17 == 'Speaking and listening':
    a += 1
elif q17 == 'Acting out words':
    k += 1
else:
    v += 1

# Q18
q18 = st.radio(
    "When following a recipe, you prefer:",
    ['Watching the cooking video',
     'Listening to instructions',
     'Cooking while learning'],index=None
)
if q18 == 'Watching the cooking video':
    v += 1
elif q18 == 'Listening to instructions':
    a += 1
else:
    k += 1

# Q19
q19 = st.radio(
    "In exams, you recall answers by:",
    ['Remembering explanations you heard',
     'Recalling diagrams or layouts',
     'Remembering how you practiced'],index=None
)
if q19 == 'Remembering explanations you heard':
    a += 1
elif q19 == 'Recalling diagrams or layouts':
    v += 1
else:
    k += 1

# Q20
q20 = st.radio(
    "When buying clothes, you decide based on:",
    ['How it looks',
     'How it feels',
     'What others say'],index=None
)
if q20 == 'How it looks':
    v += 1
elif q20 == 'How it feels':
    k += 1
else:
    a += 1

# Q21
q21 = st.radio(
    "When learning math, you understand best through:",
    ['Solving problems',
     'Listening to explanation',
     'Seeing worked examples'],index=None
)
if q21 == 'Solving problems':
    k += 1
elif q21 == 'Listening to explanation':
    a += 1
else:
    v += 1

# Q22
q22 = st.radio(
    "In meetings, you prefer:",
    ['Hands-on involvement',
     'Clear verbal discussion',
     'Visual presentations'],index=None
)
if q22 == 'Hands-on involvement':
    k += 1
elif q22 == 'Clear verbal discussion':
    a += 1
else:
    v += 1

# Q23
q23 = st.radio(
    "When remembering directions, you recall:",
    ['The route you walked',
     'Spoken instructions',
     'Landmarks'],index=None
)
if q23 == 'The route you walked':
    k += 1
elif q23 == 'Spoken instructions':
    a += 1
else:
    v += 1

# Q24
q24 = st.radio(
    "When bored, you usually:",
    ['Move or fidget',
     'Watch something',
     'Listen to something'],index=None
)
if q24 == 'Move or fidget':
    k += 1
elif q24 == 'Watch something':
    v += 1
else:
    a += 1

# Q25
q25 = st.radio(
    "To learn faster, you prefer:",
    ['Demonstrations',
     'Practice',
     'Explanations'],index=None
)
if q25 == 'Demonstrations':
    v += 1
elif q25 == 'Practice':
    k += 1
else:
    a += 1

# Q26
q26 = st.radio(
    "When revising notes, you:",
    ['Read aloud',
     'Rewrite or draw',
     'Walk around while studying'],index=None
)
if q26 == 'Read aloud':
    a += 1
elif q26 == 'Rewrite or draw':
    v += 1
else:
    k += 1

# Q27
q27 = st.radio(
    "While playing a game, you focus more on:",
    ['Sounds and alerts',
     'Controls and actions',
     'Visual layout'],index=None
)
if q27 == 'Sounds and alerts':
    a += 1
elif q27 == 'Controls and actions':
    k += 1
else:
    v += 1

# Q28
q28 = st.radio(
    "When remembering a movie, you recall:",
    ['The scenes',
     'The dialogues',
     'The emotions and actions'],index=None
)
if q28 == 'The scenes':
    v += 1
elif q28 == 'The dialogues':
    a += 1
else:
    k += 1

# Q29
q29 = st.radio(
    "In training sessions, you like:",
    ['Doing activities',
     'Watching presentations',
     'Listening to the trainer'],index=None
)
if q29 == 'Doing activities':
    k += 1
elif q29 == 'Watching presentations':
    v += 1
else:
    a += 1

# Q30
q30 = st.radio(
    "When learning something new, you feel confident when:",
    ['You see it clearly',
     'You hear it explained',
     'You try it yourself'],index=None
)
if q30 == 'You see it clearly':
    v += 1
elif q30 == 'You hear it explained':
    a += 1
else:
    k += 1

if st.button("get result"):
    st.success(f'Visual : {v/30*100} %')
    st.success(f'Auditory : {a/30*100} %')
    st.success(f'Kinesthetic : {k/30*100} %')
    
