import random
import wikipedia
from preprocessing import preprocess_text
from unsupervised_learning import train_model
from checkpoint import save_checkpoint, load_checkpoint
from logging import log_progress

# Define the sources for articles
article_sources = ['en.wikipedia.org', 'simple.wikipedia.org', 'news.google.com']

# Initialize the checkpoint file path
checkpoint_file = 'checkpoint.pkl'

# Load the checkpoint if it exists
current_state = load_checkpoint(checkpoint_file)

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
    
    # Preprocess the article content
    processed_content = preprocess_text(article_content)
    
    # Add the processed content to the corpus
    corpus.append(processed_content)
    
    # Train the unsupervised learning model on the corpus
    model = train_model(corpus)
    
    # Save the current state of the learning process
    save_checkpoint(checkpoint_file, corpus=corpus, model=model)
    
    # Log the progress
    log_progress(i, max_articles)

    # Pause the program if the user presses Ctrl+C
    try:
        pass
    except KeyboardInterrupt:
        print('Program paused. Press Ctrl+C to resume.')
        while True:
            try:
                pass
            except KeyboardInterrupt:
                print('Program resumed.')
                break
