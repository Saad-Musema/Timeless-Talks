# [Timeless-Talks](https://timeless-talks.streamlit.app/): AI-Generated Historical Conversations 🗣️

## Overview

**Timeless-Talks** is an interactive web application built with Streamlit that allows users to engage in AI-generated dialogues with historical figures. The app simulates the speaking styles of notable personalities and enables users to converse on a variety of topics. The AI model uses Google’s Gemini API to generate contextually relevant responses, and users can select from an extensive list of characters, including figures like Haile Selassie, Meles Zenawi, and many others.

### Project Highlights:
- **Generative AI**: Utilizes Google’s Gemini API to generate conversational content that mimics the speaking styles of historical figures.
- **Customizable Experience**: Users can select from a variety of famous figures or customize the conversation style.
- **Speaking Styles**: The chatbot generates responses based on each figure's unique speaking style, offering an engaging and educational experience.
- **Amharic Support**: The app aims to support Amharic-speaking characters like Haile Selassie and Meles Zenawi, though response accuracy may vary compared to other languages.

---

## Features:
- **Character Selection**: Choose from a wide range of historical personalities such as Haile Selassie, Meles Zenawi, and more.
- **Dynamic Conversation**: Engage in dialogues with AI that adjusts its tone and content based on the selected character's style.
- **Temperature & Response Length**: Select from various response lengths and styles, ensuring flexibility in the conversation.
- **Learning Mode**: Toggle the learning mode to understand more about the character’s speech and historical context.

---

### Prompting Techniques Utilized in the Codebase

1. **Role-Playing with Instructional Prompts:**
   - Explicit instructions are given to the model to simulate the speaking style and tone of a historical figure (e.g., "Respond as Haile Selassie, the Emperor of Ethiopia").

2. **Emotional Tone Calibration:**
   - Adjusts the emotional impact of responses to reflect the personality and mood of the historical figure (e.g., "Use a curious tone as Albert Einstein").

3. **Historical Event Framing:**
   - Frames responses around historical events, providing context to the figure’s thoughts and actions during specific times (e.g., "Describe your thoughts on Ethiopia's resistance in 1935 as Haile Selassie").

4. **User-Driven Customization (User-defined Prompts):**
   - Allows users to customize tone, topics, or emotional depth, offering a tailored experience based on individual preferences.

These techniques ensure **Timeless-Talks** creates dynamic, authentic, and historically accurate conversations with historical figures.


## How It Works:

### 1. **Character Selection**:
   - Users choose from a list of famous figures like Haile Selassie, Meles Zenawi, Albert Einstein, and others.
   - The app tailors the conversation to reflect the selected character’s speech and historical context.
   
### 2. **Prompting Techniques**:
   The app employs several prompting techniques for generating text, including:
   - **Zero-shot**: Direct responses without examples.
   - **Chain-of-thought**: Break down reasoning step by step.
   - **Self-reflection**: Generate, critique, and refine the response.
   - **Deliberate structure**: Respond in a specified format (e.g., bullet points, poems).
   - **Multi-turn refinement**: Refine the user’s question for more accurate answers.

### 3. **Temperature Settings**:
   The temperature controls the creativity of the AI's responses. Higher temperatures yield more creative and diverse answers, while lower temperatures give more realistic and consistent outputs. Available options include:
   - **Very Dynamic** (1.0): Creative and diverse responses.
   - **Balanced** (0.7): A mix of creativity and coherence.
   - **Realistic** (0.3): Straightforward and factual responses.
   - **Historical Accuracy** (0.2): Very focused on delivering accurate historical content.

### 4. **Response Length**:
   The max length setting controls how long the AI’s response will be. Options include:
   - **Concise** (50 tokens)
   - **Balanced** (150 tokens)
   - **In-Depth** (300 tokens)

---

## Known Issues:

- **Amharic Responses**: While the app attempts to generate conversations in Amharic for Ethiopian figures like Haile Selassie and Meles Zenawi, the quality and accuracy of responses in Amharic may not be as reliable as responses in English or other languages. The AI’s performance in generating Amharic dialogue may vary depending on the context and complexity of the prompt.

---

## Tech Stack:
- **Frontend**: Streamlit (for an interactive web interface)
- **Backend**: Python (to handle AI model requests)
- **Generative Model**: Google’s Gemini API (for generating text-based responses)
- **Deployment**: Streamlit cloud for easy access by users

---

## Installation:

### 1. Clone the Repository:
```bash
git clone https://github.com/YourUsername/Timeless-Talks.git
cd Timeless-Talks
```

### 2. Install Required Libraries:
```bash
$ pip install -r requirements.txt
```

### 3. Run the App:
```bash
$ streamlit run app.py
```
---


Enjoy exploring timeless conversations with history’s greatest minds! 🕰️💬
