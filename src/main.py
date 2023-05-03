import random
import wikipedia
from text_corpus import TextCorpus
from preprocessing import Preprocessing
from unsupervised_learning import UnsupervisedLearning
from checkpoint import Checkpoint
from logging import Logging

# Define the sources for articles
article_sources = ['en.wikipedia.org', 'simple.wikipedia.org', 'news.google.com']

# Initialize the checkpoint file path
checkpoint_file = 'checkpoint.pkl'

# Load the checkpoint if it exists
current_state = Checkpoint(checkpoint_file).load()

# Initialize the corpus and model
corpus = current_state['corpus'] if 'corpus' in current_state else []
model = current_state['model'] if 'model' in current_state else None

# Define the maximum number of articles to generate
max_articles = 1000

# Generate articles and perform unsupervised learning
for i in range(max_articles):
    # Choose a random article source
    source = random.choice(article_sources)

    # Generate a random article title
    article_title = wikipedia.random(pages=1)

    # Get the article content from Wikipedia
    try:
        article_content = wikipedia.page(article_title, auto_suggest=False, redirect=False, preload=False, 
                                          original_title='', pageid=None, follow_redirects=True, 
                                          content=True, summary=False, 
                                          redirect_count=0, preload_content=True, lang='en', 
                                          extract_format=wikipedia.ExtractFormat.HTML).content
    except wikipedia.exceptions.PageError:
        continue
    except wikipedia.exceptions.DisambiguationError:
        continue
    
    # Initialize the TextCorpus class and preprocess the article content
    text_corpus = TextCorpus(path=None)
    processed_content = ' '.join(text_corpus.clean_text(text_corpus.read_text(article_content)))
    
    # Initialize the Preprocessing class and remove punctuations and perform stemming
    preprocessing = Preprocessing()
    processed_content = preprocessing.remove_punctuations(processed_content)
    processed_content = ' '.join(preprocessing.stemming(processed_content.split()))
    
    # Add the processed content to the corpus
    corpus.append(processed_content)
    
    # Train the unsupervised learning model on the corpus
    unsupervised_learning = UnsupervisedLearning(algorithm='LDA')
    model = unsupervised_learning.train(corpus)
    
    # Save the current state of the learning process
    Checkpoint(checkpoint_file).save({'corpus': corpus, 'model': model})
    
    # Initialize the Logging class and log the progress
    logging = Logging()
    logging.log_info(f"{i+1} articles processed out of {max_articles}.")
    
    # Pause the program if the user presses Ctrl+C
    try:
        pass
    except KeyboardInterrupt:
        logging.log_info('Program paused. Press Ctrl+C to resume.')
        while True:
            try:
                pass
            except KeyboardInterrupt:
                logging.log_info('Program resumed.')
                break
