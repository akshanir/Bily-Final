import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from aitextgen import aitextgen
import BilY

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="BilY Demo", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am BilY :wave:")
    st.title("A set of smart tools for Bilingual people")
    st.write(
        "I am a Python library that every developer across the spectrum can easily use"
    )
    st.write("[Learn More >](https://en.wikipedia.org/wiki/Multilingualism)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I'm hoping to make the life of bilingual people easier and I aim to:
            - change the way we think about texting.
            - solve many of the problems bilingual people face on daily basis.
            - be easy to implement by developers
            - be efficent, fast & light(can run on any service with mutiple instances).

            If this sounds interesting to you, consider trying me out, just add \"import BilY\" to your code and start exploring what BilY can do.
            """
        )
        st.write("[source code >](https://github.com/akshanir/BilY)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
#services
with st.container():
  st.title("My Services")
  st.write(
    "now let's explore some of my features"
  )
  with st.container():
    st.title("Language Selection")
    st.write(
      "please select one or more langauge you want to use"
    )
    Arabic = st.checkbox("Arabic")
    English = st.checkbox("English")
    Italiano = st.checkbox("Italiano")
    Espanol = st.checkbox("espanol")
  #speedy input fix
  with st.container():
    st.title("super sonic input fix")
    st.write(
      "do you want to text your friends without worrying about the language or anything, this is the fastest way to do it no waiting no processing just tranform the words with the speed of light"
    )
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "اثممخ ةغ ىشةث هس شىغش بخقلثق شىي ه مهنث حثشىعفس")

    with st.spinner("AI is at Work........"):
        # text generation
        gpt_text = BilY.quickFix(prompt_text)
    st.success("AI Successfully generated the below text ")
    st.balloons()
    # print ai generated text
    print(gpt_text)

    st.text(gpt_text)

  #speedy spelling check
  with st.container():
    st.title("spelling check")
    st.write(
      "worried about spelling, don't worry BilY got you"
    )
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "اتتنتهى حدث امازون المنتظو بالإعلاخ عن مموعة من المنتجات")

    with st.spinner("AI is at Work........"):
        # text generation
        gpt_text = BilY.spellingFix(prompt_text)
    st.success("AI Successfully generated the below text ")
    st.balloons()
    # print ai generated text
    print(gpt_text)

    st.text(gpt_text)
  #speedy grammer correction
  with st.container():
    st.title("grammer helper")
    st.write(
      "BilY got your grammer right"
    )
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "Hello my name is ياسين")

    with st.spinner("AI is at Work........"):
        # text generation
        gpt_text = BilY.grammerFix(prompt_text)
    st.success("AI Successfully generated the below text ")
    st.balloons()
    # print ai generated text
    print(gpt_text)

    st.text(gpt_text)
  #speedy adding to the database
  with st.container():
    st.title("customize your own library of slang")
    st.write(
      "choose the words you wanna add to your database"
    )
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "")

    with st.spinner("AI is at Work........"):
        # text generation
        gpt_text = BilY.addSlang(prompt_text)
    # st.success("AI Successfully generated the below text ")
    st.balloons()
    # print ai generated text
    print(gpt_text)

    st.text(gpt_text)

  #adding shortcuts
  with st.container():
    st.title("add your special shortcuts")
    st.write(
      "add shortcut and the full sentence"
    )
    with st.container():
      col1, col2 = st.columns(2)

      with col1:
        prompt_text1 = st.text_input(label = "shortcut...",
                value = "")

      with col2:
        prompt_text2 = st.text_input(label = "shortfor...",
                value = "")
      x = BilY.addShortcut(prompt_text1, prompt_text2)
    st.balloons()
    st.text("added successfully" if x else "something wrong happened")


  with st.container():

    st.title("auto text generation")
    st.write("this is a fun tool to generate random text based on your input enjoy :D")
    # instantiate the model / download
    ai = aitextgen()

    # create a prompt text for the text generation 
    #prompt_text = "Python is awesome"
    prompt_text = st.text_input(label = "Enter your prompt text...",
                value = "Computer is beautiful")

    with st.spinner("AI is at Work........"):
        # text generation
        gpt_text = ai.generate_one(prompt=prompt_text,
                max_length = 100 )
    st.success("AI Successfully generated the below text ")
    st.balloons()
    # print ai generated text
    # print(gpt_text)

    st.text(gpt_text)

# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
