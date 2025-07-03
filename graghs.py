import matplotlib.pyplot as plt
import numpy as np

from test import call_functions, file_name, problems_per_file
from test import problems
from test import function_length_list
from collections import Counter

def all_graghs():
    get_pie_chart_gragh_about_number_of_issues()
    get_number_of_issues_per_file()
    get_histogram_gragh_about_function_lengths()

def get_histogram_gragh_about_function_lengths():
    plt.hist(function_length_list, edgecolor='black')

    plt.title('Distribution of function lengths')
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.show()
    plt.savefig(f'./images/histogram_functions_lengths.png')
    plt.close()

def get_pie_chart_gragh_about_number_of_issues():
    count = Counter(problems)
    labels = list(count.keys())
    sizes = list(count.values())
    sizes = np.array(sizes)

    valid_indices = ~np.isnan(sizes) & (sizes > 0)
    sizes = sizes[valid_indices]
    labels = [label for i, label in enumerate(labels) if valid_indices[i]] # check if its מסונכרן good

    # בדוק אם יש ערכים חוקיים לפני הצגת הגרף
    if sizes.size > 0:
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Number of issues per issue type')
        plt.savefig(f'./images/pie_chart_number_of_issues.png')
        plt.show()
        plt.close()
    else:
        print("No valid data to display in pie chart.")

def get_number_of_issues_per_file():
    counts = {file: len(problems) for file, problems in problems_per_file.items()}
    files = counts.keys()
    issue_counts = counts.values()
    # print("files: ", problems_per_file)
    plt.bar(files, issue_counts)
    plt.xlabel('Files')
    plt.ylabel('Number of Issues')
    plt.title('Number of Issues per File')

    # הצגת הגרף
    plt.xticks(rotation=45)  # סיבוב שמות הקבצים אם הם ארוכים
    plt.tight_layout()  # התאמת הגרף לגודל התצוגה

    plt.show()
    plt.savefig(f'./images/number_of_issues_per_file.png')
    plt.close()


