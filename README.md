
<h1>Unsupervised Learning News</h1>

<p>This is a project that utilizes unsupervised learning to analyze text corpora obtained from Wikipedia and other sources. The program scrapes articles from Wikipedia or a news source, preprocesses the text, and then trains an unsupervised learning algorithm to analyze the data. The program can be paused and resumed, allowing for the user to continue training the algorithm at a later time.</p>

<h2>File Structure</h2>

<p>The project's file structure is as follows:</p>

<ul>
  <li>data/
    <ul>
      <li>corpus/
        <ul>
          <li>wikipedia/</li>
          <li>gutenberg/</li>
          <li>open_american_national_corpus/</li>
        </ul>
      </li>
      <li>checkpoint/</li>
    </ul>
  </li>
  <li>src/
    <ul>
      <li>preprocessing.py</li>
      <li>unsupervised_learning.py</li>
      <li>wikipedia_scraper.py</li>
      <li>main.py</li>
    </ul>
  </li>
  <li>README.md</li>
</ul>

<h2>File Descriptions</h2>

<p><strong>preprocessing.py:</strong> Contains a set of functions that clean and preprocess the text corpus, such as removing stop words, stemming, and tokenizing.</p>

<p><strong>unsupervised_learning.py:</strong> Implements several unsupervised learning algorithms that can be used to learn patterns and relationships between words in the text corpus, such as Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorization (NMF), and Word2Vec.</p>

<p><strong>wikipedia_scraper.py:</strong> Contains a function that generates random articles from Wikipedia or news sources.</p>

<p><strong>main.py:</strong> The main program that utilizes the functions from the other files to scrape articles, preprocess the text, and train the unsupervised learning algorithm. The program can be paused and resumed, allowing for the user to continue training the algorithm at a later time.</p>

<h2>Instructions</h2>

<p>To use this program:</p>

<ol>
  <li>Clone the repository from <code>https://github.com/btt96/Unsupervised-Learning-News</code></li>
  <li>Navigate to the root directory of the project in your terminal.</li>
  <li>Install the necessary Python packages by running <code>pip install -r requirements.txt</code>.</li>
  <li>Run <code>python src/main.py</code> to start the program.</li>
</ol>

<p>Follow the instructions provided in the program to pause and resume the training process.</p>

<h2>Contributing</h2>

<p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="https://github.com/btt96/pUnsupervised-Learning-News/blob/main/LICENSE">LICENSE</a> file for details.</p>
