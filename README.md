# Conversational AI with Rasa

<a href="https://www.packtpub.com/product/conversational-ai-with-rasa/9781801077057?utm_source=github&utm_medium=repository&utm_campaign=9781801077057"><img src="https://static.packt-cdn.com/products/9781801077057/cover/smaller" alt="Conversational AI with Rasa" height="256px" align="right"></a>

This is the code repository for [Conversational AI with Rasa](https://www.packtpub.com/product/conversational-ai-with-rasa/9781801077057?utm_source=github&utm_medium=repository&utm_campaign=9781801077057), published by Packt.

**Build, test, and deploy AI-powered, enterprise-grade virtual assistants and chatbots**

## What is this book about?
The Rasa framework enables developers to create industrial-strength chatbots using state-of-the-art natural language processing (NLP) and machine learning technologies quickly, all in open source..

This book covers the following exciting features: 
* Use the response selector to handle chitchat and FAQs
* Create custom actions using the Rasa SDK
* Train Rasa to handle complex named entity recognition
* Become skilled at building custom components in the Rasa framework
* Validate and test dialogs end to end in Rasa

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1801077053) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
version: "2.0" 
language: en 
pipeline: 
  - name: WhitespaceTokenizer 
  - name: LanguageModelFeaturizer 
```

## Errata
* In Chapter 3, page 75, the code format should be:
```
slots:
    age:
        type: text
        influence_conversation: false
```      
        
* In Chapter 4, page 102, second paragraph should be:
RulePolicy gives the corresponding intents restat, back, and session_start for the session-level actions action_start, action_back, and action_session_start, and manages the mapping from intent to action so that session-level control can be done when system gets the intents and triggers the corresponding actions.

**Following is what you need for this book:**
This book is for NLP professionals as well as machine learning and deep learning practitioners who have knowledge of natural language processing and want to build chatbots with Rasa. Anyone with beginner-level knowledge of NLP and deep learning will be able to get the most out of the book.	

With the following software and hardware list you can run all code files present in the book (Chapter 1-11).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1 - 11   | Rasa                                | Windows, Mac OS X, and Linux (Any) |
| 1 - 11   | Python  >=3.6, <3.9                 | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781801077057_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Getting Started with Google BERT [[Packt]](https://www.packtpub.com/product/getting-started-with-google-bert/9781838821593?utm_source=github&utm_medium=repository&utm_campaign=9781838821593) [[Amazon]](https://www.amazon.com/dp/1838821597)

* Mastering spaCy [[Packt]](https://www.packtpub.com/product/mastering-spacy/9781800563353?utm_source=github&utm_medium=repository&utm_campaign=9781800563353) [[Amazon]](https://www.amazon.com/dp/1800563353)

## Get to Know the Author
**Xiaoquan** 
is a machine learning expert specializing in NLP applications. He has extensive experience in leading teams to build NLP platforms in several Fortune Global 500 companies. He is a Google developer expert in Machine Learning and has been actively involved in contributions to TensorFlow for many years. He also has actively contributed to the development of the Rasa framework since the early stage and became a Rasa Superhero in 2018. He manages the Rasa Chinese community and has also participated in the Chinese localization of TensorFlow documents as a technical reviewer.

**Guan**
is currently working on Al applications and research for the insurance industry. Prior to that, he was a machine learning researcher at several industry Al labs. He was raised and educated in Mainland China, lived in Hong Kong for 10 years before relocating to Singapore in 2020. Guan holds BSc degrees in Physics and Computer Science from Peking University, and an MPhil degree in Physics from HKUST. Guan is an active tech blogger and community contributor to open source projects including Rasa, receiving more than10,000 stars for his own projects on Github.

# Acknowledgements
Google supported this work by providing Google Cloud credit
