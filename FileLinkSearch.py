from googlesearch import search
import streamlit as st
from streamlit_option_menu import option_menu
import time

#####  setting page

st.set_page_config(
    page_title="File Searcher",
    page_icon="📑",
    initial_sidebar_state="collapsed"
)

###  side bar
SideBar = st.sidebar

with SideBar:
    st.write("## 📑 File Searcher")
    st.write("---")
   

with SideBar:   #######  menu bar
    SelectMenu =  option_menu(
        menu_title="Menu",
        menu_icon="menu-button",
        options=["File Searcher","App Info","Developer Info"],
        icons=["search","info-circle","person"]
    )


#########  social links
SocialLinks = {
    "Linkedin":"https://www.linkedin.com/in/nishantmaity",
    "Github":"https://github.com/Nishant43S/",
}

Githubid = list(SocialLinks.keys())[1]
Githuburl = list(SocialLinks.values())[1]

Linkedinid = list(SocialLinks.keys())[0]
Linkedinurl = list(SocialLinks.values())[0]

with SideBar:
    link = st.expander("Social Links")
    with link:
        st.write(f"[{Linkedinid}]({Linkedinurl})")
        st.write(f"[{Githubid}]({Githuburl})")
    
    for Blankspace in range(13):
        st.text("")
    st.write("Developer: Nishant Maity")

FrontPageText = """
        You can search any kind of file 📑 Like pdf,pptx,mp4,icon , etc you will get download link of 
        the web pages. according to your search.\n
        to create this types of projects Visit [StreamlitDoc](https://docs.streamlit.io/get-started) website 
"""

if SelectMenu == "File Searcher":
    st.header("File links Searcher")
    st.write(FrontPageText)
    Form = st.form(border=False,key="Form")   ########  input fields
    with Form:
        SearchFile = st.text_input(
            label="Search File",type="default",
            placeholder="Search pdf,ppt,csv files",
            disabled=False
        )
        
        FileCol1,FileCol2 = st.columns([5,3])

        with FileCol1:
            Number_of_Results = st.slider(
                label="Number of Results",min_value=1,
                max_value=150,value=15,
                step=1
            )
        with FileCol2:
            FileType = st.selectbox(
                label="File Type",
                options=["pdf",'docs',"pptx","ico","csv","docx","png","xlxs","mp4","jpg","gif","mp3"] ,
                index=0
            )
        SubMitBtncol , ResultsGenerate = st.columns([3,6])

        with SubMitBtncol:
            GetFiles = st.form_submit_button("Generate",use_container_width=True)
        with ResultsGenerate:
            if GetFiles:
                GeneratedResult = f"ㅤㅤㅤㅤㅤㅤㅤFile: {FileType}ㅤㅤㅤㅤResults: {Number_of_Results}"
                def stream_data():
                    for word in GeneratedResult.split(" "):
                        yield word + " "
                        time.sleep(0.02)
                st.write_stream(stream_data)
        if not SearchFile:
            st.stop()
        else:
            pass

        if GetFiles:
            if __name__=="__main__":
                try:
                    Quarary = (f"filetype {FileType}:{SearchFile}")
                    Result = search(
                        term=Quarary,
                        num_results=Number_of_Results,
                        sleep_interval=5,timeout= 2,
                        advanced=True
                    )
                    with st.spinner(text='Generating...'):
                        time.sleep(3)
                    st.toast(body=SearchFile,icon="📑")
                    for i in Result:
                        res = i.url
                        st.write(res)

                except Exception as err:
                    Error = f"Too many requests{err}"
                    st.info(Error)

if SelectMenu == "App Info":
    st.header("App Info")
    st.write("---")
    InfoText = """
            Get direct link of the files like ppt , exel ,png ,icon etc.you will get the download links of the files
            """
    st.write(InfoText)
    st.subheader("How to use")
    st.write("Enter Your query in the search box")
    st.write("Select file type according to your query")
    st.write("Select number of results you want")
    st.write("Click on Generate Button")

    st.write("---")
    st.subheader("Modules Used")
    st.markdown(
        """
            <ul>
                <li>Streamlit</li>
                <li>googlesearch-python</li>
                <li>time</li>
            </ul>
        """,
        unsafe_allow_html=True
    )



if SelectMenu == "Developer Info":
    st.header("Developer Info")
    st.write("---")
    st.write("Created by Nishant Maity")
    st.subheader("Education: ")
    st.write("ORIENTAL UNIVERSITY Indore")
    st.subheader("Field of Study")
    st.write("(BCA) Bachelor's degree, Computer Science Engineering")
    st.subheader("contact")
    st.markdown(
        """
        <ul>
            <li><a href="https://www.linkedin.com/in/nishantmaity">Linkedin</a></li>    
            <li><a href="https://github.com/Nishant43S/">Github</a></li>
            <li><a href="https://www.instagram.com/invites/contact/?i=1kgck1bm2send&utm_content=m95jbmo">instagram</a></li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    st.write("---")