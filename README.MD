<h1>LinkedIn SERP Scraper</h1>
<p>LinkedIn SERP scraper fetches results of LinkedIn public profiles from <a href="https://www.bing.com/"> Bing </a> search engine result page and returns result in JSON format</p>
<div>
<h1>Setup</h1>
<ol>
<li> Clone this project</li>
<li>Install dependencies mentioned inside <code>requirements.txt</code></li>
</ol>
</div>
<div>
<h1>How to use?</h1>
<h2>In the project directory:</h2>
<br>
<h3>To scrap single linkedin profile: </h3>
<code>$ python3 script.py --linkedin_url < url > </code>
<br>
<b>Argument:</b>
<li><code>linkedin_url</code> is the linkedin profile URL.
For example, if user wants to scrap this URL<code> https://in.linkedin.com/in/koushik-majumder-6172b412a
 </code>, the command line argument will look like <br><code>python3 script.py --linkedin_url https://in.linkedin.com/in/koushik-majumder-6172b412a
</code>
</li>
</div>
<br>

<hr>
<div>
<h3>To scrap multiple linkedin profile: </h3>
<code>$ python3 script.py --filename < filepath > </code>

<br>
<b>Argument:</b>
<li><code>filename</code> is the path of the CSV file which contains all profile URLs separated by newline. For example: <code>file.csv</code> is located at <code>/usr/documents/file.csv </code> </li> then the command line argument will look like <br>
<code> python3 script.py --filename /usr/documents/file.csv </code>
<br>
<hr>
</div>
<div>
<h3>Help: </h3>
<code>$ python3 script.py -h</code>
</div>
<br>
<hr>
<div>
</div>

<div>
<h1>Tech</h1>
<li><a href="https://selenium-python.readthedocs.io/">Selenium</a></li>
<li><a href="https://python.org">Python</a></li>
</div>
<br>
<div>
<h1>Privacy</h1>
This scraper only scrapes public data available to unauthenticated user and does not holds the capability to scrap anything private.
</div>
<br>
<div>
<h1>LICENSE</h1>
<h3>MIT</h3>
</div>
