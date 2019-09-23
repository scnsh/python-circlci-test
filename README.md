# python-circlci-test
CircleCIを使ってみる

## 参考資料
- https://qiita.com/abenben/items/b947dff2cc5613538b9a
- https://circleci.com/docs/ja/2.0/language-python/

## トラブルシューティング

#### circleciをローカルで動かそうとしてdockerと接続できなかった

以下のコマンドでcircleciとdockerを更新
```
sudo snap install docker circleci
sudo snap connect circleci:docker docker
```

