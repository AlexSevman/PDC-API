import pandas as pd
path_excel = "/Users/64513/Documents/PDC_data_submission_templates/"
excel_template = 'PDC Proteomic Data Submission Template.xlsx'

excel_template_case = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Case")
excel_template_case.columns

excel_template_demographics = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Demographic")
excel_template_demographics.columns

excel_template_diagnosis = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Diagnosis")
excel_template_diagnosis.columns
print(list(excel_template_diagnosis.columns))

excel_template_exposure = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Exposure")
print(list(excel_template_exposure.columns))

excel_template_fam_hist= pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Family History")
excel_template_fam_hist.columns

excel_template_treatments= pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Treatment")
print(list(excel_template_treatments.columns))

excel_template_followup = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Follow-Up")
print(list(excel_template_followup.columns))

excel_template_sample = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Sample")
excel_template_sample.columns

excel_template_aliquots = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Aliquots")
excel_template_aliquots.columns

excel_template_study = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Study")
excel_template_study.columns

excel_template_protocol = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Protocol", header=1)
excel_template_protocol.columns

excel_template_expMeta = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="Expt_Runmetadata")
excel_template_expMeta.columns

excel_template_file_meta = pd.read_excel(io=f"{path_excel}{excel_template}", sheet_name="File_Metadata")
excel_template_file_meta.columns