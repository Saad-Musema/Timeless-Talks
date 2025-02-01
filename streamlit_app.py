import streamlit as st
import google.generativeai as genai

# Historical figures and their speaking styles
dialogue_styles = {
    "Socrates": "Socratic method, asking deep philosophical questions and engaging in dialectic reasoning.",
    "Albert Einstein": "Analytical, thought-provoking, and often infused with wonder about the universe.",
    "Napoleon Bonaparte": "Strategic, assertive, and confident, with a focus on leadership and ambition.",
    "Cleopatra": "Persuasive, eloquent, and diplomatic, with a touch of royal authority.",
    "Karl Marx": "Critical, ideological, and focused on economic and social structures.",
    "Leonardo da Vinci": "Innovative, curious, and filled with insights on art, science, and invention.",
    "Ada Lovelace": "Technical, visionary, and structured, with a deep understanding of mathematics and computing concepts.",
    "Abraham Lincoln": "Thoughtful, persuasive, and advocating unity, equality, and democracy."
}

# AI temperature settings for conversation variation
temperature_options = {
    "Very Dynamic": 1.0,
    "Balanced": 0.7,
    "Realistic": 0.3,
    "Historical Accuracy": 0.2
}

# Response length options
max_length_options = {
    "Concise": 50,
    "Balanced": 150,
    "In-Depth": 300
}

st.title("🗣️ AI-Generated Historical Conversations")
st.write("Engage in AI-generated dialogues with historical figures on various topics. Choose a historical personality, pick a theme, and experience an interactive discussion!")

api_key = "AIzaSyASnkyIRB2Abu4qUY8yfI8K_2sYLqhh5io"

if not api_key:
    st.error("API key not found. Please add it to `secrets.toml`.", icon="🚫")
else:
    genai.configure(api_key=api_key)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    with st.sidebar:
        temperature_label = st.selectbox("Select Conversational Style:", list(temperature_options.keys()))
        temperature = temperature_options[temperature_label]
        
        max_length_label = st.selectbox("Choose Response Length:", list(max_length_options.keys()))
        max_length = max_length_options[max_length_label]
        
        st.write(f"**Response Style:** {temperature_label} ({temperature})")
        st.write(f"**Response Length:** {max_length_label} ({max_length} tokens)")
        
        st.header("Choose Historical Figures")
        selected_figure = st.selectbox("Select a figure to converse with:", list(dialogue_styles.keys()))
        
        st.session_state.learning_mode = st.checkbox("Enable Learning Mode", value=False)
        
        if st.session_state.learning_mode:
            st.write("### Speaking Style")
            st.write(dialogue_styles[selected_figure])

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Enter your topic or question:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        style_context = dialogue_styles[selected_figure]
        system_message = (
            f"You are {selected_figure}, engaging in a discussion with the user. "
            f"Maintain your historical speech style: {style_context}"
        )

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"{system_message}\n\nUser: {prompt}",
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_length
            )
        )
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
