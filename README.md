
<h1>Unsupervised Learning News</h1>

<p>This is a project that utilizes unsupervised learning to analyze text corpora obtained from Wikipedia and other sources. The program scrapes articles from Wikipedia or a news source, preprocesses the text, and then trains an unsupervised learning algorithm to analyze the data. The program can be paused and resumed, allowing for the user to continue training the algorithm at a later time.</p>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.6+</li>
        <li>NLTK</li>
        <li>scikit-learn</li>
        <li>gensim</li>
        <li>Wikipedia API</li>
    </ul>

    <h2>Files</h2>
    <ul>
        <li><code>text_corpus.py</code>: Defines the <code>TextCorpus</code> class for reading and cleaning text from a file.</li>
        <li><code>preprocessing.py</code>: Defines the <code>Preprocessing</code> class for removing punctuation and stemming words.</li>
        <li><code>unsupervised_learning.py</code>: Defines the <code>UnsupervisedLearning</code> class for training unsupervised learning models using Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorization (NMF), or Word2Vec.</li>
        <li><code>checkpoint.py</code>: Defines the <code>Checkpoint</code> class for saving and loading models.</li>
        <li><code>logging.py</code>: Defines the <code>Logging</code> class for logging progress and errors.</li>
        <li><code>main.py</code>: The main program that generates articles, preprocesses the text, trains the unsupervised learning model, and logs progress.</li>
    </ul>

    <h2>Usage</h2>
    <p>To run the program, simply execute the <code>main.py</code> file.</p>

    <code>$ python main.py</code>

    <p>The program will generate a maximum of 1000 articles and perform unsupervised learning on the corpus. The program will save its progress after each article and can be resumed if interrupted.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>

