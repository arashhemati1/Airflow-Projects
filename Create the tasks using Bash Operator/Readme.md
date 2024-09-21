# Apache Airflow ETL Project

This project demonstrates how to create an ETL (Extract, Transform, Load) pipeline using Apache Airflow's `BashOperator`. The tasks involved include unzipping data, extracting fields from various file formats (CSV, TSV, fixed-width), consolidating data, and transforming the extracted data. The project uses a DAG (Directed Acyclic Graph) to manage task dependencies.

---

## Project Structure

- `dags/ETL_toll_data.py`: Contains the Airflow DAG code to run the ETL pipeline.
- `screenshots/`: Folder to store screenshots for the assignment.
- `README.md`: Documentation for the project.

---

## Steps for Each Task

### 1. Task: `unzip_data`

The first task is to unzip the downloaded data using the `tar` command and extract it to the destination directory.

**Code:**

```python
    unzip_data = BashOperator(
        task_id='unzip_data',
        bash_command='tar -xvf /path/to/downloaded/data.tar -C /path/to/destination/folder'
    )

### 2. Task: `extract_data_from_csv`

The second task is to extract fields (Rowid, Timestamp, Anonymized Vehicle number, and Vehicle type) from vehicle-data.csv and save them into csv_data.csv.

**Code:**
    
```python
    extract_data_from_csv = BashOperator(
        task_id='extract_data_from_csv',
        bash_command="cut -d',' -f1,2,3,4 /path/to/vehicle-data.csv > /path/to/csv_data.csv"
    )

### 3. Task: `extract_data_from_tsv`

This task extracts fields (Number of axles, Tollplaza id, and Tollplaza code) from tollplaza-data.tsv and saves them into tsv_data.csv.

**Code:**

```python
    extract_data_from_tsv = BashOperator(
        task_id='extract_data_from_tsv',
        bash_command="cut -f3,4,5 /path/to/tollplaza-data.tsv > /path/to/tsv_data.csv"
    )

### 4. Task: `extract_data_from_fixed_width`

This task extracts fields (Type of Payment code and Vehicle Code) from the fixed-width file payment-data.txt and saves them into fixed_width_data.csv.

**Code:**

```python
    extract_data_from_fixed_width = BashOperator(
        task_id='extract_data_from_fixed_width',
        bash_command="awk '{print substr($0, 10, 5), substr($0, 20, 5)}' /path/to/payment-data.txt > /path/to/fixed_width_data.csv"
    )


### 5. Task: `econsolidate_data`

This task consolidates the extracted data from csv_data.csv, tsv_data.csv, and fixed_width_data.csv into a single file named extracted_data.csv. The paste command merges the columns of these files.

**Code:**

```python
    consolidate_data = BashOperator(
        task_id='consolidate_data',
        bash_command="paste /path/to/csv_data.csv /path/to/tsv_data.csv /path/to/fixed_width_data.csv > /path/to/extracted_data.csv"
    )

### 6. Task: `transform_data`

This task transforms the vehicle_type field in extracted_data.csv by converting it to uppercase and saving the result into transformed_data.csv.

**Code:**

```python
    transform_data = BashOperator(
        task_id='transform_data',
        bash_command="cat /path/to/extracted_data.csv | tr 'a-z' 'A-Z' > /path/to/transformed_data.csv"
    )

###  Task Pipeline

The tasks are arranged in the following pipeline:

**Code:**

```bash
    unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data

