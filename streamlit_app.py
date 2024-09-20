import streamlit as st
from audio_recorder_streamlit import audio_recorder
from send_voice import send_voice
import Levenshtein
import time
import os
import random
import uuid

def generate_unique_filename():
    # セッション ID やタイムスタンプを組み合わせて一意のファイル名を生成
    session_id = str(uuid.uuid4())
    timestamp = int(time.time())
    unique_filename = f"{session_id}_{timestamp}.wav"
    return unique_filename

def stream_data(text):
    for word in list(text):
        yield word + " "
        time.sleep(0.08)

def saiten(text):
    # st.write(text)
    st.write_stream(stream_data(text))
    ultima_2=ULTIMA.replace('、','')
    text_2=text.replace('、','')
    jw=int(Levenshtein.jaro_winkler(ultima_2,text_2)*100)
    
    st.write(str(jw)+'点！')
    return jw

def rnd_image(image_directory):
    # random.seed(0)
    image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
    selected_image = random.choice(image_files)
    return selected_image

ULTIMA='渦なす生命の色、七つの扉開き、力の塔の天に至らん'
LAHABREA='./wav/Lahabrea.wav'
ATHENA='./wav/Athena.wav'

st.title("唱えろ！アルテマ！！")
st.header("　")
st.write("マイクを通して唱えろ！")
st.write("「__"+ULTIMA+"__！！」")
st.write('制限時間は10秒です')


audio_bytes = audio_recorder( energy_threshold=(-1.0, 1.0),pause_threshold=10.0,sample_rate=16000)
if audio_bytes:
    unique_filename = generate_unique_filename()
    with open(unique_filename, "wb") as f:
        f.write(audio_bytes)
        st.success("Recording saved & Voice sending...")
        text=send_voice(unique_filename)
    os.remove(unique_filename)
    st.write('___')
    
    jw=saiten(text)
    
    if jw > 80:
         file_path="./image/80_/"
    elif jw > 70:
         file_path="./image/70_/"
    elif jw > 60:
         file_path="./image/60_/"
    else:
         file_path="./image/_59/"
    img_file=rnd_image(file_path)
    st.image(file_path+img_file)

st.write('___')
if st.button("ラハブレア"):
    text_LAHABREA="宇品生命の色を七つの扉開き力の党の店に行ったら、"
    if st.audio(LAHABREA,format="audio/wav"):
          time.sleep(10)
          saiten(text_LAHABREA)

if st.button("アテナ"):
    text_ATHENA="次生命の色七つの扉開き力の店に行ったら"
    if st.audio(ATHENA,format="audio/wav"):
          time.sleep(12)
          saiten(text_ATHENA)
st.write('___')
col1, col2 = st.columns(2)
with col1:
   st.text("© SQUARE ENIX")
   st.link_button("jp.finalfantasyxiv.com","https://jp.finalfantasyxiv.com/")

with col2:
   st.text("Calocen Rieti@Chocobo")
   st.link_button("Twitter","https://x.com/calcMCalcm")
   st.link_button("blog","https://blog.calocenrieti.com/")