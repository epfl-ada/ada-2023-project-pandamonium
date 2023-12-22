# Scripted Sisterhood: An Analysis of Women's Representation in Movies Using Bechdel Test
*Pandamonium: Tiago Freitas, Deniz Kasap, Riza Arseven, Eren Saydar and Matthijs Scheerder*

## Datastory
Gender equality is a pressing issue in today's world, and for good reason. Consequently, we are dedicated to exploring women's representation in the world of cinema. Join us in our quest to find out how well represented women really are and see how we try redefine the metrics for women's representation in our [Datastory](https://matthijsscheerder.github.io/PandamoniumWebsite/)!

## Abstract I write this last

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

-[**GII**](https://ourworldindata.org/grapher/gender-inequality-index-from-the-human-development-report?tab=chart) - The Gender Inequality Index can be readily downloaded and is used to enhance our dataset. .This index provides a comprehensive (quantitative) view of the challenges women face in different countries, highlighting areas where progress is needed to achieve greater gender equality. The lower the value the higher the equality between genders.

-[**HDI**](https://ourworldindata.org/grapher/human-development-index) - The Human Development Index can be readily downloaded and is used to enhance our dataset. This index offers valuable insights into a country's progress in improving the living standards and quality of life for its citizens. We want to see if this is also a predictor for women's represenation in cinema.


## Methods
### Bechdel Test Feature Addition:
The vanilla CMU dataset does not contain the Bechdel Test Score for the movies. However, using an additional dataset that accounts for this, we may add this feature as a new column to our dataset. The aforementioned dataset contains the Bechdel score, year, and movie name for more than 10,000 movies. In order to add this new column, we took the intersection of two datasets, by iteratively comparing the name of the movies. However, we observed that for the same movie, names on two datasets may not exactly match, due to some typos. For this, we have utilized some string-matching algorithms between datasets. We are running Fuzzy String-Matching algorithm on the two names and if they are above a certain threshold, we check the years on two datasets. If they match, that particular movie is added to the intersection dataset. Without the string-matching, we have 5553 movies on the intersection dataset, whereas, with the matching, we raise that number to 6521. It is favorable for us start with a dataset as large as possible.

### Natural Language Processing
#### Gender density




#### Actor mentioning



#### Sentiment analysis





####






### Linear Regression: OLS
We want to predict the movie success by finding a correlation between different variables, focusing on the women's participation metrics the Bechdel test, and female cast ratio. Movie success can be defined broadly by either box office revenue, ratings, ROI, etc.


## Executed timeline
Due to receiving a low grade on our Milestone 2, it was necessary to revisit and revise our project. Consequently, our project timeline has also undergone significant changes. Since we got the feedback late we also had to radically alter our planning.  

- 17.11.23: **Project milestone 2 deadline**
---
- 1.12.23: Discuss feedback of Milestone 2 with mentor.
---
- 05.12.23: Redo Milestone 2, keep the things that are usable. Work out new research questions and overall goal of the project.
- 08.12.23: Gather necessary additional datasets and make start 
---
- 12.12.23: 
- 15.12.23: 
- 18.12.23
---
- 20.12.23: Gather all necessary plots
- 21.12.23: Make up datastory & alter plots for interactive use 
- 22.12.23: **Project milestone 3 deadline** 



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
    <td class="tg-0lax">Data Analysis<br><br>Visualizations<br><br>Notebook organisation</td>
  </tr>
  <tr>
    <td class="tg-0lax">Deniz</td>
    <td class="tg-0lax">Machine learning<br><br>Scraping<br><br>Advanced coding</td>
  </tr>
  <tr>
    <td class="tg-0lax">Eren</td>
    <td class="tg-0lax">Scraping<br><br>Website & Datastory<br><br>Statistical Analysis</td>
  </tr>
  <tr>
    <td class="tg-0lax">Riza</td>
    <td class="tg-0lax">Natural Language Processing<br><br>Overall planning<br><br>Visualizations</td>
  </tr>
  <tr>
    <td class="tg-0lax">Matthijs</td>
    <td class="tg-0lax">Machine learning<br><br>Website & Datastory<br><br>README</td>
    </tr>
</tbody>
</table>

## Sources
Luoying Yang, Zhou Xu, and Jiebo Luo. 2020. Measuring Female Representation and Impact in Films over Time. ACM/IMS Trans. Data Sci. 1, 4, Article 30 (November 2020), 14 pages. https://doi.org/10.1145/3411213


