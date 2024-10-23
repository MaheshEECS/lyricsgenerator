# Lyrics-Generator  
(https://maheshlyricsgenerator.streamlit.app/)

![Lyrics Writing Bot](https://img.shields.io/badge/streamlit-v1.13.0-green) ![Python](https://img.shields.io/badge/python-v3.8%2B-blue)

**Lyrics Writing Bot Python**

## Overview  
The Lyrics Generator is a Streamlit application designed to assist lyricists in generating and refining lyrics. Utilizing Google's generative AI capabilities, this bot helps users create rhymes, maintain syllable counts, and provides creative rewrites while ensuring a playful and whimsical tone.

## Features  
- **Interactive Chat Interface**: Engage with the bot to get instant lyrical assistance.
- **Customizable Lyrics Generation**: Provide prompts and get tailored responses that maintain rhyme schemes and syllable counts.
- **Safety Settings**: The bot incorporates safety measures to avoid generating harmful content.

## Getting Started

### Prerequisites  
- Python 3.8 or higher  
- Streamlit library  
- Google Generative AI library  

### Installation  

**Clone the Repository**:  
```
git clone https://github.com/MaheshEECS/lyricsgenerator.git
cd lyricsgenerator
```

**Install Required Packages**:  
```
pip install -r requirements.txt
```

**Set Up Configuration**:  
Add your Google Generative AI API key using Streamlit's Secrets Management.  

## Running the App  
To start the application, run the following command:  
```
streamlit run Bot.py
```

Open your web browser and navigate to `http://localhost:8501` to access the Lyrics Writing Bot.

## Usage  
- **Input Your Prompt**: Type your lyrics-related query into the input box.  
- **Receive Suggestions**: The bot will respond with creative lyric ideas while adhering to your original request.  
- **Iterate as Needed**: Continue the conversation for further refinements or new ideas.

### Example Prompts  
- "Can you help me rewrite this chorus to make it more playful?"  
- "I need some rhymes for the word 'heart'."  
- "How can I maintain the same syllable count but change the theme of these lyrics?"

## Code Explanation  
- The app utilizes Streamlit for the web interface and Google Generative AI for lyric generation.  
- The lyrics generation is controlled by a tailored prompt that sets the context and instructions for the model.  
- Safety measures are implemented to filter out harmful or inappropriate content.

## Contributing  
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## License  
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments  
- Streamlit - for creating an easy-to-use framework for building web apps.  
- Google Generative AI - for providing the underlying AI capabilities.
