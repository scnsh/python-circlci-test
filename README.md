# python-circlci-test 
[![CircleCI](https://circleci.com/gh/scnsh/python-circlci-test.svg?style=shield&circle-token=5f3c6f98ee6478f3bee5b2b186500233150074ed)](https://circleci.com/gh/scnsh/python-circlci-test)
[![codecov](https://codecov.io/gh/scnsh/python-circlci-test/branch/master/graph/badge.svg)](https://codecov.io/gh/scnsh/python-circlci-test)


CircleCIなどのツール達を使ってみる

## 参考資料
- https://qiita.com/abenben/items/b947dff2cc5613538b9a
- https://circleci.com/docs/ja/2.0/language-python/
- https://qiita.com/Hanocha/items/8ad74258eb43d0959590
- https://yoshinorin.net/2016/12/18/change-format-of-circleci-badge/
- https://qiita.com/nasum/items/aff9bf09d49b136bbf94

## トラブルシューティング

#### circleciをローカルで動かそうとしてdockerと接続できなかった

以下のコマンドでcircleciとdockerを更新
```
sudo snap install docker circleci
sudo snap connect circleci:docker docker
```

