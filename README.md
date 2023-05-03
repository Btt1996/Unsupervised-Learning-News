
   <!DOCTYPE html>
<html>
  <head>

  </head>
  <body>
    <h1>Unsupervised Learning News</h1>
    <p>
      This is a project that utilizes unsupervised learning to analyze text corpora obtained from Wikipedia and other sources. The program scrapes articles from Wikipedia or a news source, preprocesses the text, and then trains an unsupervised learning algorithm to analyze the data. The program can be paused and resumed, allowing for the user to continue training the algorithm at a later time.
    </p>
     <h2>Requirements</h2>
    <ul>
        <li>Python 3.6+</li>
        <li>NLTK</li>
        <li>scikit-learn</li>
        <li>gensim</li>
        <li>Wikipedia API</li>
    </ul>
    <h2>Project Structure</h2>
    <pre>
    project_name/
    ├── data/
    │   ├── corpus/
    │   │   ├── wikipedia/
    │   │   └── ...
    │   └── checkpoint/
    ├── src/
    │   ├── preprocessing.py
    │   ├── unsupervised_learning.py
    │   ├── ...
    │   └── main.py
    ├── README.md
    └── ...
    </pre>
    <h2>Description</h2>
    <p>
      The Unsupervised Learning News project aims to help researchers and data scientists who are working with text data from news sources. The program provides an easy-to-use tool that can scrape news articles from multiple sources, preprocess the text, and then analyze it using unsupervised learning algorithms.
    </p>
    <h2>Utilities</h2>
    <p>
      The program provides the following utilities:
    </p>
    <ul>
      <li>Scraping articles from multiple sources (currently supports Wikipedia and news websites)</li>
      <li>Preprocessing text data to remove stopwords, punctuations, and other irrelevant information</li>
      <li>Training unsupervised learning algorithms such as LDA and LSA to cluster similar articles together</li>
      <li>Pausing and resuming the training process, allowing the user to continue from where they left off</li>
      <li>Outputting the results in a user-friendly format, such as HTML or PDF</li>
    </ul>
    <h2>How to Use</h2>
    <p>
      To use the program, simply run the main.py file in the src directory. The program will prompt the user to select the source of the articles, the number of articles to scrape, and the unsupervised learning algorithm to use. After the program finishes running, the user can find the output files in the data directory.
    </p>
    <h2>Clone this Repository</h2>

<p>To clone this repository and create the necessary file structure, run the following commands in your terminal:</p>

<pre><code>git clone https://github.com/Btt1996/Unsupervised-Learning-News.git
cd Unsupervised-Learning-News
mkdir -p data/corpus/wikipedia
mkdir -p checkpoint
</code></pre>

<p>These commands will clone the repository to your local machine and create the necessary file structure for storing the data corpus and model checkpoints.</p>

<p>Once you have created the file structure, you can start running the program by running the <code>main.py</code> file.</p>

<p>For more information on how to use the program, please refer to the <code>README.md</code> file or visit the <a href="https://github.com/Btt1996/Unsupervised-Learning-News">GitHub repository</a>.</p>

    <section>
  <h2>Log File</h2>
  <p>The main file generates a log file that contains information about the program's progress and any errors that occur during execution. The log file is located in the same directory as the main file and has the name <code>log.txt</code>. Here's an example of what the log file might look like:</p>
  <pre>
[2023-05-03 13:52:17] INFO: Starting program
[2023-05-03 13:52:17] INFO: Loading Wikipedia corpus
[2023-05-03 13:52:20] INFO: Preprocessing text data
[2023-05-03 13:52:30] INFO: Training unsupervised learning algorithm
[2023-05-03 13:53:12] INFO: Saving checkpoint
[2023-05-03 13:53:12] INFO: Program complete

  </pre>
  <p>In this example, the log file shows that the program started at 13:52:17 on May 3, 2023, and finished at 13:53:12. It also shows that the program loaded a Wikipedia corpus, preprocessed the text data, and trained an unsupervised learning algorithm. Finally, it shows that the program saved a checkpoint and completed successfully. If any errors occurred during execution, they would also be logged in the file with a corresponding error message and timestamp.</p>
</section>

  

   <h2>License</h2>
   <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>
  </body>
</html>


