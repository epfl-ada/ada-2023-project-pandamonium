# Beyond the Bechdel Test: A New Era of Measuring Women's Representation in Cinema
*Pandamonium: Tiago Freitas, Deniz Kasap, Riza Arseven, Eren Saydar and Matthijs Scheerder*

## Datastory
Gender equality is a pressing issue in today's world, and for good reason. Consequently, we are dedicated to exploring women's representation in the world of cinema. Join us in our quest to find out how well represented women really are and see how we try redefine the metrics for women's representation in our [Datastory](https://matthijsscheerder.github.io/PandamoniumWebsite/)!

## Abstract
In our research, we critically examine the portrayal of women in cinema, extending beyond the traditional Bechdel Test to develop a more comprehensive framework for assessing female representation. The Bechdel Test, with its straightforward criteria of female characters interacting and conversing on topics other than men, serves as a starting point. Our study focuses on four key areas: formulating an inclusive metric for women's representation in films, integrating Bechdel scores with other cinematic attributes to understand broader trends, investigating discrepancies between representation scores and Bechdel outcomes, and utilizing Natural Language Processing (NLP) techniques, like sentiment analysis and gender-specific verbs in plot summaries, to create nuanced metrics. This approach aims to provide a richer, more detailed understanding of how women are depicted in cinema, highlighting complexities and subtleties often overlooked by conventional methods.

## Research Questions
1. Can we develop a formulation that accounts for the representation of women in movies?
2. Introducing the Bechdel test, how are these scores and trends changed along with the other attributes?
3. Is it possible to see a discrepancy comparing the women's representation score and the Bechdel test?
4. Can we derive metrics from plot-summaries based analysis (NLP: sentiment analysis & gender verbs)?

## Additional Datasets
-[**Bechdel Test**](https://bechdeltest.com/) - The Bechdel Test Movie List, comprising more than 10,130 movies, is retrieved through its API, offering a dataset with seven fields. Key features include imdbid (facilitating integration with other datasets), title, year, and rating. The rating scale delineates the Bechdel Test outcomes: 0 signifies the absence of two women, 1 indicates no conversation, 2 denotes discussion about a man, and 3 signifies a successful passage of the test. 
<!--
-[**GII**](https://ourworldindata.org/grapher/gender-inequality-index-from-the-human-development-report?tab=chart) - The Gender Inequality Index can be readily downloaded and is used to enhance our dataset. .This index provides a comprehensive (quantitative) view of the challenges women face in different countries, highlighting areas where progress is needed to achieve greater gender equality. The lower the value the higher the equality between genders.

-[**HDI**](https://ourworldindata.org/grapher/human-development-index) - The Human Development Index can be readily downloaded and is used to enhance our dataset. This index offers valuable insights into a country's progress in improving the living standards and quality of life for its citizens. We want to see if this is also a predictor for women's represenation in cinema.-->

## Methods
### Bechdel Test Feature Addition:
The vanilla CMU dataset does not contain the Bechdel Test Score for the movies. However, using an additional dataset that accounts for this, we may add this feature as a new column to our dataset. The aforementioned dataset contains the Bechdel score, year, and movie name for more than 10,000 movies. In order to add this new column, we took the intersection of two datasets, by iteratively comparing the name of the movies. However, we observed that for the same movie, names on two datasets may not exactly match, due to some typos. For this, we have utilized some string-matching algorithms between datasets. We are running Fuzzy String-Matching algorithm on the two names and if they are above a certain threshold, we check the years on two datasets. If they match, that particular movie is added to the intersection dataset. Without the string-matching, we have 5553 movies on the intersection dataset, whereas, with the matching, we raise that number to 6521. It is favorable for us start with a dataset as large as possible.

### Natural Language Processing
#### Actor density
For the gender density we used the simple yet intuitive formula: 

$$\frac{number_{female\_characters}}{number_{female\_characters} + number_{male\_characters}}$$

To calculate the actor mention score for movies, we devised a method that begins with analyzing the plot summary of each film. This involves tokenizing the summary into words and tracking the frequency of each. The focus here is to identify how often characters are mentioned in the narrative.

The next step is aligning this data with a character dataset, which contains detailed information about each character, including their gender. We refined this list by converting character names to lowercase and extracting only their first names, ensuring accuracy in matching character mentions in the plot summary.

Finally, we correlate the frequency of character mentions with their gender to calculate the actor mention score. This score is derived by comparing the number of mentions of male and female characters, providing a quantitative measure of gender representation in the movie's narrative. This approach not only quantifies gender portrayal but also emphasizes the significance of character prominence in the storytelling process.

#### Pronoun density
The pronoun density is somewhat similar to the actor density, but it is more straightforward and thus considerably more simple: 

$$density_{pronoun} = \frac{number_{she,her}}{number_{she,her} + number_{he,his}}$$

This formula calculates the proportion of female pronouns relative to the total count of both male and female pronouns, providing a simple yet effective measure of gender representation. Unlike our previous method that analyzed actor mentions, this approach focuses solely on the usage of gender-specific pronouns in the plot summaries, offering a different perspective on the narrative's gender dynamics.

#### Sentiment analysis
##### roBERTa
We conducted sentiment analysis on movie plot summaries using the [roBERTa model](https://huggingface.co/docs/transformers/model_doc/roberta). This method bypasses the need for extensive text preprocessing, allowing us to directly analyze the tokenized summaries.

The process involves categorizing the sentiment of each summary into three moods: negative, neutral, and positive. The model calculates the probabilities for each mood, offering a clear depiction of the emotional tone of the text.

This approach not only simplifies sentiment analysis but also provides valuable insights into the emotional content of movie narratives, enhancing our understanding of their impact and tone.

##### Polarity (TextBlob)
In our approach, we aimed to calculate a polarity score for each movie's plot summary, starting with a baseline using the [TextBlob library](https://textblob.readthedocs.io/en/dev/quickstart.html). 

### Random Forests 
We wanted to include a machine learning method to try if we can actually predict the outcome of the bechdel test using some of our newly introduced metrics. Random Forest is a robust machine learning algorithm, known for its versatility and simplicity in handling both classification and regression tasks. It operates as an ensemble of decision trees, each constructed using a random subset of the data, which then vote collectively on the final prediction. 

In the context of predicting Bechdel scores, Random Forest is ideal due to its capacity for threshold-based classification, which aligns well with features like female cast ratio. The algorithm's inherent feature ranking provides an efficient method for feature selection, highlighting the most influential factors such as female cast ratio and gender pronoun density in determining a film's Bechdel status. 

## Executed timeline
Due to receiving a low grade on our Milestone 2, it was necessary to revisit and revise our project. Consequently, our project timeline has also undergone significant changes. Since we got the feedback late we also had to radically alter our planning.  

- 17.11.23: **Project milestone 2 deadline**
---
- 1.12.23: Discuss feedback of Milestone 2 with mentor.
---
- 05.12.23: Redo Milestone 2, keep the things that are usable. Work out new research questions and overall goal of the project.
- 08.12.23: Gather necessary additional datasets and make start with research questions. 
---
- 12.12.23: Sentiment analysis
- 15.12.23: Actor & pronoun density
- 18.12.23: Random Forest
---
- 20.12.23: Combine all notebooks and unify for the deliverable
- 21.12.23: Make up datastory & alter plots for interactive use 
- 22.12.23: **Project Milestone 3 deadline** 

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
    <th class="tg-0lax">Contributions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Tiago</td>
    <td class="tg-0lax">Data Analysis<br><br>Visualizations<br><br>Notebook organisation</td>
  </tr>
  <tr>
    <td class="tg-0lax">Deniz</td>
    <td class="tg-0lax">Machine learning<br><br>Scraping<br><br>Notebook organisation</td>
  </tr>
  <tr>
    <td class="tg-0lax">Eren</td>
    <td class="tg-0lax">Scraping<br><br>Website & Datastory<br><br>Statistical Analysis</td>
  </tr>
  <tr>
    <td class="tg-0lax">Riza</td>
    <td class="tg-0lax">Natural Language Processing<br><br>Overall planning<br><br>Statistical Analysis</td>
  </tr>
  <tr>
    <td class="tg-0lax">Matthijs</td>
    <td class="tg-0lax">Machine learning<br><br>Website & Datastory<br><br>README</td>
    </tr>
</tbody>
</table>

## Sources
Luoying Yang, Zhou Xu, and Jiebo Luo. 2020. Measuring Female Representation and Impact in Films over Time. ACM/IMS Trans. Data Sci. 1, 4, Article 30 (November 2020), 14 pages. https://doi.org/10.1145/3411213


