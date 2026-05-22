from google.cloud import bigquery
from config.settings import PROJECT_ID

client = bigquery.Client(project=PROJECT_ID)


QUERIES = {
    "top_attack": """
        SELECT
            name,
            attack
        FROM `your-project-id.pokemon_analytics_dev.analytics_pokemon`
        ORDER BY attack DESC
        LIMIT 10
    """
}


for query_name, query in QUERIES.items():
    print(f"Running query: {query_name}")

    query_job = client.query(query)

    for row in query_job.result():
        print(row)