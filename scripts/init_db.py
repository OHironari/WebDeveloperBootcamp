from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

from dotenv import load_dotenv
import os

# .envを読み込む
load_dotenv()

# 環境変数からMongoDB URIを取得
mongo_uri = os.getenv("MONGODB_URI")

database_name = "microblog"
collection_name = "entries"

def main():
    # MongoDBへ接続
    client = MongoClient(mongo_uri)
    print("MongoDBに接続しました。")

    # データベース取得（なければ自動で作成）
    db = client[database_name]

    # コレクション作成（既にあれば例外発生するのでcatch）
    try:
        db.create_collection(collection_name)
        print(f"コレクション '{collection_name}' を作成しました。")
    except CollectionInvalid:
        print(f"コレクション '{collection_name}' は既に存在します。")

    # 確認のため、コレクション一覧を表示
    collections = db.list_collection_names()
    print(f"データベース '{database_name}' のコレクション一覧: {collections}")

if __name__ == "__main__":
    main()

