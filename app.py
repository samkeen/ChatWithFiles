import streamlit as st
import langchain

# Define the main function
def main():
  # Upload the file
  file = st.file_uploader("Upload your file", type=["pdf", "txt"])

  # If the user has uploaded a file, then proceed
  if file is not None:
    # Load the file into Langchain
    document = langchain.Document(file)

    # Create a chat session
    session = langchain.ChatSession(document)

    # Start the chat
    while True:
      # Get the user's input
      input = st.text_input("Enter your question")

      # If the user has entered a question, then ask Langchain for an answer
      if input != "":
        answer = session.ask(input)

        # Display the answer to the user
        st.write("Answer:", answer)

  # If the user has not uploaded a file, then display an error message
  else:
    st.error("Please upload a file")

# Run the main function
if __name__ == "__main__":
  main()