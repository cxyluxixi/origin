

# 注意： google.cloud包的安装命令为
# pip install google-cloud-bigquery
import pandas as pd
from google.cloud import bigquery


# client是一个对象，有各种方法，操作数据集
client = bigquery.Client()

# 第一步，获取网络上的数据集
dataset_ref = client.dataset('dataset-name',project='bigquery-public-data')
dataset = client.get_dataset(dataset_ref)


# 第二步，获取数据集中的所有表格
tables = list(client.list_tables(dataset))
# 遍历表格id，也就是表格名称
for table in tables:
    print(table.table_id)


# 第四步，获取某个table_id表格的数据
table_ref = dataset.table('table_id')
table     = client.get_table(table_ref)

# 第五步，获取上一步中表格的column列字段，数值类型
table.schema

# 第六步，打印出前几行并转化为df结构，熟悉一下表格数据
# maxt_results  ：rows number
# start_index : rows starting index
client.list_rows(table,max_results=5,start_index=0).to_dataframe()
# selected_fields: columns index,
client.list_rows(table,selected_fields=table.schema[1:3],max_results=5,start_index=0).to_dataframe()


# 第七步，写出查询语句，并运用到数据集中,得到查询出来的数据
query = """
SELECT column-name
FROM 'bigquery-public-data.dataset-name.table-name'
WHERE country = 'US'
"""

data_queryed = client.query(query).to_dataframe()
data_queryed.value_counts().head() # 统计频次

# 第八步方法1，在运行查询扫描之前，直接获取数据集大小。因为第七步无法判断dataset的大小，
# 为防止数据集太大，直接查询扫描的时间过长，所以这里创建另一种对象，
# 这个对象叫做QueryJobConfig(dry_run=True)
dry_run_config = bigquery.QueryJobConfig(dry_run=True)
dry_run_query_job = client.query(query,job_config=dry_run_config)
# 上述返回的结果就是数据，需要使用属性得到数据量大小，属性为：object.total_bytes_processed
print("This query will process{}bytes.".format(dry_run_query_job.total_bytes_processed))



# 第八步方法2，直接运行查询，但是限制扫描
ONE_MB = 1024*1024*1024 #1GB 大小文件
safe_scan_config = bigquery.QueryJobConfig(maximum_bytes_billed = ONE_MB)
safe_scan_job  =client.query(query,job_config=safe_scan_config).to_dataframe()



#2
query2 = """xxxxx SQL commands xxxxx"""
query_job = client.query(query2).to_dataframe()
query_job.column_name.value_counts().head()
dry_run_jobConfig = bigquery.QueryJobConfig(dry_run=True)
query_limited_result = client.query(query2,job_config=dry_run_jobConfig) 
# 上述返回的结果就是数据，需要使用属性得到数据量大小，属性为：object.total_bytes_processed
print("{}kb".format(query_limited_result.total_bytes_processed))

# print(QueryJobConfig(dry_run = True,job_config=10**10))


# 3
# DATAOFWEEK 是一个内置函数，可以直接从日期数据类型的数据中计算出星期几，并返回
# SQL 中having 跟在group by 后面相当于excel透视表里的筛选条件，
# 并且直接使用重命名之前的公式或者列名，比如COUNT(column_1)
query3 = """
        SELECT COUNT(consecutive_number) AS num_accidents, 
            EXTRACT(DAYOFWEEK FROM timestamp_of_crash) AS day_of_week
        FROM `bigquery-public-data.nhtsa_traffi【zc_fatalities.accident_2015`
        GROUP BY day_of_week
        HAVING COUNT(consecutive_number)>10 
        ORDER BY num_accidents DESC
        """

# 4    
query4 = """
        WITH new_table AS
        (SELECT DATE(block_timestamp) AS trans_date
        FROM `bigquery-public-data.crypto_bitcoin.transactions`
        )
        SELECT COUNT(1) AS transactions,trans_date
        FROM new_table
        GROUP BY trans_date
        ORDER BY trans_date
        """
dry_run_jobConfig = bigquery.QueryJobConfig(dry_run=True)
query_limited_result_3 = client.query(query4,job_config=dry_run_jobConfig)
result3 = query_limited_result_3.to_dataframe() 
result3.set_index('trans_date').plot()

query4 = """
        SELECT L.license, COUNT(1) AS number_of_files
        FROM `bigquery-public-data.github_repos.sample_files` AS sf
        INNER JOIN `bigquery-public-data.github_repos.licenses` AS L 
            ON sf.repo_name = L.repo_name
        GROUP BY L.license
        ORDER BY number_of_files DESC
        """

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed = 10**10)
query_job_4 = client.query(query4,job_config=safe_config)



# 5
# Your code here
bigquery_experts_query = """
                        SELECT a.id, a.body, a.owner_user_id
                        FROM `bigquery-public-data.stackoverflow.posts_questions` AS q 
                        INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
                            ON q.id = a.parent_id
                        WHERE q.tags LIKE '%bigquery%'
                        """
