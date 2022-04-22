## Instruction For Produce the website

Copy /data/df_CA_trending.Rda to the root and knit index.Rmd in R. 

## Instruction For Produce the final report

Copy /data/df_CA_trending.Rda to the /report_markdown and knit final_report.Rmd in R.
But if you would like to run the data preprocessing procedure you can follow the section "Instruction For Data Wrangling"

## Instruction For Data Wrangling and produce df_CA_trending.Rda

1. Download CA_youtube_trending_data.csv from https://www.kaggle.com/rsrishav/youtube-trending-video-dataset and place to the data_wrangling folder.
2. Download CAvideos.csv from https://www.kaggle.com/datasnaek/youtube-new?select=CAvideos.csv and place to the data_wrangling folder.
3. Download CA_category_id.json from https://www.kaggle.com/datasnaek/youtube-new (I have included in the data_wrangling folder)
4. Run ./data_wrangling/insert_words.py and it will produce CAvideos2.csv
5. The necessarry files Run ./data_wrangling/data_wrangling.Rmd inside R studio to produce the same result (an html file).

Note that I also included my API call result All_ca_trend_vid_content.csv, so you do not have to obtain a key and run the API for a long time to obtain the additional data. 

After runnning the Data Wrangling procedure, you will get df_CA_trending.Rda that can be used to produce final report and website.