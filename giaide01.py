from concurrent.futures import ThreadPoolExecutor, as_completed
from pymongo import MongoClient
import time

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "glamira"
COLLECTION_NAME = "summary"

client = MongoClient(MONGO_URI)
collection = client[DB_NAME][COLLECTION_NAME]


def extract_product_ids(limit=1000):
    product_ids = collection.distinct(
        "product_id",
        {
            "product_id": {
                "$exists": True,
                "$nin": [None, ""]
            }
        }
    )

    return product_ids[:limit]


def fetch_product(product_id):
    """
    Lấy một số event của product từ MongoDB.
    Projection giúp không kéo toàn bộ document về Python.
    """
    documents = list(
        collection.find(
            {"product_id": product_id},
            {
                "_id": 0,
                "product_id": 1,
                "user_id_db": 1,
                "time_stamp": 1,
                "collection": 1,
                "store_id": 1,
            }
        ).limit(100)
    )

    return {
        "product_id": product_id,
        "event_count": len(documents),
        "events": documents,
    }


def main():
    # -------------------------
    # STEP 1: Extract IDs
    # -------------------------

    product_ids = extract_product_ids(1000)

    print(f"Extracted {len(product_ids)} product_ids")

    # -------------------------
    # STEP 2: Benchmark
    # -------------------------

    start = time.perf_counter()

    results = []
    errors = []

    # -------------------------
    # STEP 3: Multithreading
    # -------------------------

    with ThreadPoolExecutor(max_workers=8) as executor:

        future_to_product = {
            executor.submit(fetch_product, product_id): product_id
            for product_id in product_ids
        }

        for future in as_completed(future_to_product):

            product_id = future_to_product[future]

            try:
                result = future.result()
                results.append(result)

            except Exception as e:
                errors.append(
                    {
                        "product_id": product_id,
                        "error": str(e),
                    }
                )

    elapsed = time.perf_counter() - start

    # -------------------------
    # STEP 4: Metrics
    # -------------------------

    print("\n===== RESULT =====")
    print(f"Products:   {len(product_ids)}")
    print(f"Success:    {len(results)}")
    print(f"Errors:     {len(errors)}")
    print(f"Runtime:    {elapsed:.2f}s")

    if elapsed > 0:
        print(
            f"Throughput: "
            f"{len(product_ids) / elapsed:.2f} products/sec"
        )


if __name__ == "__main__":
    main()