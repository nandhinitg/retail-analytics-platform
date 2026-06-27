from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "Bronze Customer Load"
).getOrCreate()

df = spark.read.csv(
    "data/historical_data.csv",
    header=True,
    inferSchema=True
)

df.show()
