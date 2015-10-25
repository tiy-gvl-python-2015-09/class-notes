import pandas as pd


def load_data(apps, schema_editor):
    df = pd.read_csv("20151014211444871482_dataset.csv", names=["Student Name", "MB", "Year", "House", "GPA"]).head()
    StudentRecord = apps.get_model("pandas_data", "StudentRecord")

    for index, row in df.iterrows():
        student_name = row["Student Name"]
        MB = row.MB
        year = row.Year
        house = row.House
        GPA = row.GPA
        StudentRecord.objects.create(student_name=student_name, mb=MB, year=year, house=house, gpa=GPA)
