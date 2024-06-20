'''Домашнее задание №11: Работа с комплексными файлами - excel, json,
word. Git и Jira'''

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side

def read_excel_files(files):
    data_frames = [pd.read_excel(file, header=None) for file in files]
    combined_df = pd.concat(data_frames, ignore_index=True)
    return combined_df

def sort_dataframe(df):
    sorted_df = df.sort_values(by=0, ascending=False).reset_index(drop=True)
    return sorted_df

def write_to_excel(df, output_file):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, header=False)
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        
        # Apply font and border styles
        font = Font(name='Arial', bold=True)
        border = Border(left=Side(style='thin'), 
                        right=Side(style='thin'), 
                        top=Side(style='thin'), 
                        bottom=Side(style='thin'))
        
        for row in worksheet.iter_rows():
            for cell in row:
                cell.font = font
                cell.border = border

if __name__ == "__main__":
    FILES = ['file1.xlsx', 'file2.xlsx', 'file3.xlsx']
    OUTPUT_FILE = 'sorted_combined.xlsx'
    
    DATAFRAME = read_excel_files(FILES)
    SORTED_DATAFRAME = sort_dataframe(DATAFRAME)
    write_to_excel(SORTED_DATAFRAME, OUTPUT_FILE)
