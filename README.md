Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:
Title
Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
Research Questions: A list of research questions you would like to address during the project.
Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
Methods
Proposed timeline
Organization within the team: A list of internal milestones up until project Milestone P3.
Questions for TAs (optional): Add here any questions you have for us related to the proposed project.

# Scripted Sisterhood: Analyzing Bechdel Test Triumphs
*Pandamonium: Tiago Freitas, Deniz Kasap, Riza Arseven, Eren Saydar and Matthijs Scheerder

## Abstract
Women have been historically underrepresented in cinema, one of the most used measures to indicate the represe










In "Femme Frames," we scrutinize the portrayal of women in film through the Bechdel Test—requiring at least two women to converse about something other than a man. Our data-driven exploration investigates patterns and disparities in gender representation, sparking a conversation about storytelling's societal impact. Recent films like Oppenheimer and Avatar 2, failing the Bechdel Test, underscore its continued relevance. This project aims to unveil insights into cinematic narratives and promote positive change within the industry. Join us on a journey where every frame counts and every story told contributes to a more inclusive cinematic landscape.



## Research Questions

1. Is there a historical trend in the Bechdel test, i.e. are things improving or remaining as they have always been?
2. Are there hidden relationships for the prediction of the Bechdel test, can we come up with some formula?
3. Can we introduce another metric of representation of women in cinema, like the female cast ratio?
4. Can we extend the formula or use the Bechdel to predict box office revenue? 



## Proposed additional datasets
-[**Bechdel Test**](https://bechdeltest.com/) - The Bechdel Test Movie List, comprising more than 10,130 movies, is retrieved through its API, offering a dataset with seven fields. Key features include imdbid (facilitating integration with other datasets), title, year, and rating. The rating scale delineates the Bechdel Test outcomes: 0 signifies the absence of two women, 1 indicates no conversation, 2 denotes discussion about a man, and 3 signifies a successful passage of the test. 


-[**IMDB Box office mojo**](https://github.com/tjwaterman99/boxofficemojo-scraper) - Since a lot of box office data is missing we want to enrich our dataset by scraping the boxofficemojo website. In the linked 






-[**Inflation (CPI)**](https://www.officialdata.org/us/inflation/1923?amount=1) - In order to ensure a fair comparison of revenue/box office data between different movies we need to adjust for inflation. Sicne the box office revenue is listed in USD, we use historical dat. By normalizing financial figures for inflation, we aim to assess the financial success of movies in real dollars, facilitating meaningful comparisons across different years.





a dataset containing country names and inflation data will be used to adjust `budget` and `box office revenue` of the movies. We use the Consumer Price Index (CPI) of the United States to adjust for inflation. CPI is the most widely used measure of inflation, and we use the U.S. as a baseline because both budget and box office revenue are stated in USD. By adjusting for inflation, we can measure financial success in constant dollars, which allows us to compare movies from different years.





## Methods
What do we want to do?








## Proposed timeline

We have decided to have 2 internal deadlines for each week: Tuesday and Friday.  

- 17.11.23: **Project milestone 2 deadline**
---
- 21.11.23: Start with more in-depth statistical analysis. 
- 24.11.23: Finish statistical analysis
---
- 28.11.23: Each member works on homework 2
- 1.12.23: **Homework 2 deadline**
---
- 5.12.22: Finish statistical analysis when controlling for all confounding factors.
- 8.12.22: Visualizations and refinements.
---
- 12.12.22: All technical parts finished, start with datastory (website development).
- 15.12.22: Finish datastory
---
- 20.12.22: Check all deliverables and update README. Deliberately scheduled less to have some buffer time.
- 22.12.22: **Project milestone 3 deadline** 



## Organisation within the team

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
    <td class="tg-0lax">Initial data analysis<br><br>task2<br><br>task3</td>
  </tr>
  <tr>
    <td class="tg-0lax">Deniz</td>
    <td class="tg-0lax">Additional Dataset<br><br>task2<br><br>task3</td>
  </tr>
  <tr>
    <td class="tg-0lax">Eren</td>
    <td class="tg-0lax">website development<br><br>Develop textual context for data story<br><br>task3</td>
  </tr>
  <tr>
    <td class="tg-0lax">Riza</td>
    <td class="tg-0lax">Initial data analysis<br><br>task2<br><br>task3</td>
  </tr>
  <tr>
    <td class="tg-0lax">Matthijs</td>
    <td class="tg-0lax">task1<br><br>task2<br><br>task3</td>
    </tr>
</tbody>
</table>







