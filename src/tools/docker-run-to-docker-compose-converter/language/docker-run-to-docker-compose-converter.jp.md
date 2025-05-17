# Docker Run から Docker-Compose へのコンバータ ドキュメント

## 1. ツール概要

Docker Run から Docker-Compose へのコンバータは、開発者がコマンドラインの "docker run" を迅速に Docker-Compose ファイルへ変換するためのオンラインツールです。コンテナオーケストレーションの設定プロセスを簡素化し、開発効率を向上させます。

## 2. 主な機能

1. **コマンド変換**
   * ユーザーは、例として "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx" のような複雑な Docker コマンドを専用の入力欄に貼り付けることができます。
   * このツールは "docker run" コマンド内の各種パラメーター（ポートマッピング（"-p 80:80"）、ボリュームマウント（"-v /var/run/docker.sock:/tmp/docker.sock:ro"）、再起動ポリシー（"--restart always"）、ログオプション（"--log-opt max-size=1g"）、イメージ名（"nginx"）など）を自動的に解析します。

2. **Docker-Compose ファイル生成**
   * 解析した "docker run" コマンドのパラメーターに基づき、対応する Docker-Compose ファイルを生成します。
   * 生成される YAML 形式のファイルにはバージョン宣言（例："version: '3.9'"）、サービス定義（"services"）、イメージ指定（"image"）、ログ設定（"logging" とその "options"）、再起動設定（"restart"）、ボリューム設定（"volumes"）、ポートマッピング（"ports"）などの重要な設定項目が含まれており、コンテナのオーケストレーション情報を包括的に表現します。そのため、ユーザーはこのファイルをそのまま利用したり、必要に応じて追加修正を行ったりすることが可能です。

3. **ファイルダウンロード**
   * "Download docker-compose.yml" ボタンにより、ユーザーは生成された Docker-Compose ファイルをワンクリックでローカルにダウンロードできます。これにより、実際のプロジェクト環境での適用や管理が容易になります。