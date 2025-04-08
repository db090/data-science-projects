import streamlit as st

def display_quotes():
    try:
        with open("quotes.txt","r") as file:
            quotes=file.readlines()

        if quotes:
            st.markdown("### All Save Quotes")
            for i,line in enumerate(quotes):
                col1,col2 = st.columns([4,1])
                with col1:
                    st.write(line.strip())
                with col2:
                    if st.button("Delete", key=f"delete_{i}"):
                        delete_quotes(i)
                        st.rerun()
        else:
            st.info("No Quotes saved yet.")
    except FileNotFoundError:
        st.warning("No quotes file found")

def delete_quotes(index_to_delete):
    with open("quotes.txt","r") as file:
        quotes=file.readlines()
    del quotes[index_to_delete]
    with open("quotes.txt","w") as file:
        file.writelines(quotes)


def main():
    st.title("Quote Generator")
    col1,col2=st.columns(2)
    with col1:
        quote=st.text_input("Enter a quote")

    with col2:
        author=st.text_input("Enter the author's name")
    
    if st.button("Save Quote"):
        with open("quotes.txt","a") as file:
            file.write(f'"{quote}" - {author}\n')
        st.success("Quote saved to file" )
    else:
        st.warning("Please enter both quote and author")

 
    display_quotes()
if __name__ == "__main__":
    main()
