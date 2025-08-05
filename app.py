st.header(" Python Cheat Code")

with open ("python_cheat.txt:, "r")
as file: 
     content = file.read()
    st.text_area("Cheat Sheet",
content ,height =400)

