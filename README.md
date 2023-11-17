# Scripted Sisterhood: An Analysis of Women's Representation in Movies Using Bechdel Test
*Pandamonium: Tiago Freitas, Deniz Kasap, Riza Arseven, Eren Saydar and Matthijs Scheerder*

## Abstract
The Bechdel Test is a simple test to measure the prominence of women in movies. The test consists of three conditions to be satisfied:
1. The cast of the movie contains two women characters,
2. They talk to each other,
3. About a topic besides man.
   
Recently, this test is gaining prominence in academic circles as a benchmark for evaluating the representation of women in films. Recently, another metric has been introduced to measure female representation, the female cast ratio (Yang et al., 2020). It is interesting to research how this relates to the Bechdel test. 

<!-- I also like these titles:
'Scripted Sisterhood: Bechdel Test vs Female Cast Ratio
"Femme Frames Unveiled: A Bechdel Test vs. Female Cast Ratio Exploration
Femme Metrics: A Comparative Analysis of Bechdel and Female Cast Ratio -->

In "Scripted Sisterhood," we scrutinize the portrayal of women in film through the Bechdel Test. Our data-driven exploration investigates patterns and disparities in gender representation, sparking a conversation about storytelling's societal impact. Recent films like Oppenheimer and Avatar 2, failing the Bechdel Test, underscore its continued relevance. This project aims to unveil insights into cinematic narratives from the gender perspective.


## Research Questions
1. Can we develop a formulation that accounts for the representation of women in movies?
2. Introducing the Bechdel test, how are these scores and trends changed along with the other attributes?
3. Is it possible to see a discrepancy comparing the women's representation score and the Bechdel test?
4. Can we combine the Bechdel test and the women's representation score in one unified predictor for movie success?

## Proposed Additional Datasets
-[**Bechdel Test**](https://bechdeltest.com/) - The Bechdel Test Movie List, comprising more than 10,130 movies, is retrieved through its API, offering a dataset with seven fields. Key features include imdbid (facilitating integration with other datasets), title, year, and rating. The rating scale delineates the Bechdel Test outcomes: 0 signifies the absence of two women, 1 indicates no conversation, 2 denotes discussion about a man, and 3 signifies a successful passage of the test. 


-[**Inflation (CPI)**](https://www.officialdata.org/us/inflation/1923?amount=1) - In order to ensure a fair comparison of revenue/box office data between different movies we need to adjust for inflation. Since the box office revenue is listed in USD, we use historical data. By normalizing financial figures for inflation, we aim to assess the financial success of movies in real dollars, facilitating meaningful comparisons across different years.

## Methods
### Bechdel Test Feature Addition:
The vanilla CMU dataset does not contain the Bechdel Test Score for the movies. However, using an additional dataset that accounts for this, we may add this feature as a new column to our dataset. The aforementioned dataset contains the Bechdel score, year, and movie name for more than 10,000 movies. In order to add this new column, we took the intersection of two datasets, by iteratively comparing the name of the movies. However, we observed that for the same movie, names on two datasets may not exactly match, due to some typos. For this, we have utilized some string-matching algorithms between datasets. We are running Fuzzy String-Matching algorithm on the two names and if they are above a certain threshold, we check the years on two datasets. If they match, that particular movie is added to the intersection dataset. Without the string-matching, we have 5553 movies on the intersection dataset, whereas, with the matching, we raise that number to 6521, which is favorable for us to have an intersection as big as possible.

## Data Analysis
Utilizing the visualization tools we learned in the lecture, like line plots, bar plots, box plots, and histograms to do the first initial data analysis to extract some preliminary conclusions and get a visualization of the data to get the project rolling.

### Linear Regression: OLS
We want to predict the movie success by finding a correlation between different variables, focusing on the women's participation metrics the Bechdel test, and female cast ratio. Movie success can be defined broadly by either box office revenue, ratings, ROI, etc.


## Proposed timeline

We have decided to have 2 internal deadlines for each week: Tuesday and Friday.  

- 17.11.23: **Project milestone 2 deadline**
---
- 21.11.23: Start with more in-depth statistical analysis. Review past work/progress, 
- 24.11.23: Finish statistical analysis
---
- 28.11.23: Each member works on homework 2
- 1.12.23: **Homework 2 deadline**
---
- 5.12.22: Linear Regression/advanced methods for prediction. Start advanced visualization.
- 8.12.22: Finish visualizations and refinements. Review past work/progress, and alter the plan if necessary. 
---
- 12.12.22: All technical parts finished, start with datastory (website development).
- 15.12.22: Finish data story
---
- 20.12.22: Check all deliverables and update README. Deliberately scheduled less to have some buffer time.
- 22.12.22: **Project milestone 3 deadline** 



## Organisation within the team

We try to work as one team on the weekly internal deadlines of the proposed timeline. Based on our planning the workload will be divided.
Nonetheless, we assign some overall responsibilities of the project for each person, based on strengths and interests. 

<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Tiago</td>
    <td class="tg-0lax">Initial data analysis<br><br>Visualizations<br><br>Notebook organisation</td>
  </tr>
  <tr>
    <td class="tg-0lax">Deniz</td>
    <td class="tg-0lax">Additional Datasets<br><br>Scraping<br><br>Advanced coding</td>
  </tr>
  <tr>
    <td class="tg-0lax">Eren</td>
    <td class="tg-0lax">website development<br><br>Develop textual context for data story<br><br>Statistical Analysis</td>
  </tr>
  <tr>
    <td class="tg-0lax">Riza</td>
    <td class="tg-0lax">Initial data analysis<br><br>Overall planning/responsible for meetings with mentor<br><br>Develop textual context for data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Matthijs</td>
    <td class="tg-0lax">Statistical Analysis<br><br>Visualizations<br><br>README</td>
    </tr>
</tbody>
</table>

## Sources
Valentowitsch, J. Hollywood caught in two worlds? The impact of the Bechdel test on the international box office performance of cinematic films. Mark Lett 34, 293–308 (2023). https://doi.org/10.1007/s11002-022-09652-5

Luoying Yang, Zhou Xu, and Jiebo Luo. 2020. Measuring Female Representation and Impact in Films over Time. ACM/IMS Trans. Data Sci. 1, 4, Article 30 (November 2020), 14 pages. https://doi.org/10.1145/3411213


