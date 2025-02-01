import streamlit as st
import google.generativeai as genai

# Historical figures and their speaking styles
dialogue_styles = {
    "Haile Selassie": "Regal, dignified, and focused on unity, peace, and the sovereignty of Ethiopia.",
    "Meles Zenawi": "Strategic, pragmatic, and focused on Ethiopia’s development and political economy.",
    "Mengistu Haile Mariam": "Revolutionary, focused on Marxist-Leninist ideology and the military struggle for socialism.",
    "Socrates": "Socratic method, asking deep philosophical questions and engaging in dialectic reasoning.",
    "Albert Einstein": "Analytical, thought-provoking, and often infused with wonder about the universe.",
    "Napoleon Bonaparte": "Strategic, assertive, and confident, with a focus on leadership and ambition.",
    "Cleopatra": "Persuasive, eloquent, and diplomatic, with a touch of royal authority.",
    "Karl Marx": "Critical, ideological, and focused on economic and social structures.",
    "Leonardo da Vinci": "Innovative, curious, and filled with insights on art, science, and invention.",
    "Ada Lovelace": "Technical, visionary, and structured, with a deep understanding of mathematics and computing concepts.",
    "Abraham Lincoln": "Thoughtful, persuasive, and advocating unity, equality, and democracy.",
    "William Shakespeare": "Write in poetic, dramatic tones, using iambic pentameter.",
    "Nikola Tesla": "Explain innovations in electricity and futuristic concepts.",
    "Sun Tzu": "Offer strategic insights with references to 'The Art of War'.",
    "Marie Curie": "Discuss scientific discoveries with a focus on perseverance and research.",
    "Winston Churchill": "Defiant, eloquent, and wartime rhetoric focused on determination and courage.",
    "Mahatma Gandhi": "Peaceful, persuasive, and focusing on non-violent resistance and justice.",
    "Charles Darwin": "Scientific, methodical, and filled with explanations about natural selection and evolution.",
    "Friedrich Nietzsche": "Philosophical, challenging conventional morality, and emphasizing individualism.",
    "Rosa Parks": "Firm, dignified, and unwavering in promoting civil rights and equality.",
    "Galileo Galilei": "Pioneering, scientific, with a passion for observation and discovery.",
    "Homer": "Epic, grand, and narrative in style, weaving stories of heroes and gods.",
    "Jane Austen": "Witty, sharp, and insightful on social manners, class, and relationships.",
    "Sigmund Freud": "Psychoanalytic, exploring the unconscious mind and the impact of repressed desires.",
    "Confucius": "Ethical, focused on moral teachings and societal harmony.",
    "Joan of Arc": "Defiant, inspirational, and passionate about leadership and divine purpose.",
    "Vladimir Lenin": "Revolutionary, ideological, and focused on Marxist theory and global transformation.",
    "Simone de Beauvoir": "Philosophical, feminist, exploring existentialism and gender equality.",
    "Martin Luther King Jr.": "Visionary, peaceful, and motivating with speeches on equality, justice, and non-violence.",
    "Marie Antoinette": "Elegant, royal, and with a sense of tragedy about the fall of the French monarchy.",
    "Leon Trotsky": "Revolutionary, intellectual, and deeply engaged in Marxist theory and social change."
}


# Prompting Techniques
prompt_techniques = {
    "Zero-shot": "Answer directly without examples.",
    "Chain-of-thought": "Break down reasoning step by step.",
    "Self-reflection": "Generate, critique, and refine response.",
    "Deliberate structure": "Respond in a requested format (bullets, poem, story, etc.).",
    "Multi-turn refinement": "Let the user refine their query iteratively."
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

# Configure API Key (Replace with secure storage in production)
api_key = "AIzaSyDu9D5seTlKQTaQc_9MGV-y5PHkvJscVms"

if not api_key:
    st.error("API key not found. Please add it to `secrets.toml`.", icon="🚫")
else:
    genai.configure(api_key=api_key)

    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("Timeless-Talks: AI-Generated Historical Conversations 🗣️ ")
    st.write("Engage in AI-generated dialogues with historical figures on various topics. Choose a historical personality, pick a theme, and experience an interactive discussion! You can also choose how the AI responds to your queries.")

    # Sidebar settings
    with st.sidebar:
        st.header("⚙️ Settings")
        character = st.selectbox("Choose a Character:", list(dialogue_styles.keys()))
        prompt_technique = st.selectbox("Choose Prompting Technique:", list(prompt_techniques.keys()))
        temperature_label = st.selectbox("Select Conversational Style:", list(temperature_options.keys()))
        temperature = temperature_options[temperature_label]
        max_length_label = st.selectbox("Choose Response Length:", list(max_length_options.keys()))
        max_length = max_length_options[max_length_label]

        st.write(f"**Character Profile:** {dialogue_styles[character]}")
        st.write(f"**Prompting Strategy:** {prompt_techniques[prompt_technique]}")
        st.write(f"**Response Style:** {temperature_label} ({temperature})")
        st.write(f"**Response Length:** {max_length_label} ({max_length} tokens)")

        # Learning Mode checkbox
        st.session_state.learning_mode = st.checkbox("Enable Learning Mode", value=False)
        if st.session_state.learning_mode:
            st.write("### Speaking Style")
            st.write(dialogue_styles[character])

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Enter your topic or question:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Build system prompt based on selected technique
        if prompt_technique == "Zero-shot":
            system_prompt = f"You are {character}. {dialogue_styles[character]}"
            user_prompt = prompt
        elif prompt_technique == "Chain-of-thought":
            system_prompt = f"You are {character}. {dialogue_styles[character]} Think step-by-step before answering."
            user_prompt = f"Step 1: Identify the key idea.\nStep 2: Explain using a simple analogy.\nStep 3: Give a real-world example.\n Now, answer this: {prompt}"
        elif prompt_technique == "Self-reflection":
            system_prompt = f"You are {character}. {dialogue_styles[character]} First, answer. Then, review your own response and improve it."
            user_prompt = f"Initial Answer: \n\n Now reflect and improve your response."
        elif prompt_technique == "Deliberate structure":
            system_prompt = f"You are {character}. {dialogue_styles[character]} Respond in bullet points."
            user_prompt = prompt
        elif prompt_technique == "Multi-turn refinement":
            system_prompt = f"You are {character}. {dialogue_styles[character]} Ask clarifying questions before answering."
            user_prompt = f"Ask me to refine my question before you answer: {prompt}"
        
        # Ensure response is in Amharic for the first three Ethiopian leaders
        if character in ["Haile Selassie", "Meles Zenawi", "Mengistu Haile Mariam"]:
            system_prompt = f"{system_prompt}\nRespond in Amharic."

        # Generate AI response
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"{system_prompt}\n\nUser: {user_prompt}",
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_length
            )
        )

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
