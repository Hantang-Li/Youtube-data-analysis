# JSC370_Project_Youtube_data_analysis

YouTube, the world’s third most popular online destination, has transformed from a video-sharing site into a job opportunity for content creators in both new and mainstream media. (cite: https://www.elon.edu/u/academics/communications/journal/wp-content/uploads/sites/153/2017/06/06_Margaret_Holland.pdf) Individuals who upload videos on Youtube, also known as YouTubers, could turn on monetization features. One of the major ways YouTubers earn money is through the number of ad views (https://support.google.com/youtube/answer/72857?hl=en). Since ad views depend on each video’s views, we would like to analyze what factors could result in a high view and how people’s preferences have changed in recent years.

## Instruction For Produce the website

## Instruction For Produce the final report

We have included the preprocessed data 'df_CA_trending.Rda' inside the repository, so you can directly reproduce the final report by opening '__.rmd' and knit.
But if you would like to run the data preprocessing procedure you can follow the section "Instruction For Data Wrangling"

## Instruction For Data Wrangling and produce df_CA_trending.Rda

1. Download CA_youtube_trending_data.csv from https://www.kaggle.com/rsrishav/youtube-trending-video-dataset and place to the data_wrangling folder.
2. Download CAvideos.csv from https://www.kaggle.com/datasnaek/youtube-new?select=CAvideos.csv and place to the data_wrangling folder.
3. Download CA_category_id.json from https://www.kaggle.com/datasnaek/youtube-new (I have included in the data_wrangling folder)
4. Run ./data_wrangling/insert_words.py and it will produce CAvideos2.csv
5. The necessarry files Run ./data_wrangling/data_wrangling.Rmd inside R studio to produce the same result (an html file).

Note that I also included my API call result All_ca_trend_vid_content.csv, so you do not have to obtain a key and run the API for a long time to obtain the additional data. 
