# #482 「ng generate directive --structural」

## 概要
`ng generate directive`コマンドの`--structural`オプションは構造ディレクティブ向けの雛形を生成し、TemplateRefとViewContainerRefを自動注入してくれる。

## 学習目標
- CLIコマンドで構造ディレクティブ雛形を生成する方法を理解する
- 生成されるファイルと注入される依存を把握する
- Standaloneディレクティブとして利用する設定を学ぶ

## 技術ポイント
- `ng g directive directives/unless --standalone --structural`
- TemplateRef/ViewContainerRefが自動的にコンストラクタへ注入
- specファイルも生成されテスト準備が整う

## 📺 画面表示用コード（動画用）
```bash
ng g directive directives/unless --standalone --structural
```

## 💻 詳細実装例（学習用）
```bash
# 実行例
ng g directive shared/unless --standalone --structural

# 生成されるテンプレート
@Directive({
  selector: '[appUnless]',
  standalone: true
})
export class UnlessDirective {
  constructor(private tpl: TemplateRef<unknown>, private vc: ViewContainerRef) {}
}
```

## ベストプラクティス
- `--standalone`と併用してモジュールに依存しない構造にする
- 生成直後にselectorやInput名をプロジェクト規約に合わせて調整
- specファイルを活用し挙動を早期に検証

## 注意点
- CLIのバージョンによりオプション名称が変わる場合があるのでドキュメントを確認
- Standaloneでない場合は使用するモジュールに宣言が必要
- 雛形は最小限のコードのためロジックやテストを丁寧に追加

## 関連技術
- Angular CLI
- TemplateRef / ViewContainerRef
- Standalone構成
