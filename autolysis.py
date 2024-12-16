# -------------------Importing Libraries --------------------

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import openai  # pip install openai



# -------------------Functions --------------------


# Function to analyze the data (basic summary stats, missing values, correlation matrix)
def analyzing_data(df):
    # Summary stats for numerical columns
    summary_stat = df.describe()

    # Summary  for categorical columns
    summary_stat_cat = df.describe(include = 'object')
    
    # Checking for missing values
    missing_values = df.isnull().sum()

    # Selecting only numerical columns for correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])

    # Correlation matrix for numerical columns
    corr_matrix = numeric_df.corr() if not numeric_df.empty else pd.DataFrame()

    return summary_stat, missing_values, corr_matrix, summary_stat_cat



# Function to detect outliers using the IQR method
def detecting_outliers(df):
    # Selecting only numeric columns
    df_num = df.select_dtypes(include=[np.number])

    # Apply the IQR method to find outliers in the numeric columns
    q1 = df_num.quantile(0.25)
    q3 = df_num.quantile(0.75)
    outliers = ((df_num < (q1 - 1.5 * (q3 - q1))) | (df_num > (q3 + 1.5 * (q3 - q1)))).sum()

    return outliers


# Function to generate (correlation heatmap, outliers plot, and distribution plot)
def visualizing_data(corr_matrix, outliers, df, output_dir):
    # Generate a heatmap for the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    heatmap_file = os.path.join(output_dir, 'correlation_matrix.png')
    plt.savefig(heatmap_file)
    plt.close()

    # Checking if there are outliers to plot
    if not outliers.empty and outliers.sum() > 0:
        # Ploting the outliers
        plt.figure(figsize=(10, 6))
        outliers.plot(kind='bar', color='red')
        plt.title('Outliers Detection')
        plt.xlabel('Columns')
        plt.ylabel('Number of Outliers')
        outliers_file = os.path.join(output_dir, 'outliers.png')
        plt.savefig(outliers_file)
        plt.close()
    else:
        print("No outliers detected to visualize.")
        outliers_file = None  # No file created for outliers


    # Generating a distribution/count plot for the categorical column
    cat_columns = df.select_dtypes(include = 'object').columns
    if len(cat_columns) > 0:
        

        # Determine the number of features
        cat_features = len(cat_columns)
        if(cat_features==1):
            sns.countplot(y = cat_columns[0], data = df)
           
        else:
        # Create a subplot grid: 1 row for each feature
            fig, axes = plt.subplots(nrows=(cat_features // 4)+1, ncols=4, figsize=(40, 8 * (cat_features // 4)))

        
            t=(cat_features // 4)+1
            j=0
            i=0

        # Plot each feature's distribution
        
        
            for column in (cat_columns):
                if(i==t-1):
                    break
                if(len(df[column].unique())<20):
                    sns.countplot(y = column, data = df, ax=axes[i,j])
                    axes[i,j].set_title(f'Distribution of {column}', fontsize=14)
                    axes[i,j].set_ylabel(column, fontsize=12)
                    axes[i,j].set_xlabel('Frequency', fontsize=12)
                #print(i,j,df[column].unique())
            
                
            
                j=j+1
                if(j==3 ):
               
                    j=0
                    i=i+1


        
        dist_plot_file = os.path.join(output_dir, f'distribution_.png')
        plt.savefig(dist_plot_file)
        plt.close()
    else:
        dist_plot_file = None  # if No numeric columns to plot




    return heatmap_file, outliers_file, dist_plot_file


# Function to create the README.md ( narrative and visualizations)
def create_readme(summary_stat, missing_values, corr_matrix,summary_stat_cat, outliers, output_dir):
    # Writing the analysis report to a markdown file
    readme_file = os.path.join(output_dir, 'README.md')
    try:
        with open(readme_file, 'w') as f:
            f.write("# Automated Data Analysis Report\n\n")
            f.write("## Summary Statistics of the Dataset\n")
            f.write("```shell")
            f.write(f"{summary_stat}\n\n")
            f.write("```")
            f.write("## Categorical variables\n")
            f.write("```shell")
            f.write(f"{summary_stat_cat}\n\n")
            f.write("```")
            f.write("## Missing Values and Outliers\n")
            f.write("```shell")
            f.write(f"{missing_values}\n\n")
            f.write("```")
            f.write("## Outliers\n")
            f.write("```shell")
            f.write(f"{outliers}\n\n")
            f.write("```")
            f.write("## Correlation Matrix\n")
            f.write("Below is the correlation matrix of numerical features:\n\n")
            f.write("![Correlation Matrix](correlation_matrix.png)\n\n")

            f.write("## Outliers Visualization\n")
            f.write("Below is the outliers detection chart:\n\n")
            f.write("![Outliers](outliers.png)\n")

            f.write("## Distribution\n")
            f.write("Below is the distribution plot :\n\n")
            f.write("![Distribution](distribution_.png)\n")  # Placeholder for distribution plot

        return readme_file
    except Exception as e:
        print(f"Error writing to README.md: {e}")
        return None


# Function to generate a detailed story using the new OpenAI API through the proxy
def question_llm(prompt, context):
    try:
        # Set OpenAI API key
        openai.api_key = os.getenv("AIPROXY_TOKEN")

        # Set the custom API base URL for AI Proxy (ensure there's no trailing slash)
        openai.api_base = "https://aiproxy.sanand.workers.dev/openai/v1"  # Corrected endpoint

        # Enhance the prompt to ask for a more detailed story with paragraphs and necessary structure
        full_prompt = f"""Storytelling Task:
Imagine you're a masterful storyteller, transforming data into a vivid and engaging narrative. Using the provided analysis, craft a creative and insightful story that captivates the reader and provides a deeper understanding of the data.
Your Story Should:  
1. Have a Clear Structure: 
   - Start with an engaging introduction to set the scene and provide context.  
   - Develop a compelling body that dives into the data, exploring its significance and uncovering meaningful patterns or trends.  
   - Conclude with a thought-provoking ending that ties the insights together, reflects on potential implications, and leaves a lasting impression.  

2. Be Engaging and Descriptive:
   - Use vivid language to paint a picture of the analysis and its real-world implications.  
   - Add human elements or scenarios to make the story relatable and memorable.  

3. Ensure Logical Flow:
   - Use seamless transitions to connect ideas, ensuring the narrative feels cohesive and natural.  
   - Maintain clarity while delivering an engaging and imaginative story.  

4. Include Contextual Insight: 
   - Highlight why the data matters, connecting it to broader themes or potential outcomes.  
   - Focus on storytelling while ensuring that the insights remain accurate and impactful.  

Provided Inputs:  
- Context: {context}  
- Data Analysis Prompt: {prompt}  

Deliver a story that immerses the reader in a journey of discovery, making the data analysis feel like an integral part of an enlightening and unforgettable narrative."""

        # Request to AI Proxy's chat completions endpoint for gpt-4o-mini model
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Using GPT-4o-Mini model
            messages=[ 
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=1000,  # Increased max_tokens for longer output
            temperature=0.7,
        )

        # Extract the generated text from the response
        story = response['choices'][0]['message']['content'].strip()

        return story

    except Exception as err:
        print(f"Error with OpenAI API: {err}")
        return "Failed to generate story."


# Main function that integrates all the steps
def main(csv_file):
    

    # Try reading the CSV file with 'ISO-8859-1' encoding 
    try:
        df = pd.read_csv(csv_file, encoding='ISO-8859-1')
    except UnicodeDecodeError as err:
        print(f"Error reading file: {err}")
        return

    # Analyze the data: summary statistics, missing values, correlation matrix
    summary_stat, missing_values, corr_matrix, summary_stat_cat = analyzing_data(df)

    # Detect outliers
    outliers = detecting_outliers(df)

    # Create the output directory if it doesn't exist
    output_dir = os.path.splitext(csv_file)[0]
    os.makedirs(output_dir, exist_ok=True)

    # Visualize the data
    heatmap_file, outliers_file, dist_plot_file = visualizing_data(corr_matrix, outliers, df, output_dir)

    # Generate the story using the LLM
    story = question_llm("Generate a clear and creative story from the analysis", 
                         context=f"Dataset Analysis:\nSummary Statistics:\n{summary_stat}\nCategorical stats:\n{summary_stat_cat}\n\nMissing Values:\n{missing_values}\n\nCorrelation Matrix:\n{corr_matrix}\n\nOutliers:\n{outliers}")

    # Create the README.md file with the analysis and the story
    readme_file = create_readme(summary_stat, missing_values, corr_matrix,summary_stat_cat, outliers, output_dir)

    if readme_file:
        try:
            # Append the story to the README.md file
            with open(readme_file, 'a') as f:
                f.write("## Story\n")
                f.write(f"{story}\n")

            print(f"Analysis complete! Results saved in '{output_dir}' directory.")
            print(f"README file: {readme_file}")
            print(f"Visualizations: {heatmap_file}, {outliers_file}, {dist_plot_file}")
        except Exception as e:
            print(f"Error appending story to README.md: {e}")
    else:
        print("Error generating the README.md file.")


if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Automated Data Analysis")
    parser.add_argument("csv_file", help="CSV file for analysis")
    
    args = parser.parse_args()

    # Run the main function with the provided CSV file and API token
    main(args.csv_file)
