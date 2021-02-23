# Python Object-Oriented Programming with Type annotation

* 継承 (インターフェース): [python_oop/interface.py](./python_oop/interface.py)
* ポリモーフィズム: [python_oop/polymorphism.py](./python_oop/polymorphism.py)
* カプセル化: [python_oop/encapsulation.py](./python_oop/encapsulation.py)

## 環境構築

まず、Poetryが必要です。[公式ガイド](https://python-poetry.org/docs/)にしたがってインストールして下さい。

次に、:

```sh
$ poetry install
```

で仮想環境が作成されます。

次の様にコマンドを実行すると、`mypy` が静的解析を行います。

```sh
$ poetry run mypy python_oop/
```

また、VScodeを使っている場合は、インタラクティブに静的解析を行ってくれます。適宜ファイルを開いてmypyの静的解析結果を確認してみて下さい。
